import React from 'react';
import { motion } from 'framer-motion';

const Footer = () => {
  return (
    <footer className="text-center">
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.6 }}
        className="glass-effect rounded-2xl p-6"
      >
        <div className="grid md:grid-cols-3 gap-6 text-white/80">
          <div>
            <h4 className="font-semibold text-white mb-2">Algorithm</h4>
            <p className="text-sm">Multinomial Naive Bayes with Bag-of-Words feature extraction</p>
          </div>
          <div>
            <h4 className="font-semibold text-white mb-2">Dataset</h4>
            <p className="text-sm">20 Newsgroups dataset with ~20,000 documents</p>
          </div>
          <div>
            <h4 className="font-semibold text-white mb-2">Performance</h4>
            <p className="text-sm">Achieves 85%+ accuracy on test data</p>
          </div>
        </div>
        
        <div className="mt-6 pt-6 border-t border-white/20">
          <p className="text-white/60 text-sm">
            Built with React, Python, and scikit-learn • Text Classification Demo
          </p>
        </div>
      </motion.div>
    </footer>
  );
};

export default Footer;