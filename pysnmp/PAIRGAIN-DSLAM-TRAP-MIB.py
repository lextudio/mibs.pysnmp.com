# SNMP MIB module (PAIRGAIN-DSLAM-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PAIRGAIN-DSLAM-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:21 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pgainDSLAM,) = mibBuilder.importSymbols(
    "PAIRGAIN-COMMON-HD-MIB",
    "pgainDSLAM")

(pgDSLAMChassisFanStatus,
 pgDSLAMChassisPsStatus,
 pgDSLAMChassisTemperature,
 pgDSLAMConfigChangeCnts,
 pgDSLAMConfigLastChange) = mibBuilder.importSymbols(
    "PAIRGAIN-DSLAM-CHASSIS-MIB",
    "pgDSLAMChassisFanStatus",
    "pgDSLAMChassisPsStatus",
    "pgDSLAMChassisTemperature",
    "pgDSLAMConfigChangeCnts",
    "pgDSLAMConfigLastChange")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(snmp,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmp")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

coldStart = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 0)
)
if mibBuilder.loadTexts:
    coldStart.setStatus(
        ""
    )

linkDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 2)
)
linkDown.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    linkDown.setStatus(
        ""
    )

linkUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 3)
)
linkUp.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    linkUp.setStatus(
        ""
    )

authenticationFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 4)
)
if mibBuilder.loadTexts:
    authenticationFailure.setStatus(
        ""
    )

pgDSLAMchassisPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 0, 0)
)
pgDSLAMchassisPowerSupplyFailure.setObjects(
    ("PAIRGAIN-DSLAM-CHASSIS-MIB", "pgDSLAMChassisPsStatus")
)
if mibBuilder.loadTexts:
    pgDSLAMchassisPowerSupplyFailure.setStatus(
        ""
    )

pgDSLAMchassisFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 0, 1)
)
pgDSLAMchassisFanFailure.setObjects(
    ("PAIRGAIN-DSLAM-CHASSIS-MIB", "pgDSLAMChassisFanStatus")
)
if mibBuilder.loadTexts:
    pgDSLAMchassisFanFailure.setStatus(
        ""
    )

pgDSLAMchassisConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 0, 2)
)
pgDSLAMchassisConfigChange.setObjects(
      *(("PAIRGAIN-DSLAM-CHASSIS-MIB", "pgDSLAMConfigChangeCnts"),
        ("PAIRGAIN-DSLAM-CHASSIS-MIB", "pgDSLAMConfigLastChange"))
)
if mibBuilder.loadTexts:
    pgDSLAMchassisConfigChange.setStatus(
        ""
    )

pgDSLAMchassisTemperatureThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 0, 3)
)
if mibBuilder.loadTexts:
    pgDSLAMchassisTemperatureThresholdExceeded.setStatus(
        ""
    )

pgDSLAMHDSLESThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 0, 4)
)
pgDSLAMHDSLESThresholdExceeded.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    pgDSLAMHDSLESThresholdExceeded.setStatus(
        ""
    )

pgDSLAMHDSLMarginThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 0, 5)
)
pgDSLAMHDSLMarginThresholdExceeded.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    pgDSLAMHDSLMarginThresholdExceeded.setStatus(
        ""
    )

pgDSLAMHDSLPFO = NotificationType(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 0, 6)
)
pgDSLAMHDSLPFO.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    pgDSLAMHDSLPFO.setStatus(
        ""
    )

pgDSLAMHDSLPFS = NotificationType(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 0, 7)
)
pgDSLAMHDSLPFS.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    pgDSLAMHDSLPFS.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAIRGAIN-DSLAM-TRAP-MIB",
    **{"coldStart": coldStart,
       "linkDown": linkDown,
       "linkUp": linkUp,
       "authenticationFailure": authenticationFailure,
       "pgDSLAMchassisPowerSupplyFailure": pgDSLAMchassisPowerSupplyFailure,
       "pgDSLAMchassisFanFailure": pgDSLAMchassisFanFailure,
       "pgDSLAMchassisConfigChange": pgDSLAMchassisConfigChange,
       "pgDSLAMchassisTemperatureThresholdExceeded": pgDSLAMchassisTemperatureThresholdExceeded,
       "pgDSLAMHDSLESThresholdExceeded": pgDSLAMHDSLESThresholdExceeded,
       "pgDSLAMHDSLMarginThresholdExceeded": pgDSLAMHDSLMarginThresholdExceeded,
       "pgDSLAMHDSLPFO": pgDSLAMHDSLPFO,
       "pgDSLAMHDSLPFS": pgDSLAMHDSLPFS}
)
