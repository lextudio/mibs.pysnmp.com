# SNMP MIB module (CISCO-ADAPTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ADAPTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:30 2024
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
 enterprises,
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
    "enterprises",
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

_Cisco_ObjectIdentity = ObjectIdentity
cisco = _Cisco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9)
)
_Workgroup_ObjectIdentity = ObjectIdentity
workgroup = _Workgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5)
)
_AdapterCard_ObjectIdentity = ObjectIdentity
adapterCard = _AdapterCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 2)
)


class _AdptrNumber_Type(Integer32):
    """Custom type adptrNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AdptrNumber_Type.__name__ = "Integer32"
_AdptrNumber_Object = MibScalar
adptrNumber = _AdptrNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 1),
    _AdptrNumber_Type()
)
adptrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adptrNumber.setStatus("mandatory")
_AdptrTable_Object = MibTable
adptrTable = _AdptrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 2)
)
if mibBuilder.loadTexts:
    adptrTable.setStatus("mandatory")
_AdptrEntry_Object = MibTableRow
adptrEntry = _AdptrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1)
)
adptrEntry.setIndexNames(
    (0, "CISCO-ADAPTER-MIB", "adptrIndex"),
)
if mibBuilder.loadTexts:
    adptrEntry.setStatus("mandatory")


class _AdptrIndex_Type(Integer32):
    """Custom type adptrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AdptrIndex_Type.__name__ = "Integer32"
_AdptrIndex_Object = MibTableColumn
adptrIndex = _AdptrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 1),
    _AdptrIndex_Type()
)
adptrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adptrIndex.setStatus("mandatory")


class _AdptrType_Type(Integer32):
    """Custom type adptrType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("eisaCddi", 8),
          ("eisaFddi", 10),
          ("mcaCddi", 5),
          ("mcaFddi", 7),
          ("mcaFddiSt", 6),
          ("other", 1),
          ("sBusCddi", 2),
          ("sBusFddi", 4),
          ("sBusFddiSt", 3))
    )


_AdptrType_Type.__name__ = "Integer32"
_AdptrType_Object = MibTableColumn
adptrType = _AdptrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 2),
    _AdptrType_Type()
)
adptrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adptrType.setStatus("mandatory")


class _AdptrSerialNumber_Type(Integer32):
    """Custom type adptrSerialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999999),
    )


_AdptrSerialNumber_Type.__name__ = "Integer32"
_AdptrSerialNumber_Object = MibTableColumn
adptrSerialNumber = _AdptrSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 3),
    _AdptrSerialNumber_Type()
)
adptrSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adptrSerialNumber.setStatus("mandatory")


class _AdptrHwHiVersion_Type(Integer32):
    """Custom type adptrHwHiVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdptrHwHiVersion_Type.__name__ = "Integer32"
_AdptrHwHiVersion_Object = MibTableColumn
adptrHwHiVersion = _AdptrHwHiVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 4),
    _AdptrHwHiVersion_Type()
)
adptrHwHiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adptrHwHiVersion.setStatus("mandatory")


class _AdptrHwLoVersion_Type(Integer32):
    """Custom type adptrHwLoVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdptrHwLoVersion_Type.__name__ = "Integer32"
_AdptrHwLoVersion_Object = MibTableColumn
adptrHwLoVersion = _AdptrHwLoVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 5),
    _AdptrHwLoVersion_Type()
)
adptrHwLoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adptrHwLoVersion.setStatus("mandatory")


class _AdptrFwHiVersion_Type(Integer32):
    """Custom type adptrFwHiVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdptrFwHiVersion_Type.__name__ = "Integer32"
_AdptrFwHiVersion_Object = MibTableColumn
adptrFwHiVersion = _AdptrFwHiVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 6),
    _AdptrFwHiVersion_Type()
)
adptrFwHiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adptrFwHiVersion.setStatus("mandatory")


class _AdptrFwLoVersion_Type(Integer32):
    """Custom type adptrFwLoVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdptrFwLoVersion_Type.__name__ = "Integer32"
_AdptrFwLoVersion_Object = MibTableColumn
adptrFwLoVersion = _AdptrFwLoVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 7),
    _AdptrFwLoVersion_Type()
)
adptrFwLoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adptrFwLoVersion.setStatus("mandatory")


class _AdptrSwHiVersion_Type(Integer32):
    """Custom type adptrSwHiVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdptrSwHiVersion_Type.__name__ = "Integer32"
_AdptrSwHiVersion_Object = MibTableColumn
adptrSwHiVersion = _AdptrSwHiVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 8),
    _AdptrSwHiVersion_Type()
)
adptrSwHiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adptrSwHiVersion.setStatus("mandatory")


class _AdptrSwLoVersion_Type(Integer32):
    """Custom type adptrSwLoVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdptrSwLoVersion_Type.__name__ = "Integer32"
