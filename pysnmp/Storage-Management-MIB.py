# SNMP MIB module (Storage-Management-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Storage-Management-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:21 2024
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
 NotificationType,
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
    "NotificationType",
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

_Sni_ObjectIdentity = ObjectIdentity
sni = _Sni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231)
)
_SniProductMibs_ObjectIdentity = ObjectIdentity
sniProductMibs = _SniProductMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2)
)
_SniStorMgmt_ObjectIdentity = ObjectIdentity
sniStorMgmt = _SniStorMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 20)
)
_SniStorMgmtAvailInfo_ObjectIdentity = ObjectIdentity
sniStorMgmtAvailInfo = _SniStorMgmtAvailInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1)
)
_SniStorMgmtProductInfo_ObjectIdentity = ObjectIdentity
sniStorMgmtProductInfo = _SniStorMgmtProductInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 1)
)
_StorMgmtProductTabNum_Type = Integer32
_StorMgmtProductTabNum_Object = MibScalar
storMgmtProductTabNum = _StorMgmtProductTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 1, 1),
    _StorMgmtProductTabNum_Type()
)
storMgmtProductTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtProductTabNum.setStatus("mandatory")
_StorMgmtProductTable_Object = MibTable
storMgmtProductTable = _StorMgmtProductTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 1, 2)
)
if mibBuilder.loadTexts:
    storMgmtProductTable.setStatus("mandatory")
_StorMgmtProductEntry_Object = MibTableRow
storMgmtProductEntry = _StorMgmtProductEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 1, 2, 1)
)
storMgmtProductEntry.setIndexNames(
    (0, "Storage-Management-MIB", "storMgmtProductIndex"),
)
if mibBuilder.loadTexts:
    storMgmtProductEntry.setStatus("mandatory")
_StorMgmtProductIndex_Type = Integer32
_StorMgmtProductIndex_Object = MibTableColumn
storMgmtProductIndex = _StorMgmtProductIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 1, 2, 1, 1),
    _StorMgmtProductIndex_Type()
)
storMgmtProductIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtProductIndex.setStatus("mandatory")
_StorMgmtProductName_Type = DisplayString
_StorMgmtProductName_Object = MibTableColumn
storMgmtProductName = _StorMgmtProductName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 1, 2, 1, 2),
    _StorMgmtProductName_Type()
)
storMgmtProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtProductName.setStatus("mandatory")
_StorMgmtProductVersion_Type = DisplayString
_StorMgmtProductVersion_Object = MibTableColumn
storMgmtProductVersion = _StorMgmtProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 1, 2, 1, 3),
    _StorMgmtProductVersion_Type()
)
storMgmtProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtProductVersion.setStatus("mandatory")


class _StorMgmtProductState_Type(Integer32):
    """Custom type storMgmtProductState based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("in-create", 4),
          ("in-delete", 3),
          ("in-hold", 6),
          ("in-resume", 5),
          ("locked", 8),
          ("not-created", 2),
          ("not-installed", 255),
          ("not-resumed", 7))
    )


_StorMgmtProductState_Type.__name__ = "Integer32"
_StorMgmtProductState_Object = MibTableColumn
storMgmtProductState = _StorMgmtProductState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 1, 2, 1, 4),
    _StorMgmtProductState_Type()
)
storMgmtProductState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtProductState.setStatus("mandatory")
_StorMgmtProductTimestamp_Type = DisplayString
_StorMgmtProductTimestamp_Object = MibTableColumn
storMgmtProductTimestamp = _StorMgmtProductTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 1, 2, 1, 5),
    _StorMgmtProductTimestamp_Type()
)
storMgmtProductTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtProductTimestamp.setStatus("mandatory")
_SniStorMgmtHsmsInfo_ObjectIdentity = ObjectIdentity
sniStorMgmtHsmsInfo = _SniStorMgmtHsmsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 2)
)


class _StorMgmtHsmsOpmode_Type(Integer32):
    """Custom type storMgmtHsmsOpmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("defineshow", 1),
          ("operation", 3),
          ("simulation", 2))
    )


_StorMgmtHsmsOpmode_Type.__name__ = "Integer32"
_StorMgmtHsmsOpmode_Object = MibScalar
storMgmtHsmsOpmode = _StorMgmtHsmsOpmode_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 2, 1),
    _StorMgmtHsmsOpmode_Type()
)
storMgmtHsmsOpmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    storMgmtHsmsOpmode.setStatus("mandatory")
_StorMgmtHsmsModeTimestamp_Type = DisplayString
_StorMgmtHsmsModeTimestamp_Object = MibScalar
storMgmtHsmsModeTimestamp = _StorMgmtHsmsModeTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 2, 2),
    _StorMgmtHsmsModeTimestamp_Type()
)
storMgmtHsmsModeTimestamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    storMgmtHsmsModeTimestamp.setStatus("mandatory")


class _StorMgmtHsmsServertask_Type(Integer32):
    """Custom type storMgmtHsmsServertask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_StorMgmtHsmsServertask_Type.__name__ = "Integer32"
_StorMgmtHsmsServertask_Object = MibScalar
storMgmtHsmsServertask = _StorMgmtHsmsServertask_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 2, 3),
    _StorMgmtHsmsServertask_Type()
)
storMgmtHsmsServertask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    storMgmtHsmsServertask.setStatus("mandatory")
_StorMgmtHsmsWaitJobs_Type = Integer32
_StorMgmtHsmsWaitJobs_Object = MibScalar
storMgmtHsmsWaitJobs = _StorMgmtHsmsWaitJobs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 2, 4),
    _StorMgmtHsmsWaitJobs_Type()
)
storMgmtHsmsWaitJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtHsmsWaitJobs.setStatus("mandatory")
_StorMgmtHsmsInstances_Type = Integer32
_StorMgmtHsmsInstances_Object = MibScalar
storMgmtHsmsInstances = _StorMgmtHsmsInstances_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 2, 5),
    _StorMgmtHsmsInstances_Type()
)
storMgmtHsmsInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtHsmsInstances.setStatus("mandatory")
_StorMgmtHsmsAcceptReqs_Type = Integer32
_StorMgmtHsmsAcceptReqs_Object = MibScalar
storMgmtHsmsAcceptReqs = _StorMgmtHsmsAcceptReqs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 2, 6),
    _StorMgmtHsmsAcceptReqs_Type()
)
storMgmtHsmsAcceptReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtHsmsAcceptReqs.setStatus("mandatory")
_StorMgmtHsmsCompleteReqs_Type = Integer32
_StorMgmtHsmsCompleteReqs_Object = MibScalar
storMgmtHsmsCompleteReqs = _StorMgmtHsmsCompleteReqs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 2, 7),
    _StorMgmtHsmsCompleteReqs_Type()
)
storMgmtHsmsCompleteReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtHsmsCompleteReqs.setStatus("mandatory")
_StorMgmtHsmsInterruptReqs_Type = Integer32
_StorMgmtHsmsInterruptReqs_Object = MibScalar
storMgmtHsmsInterruptReqs = _StorMgmtHsmsInterruptReqs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 2, 8),
    _StorMgmtHsmsInterruptReqs_Type()
)
storMgmtHsmsInterruptReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtHsmsInterruptReqs.setStatus("mandatory")
_StorMgmtHsmsWaitReqsRead_Type = Integer32
_StorMgmtHsmsWaitReqsRead_Object = MibScalar
storMgmtHsmsWaitReqsRead = _StorMgmtHsmsWaitReqsRead_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 2, 9),
    _StorMgmtHsmsWaitReqsRead_Type()
)
storMgmtHsmsWaitReqsRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtHsmsWaitReqsRead.setStatus("mandatory")
_StorMgmtHsmsWaitReqsWrite_Type = Integer32
_StorMgmtHsmsWaitReqsWrite_Object = MibScalar
storMgmtHsmsWaitReqsWrite = _StorMgmtHsmsWaitReqsWrite_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 2, 10),
    _StorMgmtHsmsWaitReqsWrite_Type()
)
storMgmtHsmsWaitReqsWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtHsmsWaitReqsWrite.setStatus("mandatory")
_StorMgmtHsmsWaitReqsExpress_Type = Integer32
_StorMgmtHsmsWaitReqsExpress_Object = MibScalar
storMgmtHsmsWaitReqsExpress = _StorMgmtHsmsWaitReqsExpress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 2, 11),
    _StorMgmtHsmsWaitReqsExpress_Type()
)
storMgmtHsmsWaitReqsExpress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtHsmsWaitReqsExpress.setStatus("mandatory")
_StorMgmtHsmsStimeRead_Type = Integer32
_StorMgmtHsmsStimeRead_Object = MibScalar
storMgmtHsmsStimeRead = _StorMgmtHsmsStimeRead_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 2, 12),
    _StorMgmtHsmsStimeRead_Type()
)
storMgmtHsmsStimeRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtHsmsStimeRead.setStatus("mandatory")
_StorMgmtHsmsStimeWrite_Type = Integer32
_StorMgmtHsmsStimeWrite_Object = MibScalar
storMgmtHsmsStimeWrite = _StorMgmtHsmsStimeWrite_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 2, 13),
    _StorMgmtHsmsStimeWrite_Type()
)
storMgmtHsmsStimeWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtHsmsStimeWrite.setStatus("mandatory")
_StorMgmtHsmsStimeExpress_Type = Integer32
_StorMgmtHsmsStimeExpress_Object = MibScalar
storMgmtHsmsStimeExpress = _StorMgmtHsmsStimeExpress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 2, 14),
    _StorMgmtHsmsStimeExpress_Type()
)
storMgmtHsmsStimeExpress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtHsmsStimeExpress.setStatus("mandatory")
_StorMgmtHsmsNetload_Type = Integer32
_StorMgmtHsmsNetload_Object = MibScalar
storMgmtHsmsNetload = _StorMgmtHsmsNetload_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 2, 15),
    _StorMgmtHsmsNetload_Type()
)
storMgmtHsmsNetload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtHsmsNetload.setStatus("mandatory")
_SniStorMgmtMarenInfo_ObjectIdentity = ObjectIdentity
sniStorMgmtMarenInfo = _SniStorMgmtMarenInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 3)
)


class _StorMgmtMarenCPTask_Type(DisplayString):
    """Custom type storMgmtMarenCPTask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StorMgmtMarenCPTask_Type.__name__ = "DisplayString"
