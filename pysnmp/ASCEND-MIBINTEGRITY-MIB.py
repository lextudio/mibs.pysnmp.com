# SNMP MIB module (ASCEND-MIBINTEGRITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBINTEGRITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:43 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibsystemIntegrityProfile_ObjectIdentity = ObjectIdentity
mibsystemIntegrityProfile = _MibsystemIntegrityProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 81)
)
_MibsystemIntegrityProfileTable_Object = MibTable
mibsystemIntegrityProfileTable = _MibsystemIntegrityProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 81, 1)
)
if mibBuilder.loadTexts:
    mibsystemIntegrityProfileTable.setStatus("mandatory")
_MibsystemIntegrityProfileEntry_Object = MibTableRow
mibsystemIntegrityProfileEntry = _MibsystemIntegrityProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 81, 1, 1)
)
mibsystemIntegrityProfileEntry.setIndexNames(
    (0, "ASCEND-MIBINTEGRITY-MIB", "systemIntegrityProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibsystemIntegrityProfileEntry.setStatus("mandatory")
_SystemIntegrityProfile_Index_o_Type = Integer32
_SystemIntegrityProfile_Index_o_Object = MibScalar
systemIntegrityProfile_Index_o = _SystemIntegrityProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 81, 1, 1, 1),
    _SystemIntegrityProfile_Index_o_Type()
)
systemIntegrityProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemIntegrityProfile_Index_o.setStatus("mandatory")


class _SystemIntegrityProfile_EnableCentralizedDetection_Type(Integer32):
    """Custom type systemIntegrityProfile_EnableCentralizedDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SystemIntegrityProfile_EnableCentralizedDetection_Type.__name__ = "Integer32"
_SystemIntegrityProfile_EnableCentralizedDetection_Object = MibScalar
systemIntegrityProfile_EnableCentralizedDetection = _SystemIntegrityProfile_EnableCentralizedDetection_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 81, 1, 1, 2),
    _SystemIntegrityProfile_EnableCentralizedDetection_Type()
)
systemIntegrityProfile_EnableCentralizedDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemIntegrityProfile_EnableCentralizedDetection.setStatus("mandatory")
_SystemIntegrityProfile_RatioCentralizedDetection_Type = Integer32
_SystemIntegrityProfile_RatioCentralizedDetection_Object = MibScalar
systemIntegrityProfile_RatioCentralizedDetection = _SystemIntegrityProfile_RatioCentralizedDetection_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 81, 1, 1, 3),
    _SystemIntegrityProfile_RatioCentralizedDetection_Type()
)
systemIntegrityProfile_RatioCentralizedDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemIntegrityProfile_RatioCentralizedDetection.setStatus("mandatory")


class _SystemIntegrityProfile_Action_o_Type(Integer32):
    """Custom type systemIntegrityProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_SystemIntegrityProfile_Action_o_Type.__name__ = "Integer32"
_SystemIntegrityProfile_Action_o_Object = MibScalar
systemIntegrityProfile_Action_o = _SystemIntegrityProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 81, 1, 1, 4),
    _SystemIntegrityProfile_Action_o_Type()
)
systemIntegrityProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemIntegrityProfile_Action_o.setStatus("mandatory")
_MibsystemIntegrityProfile_IntegrityConfigTable_Object = MibTable
mibsystemIntegrityProfile_IntegrityConfigTable = _MibsystemIntegrityProfile_IntegrityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 81, 2)
)
if mibBuilder.loadTexts:
    mibsystemIntegrityProfile_IntegrityConfigTable.setStatus("mandatory")
_MibsystemIntegrityProfile_IntegrityConfigEntry_Object = MibTableRow
mibsystemIntegrityProfile_IntegrityConfigEntry = _MibsystemIntegrityProfile_IntegrityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 81, 2, 1)
)
mibsystemIntegrityProfile_IntegrityConfigEntry.setIndexNames(
    (0, "ASCEND-MIBINTEGRITY-MIB", "systemIntegrityProfile-IntegrityConfig-Index-o"),
    (0, "ASCEND-MIBINTEGRITY-MIB", "systemIntegrityProfile-IntegrityConfig-Index1-o"),
)
if mibBuilder.loadTexts:
    mibsystemIntegrityProfile_IntegrityConfigEntry.setStatus("mandatory")
