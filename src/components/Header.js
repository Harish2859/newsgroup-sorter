import React from 'react';
import { motion } from 'framer-motion';

const Header = () => {
  return (
    <header className="text-center">
      <motion.div
        initial={{ opacity: 0, y: -30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
      >
        <h1 className="text-5xl md:text-6xl font-bold text-white mb-4">
          Newsgroup
          <span className="block text-gradient bg-white bg-clip-text text-transparent">
            Classifier
          </span>
        </h1>
        <p className="text-xl text-white/80 max-w-2xl mx-auto leading-relaxed">
          Advanced AI-powered text classification using Multinomial Naive Bayes
          to categorize newsgroup posts across 20 different topics
        </p>
      </motion.div>
      
      <motion.div
        initial={{ opacity: 0, scale: 0 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.6, delay: 0.3 }}
        className="mt-8 flex justify-center space-x-8"
      >
        <div className="glass-effect rounded-xl px-6 py-3">
          <div className="text-2xl font-bold text-white">20</div>
          <div className="text-sm text-white/70">Categories</div>
        </div>
        <div className="glass-effect rounded-xl px-6 py-3">
          <div className="text-2xl font-bold text-white">~20K</div>
          <div className="text-sm text-white/70">Documents</div>
        </div>
        <div className="glass-effect rounded-xl px-6 py-3">
          <div className="text-2xl font-bold text-white">85%+</div>
          <div className="text-sm text-white/70">Accuracy</div>
        </div>
      </motion.div>
    </header>
  );
};

export default Header;