_StorMgmtMarenCPTask_Object = MibScalar
storMgmtMarenCPTask = _StorMgmtMarenCPTask_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 3, 1),
    _StorMgmtMarenCPTask_Type()
)
storMgmtMarenCPTask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtMarenCPTask.setStatus("mandatory")


class _StorMgmtMarenUCPTask_Type(DisplayString):
    """Custom type storMgmtMarenUCPTask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StorMgmtMarenUCPTask_Type.__name__ = "DisplayString"
_StorMgmtMarenUCPTask_Object = MibScalar
storMgmtMarenUCPTask = _StorMgmtMarenUCPTask_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 3, 2),
    _StorMgmtMarenUCPTask_Type()
)
storMgmtMarenUCPTask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtMarenUCPTask.setStatus("mandatory")


class _StorMgmtMarenCatConn_Type(Integer32):
    """Custom type storMgmtMarenCatConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rfalocal", 2),
          ("rfaremote", 3),
          ("spd", 1))
    )


_StorMgmtMarenCatConn_Type.__name__ = "Integer32"
_StorMgmtMarenCatConn_Object = MibScalar
storMgmtMarenCatConn = _StorMgmtMarenCatConn_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 3, 3),
    _StorMgmtMarenCatConn_Type()
)
storMgmtMarenCatConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtMarenCatConn.setStatus("mandatory")


class _StorMgmtMarenConnState_Type(Integer32):
    """Custom type storMgmtMarenConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_StorMgmtMarenConnState_Type.__name__ = "Integer32"
_StorMgmtMarenConnState_Object = MibScalar
storMgmtMarenConnState = _StorMgmtMarenConnState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 3, 4),
    _StorMgmtMarenConnState_Type()
)
storMgmtMarenConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtMarenConnState.setStatus("mandatory")
_StorMgmtMarenLocTabNum_Type = Integer32
_StorMgmtMarenLocTabNum_Object = MibScalar
storMgmtMarenLocTabNum = _StorMgmtMarenLocTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 3, 5),
    _StorMgmtMarenLocTabNum_Type()
)
storMgmtMarenLocTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtMarenLocTabNum.setStatus("mandatory")
_StorMgmtMarenLocTable_Object = MibTable
storMgmtMarenLocTable = _StorMgmtMarenLocTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 3, 6)
)
if mibBuilder.loadTexts:
    storMgmtMarenLocTable.setStatus("mandatory")
_StorMgmtMarenLocEntry_Object = MibTableRow
storMgmtMarenLocEntry = _StorMgmtMarenLocEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 3, 6, 1)
)
storMgmtMarenLocEntry.setIndexNames(
    (0, "Storage-Management-MIB", "storMgmtMarenLocIndex"),
)
if mibBuilder.loadTexts:
    storMgmtMarenLocEntry.setStatus("mandatory")
_StorMgmtMarenLocIndex_Type = Integer32
_StorMgmtMarenLocIndex_Object = MibTableColumn
storMgmtMarenLocIndex = _StorMgmtMarenLocIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 3, 6, 1, 1),
    _StorMgmtMarenLocIndex_Type()
)
storMgmtMarenLocIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtMarenLocIndex.setStatus("mandatory")


class _StorMgmtMarenLocName_Type(DisplayString):
    """Custom type storMgmtMarenLocName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_StorMgmtMarenLocName_Type.__name__ = "DisplayString"
_StorMgmtMarenLocName_Object = MibTableColumn
storMgmtMarenLocName = _StorMgmtMarenLocName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 3, 6, 1, 2),
    _StorMgmtMarenLocName_Type()
)
storMgmtMarenLocName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtMarenLocName.setStatus("mandatory")


class _StorMgmtMarenLocOpmode_Type(DisplayString):
    """Custom type storMgmtMarenLocOpmode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_StorMgmtMarenLocOpmode_Type.__name__ = "DisplayString"
_StorMgmtMarenLocOpmode_Object = MibTableColumn
storMgmtMarenLocOpmode = _StorMgmtMarenLocOpmode_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 3, 6, 1, 3),
    _StorMgmtMarenLocOpmode_Type()
)
storMgmtMarenLocOpmode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtMarenLocOpmode.setStatus("mandatory")


class _StorMgmtMarenLocFreevol_Type(DisplayString):
    """Custom type storMgmtMarenLocFreevol based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_StorMgmtMarenLocFreevol_Type.__name__ = "DisplayString"
_StorMgmtMarenLocFreevol_Object = MibTableColumn
storMgmtMarenLocFreevol = _StorMgmtMarenLocFreevol_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 3, 6, 1, 4),
    _StorMgmtMarenLocFreevol_Type()
)
storMgmtMarenLocFreevol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtMarenLocFreevol.setStatus("mandatory")
_StorMgmtMarenNetworkTabNum_Type = Integer32
_StorMgmtMarenNetworkTabNum_Object = MibScalar
storMgmtMarenNetworkTabNum = _StorMgmtMarenNetworkTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 3, 7),
    _StorMgmtMarenNetworkTabNum_Type()
)
storMgmtMarenNetworkTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtMarenNetworkTabNum.setStatus("mandatory")
_StorMgmtMarenNetworkTable_Object = MibTable
storMgmtMarenNetworkTable = _StorMgmtMarenNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 3, 8)
)
if mibBuilder.loadTexts:
    storMgmtMarenNetworkTable.setStatus("mandatory")