_SystemIntegrityProfile_IntegrityConfig_Index_o_Type = Integer32
_SystemIntegrityProfile_IntegrityConfig_Index_o_Object = MibScalar
systemIntegrityProfile_IntegrityConfig_Index_o = _SystemIntegrityProfile_IntegrityConfig_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 81, 2, 1, 1),
    _SystemIntegrityProfile_IntegrityConfig_Index_o_Type()
)
systemIntegrityProfile_IntegrityConfig_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemIntegrityProfile_IntegrityConfig_Index_o.setStatus("mandatory")
_SystemIntegrityProfile_IntegrityConfig_Index1_o_Type = Integer32
_SystemIntegrityProfile_IntegrityConfig_Index1_o_Object = MibScalar
systemIntegrityProfile_IntegrityConfig_Index1_o = _SystemIntegrityProfile_IntegrityConfig_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 81, 2, 1, 2),
    _SystemIntegrityProfile_IntegrityConfig_Index1_o_Type()
)
systemIntegrityProfile_IntegrityConfig_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemIntegrityProfile_IntegrityConfig_Index1_o.setStatus("mandatory")


class _SystemIntegrityProfile_IntegrityConfig_EnableContinuousDetection_Type(Integer32):
    """Custom type systemIntegrityProfile_IntegrityConfig_EnableContinuousDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SystemIntegrityProfile_IntegrityConfig_EnableContinuousDetection_Type.__name__ = "Integer32"
_SystemIntegrityProfile_IntegrityConfig_EnableContinuousDetection_Object = MibScalar
systemIntegrityProfile_IntegrityConfig_EnableContinuousDetection = _SystemIntegrityProfile_IntegrityConfig_EnableContinuousDetection_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 81, 2, 1, 3),
    _SystemIntegrityProfile_IntegrityConfig_EnableContinuousDetection_Type()
)
systemIntegrityProfile_IntegrityConfig_EnableContinuousDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemIntegrityProfile_IntegrityConfig_EnableContinuousDetection.setStatus("mandatory")
_SystemIntegrityProfile_IntegrityConfig_DetectionInterval_Type = Integer32
_SystemIntegrityProfile_IntegrityConfig_DetectionInterval_Object = MibScalar
systemIntegrityProfile_IntegrityConfig_DetectionInterval = _SystemIntegrityProfile_IntegrityConfig_DetectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 81, 2, 1, 4),
    _SystemIntegrityProfile_IntegrityConfig_DetectionInterval_Type()
)
systemIntegrityProfile_IntegrityConfig_DetectionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemIntegrityProfile_IntegrityConfig_DetectionInterval.setStatus("mandatory")


class _SystemIntegrityProfile_IntegrityConfig_OnlyOneCorrection_Type(Integer32):
    """Custom type systemIntegrityProfile_IntegrityConfig_OnlyOneCorrection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SystemIntegrityProfile_IntegrityConfig_OnlyOneCorrection_Type.__name__ = "Integer32"
_SystemIntegrityProfile_IntegrityConfig_OnlyOneCorrection_Object = MibScalar
systemIntegrityProfile_IntegrityConfig_OnlyOneCorrection = _SystemIntegrityProfile_IntegrityConfig_OnlyOneCorrection_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 81, 2, 1, 5),
    _SystemIntegrityProfile_IntegrityConfig_OnlyOneCorrection_Type()
)
systemIntegrityProfile_IntegrityConfig_OnlyOneCorrection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemIntegrityProfile_IntegrityConfig_OnlyOneCorrection.setStatus("mandatory")
_SystemIntegrityProfile_IntegrityConfig_CorrectionFactor_Type = Integer32
_SystemIntegrityProfile_IntegrityConfig_CorrectionFactor_Object = MibScalar
systemIntegrityProfile_IntegrityConfig_CorrectionFactor = _SystemIntegrityProfile_IntegrityConfig_CorrectionFactor_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 81, 2, 1, 6),
    _SystemIntegrityProfile_IntegrityConfig_CorrectionFactor_Type()
)
systemIntegrityProfile_IntegrityConfig_CorrectionFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemIntegrityProfile_IntegrityConfig_CorrectionFactor.setStatus("mandatory")