_AdptrSwLoVersion_Object = MibTableColumn
adptrSwLoVersion = _AdptrSwLoVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 9),
    _AdptrSwLoVersion_Type()
)
adptrSwLoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adptrSwLoVersion.setStatus("mandatory")


class _AdptrStatus_Type(Integer32):
    """Custom type adptrStatus based on Integer32"""
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
        *(("majorFault", 4),
          ("minorFault", 3),
          ("ok", 2),
          ("other", 1))
    )


_AdptrStatus_Type.__name__ = "Integer32"
_AdptrStatus_Object = MibTableColumn
adptrStatus = _AdptrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 10),
    _AdptrStatus_Type()
)
adptrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adptrStatus.setStatus("mandatory")


class _AdptrSelfTestResult_Type(Integer32):
    """Custom type adptrSelfTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdptrSelfTestResult_Type.__name__ = "Integer32"
_AdptrSelfTestResult_Object = MibTableColumn
adptrSelfTestResult = _AdptrSelfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 11),
    _AdptrSelfTestResult_Type()
)
adptrSelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adptrSelfTestResult.setStatus("mandatory")


class _AdptrDriverHiVersion_Type(Integer32):
    """Custom type adptrDriverHiVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdptrDriverHiVersion_Type.__name__ = "Integer32"
_AdptrDriverHiVersion_Object = MibTableColumn
adptrDriverHiVersion = _AdptrDriverHiVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 13),
    _AdptrDriverHiVersion_Type()
)
adptrDriverHiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adptrDriverHiVersion.setStatus("mandatory")


class _AdptrDriverLoVersion_Type(Integer32):
    """Custom type adptrDriverLoVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdptrDriverLoVersion_Type.__name__ = "Integer32"
_AdptrDriverLoVersion_Object = MibTableColumn
adptrDriverLoVersion = _AdptrDriverLoVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 14),
    _AdptrDriverLoVersion_Type()
)
adptrDriverLoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adptrDriverLoVersion.setStatus("mandatory")


class _AdptrMediaType_Type(Integer32):
    """Custom type adptrMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cddi", 2),
          ("fiber", 3),
          ("mlt3", 5),
          ("other", 1),
          ("sddi", 6),
          ("smf", 7),
          ("tppmd", 4))
    )


_AdptrMediaType_Type.__name__ = "Integer32"
_AdptrMediaType_Object = MibTableColumn
adptrMediaType = _AdptrMediaType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 17),
    _AdptrMediaType_Type()
)
adptrMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adptrMediaType.setStatus("mandatory")


class _AdptrModel_Type(DisplayString):
    """Custom type adptrModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AdptrModel_Type.__name__ = "DisplayString"
_AdptrModel_Object = MibTableColumn
adptrModel = _AdptrModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 18),
    _AdptrModel_Type()
)
adptrModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adptrModel.setStatus("mandatory")
_AdptrTrapReceiverTable_Object = MibTable
adptrTrapReceiverTable = _AdptrTrapReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 3)
)
if mibBuilder.loadTexts:
    adptrTrapReceiverTable.setStatus("mandatory")
_AdptrTrapReceiverEntry_Object = MibTableRow
adptrTrapReceiverEntry = _AdptrTrapReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 3, 1)
)
adptrTrapReceiverEntry.setIndexNames(
    (0, "CISCO-ADAPTER-MIB", "adptrTrapReceiverAddr"),
)
if mibBuilder.loadTexts:
    adptrTrapReceiverEntry.setStatus("mandatory")


class _AdptrTrapReceiverType_Type(Integer32):
    """Custom type adptrTrapReceiverType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AdptrTrapReceiverType_Type.__name__ = "Integer32"
_AdptrTrapReceiverType_Object = MibTableColumn
adptrTrapReceiverType = _AdptrTrapReceiverType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 3, 1, 1),
    _AdptrTrapReceiverType_Type()
)
adptrTrapReceiverType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adptrTrapReceiverType.setStatus("mandatory")
_AdptrTrapReceiverAddr_Type = IpAddress
_AdptrTrapReceiverAddr_Object = MibTableColumn
adptrTrapReceiverAddr = _AdptrTrapReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 3, 1, 2),
    _AdptrTrapReceiverAddr_Type()
)
adptrTrapReceiverAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adptrTrapReceiverAddr.setStatus("mandatory")