_StorMgmtMarenNetworkEntry_Object = MibTableRow
storMgmtMarenNetworkEntry = _StorMgmtMarenNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 3, 8, 1)
)
storMgmtMarenNetworkEntry.setIndexNames(
    (0, "Storage-Management-MIB", "storMgmtMarenNetworkIndex"),
)
if mibBuilder.loadTexts:
    storMgmtMarenNetworkEntry.setStatus("mandatory")
_StorMgmtMarenNetworkIndex_Type = Integer32
_StorMgmtMarenNetworkIndex_Object = MibTableColumn
storMgmtMarenNetworkIndex = _StorMgmtMarenNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 3, 8, 1, 1),
    _StorMgmtMarenNetworkIndex_Type()
)
storMgmtMarenNetworkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtMarenNetworkIndex.setStatus("mandatory")


class _StorMgmtMarenNetworkHost_Type(DisplayString):
    """Custom type storMgmtMarenNetworkHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_StorMgmtMarenNetworkHost_Type.__name__ = "DisplayString"
_StorMgmtMarenNetworkHost_Object = MibTableColumn
storMgmtMarenNetworkHost = _StorMgmtMarenNetworkHost_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 3, 8, 1, 2),
    _StorMgmtMarenNetworkHost_Type()
)
storMgmtMarenNetworkHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtMarenNetworkHost.setStatus("mandatory")
_SniStorMgmtTlsInfo_ObjectIdentity = ObjectIdentity
sniStorMgmtTlsInfo = _SniStorMgmtTlsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 4)
)
_StorMgmtTlsTabNum_Type = Integer32
_StorMgmtTlsTabNum_Object = MibScalar
storMgmtTlsTabNum = _StorMgmtTlsTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 4, 1),
    _StorMgmtTlsTabNum_Type()
)
storMgmtTlsTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtTlsTabNum.setStatus("mandatory")
_StorMgmtTlsTable_Object = MibTable
storMgmtTlsTable = _StorMgmtTlsTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 4, 2)
)
if mibBuilder.loadTexts:
    storMgmtTlsTable.setStatus("mandatory")
_StorMgmtTlsEntry_Object = MibTableRow
storMgmtTlsEntry = _StorMgmtTlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 4, 2, 1)
)
storMgmtTlsEntry.setIndexNames(
    (0, "Storage-Management-MIB", "storMgmtTlsIndex"),
)
if mibBuilder.loadTexts:
    storMgmtTlsEntry.setStatus("mandatory")
_StorMgmtTlsIndex_Type = Integer32
_StorMgmtTlsIndex_Object = MibTableColumn
storMgmtTlsIndex = _StorMgmtTlsIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 4, 2, 1, 1),
    _StorMgmtTlsIndex_Type()
)
storMgmtTlsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtTlsIndex.setStatus("mandatory")


class _StorMgmtTlsRobState_Type(Integer32):
    """Custom type storMgmtTlsRobState based on Integer32"""
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
        *(("automatic", 1),
          ("manual", 3),
          ("off", 4),
          ("pause", 2))
    )


_StorMgmtTlsRobState_Type.__name__ = "Integer32"
_StorMgmtTlsRobState_Object = MibTableColumn
storMgmtTlsRobState = _StorMgmtTlsRobState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 4, 2, 1, 2),
    _StorMgmtTlsRobState_Type()
)
storMgmtTlsRobState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtTlsRobState.setStatus("mandatory")
_StorMgmtTlsFreeboxno_Type = Integer32
_StorMgmtTlsFreeboxno_Object = MibTableColumn
storMgmtTlsFreeboxno = _StorMgmtTlsFreeboxno_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 4, 2, 1, 3),
    _StorMgmtTlsFreeboxno_Type()
)
storMgmtTlsFreeboxno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtTlsFreeboxno.setStatus("mandatory")
_StorMgmtTlsCleanno_Type = Integer32
_StorMgmtTlsCleanno_Object = MibTableColumn
storMgmtTlsCleanno = _StorMgmtTlsCleanno_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 4, 2, 1, 4),
    _StorMgmtTlsCleanno_Type()
)
storMgmtTlsCleanno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtTlsCleanno.setStatus("mandatory")


class _StorMgmtTlsLocation_Type(DisplayString):
    """Custom type storMgmtTlsLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_StorMgmtTlsLocation_Type.__name__ = "DisplayString"
_StorMgmtTlsLocation_Object = MibTableColumn
storMgmtTlsLocation = _StorMgmtTlsLocation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 4, 2, 1, 5),
    _StorMgmtTlsLocation_Type()
)
storMgmtTlsLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtTlsLocation.setStatus("mandatory")
_SniStorMgmtRobarInfo_ObjectIdentity = ObjectIdentity
sniStorMgmtRobarInfo = _SniStorMgmtRobarInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 5)
)
_StorMgmtRobarTabNum_Type = Integer32
_StorMgmtRobarTabNum_Object = MibScalar
storMgmtRobarTabNum = _StorMgmtRobarTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 5, 1),
    _StorMgmtRobarTabNum_Type()
)
storMgmtRobarTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtRobarTabNum.setStatus("mandatory")
_StorMgmtRobarTable_Object = MibTable
storMgmtRobarTable = _StorMgmtRobarTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 5, 2)
)
if mibBuilder.loadTexts:
    storMgmtRobarTable.setStatus("mandatory")
_StorMgmtRobarEntry_Object = MibTableRow
storMgmtRobarEntry = _StorMgmtRobarEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 5, 2, 1)
)
storMgmtRobarEntry.setIndexNames(
    (0, "Storage-Management-MIB", "storMgmtRobarIndex"),
)
if mibBuilder.loadTexts:
    storMgmtRobarEntry.setStatus("mandatory")
_StorMgmtRobarIndex_Type = Integer32
_StorMgmtRobarIndex_Object = MibTableColumn
storMgmtRobarIndex = _StorMgmtRobarIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 5, 2, 1, 1),
    _StorMgmtRobarIndex_Type()
)
storMgmtRobarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtRobarIndex.setStatus("mandatory")


class _StorMgmtRobarLocation_Type(DisplayString):
    """Custom type storMgmtRobarLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_StorMgmtRobarLocation_Type.__name__ = "DisplayString"
_StorMgmtRobarLocation_Object = MibTableColumn
storMgmtRobarLocation = _StorMgmtRobarLocation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 5, 2, 1, 2),
    _StorMgmtRobarLocation_Type()
)
storMgmtRobarLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtRobarLocation.setStatus("mandatory")


class _StorMgmtRobarState_Type(Integer32):
    """Custom type storMgmtRobarState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 3),
          ("in-hold", 5),
          ("loaded", 4),
          ("not-installed", 255),
          ("running", 1),
          ("terminated", 2))
    )


_StorMgmtRobarState_Type.__name__ = "Integer32"
_StorMgmtRobarState_Object = MibTableColumn
storMgmtRobarState = _StorMgmtRobarState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 5, 2, 1, 3),
    _StorMgmtRobarState_Type()
)
storMgmtRobarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtRobarState.setStatus("mandatory")


class _StorMgmtRobarVersion_Type(DisplayString):
    """Custom type storMgmtRobarVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_StorMgmtRobarVersion_Type.__name__ = "DisplayString"
_StorMgmtRobarVersion_Object = MibTableColumn
storMgmtRobarVersion = _StorMgmtRobarVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 5, 2, 1, 4),
    _StorMgmtRobarVersion_Type()
)
storMgmtRobarVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtRobarVersion.setStatus("mandatory")


class _StorMgmtRobarConnState_Type(Integer32):
    """Custom type storMgmtRobarConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("not-available", 255))
    )