class _SystemIntegrityProfile_IntegrityConfig_AutoCorrectionEnable_Type(Integer32):
    """Custom type systemIntegrityProfile_IntegrityConfig_AutoCorrectionEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SystemIntegrityProfile_IntegrityConfig_AutoCorrectionEnable_Type.__name__ = "Integer32"
_SystemIntegrityProfile_IntegrityConfig_AutoCorrectionEnable_Object = MibScalar
systemIntegrityProfile_IntegrityConfig_AutoCorrectionEnable = _SystemIntegrityProfile_IntegrityConfig_AutoCorrectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 81, 2, 1, 7),
    _SystemIntegrityProfile_IntegrityConfig_AutoCorrectionEnable_Type()
)
systemIntegrityProfile_IntegrityConfig_AutoCorrectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemIntegrityProfile_IntegrityConfig_AutoCorrectionEnable.setStatus("mandatory")
_SystemIntegrityProfile_IntegrityConfig_IntervalAutoCorrection_Type = Integer32
_SystemIntegrityProfile_IntegrityConfig_IntervalAutoCorrection_Object = MibScalar
systemIntegrityProfile_IntegrityConfig_IntervalAutoCorrection = _SystemIntegrityProfile_IntegrityConfig_IntervalAutoCorrection_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 81, 2, 1, 8),
    _SystemIntegrityProfile_IntegrityConfig_IntervalAutoCorrection_Type()
)
systemIntegrityProfile_IntegrityConfig_IntervalAutoCorrection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemIntegrityProfile_IntegrityConfig_IntervalAutoCorrection.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBINTEGRITY-MIB",
    **{"DisplayString": DisplayString,
       "mibsystemIntegrityProfile": mibsystemIntegrityProfile,
       "mibsystemIntegrityProfileTable": mibsystemIntegrityProfileTable,
       "mibsystemIntegrityProfileEntry": mibsystemIntegrityProfileEntry,
       "systemIntegrityProfile-Index-o": systemIntegrityProfile_Index_o,
       "systemIntegrityProfile-EnableCentralizedDetection": systemIntegrityProfile_EnableCentralizedDetection,
       "systemIntegrityProfile-RatioCentralizedDetection": systemIntegrityProfile_RatioCentralizedDetection,
       "systemIntegrityProfile-Action-o": systemIntegrityProfile_Action_o,
       "mibsystemIntegrityProfile-IntegrityConfigTable": mibsystemIntegrityProfile_IntegrityConfigTable,
       "mibsystemIntegrityProfile-IntegrityConfigEntry": mibsystemIntegrityProfile_IntegrityConfigEntry,
       "systemIntegrityProfile-IntegrityConfig-Index-o": systemIntegrityProfile_IntegrityConfig_Index_o,
       "systemIntegrityProfile-IntegrityConfig-Index1-o": systemIntegrityProfile_IntegrityConfig_Index1_o,
       "systemIntegrityProfile-IntegrityConfig-EnableContinuousDetection": systemIntegrityProfile_IntegrityConfig_EnableContinuousDetection,
       "systemIntegrityProfile-IntegrityConfig-DetectionInterval": systemIntegrityProfile_IntegrityConfig_DetectionInterval,
       "systemIntegrityProfile-IntegrityConfig-OnlyOneCorrection": systemIntegrityProfile_IntegrityConfig_OnlyOneCorrection,
       "systemIntegrityProfile-IntegrityConfig-CorrectionFactor": systemIntegrityProfile_IntegrityConfig_CorrectionFactor,
       "systemIntegrityProfile-IntegrityConfig-AutoCorrectionEnable": systemIntegrityProfile_IntegrityConfig_AutoCorrectionEnable,
       "systemIntegrityProfile-IntegrityConfig-IntervalAutoCorrection": systemIntegrityProfile_IntegrityConfig_IntervalAutoCorrection}
)
