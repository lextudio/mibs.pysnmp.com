#
# PySNMP MIB module PAIRGAIN-DSLAM-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PAIRGAIN-DSLAM-TRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:36:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pgainDSLAM, = mibBuilder.importSymbols("PAIRGAIN-COMMON-HD-MIB", "pgainDSLAM")
pgDSLAMChassisPsStatus, pgDSLAMConfigChangeCnts, pgDSLAMChassisTemperature, pgDSLAMChassisFanStatus, pgDSLAMConfigLastChange = mibBuilder.importSymbols("PAIRGAIN-DSLAM-CHASSIS-MIB", "pgDSLAMChassisPsStatus", "pgDSLAMConfigChangeCnts", "pgDSLAMChassisTemperature", "pgDSLAMChassisFanStatus", "pgDSLAMConfigLastChange")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
snmp, = mibBuilder.importSymbols("SNMPv2-MIB", "snmp")
Counter32, NotificationType, Counter64, ModuleIdentity, iso, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, NotificationType, Bits, ObjectIdentity, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "Counter64", "ModuleIdentity", "iso", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "NotificationType", "Bits", "ObjectIdentity", "Unsigned32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
coldStart = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,0))
if mibBuilder.loadTexts: coldStart.setDescription("A coldStart trap signifies that the sending protocol entity is reinitializing itself such that the agent's configuration or the protocol entity implementation may be altered.")
linkDown = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,2)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: linkDown.setDescription("A linkDown trap signifies that the sending protocol entity recognizes a failure in one of the communication links represented in the agent's configuration.")
linkUp = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,3)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: linkUp.setDescription("A linkUp trap signifies that the sending protocol entity recognizes that one of the communication links represented in the agent's configuration has come up.")
authenticationFailure = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,4))
if mibBuilder.loadTexts: authenticationFailure.setDescription('An authenticationFailure trap signifies that the sending protocol entity is the addressee of a protocol message that is not properly authenticated. While implementations of the SNMP must be capable of generating this trap, they must also be capable of suppressing the emission of such traps via an implementation-specific mechanism.')
pgDSLAMchassisPowerSupplyFailure = NotificationType((1, 3, 6, 1, 4, 1, 927, 1, 9) + (0,0)).setObjects(("PAIRGAIN-DSLAM-CHASSIS-MIB", "pgDSLAMChassisPsStatus"))
if mibBuilder.loadTexts: pgDSLAMchassisPowerSupplyFailure.setDescription('Power supply failure.')
pgDSLAMchassisFanFailure = NotificationType((1, 3, 6, 1, 4, 1, 927, 1, 9) + (0,1)).setObjects(("PAIRGAIN-DSLAM-CHASSIS-MIB", "pgDSLAMChassisFanStatus"))
if mibBuilder.loadTexts: pgDSLAMchassisFanFailure.setDescription('Fan failure.')
pgDSLAMchassisConfigChange = NotificationType((1, 3, 6, 1, 4, 1, 927, 1, 9) + (0,2)).setObjects(("PAIRGAIN-DSLAM-CHASSIS-MIB", "pgDSLAMConfigChangeCnts"), ("PAIRGAIN-DSLAM-CHASSIS-MIB", "pgDSLAMConfigLastChange"))
if mibBuilder.loadTexts: pgDSLAMchassisConfigChange.setDescription('General configuration change detected.')
pgDSLAMchassisTemperatureThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 927, 1, 9) + (0,3))
if mibBuilder.loadTexts: pgDSLAMchassisTemperatureThresholdExceeded.setDescription('Temperature Threshold Exceeded.')
pgDSLAMHDSLESThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 927, 1, 9) + (0,4)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pgDSLAMHDSLESThresholdExceeded.setDescription('HDSL ES Threshold Exceeded.')
pgDSLAMHDSLMarginThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 927, 1, 9) + (0,5)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pgDSLAMHDSLMarginThresholdExceeded.setDescription('HDSL Margin Threshold Exceeded.')
pgDSLAMHDSLPFO = NotificationType((1, 3, 6, 1, 4, 1, 927, 1, 9) + (0,6)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pgDSLAMHDSLPFO.setDescription('HDSL Power Feed Open.')
pgDSLAMHDSLPFS = NotificationType((1, 3, 6, 1, 4, 1, 927, 1, 9) + (0,7)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pgDSLAMHDSLPFS.setDescription('HDSL Power Feed Short.')
mibBuilder.exportSymbols("PAIRGAIN-DSLAM-TRAP-MIB", pgDSLAMHDSLPFO=pgDSLAMHDSLPFO, linkDown=linkDown, pgDSLAMchassisPowerSupplyFailure=pgDSLAMchassisPowerSupplyFailure, pgDSLAMHDSLMarginThresholdExceeded=pgDSLAMHDSLMarginThresholdExceeded, pgDSLAMHDSLPFS=pgDSLAMHDSLPFS, pgDSLAMchassisConfigChange=pgDSLAMchassisConfigChange, authenticationFailure=authenticationFailure, pgDSLAMchassisTemperatureThresholdExceeded=pgDSLAMchassisTemperatureThresholdExceeded, linkUp=linkUp, coldStart=coldStart, pgDSLAMchassisFanFailure=pgDSLAMchassisFanFailure, pgDSLAMHDSLESThresholdExceeded=pgDSLAMHDSLESThresholdExceeded)