_StorMgmtRobarConnState_Type.__name__ = "Integer32"
_StorMgmtRobarConnState_Object = MibTableColumn
storMgmtRobarConnState = _StorMgmtRobarConnState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 5, 2, 1, 5),
    _StorMgmtRobarConnState_Type()
)
storMgmtRobarConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtRobarConnState.setStatus("mandatory")


class _StorMgmtRobarRobState_Type(Integer32):
    """Custom type storMgmtRobarRobState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_StorMgmtRobarRobState_Type.__name__ = "Integer32"
_StorMgmtRobarRobState_Object = MibTableColumn
storMgmtRobarRobState = _StorMgmtRobarRobState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 5, 2, 1, 6),
    _StorMgmtRobarRobState_Type()
)
storMgmtRobarRobState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtRobarRobState.setStatus("mandatory")


class _StorMgmtRobarRouting_Type(DisplayString):
    """Custom type storMgmtRobarRouting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_StorMgmtRobarRouting_Type.__name__ = "DisplayString"
_StorMgmtRobarRouting_Object = MibTableColumn
storMgmtRobarRouting = _StorMgmtRobarRouting_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 5, 2, 1, 7),
    _StorMgmtRobarRouting_Type()
)
storMgmtRobarRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    storMgmtRobarRouting.setStatus("mandatory")
_SniStorMgmtResourceInfo_ObjectIdentity = ObjectIdentity
sniStorMgmtResourceInfo = _SniStorMgmtResourceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 2)
)


class _StorMgmtResourcePubset_Type(DisplayString):
    """Custom type storMgmtResourcePubset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_StorMgmtResourcePubset_Type.__name__ = "DisplayString"
_StorMgmtResourcePubset_Object = MibScalar
storMgmtResourcePubset = _StorMgmtResourcePubset_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 2, 1),
    _StorMgmtResourcePubset_Type()
)
storMgmtResourcePubset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    storMgmtResourcePubset.setStatus("mandatory")


class _StorMgmtResourceSaturation_Type(Integer32):
    """Custom type storMgmtResourceSaturation based on Integer32"""
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
        *(("level-0", 1),
          ("level-1", 2),
          ("level-2", 3),
          ("level-3", 4),
          ("level-4", 5),
          ("level-5", 6),
          ("unknown-level", 7))
    )


_StorMgmtResourceSaturation_Type.__name__ = "Integer32"
_StorMgmtResourceSaturation_Object = MibScalar
storMgmtResourceSaturation = _StorMgmtResourceSaturation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 2, 2),
    _StorMgmtResourceSaturation_Type()
)
storMgmtResourceSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtResourceSaturation.setStatus("mandatory")
_StorMgmtResourceCapacity_Type = Integer32
_StorMgmtResourceCapacity_Object = MibScalar
storMgmtResourceCapacity = _StorMgmtResourceCapacity_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 2, 3),
    _StorMgmtResourceCapacity_Type()
)
storMgmtResourceCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtResourceCapacity.setStatus("mandatory")
_StorMgmtResourceSpaceAllocated_Type = Integer32
_StorMgmtResourceSpaceAllocated_Object = MibScalar
storMgmtResourceSpaceAllocated = _StorMgmtResourceSpaceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 2, 4),
    _StorMgmtResourceSpaceAllocated_Type()
)
storMgmtResourceSpaceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtResourceSpaceAllocated.setStatus("mandatory")


class _StorMgmtResourceFragment_Type(DisplayString):
    """Custom type storMgmtResourceFragment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_StorMgmtResourceFragment_Type.__name__ = "DisplayString"
_StorMgmtResourceFragment_Object = MibScalar
storMgmtResourceFragment = _StorMgmtResourceFragment_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 2, 5),
    _StorMgmtResourceFragment_Type()
)
storMgmtResourceFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtResourceFragment.setStatus("mandatory")
_StorMgmtResourceReusableS1_Type = DisplayString
_StorMgmtResourceReusableS1_Object = MibScalar
storMgmtResourceReusableS1 = _StorMgmtResourceReusableS1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 2, 6),
    _StorMgmtResourceReusableS1_Type()
)
storMgmtResourceReusableS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtResourceReusableS1.setStatus("mandatory")
_StorMgmtResourceSecureQueue_Type = Integer32
_StorMgmtResourceSecureQueue_Object = MibScalar
storMgmtResourceSecureQueue = _StorMgmtResourceSecureQueue_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 2, 7),
    _StorMgmtResourceSecureQueue_Type()
)
storMgmtResourceSecureQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtResourceSecureQueue.setStatus("mandatory")
_SniStorMgmtPubsetInfo_ObjectIdentity = ObjectIdentity
sniStorMgmtPubsetInfo = _SniStorMgmtPubsetInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 3)
)
_StorMgmtPubsetTabNum_Type = Integer32
_StorMgmtPubsetTabNum_Object = MibScalar
storMgmtPubsetTabNum = _StorMgmtPubsetTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 3, 1),
    _StorMgmtPubsetTabNum_Type()
)
storMgmtPubsetTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtPubsetTabNum.setStatus("mandatory")


class _StorMgmtPubsetTabState_Type(Integer32):
    """Custom type storMgmtPubsetTabState based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("accessible", 5),
          ("all", 1),
          ("exclusive", 8),
          ("hsms-supported", 12),
          ("local", 3),
          ("local-accessible", 6),
          ("local-accessible-speedcat", 10),
          ("master-change-error", 17),
          ("paging", 2),
          ("remote", 4),
          ("remote-accessible", 9),
          ("shared", 7),
          ("single-feature", 13),
          ("system-managed", 14),
          ("unused-volsets", 16),
          ("volume-sets", 15),
          ("xcs-pubset", 11))
    )


_StorMgmtPubsetTabState_Type.__name__ = "Integer32"
_StorMgmtPubsetTabState_Object = MibScalar
storMgmtPubsetTabState = _StorMgmtPubsetTabState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 3, 2),
    _StorMgmtPubsetTabState_Type()
)
storMgmtPubsetTabState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    storMgmtPubsetTabState.setStatus("mandatory")
_StorMgmtPubsetTable_Object = MibTable
storMgmtPubsetTable = _StorMgmtPubsetTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 3, 10)
)
if mibBuilder.loadTexts:
    storMgmtPubsetTable.setStatus("mandatory")
_StorMgmtPubsetEntry_Object = MibTableRow
storMgmtPubsetEntry = _StorMgmtPubsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 3, 10, 1)
)
storMgmtPubsetEntry.setIndexNames(
    (0, "Storage-Management-MIB", "storMgmtPubsetIndex"),
)
if mibBuilder.loadTexts:
    storMgmtPubsetEntry.setStatus("mandatory")
_StorMgmtPubsetIndex_Type = DisplayString
_StorMgmtPubsetIndex_Object = MibTableColumn
storMgmtPubsetIndex = _StorMgmtPubsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 3, 10, 1, 1),
    _StorMgmtPubsetIndex_Type()
)
storMgmtPubsetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtPubsetIndex.setStatus("mandatory")


class _StorMgmtPubsetTyp_Type(Integer32):
    """Custom type storMgmtPubsetTyp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("single-feature", 1),
          ("system-managed", 2),
          ("unknown", 255),
          ("volumeset", 3))
    )


_StorMgmtPubsetTyp_Type.__name__ = "Integer32"
_StorMgmtPubsetTyp_Object = MibTableColumn
storMgmtPubsetTyp = _StorMgmtPubsetTyp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 3, 10, 1, 4),
    _StorMgmtPubsetTyp_Type()
)
storMgmtPubsetTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtPubsetTyp.setStatus("mandatory")