class _AdptrTrapReceiverComm_Type(DisplayString):
    """Custom type adptrTrapReceiverComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AdptrTrapReceiverComm_Type.__name__ = "DisplayString"
_AdptrTrapReceiverComm_Object = MibTableColumn
adptrTrapReceiverComm = _AdptrTrapReceiverComm_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 3, 1, 3),
    _AdptrTrapReceiverComm_Type()
)
adptrTrapReceiverComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adptrTrapReceiverComm.setStatus("mandatory")
_AdptrCommunityTable_Object = MibTable
adptrCommunityTable = _AdptrCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 4)
)
if mibBuilder.loadTexts:
    adptrCommunityTable.setStatus("mandatory")
_AdptrCommunityEntry_Object = MibTableRow
adptrCommunityEntry = _AdptrCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 4, 1)
)
adptrCommunityEntry.setIndexNames(
    (0, "CISCO-ADAPTER-MIB", "adptrCommunityAccess"),
)
if mibBuilder.loadTexts:
    adptrCommunityEntry.setStatus("mandatory")


class _AdptrCommunityAccess_Type(Integer32):
    """Custom type adptrCommunityAccess based on Integer32"""
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
        *(("other", 1),
          ("readOnly", 2),
          ("readWrite", 3),
          ("readWriteAll", 4))
    )


_AdptrCommunityAccess_Type.__name__ = "Integer32"
_AdptrCommunityAccess_Object = MibTableColumn
adptrCommunityAccess = _AdptrCommunityAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 4, 1, 1),
    _AdptrCommunityAccess_Type()
)
adptrCommunityAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adptrCommunityAccess.setStatus("mandatory")


class _AdptrCommunityString_Type(DisplayString):
    """Custom type adptrCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AdptrCommunityString_Type.__name__ = "DisplayString"
_AdptrCommunityString_Object = MibTableColumn
adptrCommunityString = _AdptrCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 4, 1, 2),
    _AdptrCommunityString_Type()
)
adptrCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adptrCommunityString.setStatus("mandatory")


class _AdptrMgmtType_Type(Integer32):
    """Custom type adptrMgmtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("smux", 3),
          ("snmp", 2))
    )


_AdptrMgmtType_Type.__name__ = "Integer32"
_AdptrMgmtType_Object = MibScalar
adptrMgmtType = _AdptrMgmtType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 5),
    _AdptrMgmtType_Type()
)
adptrMgmtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adptrMgmtType.setStatus("mandatory")


class _AdptrMgmtHiVersion_Type(Integer32):
    """Custom type adptrMgmtHiVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdptrMgmtHiVersion_Type.__name__ = "Integer32"
_AdptrMgmtHiVersion_Object = MibScalar
adptrMgmtHiVersion = _AdptrMgmtHiVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 6),
    _AdptrMgmtHiVersion_Type()
)
adptrMgmtHiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adptrMgmtHiVersion.setStatus("mandatory")


class _AdptrMgmtLoVersion_Type(Integer32):
    """Custom type adptrMgmtLoVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdptrMgmtLoVersion_Type.__name__ = "Integer32"
_AdptrMgmtLoVersion_Object = MibScalar
adptrMgmtLoVersion = _AdptrMgmtLoVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 2, 7),
    _AdptrMgmtLoVersion_Type()
)
adptrMgmtLoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adptrMgmtLoVersion.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ADAPTER-MIB",
    **{"cisco": cisco,
       "workgroup": workgroup,
       "adapterCard": adapterCard,
       "adptrNumber": adptrNumber,
       "adptrTable": adptrTable,
       "adptrEntry": adptrEntry,
       "adptrIndex": adptrIndex,
       "adptrType": adptrType,
       "adptrSerialNumber": adptrSerialNumber,
       "adptrHwHiVersion": adptrHwHiVersion,
       "adptrHwLoVersion": adptrHwLoVersion,
       "adptrFwHiVersion": adptrFwHiVersion,
       "adptrFwLoVersion": adptrFwLoVersion,
       "adptrSwHiVersion": adptrSwHiVersion,
       "adptrSwLoVersion": adptrSwLoVersion,
       "adptrStatus": adptrStatus,
       "adptrSelfTestResult": adptrSelfTestResult,
       "adptrDriverHiVersion": adptrDriverHiVersion,
       "adptrDriverLoVersion": adptrDriverLoVersion,
       "adptrMediaType": adptrMediaType,
       "adptrModel": adptrModel,
       "adptrTrapReceiverTable": adptrTrapReceiverTable,
       "adptrTrapReceiverEntry": adptrTrapReceiverEntry,
       "adptrTrapReceiverType": adptrTrapReceiverType,
       "adptrTrapReceiverAddr": adptrTrapReceiverAddr,
       "adptrTrapReceiverComm": adptrTrapReceiverComm,
       "adptrCommunityTable": adptrCommunityTable,
       "adptrCommunityEntry": adptrCommunityEntry,
       "adptrCommunityAccess": adptrCommunityAccess,
       "adptrCommunityString": adptrCommunityString,
       "adptrMgmtType": adptrMgmtType,
       "adptrMgmtHiVersion": adptrMgmtHiVersion,
       "adptrMgmtLoVersion": adptrMgmtLoVersion}
)
