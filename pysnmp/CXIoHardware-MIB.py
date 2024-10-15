# SNMP MIB module (CXIoHardware-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXIoHardware-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:33 2024
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

(Alias,
 cxIoHardware) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "cxIoHardware")

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

_CxIoCardAdmTable_Object = MibTable
cxIoCardAdmTable = _CxIoCardAdmTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    cxIoCardAdmTable.setStatus("mandatory")
_CxIoCardAdmEntry_Object = MibTableRow
cxIoCardAdmEntry = _CxIoCardAdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 1, 1)
)
cxIoCardAdmEntry.setIndexNames(
    (0, "CXIoHardware-MIB", "cxIoCardAdmIndex"),
)
if mibBuilder.loadTexts:
    cxIoCardAdmEntry.setStatus("mandatory")
_CxIoCardAdmIndex_Type = Integer32
_CxIoCardAdmIndex_Object = MibTableColumn
cxIoCardAdmIndex = _CxIoCardAdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 1, 1, 1),
    _CxIoCardAdmIndex_Type()
)
cxIoCardAdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxIoCardAdmIndex.setStatus("mandatory")


class _CxIoCardAdmRowStatus_Type(Integer32):
    """Custom type cxIoCardAdmRowStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("invalid", 1),
          ("valid", 2))
    )


_CxIoCardAdmRowStatus_Type.__name__ = "Integer32"
_CxIoCardAdmRowStatus_Object = MibTableColumn
cxIoCardAdmRowStatus = _CxIoCardAdmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 1, 1, 2),
    _CxIoCardAdmRowStatus_Type()
)
cxIoCardAdmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxIoCardAdmRowStatus.setStatus("mandatory")
_CxIoCardAdmAlias_Type = Alias
_CxIoCardAdmAlias_Object = MibTableColumn
cxIoCardAdmAlias = _CxIoCardAdmAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 1, 1, 3),
    _CxIoCardAdmAlias_Type()
)
cxIoCardAdmAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxIoCardAdmAlias.setStatus("mandatory")
_CxIoCardAdmPhysSlot_Type = Integer32
_CxIoCardAdmPhysSlot_Object = MibTableColumn
cxIoCardAdmPhysSlot = _CxIoCardAdmPhysSlot_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 1, 1, 4),
    _CxIoCardAdmPhysSlot_Type()
)
cxIoCardAdmPhysSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxIoCardAdmPhysSlot.setStatus("mandatory")


class _CxIoCardAdmType_Type(Integer32):
    """Custom type cxIoCardAdmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("digitalVceCmpCard", 7),
          ("ethernetCard", 5),
          ("highSpeedFr4LIDCard", 8),
          ("isdnCard", 6),
          ("iuscFourPortCard", 1),
          ("lanCard", 2),
          ("octalV34ModemCard", 9),
          ("tokenRingCard", 4),
          ("vceCmpCard", 3))
    )


_CxIoCardAdmType_Type.__name__ = "Integer32"
_CxIoCardAdmType_Object = MibTableColumn
cxIoCardAdmType = _CxIoCardAdmType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 1, 1, 5),
    _CxIoCardAdmType_Type()
)
cxIoCardAdmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxIoCardAdmType.setStatus("mandatory")


class _CxIoCardAdmState_Type(Integer32):
    """Custom type cxIoCardAdmState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_CxIoCardAdmState_Type.__name__ = "Integer32"
_CxIoCardAdmState_Object = MibTableColumn
cxIoCardAdmState = _CxIoCardAdmState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 1, 1, 6),
    _CxIoCardAdmState_Type()
)
cxIoCardAdmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxIoCardAdmState.setStatus("mandatory")
_CxIoPortAdmTable_Object = MibTable
cxIoPortAdmTable = _CxIoPortAdmTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    cxIoPortAdmTable.setStatus("mandatory")
_CxIoPortAdmEntry_Object = MibTableRow
cxIoPortAdmEntry = _CxIoPortAdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 2, 1)
)
cxIoPortAdmEntry.setIndexNames(
    (0, "CXIoHardware-MIB", "cxIoPortAdmIndex"),
)
if mibBuilder.loadTexts:
    cxIoPortAdmEntry.setStatus("mandatory")
_CxIoPortAdmIndex_Type = Integer32
_CxIoPortAdmIndex_Object = MibTableColumn
cxIoPortAdmIndex = _CxIoPortAdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 2, 1, 1),
    _CxIoPortAdmIndex_Type()
)
cxIoPortAdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxIoPortAdmIndex.setStatus("mandatory")


class _CxIoPortAdmRowStatus_Type(Integer32):
    """Custom type cxIoPortAdmRowStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("invalid", 1),
          ("valid", 2))
    )