class _StorMgmtPubsetLocal_Type(Integer32):
    """Custom type storMgmtPubsetLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2),
          ("unknown", 255))
    )


_StorMgmtPubsetLocal_Type.__name__ = "Integer32"
_StorMgmtPubsetLocal_Object = MibTableColumn
storMgmtPubsetLocal = _StorMgmtPubsetLocal_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 3, 10, 1, 5),
    _StorMgmtPubsetLocal_Type()
)
storMgmtPubsetLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtPubsetLocal.setStatus("mandatory")


class _StorMgmtPubsetHome_Type(Integer32):
    """Custom type storMgmtPubsetHome based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("home", 1),
          ("imported", 2),
          ("unknown", 255))
    )


_StorMgmtPubsetHome_Type.__name__ = "Integer32"
_StorMgmtPubsetHome_Object = MibTableColumn
storMgmtPubsetHome = _StorMgmtPubsetHome_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 3, 10, 1, 6),
    _StorMgmtPubsetHome_Type()
)
storMgmtPubsetHome.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtPubsetHome.setStatus("mandatory")


class _StorMgmtPubsetShared_Type(Integer32):
    """Custom type storMgmtPubsetShared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 2),
          ("shared", 1),
          ("unknown", 255))
    )


_StorMgmtPubsetShared_Type.__name__ = "Integer32"
_StorMgmtPubsetShared_Object = MibTableColumn
storMgmtPubsetShared = _StorMgmtPubsetShared_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 3, 10, 1, 7),
    _StorMgmtPubsetShared_Type()
)
storMgmtPubsetShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtPubsetShared.setStatus("mandatory")


class _StorMgmtPubsetMaster_Type(Integer32):
    """Custom type storMgmtPubsetMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 255),
          ("yes", 1))
    )


_StorMgmtPubsetMaster_Type.__name__ = "Integer32"
_StorMgmtPubsetMaster_Object = MibTableColumn
storMgmtPubsetMaster = _StorMgmtPubsetMaster_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 3, 10, 1, 8),
    _StorMgmtPubsetMaster_Type()
)
storMgmtPubsetMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtPubsetMaster.setStatus("mandatory")


class _StorMgmtPubsetAccessible_Type(Integer32):
    """Custom type storMgmtPubsetAccessible based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("accessible", 1),
          ("inaccessible", 2),
          ("unknown", 255))
    )


_StorMgmtPubsetAccessible_Type.__name__ = "Integer32"
_StorMgmtPubsetAccessible_Object = MibTableColumn
storMgmtPubsetAccessible = _StorMgmtPubsetAccessible_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 3, 10, 1, 9),
    _StorMgmtPubsetAccessible_Type()
)
storMgmtPubsetAccessible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtPubsetAccessible.setStatus("mandatory")


class _StorMgmtPubsetQuiet_Type(Integer32):
    """Custom type storMgmtPubsetQuiet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 255),
          ("yes", 1))
    )


_StorMgmtPubsetQuiet_Type.__name__ = "Integer32"
_StorMgmtPubsetQuiet_Object = MibTableColumn
storMgmtPubsetQuiet = _StorMgmtPubsetQuiet_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 3, 10, 1, 10),
    _StorMgmtPubsetQuiet_Type()
)
storMgmtPubsetQuiet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtPubsetQuiet.setStatus("mandatory")


class _StorMgmtPubsetPaging_Type(Integer32):
    """Custom type storMgmtPubsetPaging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 255),
          ("yes", 1))
    )


_StorMgmtPubsetPaging_Type.__name__ = "Integer32"
_StorMgmtPubsetPaging_Object = MibTableColumn
storMgmtPubsetPaging = _StorMgmtPubsetPaging_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 3, 10, 1, 11),
    _StorMgmtPubsetPaging_Type()
)
storMgmtPubsetPaging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtPubsetPaging.setStatus("mandatory")
_StorMgmtPubsetSize_Type = Integer32
_StorMgmtPubsetSize_Object = MibTableColumn
storMgmtPubsetSize = _StorMgmtPubsetSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 3, 10, 1, 12),
    _StorMgmtPubsetSize_Type()
)
storMgmtPubsetSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtPubsetSize.setStatus("mandatory")
_StorMgmtPubsetUsedSize_Type = Integer32
_StorMgmtPubsetUsedSize_Object = MibTableColumn
storMgmtPubsetUsedSize = _StorMgmtPubsetUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 3, 10, 1, 13),
    _StorMgmtPubsetUsedSize_Type()
)
storMgmtPubsetUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtPubsetUsedSize.setStatus("mandatory")


class _StorMgmtPubsetSaturationLevel_Type(Integer32):
    """Custom type storMgmtPubsetSaturationLevel based on Integer32"""
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
        *(("level-0", 1),
          ("level-1", 2),
          ("level-2", 3),
          ("level-3", 4),
          ("level-4", 5),
          ("level-5", 6),
          ("unknown-level", 7))
    )


_StorMgmtPubsetSaturationLevel_Type.__name__ = "Integer32"
_StorMgmtPubsetSaturationLevel_Object = MibTableColumn
storMgmtPubsetSaturationLevel = _StorMgmtPubsetSaturationLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 3, 10, 1, 14),
    _StorMgmtPubsetSaturationLevel_Type()
)
storMgmtPubsetSaturationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtPubsetSaturationLevel.setStatus("mandatory")
_SniStorMgmtDiskInfo_ObjectIdentity = ObjectIdentity
sniStorMgmtDiskInfo = _SniStorMgmtDiskInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 4)
)
_StorMgmtDiskTabNum_Type = Integer32
_StorMgmtDiskTabNum_Object = MibScalar
storMgmtDiskTabNum = _StorMgmtDiskTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 4, 1),
    _StorMgmtDiskTabNum_Type()
)
storMgmtDiskTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtDiskTabNum.setStatus("mandatory")


class _StorMgmtDiskTabReconfState_Type(Integer32):
    """Custom type storMgmtDiskTabReconfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("attached", 2),
          ("detached", 3),
          ("other", 255))
    )


_StorMgmtDiskTabReconfState_Type.__name__ = "Integer32"
_StorMgmtDiskTabReconfState_Object = MibScalar
storMgmtDiskTabReconfState = _StorMgmtDiskTabReconfState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 4, 2),
    _StorMgmtDiskTabReconfState_Type()
)
storMgmtDiskTabReconfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    storMgmtDiskTabReconfState.setStatus("mandatory")
_StorMgmtDiskTable_Object = MibTable
storMgmtDiskTable = _StorMgmtDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 4, 10)
)
if mibBuilder.loadTexts:
    storMgmtDiskTable.setStatus("mandatory")
_StorMgmtDiskEntry_Object = MibTableRow
storMgmtDiskEntry = _StorMgmtDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 4, 10, 1)
)
storMgmtDiskEntry.setIndexNames(
    (0, "Storage-Management-MIB", "storMgmtDiskIndex"),
)
if mibBuilder.loadTexts:
    storMgmtDiskEntry.setStatus("mandatory")


class _StorMgmtDiskIndex_Type(DisplayString):
    """Custom type storMgmtDiskIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_StorMgmtDiskIndex_Type.__name__ = "DisplayString"
_StorMgmtDiskIndex_Object = MibTableColumn
storMgmtDiskIndex = _StorMgmtDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 4, 10, 1, 1),
    _StorMgmtDiskIndex_Type()
)
storMgmtDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtDiskIndex.setStatus("mandatory")


class _StorMgmtDiskVSN_Type(DisplayString):
    """Custom type storMgmtDiskVSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_StorMgmtDiskVSN_Type.__name__ = "DisplayString"
