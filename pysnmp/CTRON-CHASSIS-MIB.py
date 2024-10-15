# SNMP MIB module (CTRON-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:38 2024
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

(ctronChassis,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctronChassis")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtChas_ObjectIdentity = ObjectIdentity
ctChas = _CtChas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 1)
)


class _CtChasFNB_Type(Integer32):
    """Custom type ctChasFNB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("present", 2))
    )


_CtChasFNB_Type.__name__ = "Integer32"
_CtChasFNB_Object = MibScalar
ctChasFNB = _CtChasFNB_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 1, 1),
    _CtChasFNB_Type()
)
ctChasFNB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctChasFNB.setStatus("mandatory")


class _CtChasAlarmEna_Type(Integer32):
    """Custom type ctChasAlarmEna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("notSupported", 3))
    )


_CtChasAlarmEna_Type.__name__ = "Integer32"
_CtChasAlarmEna_Object = MibScalar
ctChasAlarmEna = _CtChasAlarmEna_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 1, 2),
    _CtChasAlarmEna_Type()
)
ctChasAlarmEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctChasAlarmEna.setStatus("mandatory")


class _ChassisAlarmState_Type(Integer32):
    """Custom type chassisAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chassisFaultCondition", 2),
          ("chassisNoFaultCondition", 1),
          ("notSupported", 3))
    )


_ChassisAlarmState_Type.__name__ = "Integer32"
_ChassisAlarmState_Object = MibScalar
chassisAlarmState = _ChassisAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 1, 3),
    _ChassisAlarmState_Type()
)
chassisAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisAlarmState.setStatus("mandatory")
_CtEnviron_ObjectIdentity = ObjectIdentity
ctEnviron = _CtEnviron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 2)
)
_CtChasPowerTable_Object = MibTable
ctChasPowerTable = _CtChasPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ctChasPowerTable.setStatus("mandatory")
_CtChasPowerEntry_Object = MibTableRow
ctChasPowerEntry = _CtChasPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 2, 1, 1)
)
ctChasPowerEntry.setIndexNames(
    (0, "CTRON-CHASSIS-MIB", "ctChasPowerSupplyNum"),
)
if mibBuilder.loadTexts:
    ctChasPowerEntry.setStatus("mandatory")
_CtChasPowerSupplyNum_Type = Integer32
_CtChasPowerSupplyNum_Object = MibTableColumn
ctChasPowerSupplyNum = _CtChasPowerSupplyNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 2, 1, 1, 1),
    _CtChasPowerSupplyNum_Type()
)
ctChasPowerSupplyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctChasPowerSupplyNum.setStatus("mandatory")


class _CtChasPowerSupplyState_Type(Integer32):
    """Custom type ctChasPowerSupplyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("infoNotAvailable", 1),
          ("installedAndNotOperating", 4),
          ("installedAndOperating", 3),
          ("notInstalled", 2))
    )


_CtChasPowerSupplyState_Type.__name__ = "Integer32"
_CtChasPowerSupplyState_Object = MibTableColumn
ctChasPowerSupplyState = _CtChasPowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 2, 1, 1, 2),
    _CtChasPowerSupplyState_Type()
)
ctChasPowerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctChasPowerSupplyState.setStatus("mandatory")


class _CtChasPowerSupplyType_Type(Integer32):
    """Custom type ctChasPowerSupplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ac-dc", 1),
          ("dc-dc", 2),
          ("highOutput", 4),
          ("notSupported", 3))
    )


_CtChasPowerSupplyType_Type.__name__ = "Integer32"
_CtChasPowerSupplyType_Object = MibTableColumn
ctChasPowerSupplyType = _CtChasPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 2, 1, 1, 3),
    _CtChasPowerSupplyType_Type()
)
ctChasPowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctChasPowerSupplyType.setStatus("mandatory")


class _CtChasPowerSupplyRedundancy_Type(Integer32):
    """Custom type ctChasPowerSupplyRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRedundant", 2),
          ("notSupported", 3),
          ("redundant", 1))
    )


_CtChasPowerSupplyRedundancy_Type.__name__ = "Integer32"
_CtChasPowerSupplyRedundancy_Object = MibTableColumn
ctChasPowerSupplyRedundancy = _CtChasPowerSupplyRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 2, 1, 1, 4),
    _CtChasPowerSupplyRedundancy_Type()
)
ctChasPowerSupplyRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctChasPowerSupplyRedundancy.setStatus("mandatory")
_CtFanModule_ObjectIdentity = ObjectIdentity
ctFanModule = _CtFanModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 3)
)
_CtChasFanModuleTable_Object = MibTable
ctChasFanModuleTable = _CtChasFanModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ctChasFanModuleTable.setStatus("mandatory")
_CtChasFanModuleEntry_Object = MibTableRow
ctChasFanModuleEntry = _CtChasFanModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 3, 1, 1)
)
ctChasFanModuleEntry.setIndexNames(
    (0, "CTRON-CHASSIS-MIB", "ctChasFanModuleNum"),
)
if mibBuilder.loadTexts:
    ctChasFanModuleEntry.setStatus("mandatory")
_CtChasFanModuleNum_Type = Integer32
_CtChasFanModuleNum_Object = MibTableColumn
ctChasFanModuleNum = _CtChasFanModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 3, 1, 1, 1),
    _CtChasFanModuleNum_Type()
)
ctChasFanModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctChasFanModuleNum.setStatus("mandatory")


class _CtChasFanModuleState_Type(Integer32):
    """Custom type ctChasFanModuleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("infoNotAvailable", 1),
          ("installedAndNotOperating", 4),
          ("installedAndOperating", 3),
          ("notInstalled", 2))
    )


_CtChasFanModuleState_Type.__name__ = "Integer32"
_CtChasFanModuleState_Object = MibTableColumn
ctChasFanModuleState = _CtChasFanModuleState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 3, 1, 1, 2),
    _CtChasFanModuleState_Type()
)
ctChasFanModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctChasFanModuleState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-CHASSIS-MIB",
    **{"ctChas": ctChas,
       "ctChasFNB": ctChasFNB,
       "ctChasAlarmEna": ctChasAlarmEna,
       "chassisAlarmState": chassisAlarmState,
       "ctEnviron": ctEnviron,
       "ctChasPowerTable": ctChasPowerTable,
       "ctChasPowerEntry": ctChasPowerEntry,
       "ctChasPowerSupplyNum": ctChasPowerSupplyNum,
       "ctChasPowerSupplyState": ctChasPowerSupplyState,
       "ctChasPowerSupplyType": ctChasPowerSupplyType,
       "ctChasPowerSupplyRedundancy": ctChasPowerSupplyRedundancy,
       "ctFanModule": ctFanModule,
       "ctChasFanModuleTable": ctChasFanModuleTable,
       "ctChasFanModuleEntry": ctChasFanModuleEntry,
       "ctChasFanModuleNum": ctChasFanModuleNum,
       "ctChasFanModuleState": ctChasFanModuleState}
)