_CxIoPortAdmRowStatus_Type.__name__ = "Integer32"
_CxIoPortAdmRowStatus_Object = MibTableColumn
cxIoPortAdmRowStatus = _CxIoPortAdmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 2, 1, 2),
    _CxIoPortAdmRowStatus_Type()
)
cxIoPortAdmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxIoPortAdmRowStatus.setStatus("mandatory")
_CxIoPortAdmAlias_Type = Alias
_CxIoPortAdmAlias_Object = MibTableColumn
cxIoPortAdmAlias = _CxIoPortAdmAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 2, 1, 3),
    _CxIoPortAdmAlias_Type()
)
cxIoPortAdmAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxIoPortAdmAlias.setStatus("mandatory")
_CxIoPortAdmCardAlias_Type = Alias
_CxIoPortAdmCardAlias_Object = MibTableColumn
cxIoPortAdmCardAlias = _CxIoPortAdmCardAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 2, 1, 4),
    _CxIoPortAdmCardAlias_Type()
)
cxIoPortAdmCardAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxIoPortAdmCardAlias.setStatus("mandatory")
_CxIoPortAdmCardLocalIndex_Type = Integer32
_CxIoPortAdmCardLocalIndex_Object = MibTableColumn
cxIoPortAdmCardLocalIndex = _CxIoPortAdmCardLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 2, 1, 5),
    _CxIoPortAdmCardLocalIndex_Type()
)
cxIoPortAdmCardLocalIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxIoPortAdmCardLocalIndex.setStatus("mandatory")
_CxIoCardOperTable_Object = MibTable
cxIoCardOperTable = _CxIoCardOperTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    cxIoCardOperTable.setStatus("mandatory")
_CxIoCardOperEntry_Object = MibTableRow
cxIoCardOperEntry = _CxIoCardOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 3, 1)
)
cxIoCardOperEntry.setIndexNames(
    (0, "CXIoHardware-MIB", "cxIoCardOperPhysSlot"),
)
if mibBuilder.loadTexts:
    cxIoCardOperEntry.setStatus("mandatory")
_CxIoCardOperPhysSlot_Type = Integer32
_CxIoCardOperPhysSlot_Object = MibTableColumn
cxIoCardOperPhysSlot = _CxIoCardOperPhysSlot_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 3, 1, 1),
    _CxIoCardOperPhysSlot_Type()
)
cxIoCardOperPhysSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxIoCardOperPhysSlot.setStatus("mandatory")


class _CxIoCardOperState_Type(Integer32):
    """Custom type cxIoCardOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_CxIoCardOperState_Type.__name__ = "Integer32"
_CxIoCardOperState_Object = MibTableColumn
cxIoCardOperState = _CxIoCardOperState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 3, 1, 2),
    _CxIoCardOperState_Type()
)
cxIoCardOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxIoCardOperState.setStatus("mandatory")


class _CxIoCardOperType_Type(Integer32):
    """Custom type cxIoCardOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              255)
        )
    )
    namedValues = NamedValues(
        *(("digitalVceCmpCard", 7),
          ("ethernetCard", 5),
          ("highSpeedFr4LIDCard", 8),
          ("isdnCard", 6),
          ("iuscFourPortCard", 1),
          ("lanCard", 2),
          ("octalV34ModemCard", 9),
          ("other", 255),
          ("tokenRingCard", 4),
          ("vceCmpCard", 3))
    )