_StorMgmtDiskVSN_Object = MibTableColumn
storMgmtDiskVSN = _StorMgmtDiskVSN_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 4, 10, 1, 2),
    _StorMgmtDiskVSN_Type()
)
storMgmtDiskVSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtDiskVSN.setStatus("mandatory")


class _StorMgmtDiskDeviceAllocState_Type(Integer32):
    """Custom type storMgmtDiskDeviceAllocState based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("allocated", 2),
          ("current-public-assigned", 4),
          ("dms-used-volume-assigned", 5),
          ("drv-assigned", 6),
          ("drv-dms-used-volume-assigned", 8),
          ("drv-public-assigned", 7),
          ("exclusive-allocated", 3),
          ("free", 1),
          ("invalid", 255))
    )


_StorMgmtDiskDeviceAllocState_Type.__name__ = "Integer32"
_StorMgmtDiskDeviceAllocState_Object = MibTableColumn
storMgmtDiskDeviceAllocState = _StorMgmtDiskDeviceAllocState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 4, 10, 1, 3),
    _StorMgmtDiskDeviceAllocState_Type()
)
storMgmtDiskDeviceAllocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtDiskDeviceAllocState.setStatus("mandatory")


class _StorMgmtDiskSystemUse_Type(Integer32):
    """Custom type storMgmtDiskSystemUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("paging-device", 1),
          ("public-device", 2),
          ("unknown", 255))
    )


_StorMgmtDiskSystemUse_Type.__name__ = "Integer32"
_StorMgmtDiskSystemUse_Object = MibTableColumn
storMgmtDiskSystemUse = _StorMgmtDiskSystemUse_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 4, 10, 1, 4),
    _StorMgmtDiskSystemUse_Type()
)
storMgmtDiskSystemUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtDiskSystemUse.setStatus("mandatory")


class _StorMgmtDiskPoolAttribut_Type(Integer32):
    """Custom type storMgmtDiskPoolAttribut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("device-switchable", 2),
          ("shared-privat-disk", 1),
          ("unknown", 255))
    )


_StorMgmtDiskPoolAttribut_Type.__name__ = "Integer32"
_StorMgmtDiskPoolAttribut_Object = MibTableColumn
storMgmtDiskPoolAttribut = _StorMgmtDiskPoolAttribut_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 4, 10, 1, 5),
    _StorMgmtDiskPoolAttribut_Type()
)
storMgmtDiskPoolAttribut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtDiskPoolAttribut.setStatus("mandatory")


class _StorMgmtDiskReconfState_Type(Integer32):
    """Custom type storMgmtDiskReconfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("assignment-in-progress", 4),
          ("attached", 1),
          ("detach-pending", 2),
          ("detached", 3),
          ("invalid", 255))
    )


_StorMgmtDiskReconfState_Type.__name__ = "Integer32"
_StorMgmtDiskReconfState_Object = MibTableColumn
storMgmtDiskReconfState = _StorMgmtDiskReconfState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 4, 10, 1, 6),
    _StorMgmtDiskReconfState_Type()
)
storMgmtDiskReconfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtDiskReconfState.setStatus("mandatory")


class _StorMgmtDiskVolAllocState_Type(Integer32):
    """Custom type storMgmtDiskVolAllocState based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("current-paging", 5),
          ("current-public", 4),
          ("free", 1),
          ("invalid", 255),
          ("task-exclusive", 2),
          ("task-sharable", 3),
          ("volume-allocated", 7),
          ("volume-cancelled", 6))
    )


_StorMgmtDiskVolAllocState_Type.__name__ = "Integer32"
_StorMgmtDiskVolAllocState_Object = MibTableColumn
storMgmtDiskVolAllocState = _StorMgmtDiskVolAllocState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 4, 10, 1, 7),
    _StorMgmtDiskVolAllocState_Type()
)
storMgmtDiskVolAllocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtDiskVolAllocState.setStatus("mandatory")


class _StorMgmtDiskPrivDiskRunState_Type(Integer32):
    """Custom type storMgmtDiskPrivDiskRunState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("end-in-process", 4),
          ("inactive", 3),
          ("offline", 1),
          ("unknown", 255))
    )


_StorMgmtDiskPrivDiskRunState_Type.__name__ = "Integer32"
_StorMgmtDiskPrivDiskRunState_Object = MibTableColumn
storMgmtDiskPrivDiskRunState = _StorMgmtDiskPrivDiskRunState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 4, 10, 1, 8),
    _StorMgmtDiskPrivDiskRunState_Type()
)
storMgmtDiskPrivDiskRunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtDiskPrivDiskRunState.setStatus("mandatory")


class _StorMgmtDiskPhaseSet_Type(Integer32):
    """Custom type storMgmtDiskPhaseSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("in-use", 4),
          ("mounting", 3),
          ("not-specified", 5),
          ("online-only", 1),
          ("premounting", 2),
          ("unknown", 255))
    )


_StorMgmtDiskPhaseSet_Type.__name__ = "Integer32"
_StorMgmtDiskPhaseSet_Object = MibTableColumn
storMgmtDiskPhaseSet = _StorMgmtDiskPhaseSet_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 4, 10, 1, 9),
    _StorMgmtDiskPhaseSet_Type()
)
storMgmtDiskPhaseSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtDiskPhaseSet.setStatus("mandatory")


class _StorMgmtDiskActionState_Type(Integer32):
    """Custom type storMgmtDiskActionState based on Integer32"""
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
              10,
              11,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cancelled", 4),
          ("dismount", 11),
          ("inoperable", 2),
          ("no-action", 1),
          ("no-device-available", 5),
          ("positioning", 7),
          ("recover", 6),
          ("remount", 3),
          ("svl-update", 10),
          ("unknown", 255),
          ("unlock", 9),
          ("writepermission-missing", 8))
    )


_StorMgmtDiskActionState_Type.__name__ = "Integer32"
_StorMgmtDiskActionState_Object = MibTableColumn
storMgmtDiskActionState = _StorMgmtDiskActionState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 4, 10, 1, 10),
    _StorMgmtDiskActionState_Type()
)
storMgmtDiskActionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtDiskActionState.setStatus("mandatory")


class _StorMgmtDiskUse_Type(Integer32):
    """Custom type storMgmtDiskUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dms", 1),
          ("special", 2),
          ("unknown", 255),
          ("work", 3))
    )


_StorMgmtDiskUse_Type.__name__ = "Integer32"
_StorMgmtDiskUse_Object = MibTableColumn
storMgmtDiskUse = _StorMgmtDiskUse_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 4, 10, 1, 11),
    _StorMgmtDiskUse_Type()
)
storMgmtDiskUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtDiskUse.setStatus("mandatory")


class _StorMgmtDiskAssignTime_Type(Integer32):
    """Custom type storMgmtDiskAssignTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("operator", 4),
          ("operator-by-default", 5),
          ("standard", 1),
          ("unknown", 255),
          ("user", 2),
          ("user-by-default", 3))
    )


_StorMgmtDiskAssignTime_Type.__name__ = "Integer32"
_StorMgmtDiskAssignTime_Object = MibTableColumn
storMgmtDiskAssignTime = _StorMgmtDiskAssignTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 4, 10, 1, 12),
    _StorMgmtDiskAssignTime_Type()
)
storMgmtDiskAssignTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtDiskAssignTime.setStatus("mandatory")


class _StorMgmtDiskUserAllocation_Type(Integer32):
    """Custom type storMgmtDiskUserAllocation based on Integer32"""
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
        *(("all", 8),
          ("all-by-default", 9),
          ("exclusive", 4),
          ("exclusive-by-default", 5),
          ("no", 6),
          ("no-by-default", 7),
          ("shared", 2),
          ("shared-by-default", 3),
          ("standard", 1),
          ("unknown", 255))
    )


_StorMgmtDiskUserAllocation_Type.__name__ = "Integer32"
_StorMgmtDiskUserAllocation_Object = MibTableColumn
storMgmtDiskUserAllocation = _StorMgmtDiskUserAllocation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 4, 10, 1, 13),
    _StorMgmtDiskUserAllocation_Type()
)
storMgmtDiskUserAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtDiskUserAllocation.setStatus("mandatory")


class _StorMgmtDiskOperatorControl_Type(Integer32):
    """Custom type storMgmtDiskOperatorControl based on Integer32"""
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
        *(("all", 8),
          ("all-by-default", 9),
          ("exclusive", 4),
          ("exclusive-by-default", 5),
          ("no", 6),
          ("no-by-default", 7),
          ("shared", 2),
          ("shared-by-default", 3),
          ("standard", 1),
          ("unknown", 255))
    )


_StorMgmtDiskOperatorControl_Type.__name__ = "Integer32"
_StorMgmtDiskOperatorControl_Object = MibTableColumn
storMgmtDiskOperatorControl = _StorMgmtDiskOperatorControl_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 4, 10, 1, 14),
    _StorMgmtDiskOperatorControl_Type()
)
storMgmtDiskOperatorControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtDiskOperatorControl.setStatus("mandatory")


class _StorMgmtDiskSystemAllocation_Type(Integer32):
    """Custom type storMgmtDiskSystemAllocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("current-exclusive", 5),
          ("current-shared", 4),
          ("exclusive", 2),
          ("shared", 1),
          ("unknown", 255))
    )


_StorMgmtDiskSystemAllocation_Type.__name__ = "Integer32"
_StorMgmtDiskSystemAllocation_Object = MibTableColumn
storMgmtDiskSystemAllocation = _StorMgmtDiskSystemAllocation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 4, 10, 1, 15),
    _StorMgmtDiskSystemAllocation_Type()
)
storMgmtDiskSystemAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtDiskSystemAllocation.setStatus("mandatory")


class _StorMgmtDiskAccess_Type(Integer32):
    """Custom type storMgmtDiskAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("from-device", 3),
          ("ppd", 2),
          ("ppd-from-device", 5),
          ("unknown", 255),
          ("write", 1),
          ("write-from-device", 4))
    )


_StorMgmtDiskAccess_Type.__name__ = "Integer32"
_StorMgmtDiskAccess_Object = MibTableColumn
storMgmtDiskAccess = _StorMgmtDiskAccess_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 4, 10, 1, 16),
    _StorMgmtDiskAccess_Type()
)
storMgmtDiskAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtDiskAccess.setStatus("mandatory")


class _StorMgmtDiskRecordingMode_Type(Integer32):
    """Custom type storMgmtDiskRecordingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dual-recording-by-volume", 2),
          ("single-recording", 1),
          ("unknown", 255))
    )


_StorMgmtDiskRecordingMode_Type.__name__ = "Integer32"
_StorMgmtDiskRecordingMode_Object = MibTableColumn
storMgmtDiskRecordingMode = _StorMgmtDiskRecordingMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 4, 10, 1, 17),
    _StorMgmtDiskRecordingMode_Type()
)
storMgmtDiskRecordingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtDiskRecordingMode.setStatus("mandatory")
_SniStorMgmtGlobalData_ObjectIdentity = ObjectIdentity
sniStorMgmtGlobalData = _SniStorMgmtGlobalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 18)
)