_CxIoCardOperType_Type.__name__ = "Integer32"
_CxIoCardOperType_Object = MibTableColumn
cxIoCardOperType = _CxIoCardOperType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 3, 1, 3),
    _CxIoCardOperType_Type()
)
cxIoCardOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxIoCardOperType.setStatus("mandatory")
_CxIoCardOperRevision_Type = Integer32
_CxIoCardOperRevision_Object = MibTableColumn
cxIoCardOperRevision = _CxIoCardOperRevision_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 3, 1, 4),
    _CxIoCardOperRevision_Type()
)
cxIoCardOperRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxIoCardOperRevision.setStatus("mandatory")
_CxIoCardOperAssemblyAndEco_Type = Integer32
_CxIoCardOperAssemblyAndEco_Object = MibTableColumn
cxIoCardOperAssemblyAndEco = _CxIoCardOperAssemblyAndEco_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 3, 1, 5),
    _CxIoCardOperAssemblyAndEco_Type()
)
cxIoCardOperAssemblyAndEco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxIoCardOperAssemblyAndEco.setStatus("mandatory")
_CxIoCardOperSpecialEco_Type = Integer32
_CxIoCardOperSpecialEco_Object = MibTableColumn
cxIoCardOperSpecialEco = _CxIoCardOperSpecialEco_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 3, 1, 6),
    _CxIoCardOperSpecialEco_Type()
)
cxIoCardOperSpecialEco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxIoCardOperSpecialEco.setStatus("mandatory")


class _CxIoHwCardTypeTrapReport_Type(Integer32):
    """Custom type cxIoHwCardTypeTrapReport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CxIoHwCardTypeTrapReport_Type.__name__ = "Integer32"
_CxIoHwCardTypeTrapReport_Object = MibScalar
cxIoHwCardTypeTrapReport = _CxIoHwCardTypeTrapReport_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 4),
    _CxIoHwCardTypeTrapReport_Type()
)
cxIoHwCardTypeTrapReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxIoHwCardTypeTrapReport.setStatus("mandatory")


class _CxIHMibLevel_Type(Integer32):
    """Custom type cxIHMibLevel based on Integer32"""
    defaultValue = 0


_CxIHMibLevel_Object = MibScalar
cxIHMibLevel = _CxIHMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 5),
    _CxIHMibLevel_Type()
)
cxIHMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxIHMibLevel.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cxIoHwCardTypeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2, 0, 1)
)
cxIoHwCardTypeTrap.setObjects(
      *(("CXIoHardware-MIB", "cxIoCardOperPhysSlot"),
        ("CXIoHardware-MIB", "cxIoCardOperState"),
        ("CXIoHardware-MIB", "cxIoCardOperType"))
)
if mibBuilder.loadTexts:
    cxIoHwCardTypeTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXIoHardware-MIB",
    **{"cxIoHwCardTypeTrap": cxIoHwCardTypeTrap,
       "cxIoCardAdmTable": cxIoCardAdmTable,
       "cxIoCardAdmEntry": cxIoCardAdmEntry,
       "cxIoCardAdmIndex": cxIoCardAdmIndex,
       "cxIoCardAdmRowStatus": cxIoCardAdmRowStatus,
       "cxIoCardAdmAlias": cxIoCardAdmAlias,
       "cxIoCardAdmPhysSlot": cxIoCardAdmPhysSlot,
       "cxIoCardAdmType": cxIoCardAdmType,
       "cxIoCardAdmState": cxIoCardAdmState,
       "cxIoPortAdmTable": cxIoPortAdmTable,
       "cxIoPortAdmEntry": cxIoPortAdmEntry,
       "cxIoPortAdmIndex": cxIoPortAdmIndex,
       "cxIoPortAdmRowStatus": cxIoPortAdmRowStatus,
       "cxIoPortAdmAlias": cxIoPortAdmAlias,
       "cxIoPortAdmCardAlias": cxIoPortAdmCardAlias,
       "cxIoPortAdmCardLocalIndex": cxIoPortAdmCardLocalIndex,
       "cxIoCardOperTable": cxIoCardOperTable,
       "cxIoCardOperEntry": cxIoCardOperEntry,
       "cxIoCardOperPhysSlot": cxIoCardOperPhysSlot,
       "cxIoCardOperState": cxIoCardOperState,
       "cxIoCardOperType": cxIoCardOperType,
       "cxIoCardOperRevision": cxIoCardOperRevision,
       "cxIoCardOperAssemblyAndEco": cxIoCardOperAssemblyAndEco,
       "cxIoCardOperSpecialEco": cxIoCardOperSpecialEco,
       "cxIoHwCardTypeTrapReport": cxIoHwCardTypeTrapReport,
       "cxIHMibLevel": cxIHMibLevel}
)