class _StorMgmtGlobalDataVersion_Type(DisplayString):
    """Custom type storMgmtGlobalDataVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_StorMgmtGlobalDataVersion_Type.__name__ = "DisplayString"
_StorMgmtGlobalDataVersion_Object = MibScalar
storMgmtGlobalDataVersion = _StorMgmtGlobalDataVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 18, 1),
    _StorMgmtGlobalDataVersion_Type()
)
storMgmtGlobalDataVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storMgmtGlobalDataVersion.setStatus("mandatory")
_StorMgmtGlobalDataInputFile_Type = DisplayString
_StorMgmtGlobalDataInputFile_Object = MibScalar
storMgmtGlobalDataInputFile = _StorMgmtGlobalDataInputFile_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 18, 2),
    _StorMgmtGlobalDataInputFile_Type()
)
storMgmtGlobalDataInputFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    storMgmtGlobalDataInputFile.setStatus("mandatory")
_SniStorMgmtPubsetTraps_ObjectIdentity = ObjectIdentity
sniStorMgmtPubsetTraps = _SniStorMgmtPubsetTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 20)
)
_SniStorMgmtDiskTraps_ObjectIdentity = ObjectIdentity
sniStorMgmtDiskTraps = _SniStorMgmtDiskTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 21)
)

# Managed Objects groups


# Notification objects

storMgmtHsmsS1Bottleneck = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 2, 0, 1)
)
if mibBuilder.loadTexts:
    storMgmtHsmsS1Bottleneck.setStatus(
        ""
    )

storMgmtMarenNoVolume = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 3, 0, 1)
)
if mibBuilder.loadTexts:
    storMgmtMarenNoVolume.setStatus(
        ""
    )

storMgmtTlsOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 4, 0, 1)
)
if mibBuilder.loadTexts:
    storMgmtTlsOffline.setStatus(
        ""
    )

storMgmtRobarBs2Messages = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 1, 5, 0, 1)
)
if mibBuilder.loadTexts:
    storMgmtRobarBs2Messages.setStatus(
        ""
    )

storMgmtPubsetSatLevTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 20, 0, 301)
)
storMgmtPubsetSatLevTrap.setObjects(
      *(("Storage-Management-MIB", "storMgmtPubsetIndex"),
        ("Storage-Management-MIB", "storMgmtPubsetSaturationLevel"))
)
if mibBuilder.loadTexts:
    storMgmtPubsetSatLevTrap.setStatus(
        ""
    )

storMgmtDiskReconfStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 20, 21, 0, 301)
)
storMgmtDiskReconfStateTrap.setObjects(
      *(("Storage-Management-MIB", "storMgmtDiskIndex"),
        ("Storage-Management-MIB", "storMgmtDiskReconfState"))
)
if mibBuilder.loadTexts:
    storMgmtDiskReconfStateTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Storage-Management-MIB",
    **{"sni": sni,
       "sniProductMibs": sniProductMibs,
       "sniStorMgmt": sniStorMgmt,
       "sniStorMgmtAvailInfo": sniStorMgmtAvailInfo,
       "sniStorMgmtProductInfo": sniStorMgmtProductInfo,
       "storMgmtProductTabNum": storMgmtProductTabNum,
       "storMgmtProductTable": storMgmtProductTable,
       "storMgmtProductEntry": storMgmtProductEntry,
       "storMgmtProductIndex": storMgmtProductIndex,
       "storMgmtProductName": storMgmtProductName,
       "storMgmtProductVersion": storMgmtProductVersion,
       "storMgmtProductState": storMgmtProductState,
       "storMgmtProductTimestamp": storMgmtProductTimestamp,
       "sniStorMgmtHsmsInfo": sniStorMgmtHsmsInfo,
       "storMgmtHsmsS1Bottleneck": storMgmtHsmsS1Bottleneck,
       "storMgmtHsmsOpmode": storMgmtHsmsOpmode,
       "storMgmtHsmsModeTimestamp": storMgmtHsmsModeTimestamp,
       "storMgmtHsmsServertask": storMgmtHsmsServertask,
       "storMgmtHsmsWaitJobs": storMgmtHsmsWaitJobs,
       "storMgmtHsmsInstances": storMgmtHsmsInstances,
       "storMgmtHsmsAcceptReqs": storMgmtHsmsAcceptReqs,
       "storMgmtHsmsCompleteReqs": storMgmtHsmsCompleteReqs,
       "storMgmtHsmsInterruptReqs": storMgmtHsmsInterruptReqs,
       "storMgmtHsmsWaitReqsRead": storMgmtHsmsWaitReqsRead,
       "storMgmtHsmsWaitReqsWrite": storMgmtHsmsWaitReqsWrite,
       "storMgmtHsmsWaitReqsExpress": storMgmtHsmsWaitReqsExpress,
       "storMgmtHsmsStimeRead": storMgmtHsmsStimeRead,
       "storMgmtHsmsStimeWrite": storMgmtHsmsStimeWrite,
       "storMgmtHsmsStimeExpress": storMgmtHsmsStimeExpress,
       "storMgmtHsmsNetload": storMgmtHsmsNetload,
       "sniStorMgmtMarenInfo": sniStorMgmtMarenInfo,
       "storMgmtMarenNoVolume": storMgmtMarenNoVolume,
       "storMgmtMarenCPTask": storMgmtMarenCPTask,
       "storMgmtMarenUCPTask": storMgmtMarenUCPTask,
       "storMgmtMarenCatConn": storMgmtMarenCatConn,
       "storMgmtMarenConnState": storMgmtMarenConnState,
       "storMgmtMarenLocTabNum": storMgmtMarenLocTabNum,
       "storMgmtMarenLocTable": storMgmtMarenLocTable,
       "storMgmtMarenLocEntry": storMgmtMarenLocEntry,
       "storMgmtMarenLocIndex": storMgmtMarenLocIndex,
       "storMgmtMarenLocName": storMgmtMarenLocName,
       "storMgmtMarenLocOpmode": storMgmtMarenLocOpmode,
       "storMgmtMarenLocFreevol": storMgmtMarenLocFreevol,
       "storMgmtMarenNetworkTabNum": storMgmtMarenNetworkTabNum,
       "storMgmtMarenNetworkTable": storMgmtMarenNetworkTable,
       "storMgmtMarenNetworkEntry": storMgmtMarenNetworkEntry,
       "storMgmtMarenNetworkIndex": storMgmtMarenNetworkIndex,
       "storMgmtMarenNetworkHost": storMgmtMarenNetworkHost,
       "sniStorMgmtTlsInfo": sniStorMgmtTlsInfo,
       "storMgmtTlsOffline": storMgmtTlsOffline,
       "storMgmtTlsTabNum": storMgmtTlsTabNum,
       "storMgmtTlsTable": storMgmtTlsTable,
       "storMgmtTlsEntry": storMgmtTlsEntry,
       "storMgmtTlsIndex": storMgmtTlsIndex,
       "storMgmtTlsRobState": storMgmtTlsRobState,
       "storMgmtTlsFreeboxno": storMgmtTlsFreeboxno,
       "storMgmtTlsCleanno": storMgmtTlsCleanno,
       "storMgmtTlsLocation": storMgmtTlsLocation,
       "sniStorMgmtRobarInfo": sniStorMgmtRobarInfo,
       "storMgmtRobarBs2Messages": storMgmtRobarBs2Messages,
       "storMgmtRobarTabNum": storMgmtRobarTabNum,
       "storMgmtRobarTable": storMgmtRobarTable,
       "storMgmtRobarEntry": storMgmtRobarEntry,
       "storMgmtRobarIndex": storMgmtRobarIndex,
       "storMgmtRobarLocation": storMgmtRobarLocation,
       "storMgmtRobarState": storMgmtRobarState,
       "storMgmtRobarVersion": storMgmtRobarVersion,
       "storMgmtRobarConnState": storMgmtRobarConnState,
       "storMgmtRobarRobState": storMgmtRobarRobState,
       "storMgmtRobarRouting": storMgmtRobarRouting,
       "sniStorMgmtResourceInfo": sniStorMgmtResourceInfo,
       "storMgmtResourcePubset": storMgmtResourcePubset,
       "storMgmtResourceSaturation": storMgmtResourceSaturation,
       "storMgmtResourceCapacity": storMgmtResourceCapacity,
       "storMgmtResourceSpaceAllocated": storMgmtResourceSpaceAllocated,
       "storMgmtResourceFragment": storMgmtResourceFragment,
       "storMgmtResourceReusableS1": storMgmtResourceReusableS1,
       "storMgmtResourceSecureQueue": storMgmtResourceSecureQueue,
       "sniStorMgmtPubsetInfo": sniStorMgmtPubsetInfo,
       "storMgmtPubsetTabNum": storMgmtPubsetTabNum,
       "storMgmtPubsetTabState": storMgmtPubsetTabState,
       "storMgmtPubsetTable": storMgmtPubsetTable,
       "storMgmtPubsetEntry": storMgmtPubsetEntry,
       "storMgmtPubsetIndex": storMgmtPubsetIndex,
       "storMgmtPubsetTyp": storMgmtPubsetTyp,
       "storMgmtPubsetLocal": storMgmtPubsetLocal,
       "storMgmtPubsetHome": storMgmtPubsetHome,
       "storMgmtPubsetShared": storMgmtPubsetShared,
       "storMgmtPubsetMaster": storMgmtPubsetMaster,
       "storMgmtPubsetAccessible": storMgmtPubsetAccessible,
       "storMgmtPubsetQuiet": storMgmtPubsetQuiet,
       "storMgmtPubsetPaging": storMgmtPubsetPaging,
       "storMgmtPubsetSize": storMgmtPubsetSize,
       "storMgmtPubsetUsedSize": storMgmtPubsetUsedSize,
       "storMgmtPubsetSaturationLevel": storMgmtPubsetSaturationLevel,
       "sniStorMgmtDiskInfo": sniStorMgmtDiskInfo,
       "storMgmtDiskTabNum": storMgmtDiskTabNum,
       "storMgmtDiskTabReconfState": storMgmtDiskTabReconfState,
       "storMgmtDiskTable": storMgmtDiskTable,
       "storMgmtDiskEntry": storMgmtDiskEntry,
       "storMgmtDiskIndex": storMgmtDiskIndex,
       "storMgmtDiskVSN": storMgmtDiskVSN,
       "storMgmtDiskDeviceAllocState": storMgmtDiskDeviceAllocState,
       "storMgmtDiskSystemUse": storMgmtDiskSystemUse,
       "storMgmtDiskPoolAttribut": storMgmtDiskPoolAttribut,
       "storMgmtDiskReconfState": storMgmtDiskReconfState,
       "storMgmtDiskVolAllocState": storMgmtDiskVolAllocState,
       "storMgmtDiskPrivDiskRunState": storMgmtDiskPrivDiskRunState,
       "storMgmtDiskPhaseSet": storMgmtDiskPhaseSet,
       "storMgmtDiskActionState": storMgmtDiskActionState,
       "storMgmtDiskUse": storMgmtDiskUse,
       "storMgmtDiskAssignTime": storMgmtDiskAssignTime,
       "storMgmtDiskUserAllocation": storMgmtDiskUserAllocation,
       "storMgmtDiskOperatorControl": storMgmtDiskOperatorControl,
       "storMgmtDiskSystemAllocation": storMgmtDiskSystemAllocation,
       "storMgmtDiskAccess": storMgmtDiskAccess,
       "storMgmtDiskRecordingMode": storMgmtDiskRecordingMode,
       "sniStorMgmtGlobalData": sniStorMgmtGlobalData,
       "storMgmtGlobalDataVersion": storMgmtGlobalDataVersion,
       "storMgmtGlobalDataInputFile": storMgmtGlobalDataInputFile,
       "sniStorMgmtPubsetTraps": sniStorMgmtPubsetTraps,
       "storMgmtPubsetSatLevTrap": storMgmtPubsetSatLevTrap,
       "sniStorMgmtDiskTraps": sniStorMgmtDiskTraps,
       "storMgmtDiskReconfStateTrap": storMgmtDiskReconfStateTrap}
)
