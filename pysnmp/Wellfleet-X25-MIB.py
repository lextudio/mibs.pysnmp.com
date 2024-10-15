# SNMP MIB module (Wellfleet-X25-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-X25-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:32 2024
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

(wfX25Group,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfX25Group")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfX25_ObjectIdentity = ObjectIdentity
wfX25 = _WfX25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 1)
)


class _WfX25Delete_Type(Integer32):
    """Custom type wfX25Delete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfX25Delete_Type.__name__ = "Integer32"
_WfX25Delete_Object = MibScalar
wfX25Delete = _WfX25Delete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 1, 1),
    _WfX25Delete_Type()
)
wfX25Delete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25Delete.setStatus("mandatory")


class _WfX25Disable_Type(Integer32):
    """Custom type wfX25Disable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfX25Disable_Type.__name__ = "Integer32"
_WfX25Disable_Object = MibScalar
wfX25Disable = _WfX25Disable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 1, 2),
    _WfX25Disable_Type()
)
wfX25Disable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25Disable.setStatus("mandatory")


class _WfX25State_Type(Integer32):
    """Custom type wfX25State based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfX25State_Type.__name__ = "Integer32"
_WfX25State_Object = MibScalar
wfX25State = _WfX25State_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 1, 3),
    _WfX25State_Type()
)
wfX25State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25State.setStatus("mandatory")
_WfX25ServiceTable_Object = MibTable
wfX25ServiceTable = _WfX25ServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2)
)
if mibBuilder.loadTexts:
    wfX25ServiceTable.setStatus("mandatory")
_WfX25ServiceEntry_Object = MibTableRow
wfX25ServiceEntry = _WfX25ServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1)
)
wfX25ServiceEntry.setIndexNames(
    (0, "Wellfleet-X25-MIB", "wfX25ServiceSlot"),
    (0, "Wellfleet-X25-MIB", "wfX25ServiceConnector"),
    (0, "Wellfleet-X25-MIB", "wfX25ServiceLineNumber"),
    (0, "Wellfleet-X25-MIB", "wfX25ServiceLLIndex"),
    (0, "Wellfleet-X25-MIB", "wfX25ServiceCct"),
    (0, "Wellfleet-X25-MIB", "wfX25ServiceIndex"),
)
if mibBuilder.loadTexts:
    wfX25ServiceEntry.setStatus("mandatory")


class _WfX25ServiceDelete_Type(Integer32):
    """Custom type wfX25ServiceDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfX25ServiceDelete_Type.__name__ = "Integer32"
_WfX25ServiceDelete_Object = MibTableColumn
wfX25ServiceDelete = _WfX25ServiceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 1),
    _WfX25ServiceDelete_Type()
)
wfX25ServiceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceDelete.setStatus("mandatory")


class _WfX25ServiceDisable_Type(Integer32):
    """Custom type wfX25ServiceDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfX25ServiceDisable_Type.__name__ = "Integer32"
_WfX25ServiceDisable_Object = MibTableColumn
wfX25ServiceDisable = _WfX25ServiceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 2),
    _WfX25ServiceDisable_Type()
)
wfX25ServiceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceDisable.setStatus("mandatory")


class _WfX25ServiceSlot_Type(Integer32):
    """Custom type wfX25ServiceSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfX25ServiceSlot_Type.__name__ = "Integer32"
_WfX25ServiceSlot_Object = MibTableColumn
wfX25ServiceSlot = _WfX25ServiceSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 3),
    _WfX25ServiceSlot_Type()
)
wfX25ServiceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25ServiceSlot.setStatus("mandatory")


class _WfX25ServiceConnector_Type(Integer32):
    """Custom type wfX25ServiceConnector based on Integer32"""
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
        *(("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfX25ServiceConnector_Type.__name__ = "Integer32"
_WfX25ServiceConnector_Object = MibTableColumn
wfX25ServiceConnector = _WfX25ServiceConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 4),
    _WfX25ServiceConnector_Type()
)
wfX25ServiceConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25ServiceConnector.setStatus("mandatory")
_WfX25ServiceLineNumber_Type = Integer32
_WfX25ServiceLineNumber_Object = MibTableColumn
wfX25ServiceLineNumber = _WfX25ServiceLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 5),
    _WfX25ServiceLineNumber_Type()
)
wfX25ServiceLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25ServiceLineNumber.setStatus("mandatory")
_WfX25ServiceLLIndex_Type = Integer32
_WfX25ServiceLLIndex_Object = MibTableColumn
wfX25ServiceLLIndex = _WfX25ServiceLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 6),
    _WfX25ServiceLLIndex_Type()
)
wfX25ServiceLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25ServiceLLIndex.setStatus("mandatory")


class _WfX25ServiceCct_Type(Integer32):
    """Custom type wfX25ServiceCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfX25ServiceCct_Type.__name__ = "Integer32"
_WfX25ServiceCct_Object = MibTableColumn
wfX25ServiceCct = _WfX25ServiceCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 7),
    _WfX25ServiceCct_Type()
)
wfX25ServiceCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25ServiceCct.setStatus("mandatory")


class _WfX25ServiceIndex_Type(Integer32):
    """Custom type wfX25ServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_WfX25ServiceIndex_Type.__name__ = "Integer32"
_WfX25ServiceIndex_Object = MibTableColumn
wfX25ServiceIndex = _WfX25ServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 8),
    _WfX25ServiceIndex_Type()
)
wfX25ServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25ServiceIndex.setStatus("mandatory")


class _WfX25ServiceType_Type(Integer32):
    """Custom type wfX25ServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64)
        )
    )
    namedValues = NamedValues(
        *(("ddntype", 2),
          ("defaulttype", 64),
          ("ipextype", 16),
          ("npttype", 8),
          ("pdntype", 1),
          ("ptoptype", 4),
          ("qllctype", 32))
    )


_WfX25ServiceType_Type.__name__ = "Integer32"
_WfX25ServiceType_Object = MibTableColumn
wfX25ServiceType = _WfX25ServiceType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 9),
    _WfX25ServiceType_Type()
)
wfX25ServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceType.setStatus("mandatory")


class _WfX25ServiceConnRef_Type(Integer32):
    """Custom type wfX25ServiceConnRef based on Integer32"""
    defaultValue = 2

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


_WfX25ServiceConnRef_Type.__name__ = "Integer32"
_WfX25ServiceConnRef_Object = MibTableColumn
wfX25ServiceConnRef = _WfX25ServiceConnRef_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 10),
    _WfX25ServiceConnRef_Type()
)
wfX25ServiceConnRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25ServiceConnRef.setStatus("mandatory")


class _WfX25ServiceConnId_Type(Integer32):
    """Custom type wfX25ServiceConnId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfX25ServiceConnId_Type.__name__ = "Integer32"
_WfX25ServiceConnId_Object = MibTableColumn
wfX25ServiceConnId = _WfX25ServiceConnId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 11),
    _WfX25ServiceConnId_Type()
)
wfX25ServiceConnId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceConnId.setStatus("mandatory")
_WfX25ServiceRemoteX121Addr_Type = DisplayString
_WfX25ServiceRemoteX121Addr_Object = MibTableColumn
wfX25ServiceRemoteX121Addr = _WfX25ServiceRemoteX121Addr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 12),
    _WfX25ServiceRemoteX121Addr_Type()
)
wfX25ServiceRemoteX121Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceRemoteX121Addr.setStatus("mandatory")
_WfX25ServiceRemoteIpAddr_Type = IpAddress
_WfX25ServiceRemoteIpAddr_Object = MibTableColumn
wfX25ServiceRemoteIpAddr = _WfX25ServiceRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 13),
    _WfX25ServiceRemoteIpAddr_Type()
)
wfX25ServiceRemoteIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceRemoteIpAddr.setStatus("mandatory")


class _WfX25ServiceBCast_Type(Integer32):
    """Custom type wfX25ServiceBCast based on Integer32"""
    defaultValue = 2

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


_WfX25ServiceBCast_Type.__name__ = "Integer32"
_WfX25ServiceBCast_Object = MibTableColumn
wfX25ServiceBCast = _WfX25ServiceBCast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 14),
    _WfX25ServiceBCast_Type()
)
wfX25ServiceBCast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceBCast.setStatus("mandatory")


class _WfX25ServiceMaxConn_Type(Integer32):
    """Custom type wfX25ServiceMaxConn based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WfX25ServiceMaxConn_Type.__name__ = "Integer32"
_WfX25ServiceMaxConn_Object = MibTableColumn
wfX25ServiceMaxConn = _WfX25ServiceMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 15),
    _WfX25ServiceMaxConn_Type()
)
wfX25ServiceMaxConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceMaxConn.setStatus("mandatory")


class _WfX25ServicePrecedence_Type(Integer32):
    """Custom type wfX25ServicePrecedence based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 2),
          ("negot", 1))
    )


_WfX25ServicePrecedence_Type.__name__ = "Integer32"
_WfX25ServicePrecedence_Object = MibTableColumn
wfX25ServicePrecedence = _WfX25ServicePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 16),
    _WfX25ServicePrecedence_Type()
)
wfX25ServicePrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServicePrecedence.setStatus("mandatory")


class _WfX25ServiceMaxIdle_Type(Integer32):
    """Custom type wfX25ServiceMaxIdle based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_WfX25ServiceMaxIdle_Type.__name__ = "Integer32"
_WfX25ServiceMaxIdle_Object = MibTableColumn
wfX25ServiceMaxIdle = _WfX25ServiceMaxIdle_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 17),
    _WfX25ServiceMaxIdle_Type()
)
wfX25ServiceMaxIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceMaxIdle.setStatus("mandatory")


class _WfX25ServiceCallRetry_Type(Integer32):
    """Custom type wfX25ServiceCallRetry based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 999),
    )


_WfX25ServiceCallRetry_Type.__name__ = "Integer32"
_WfX25ServiceCallRetry_Object = MibTableColumn
wfX25ServiceCallRetry = _WfX25ServiceCallRetry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 18),
    _WfX25ServiceCallRetry_Type()
)
wfX25ServiceCallRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceCallRetry.setStatus("mandatory")


class _WfX25ServiceFlowFacility_Type(Integer32):
    """Custom type wfX25ServiceFlowFacility based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 2),
          ("negot", 1))
    )


_WfX25ServiceFlowFacility_Type.__name__ = "Integer32"
_WfX25ServiceFlowFacility_Object = MibTableColumn
wfX25ServiceFlowFacility = _WfX25ServiceFlowFacility_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 19),
    _WfX25ServiceFlowFacility_Type()
)
wfX25ServiceFlowFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceFlowFacility.setStatus("mandatory")


class _WfX25ServiceWinSize_Type(Integer32):
    """Custom type wfX25ServiceWinSize based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WfX25ServiceWinSize_Type.__name__ = "Integer32"
_WfX25ServiceWinSize_Object = MibTableColumn
wfX25ServiceWinSize = _WfX25ServiceWinSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 20),
    _WfX25ServiceWinSize_Type()
)
wfX25ServiceWinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceWinSize.setStatus("mandatory")


class _WfX25ServicePktSize_Type(Integer32):
    """Custom type wfX25ServicePktSize based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("size1024", 10),
          ("size128", 7),
          ("size16", 4),
          ("size2048", 11),
          ("size256", 8),
          ("size32", 5),
          ("size4096", 12),
          ("size512", 9),
          ("size64", 6))
    )


_WfX25ServicePktSize_Type.__name__ = "Integer32"
_WfX25ServicePktSize_Object = MibTableColumn
wfX25ServicePktSize = _WfX25ServicePktSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 21),
    _WfX25ServicePktSize_Type()
)
wfX25ServicePktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServicePktSize.setStatus("mandatory")


class _WfX25ServiceFastSelRequest_Type(Integer32):
    """Custom type wfX25ServiceFastSelRequest based on Integer32"""
    defaultValue = 2

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


_WfX25ServiceFastSelRequest_Type.__name__ = "Integer32"
_WfX25ServiceFastSelRequest_Object = MibTableColumn
wfX25ServiceFastSelRequest = _WfX25ServiceFastSelRequest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 22),
    _WfX25ServiceFastSelRequest_Type()
)
wfX25ServiceFastSelRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceFastSelRequest.setStatus("mandatory")


class _WfX25ServiceFastSelAccept_Type(Integer32):
    """Custom type wfX25ServiceFastSelAccept based on Integer32"""
    defaultValue = 2

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


_WfX25ServiceFastSelAccept_Type.__name__ = "Integer32"
_WfX25ServiceFastSelAccept_Object = MibTableColumn
wfX25ServiceFastSelAccept = _WfX25ServiceFastSelAccept_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 23),
    _WfX25ServiceFastSelAccept_Type()
)
wfX25ServiceFastSelAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceFastSelAccept.setStatus("mandatory")


class _WfX25ServiceRevChRequest_Type(Integer32):
    """Custom type wfX25ServiceRevChRequest based on Integer32"""
    defaultValue = 2

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


_WfX25ServiceRevChRequest_Type.__name__ = "Integer32"
_WfX25ServiceRevChRequest_Object = MibTableColumn
wfX25ServiceRevChRequest = _WfX25ServiceRevChRequest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 24),
    _WfX25ServiceRevChRequest_Type()
)
wfX25ServiceRevChRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceRevChRequest.setStatus("mandatory")


class _WfX25ServiceRevChAccept_Type(Integer32):
    """Custom type wfX25ServiceRevChAccept based on Integer32"""
    defaultValue = 2

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


_WfX25ServiceRevChAccept_Type.__name__ = "Integer32"
_WfX25ServiceRevChAccept_Object = MibTableColumn
wfX25ServiceRevChAccept = _WfX25ServiceRevChAccept_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 25),
    _WfX25ServiceRevChAccept_Type()
)
wfX25ServiceRevChAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceRevChAccept.setStatus("mandatory")


class _WfX25ServiceCugFormat_Type(Integer32):
    """Custom type wfX25ServiceCugFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("basic", 2),
          ("ext", 3),
          ("none", 1))
    )


_WfX25ServiceCugFormat_Type.__name__ = "Integer32"
_WfX25ServiceCugFormat_Object = MibTableColumn
wfX25ServiceCugFormat = _WfX25ServiceCugFormat_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 26),
    _WfX25ServiceCugFormat_Type()
)
wfX25ServiceCugFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceCugFormat.setStatus("mandatory")


class _WfX25ServiceCugType_Type(Integer32):
    """Custom type wfX25ServiceCugType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bilat", 3),
          ("normal", 1),
          ("oa", 2))
    )


_WfX25ServiceCugType_Type.__name__ = "Integer32"
_WfX25ServiceCugType_Object = MibTableColumn
wfX25ServiceCugType = _WfX25ServiceCugType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 27),
    _WfX25ServiceCugType_Type()
)
wfX25ServiceCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceCugType.setStatus("mandatory")


class _WfX25ServiceCugNum_Type(Integer32):
    """Custom type wfX25ServiceCugNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_WfX25ServiceCugNum_Type.__name__ = "Integer32"
_WfX25ServiceCugNum_Object = MibTableColumn
wfX25ServiceCugNum = _WfX25ServiceCugNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 28),
    _WfX25ServiceCugNum_Type()
)
wfX25ServiceCugNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceCugNum.setStatus("mandatory")
_WfX25ServiceUserFacility_Type = OctetString
_WfX25ServiceUserFacility_Object = MibTableColumn
wfX25ServiceUserFacility = _WfX25ServiceUserFacility_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 29),
    _WfX25ServiceUserFacility_Type()
)
wfX25ServiceUserFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceUserFacility.setStatus("mandatory")


class _WfX25ServiceValid_Type(Integer32):
    """Custom type wfX25ServiceValid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_WfX25ServiceValid_Type.__name__ = "Integer32"
_WfX25ServiceValid_Object = MibTableColumn
wfX25ServiceValid = _WfX25ServiceValid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 30),
    _WfX25ServiceValid_Type()
)
wfX25ServiceValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25ServiceValid.setStatus("mandatory")


class _WfX25ServiceBFE_Type(Integer32):
    """Custom type wfX25ServiceBFE based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfX25ServiceBFE_Type.__name__ = "Integer32"
_WfX25ServiceBFE_Object = MibTableColumn
wfX25ServiceBFE = _WfX25ServiceBFE_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 31),
    _WfX25ServiceBFE_Type()
)
wfX25ServiceBFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceBFE.setStatus("mandatory")


class _WfX25ServiceForceCugZero_Type(Integer32):
    """Custom type wfX25ServiceForceCugZero based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfX25ServiceForceCugZero_Type.__name__ = "Integer32"
_WfX25ServiceForceCugZero_Object = MibTableColumn
wfX25ServiceForceCugZero = _WfX25ServiceForceCugZero_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 32),
    _WfX25ServiceForceCugZero_Type()
)
wfX25ServiceForceCugZero.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceForceCugZero.setStatus("mandatory")


class _WfX25ServiceWcpEnable_Type(Integer32):
    """Custom type wfX25ServiceWcpEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfX25ServiceWcpEnable_Type.__name__ = "Integer32"
_WfX25ServiceWcpEnable_Object = MibTableColumn
wfX25ServiceWcpEnable = _WfX25ServiceWcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 33),
    _WfX25ServiceWcpEnable_Type()
)
wfX25ServiceWcpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceWcpEnable.setStatus("mandatory")


class _WfX25ServiceMUX_Type(Integer32):
    """Custom type wfX25ServiceMUX based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfX25ServiceMUX_Type.__name__ = "Integer32"
_WfX25ServiceMUX_Object = MibTableColumn
wfX25ServiceMUX = _WfX25ServiceMUX_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 34),
    _WfX25ServiceMUX_Type()
)
wfX25ServiceMUX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceMUX.setStatus("mandatory")


class _WfX25ServicePtopCallRequest_Type(Integer32):
    """Custom type wfX25ServicePtopCallRequest based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("local", 2),
          ("remote", 3))
    )


_WfX25ServicePtopCallRequest_Type.__name__ = "Integer32"
_WfX25ServicePtopCallRequest_Object = MibTableColumn
wfX25ServicePtopCallRequest = _WfX25ServicePtopCallRequest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 35),
    _WfX25ServicePtopCallRequest_Type()
)
wfX25ServicePtopCallRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServicePtopCallRequest.setStatus("mandatory")


class _WfX25ServiceVcType_Type(Integer32):
    """Custom type wfX25ServiceVcType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 2),
          ("svc", 1))
    )


_WfX25ServiceVcType_Type.__name__ = "Integer32"
_WfX25ServiceVcType_Object = MibTableColumn
wfX25ServiceVcType = _WfX25ServiceVcType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 36),
    _WfX25ServiceVcType_Type()
)
wfX25ServiceVcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceVcType.setStatus("mandatory")


class _WfX25ServicePvcLcn_Type(Integer32):
    """Custom type wfX25ServicePvcLcn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WfX25ServicePvcLcn_Type.__name__ = "Integer32"
_WfX25ServicePvcLcn_Object = MibTableColumn
wfX25ServicePvcLcn = _WfX25ServicePvcLcn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 37),
    _WfX25ServicePvcLcn_Type()
)
wfX25ServicePvcLcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServicePvcLcn.setStatus("mandatory")


class _WfX25ServiceMacPoolStart_Type(OctetString):
    """Custom type wfX25ServiceMacPoolStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfX25ServiceMacPoolStart_Type.__name__ = "OctetString"
_WfX25ServiceMacPoolStart_Object = MibTableColumn
wfX25ServiceMacPoolStart = _WfX25ServiceMacPoolStart_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 38),
    _WfX25ServiceMacPoolStart_Type()
)
wfX25ServiceMacPoolStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceMacPoolStart.setStatus("mandatory")
_WfX25ServiceMacPoolSize_Type = Integer32
_WfX25ServiceMacPoolSize_Object = MibTableColumn
wfX25ServiceMacPoolSize = _WfX25ServiceMacPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 39),
    _WfX25ServiceMacPoolSize_Type()
)
wfX25ServiceMacPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceMacPoolSize.setStatus("mandatory")


class _WfX25ServiceWindowTimeout_Type(Integer32):
    """Custom type wfX25ServiceWindowTimeout based on Integer32"""
    defaultValue = 0


_WfX25ServiceWindowTimeout_Object = MibTableColumn
wfX25ServiceWindowTimeout = _WfX25ServiceWindowTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 40),
    _WfX25ServiceWindowTimeout_Type()
)
wfX25ServiceWindowTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceWindowTimeout.setStatus("mandatory")


class _WfX25ServiceVcBurstThroughput_Type(Integer32):
    """Custom type wfX25ServiceVcBurstThroughput based on Integer32"""
    defaultValue = 0


_WfX25ServiceVcBurstThroughput_Object = MibTableColumn
wfX25ServiceVcBurstThroughput = _WfX25ServiceVcBurstThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 41),
    _WfX25ServiceVcBurstThroughput_Type()
)
wfX25ServiceVcBurstThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceVcBurstThroughput.setStatus("mandatory")


class _WfX25ServiceVcBurstQDepth_Type(Integer32):
    """Custom type wfX25ServiceVcBurstQDepth based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfX25ServiceVcBurstQDepth_Type.__name__ = "Integer32"
_WfX25ServiceVcBurstQDepth_Object = MibTableColumn
wfX25ServiceVcBurstQDepth = _WfX25ServiceVcBurstQDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 42),
    _WfX25ServiceVcBurstQDepth_Type()
)
wfX25ServiceVcBurstQDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceVcBurstQDepth.setStatus("mandatory")


class _WfX25ServiceVcPriority_Type(Integer32):
    """Custom type wfX25ServiceVcPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_WfX25ServiceVcPriority_Type.__name__ = "Integer32"
_WfX25ServiceVcPriority_Object = MibTableColumn
wfX25ServiceVcPriority = _WfX25ServiceVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 43),
    _WfX25ServiceVcPriority_Type()
)
wfX25ServiceVcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceVcPriority.setStatus("mandatory")
_WfX25ServiceVcBurstQClippedPkts_Type = Counter32
_WfX25ServiceVcBurstQClippedPkts_Object = MibTableColumn
wfX25ServiceVcBurstQClippedPkts = _WfX25ServiceVcBurstQClippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 44),
    _WfX25ServiceVcBurstQClippedPkts_Type()
)
wfX25ServiceVcBurstQClippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25ServiceVcBurstQClippedPkts.setStatus("mandatory")
_WfX25ServiceVcBurstQPktCnt_Type = Counter32
_WfX25ServiceVcBurstQPktCnt_Object = MibTableColumn
wfX25ServiceVcBurstQPktCnt = _WfX25ServiceVcBurstQPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 45),
    _WfX25ServiceVcBurstQPktCnt_Type()
)
wfX25ServiceVcBurstQPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25ServiceVcBurstQPktCnt.setStatus("mandatory")
_WfX25ServiceVcBurstQHighWaterPkts_Type = Gauge32
_WfX25ServiceVcBurstQHighWaterPkts_Object = MibTableColumn
wfX25ServiceVcBurstQHighWaterPkts = _WfX25ServiceVcBurstQHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 46),
    _WfX25ServiceVcBurstQHighWaterPkts_Type()
)
wfX25ServiceVcBurstQHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25ServiceVcBurstQHighWaterPkts.setStatus("mandatory")
_WfX25ServiceVcPktDrops_Type = Counter32
_WfX25ServiceVcPktDrops_Object = MibTableColumn
wfX25ServiceVcPktDrops = _WfX25ServiceVcPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 47),
    _WfX25ServiceVcPktDrops_Type()
)
wfX25ServiceVcPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25ServiceVcPktDrops.setStatus("mandatory")
_WfX25ServicePlpPktDrops_Type = Counter32
_WfX25ServicePlpPktDrops_Object = MibTableColumn
wfX25ServicePlpPktDrops = _WfX25ServicePlpPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 48),
    _WfX25ServicePlpPktDrops_Type()
)
wfX25ServicePlpPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25ServicePlpPktDrops.setStatus("mandatory")
_WfX25ServiceBurstThrPerVc_Type = Integer32
_WfX25ServiceBurstThrPerVc_Object = MibTableColumn
wfX25ServiceBurstThrPerVc = _WfX25ServiceBurstThrPerVc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 49),
    _WfX25ServiceBurstThrPerVc_Type()
)
wfX25ServiceBurstThrPerVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25ServiceBurstThrPerVc.setStatus("mandatory")


class _WfX25ServiceBackupRecoveryDelay_Type(Integer32):
    """Custom type wfX25ServiceBackupRecoveryDelay based on Integer32"""
    defaultValue = 0


_WfX25ServiceBackupRecoveryDelay_Object = MibTableColumn
wfX25ServiceBackupRecoveryDelay = _WfX25ServiceBackupRecoveryDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 50),
    _WfX25ServiceBackupRecoveryDelay_Type()
)
wfX25ServiceBackupRecoveryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceBackupRecoveryDelay.setStatus("mandatory")


class _WfX25ServiceSetupTime_Type(Integer32):
    """Custom type wfX25ServiceSetupTime based on Integer32"""
    defaultValue = 60


_WfX25ServiceSetupTime_Object = MibTableColumn
wfX25ServiceSetupTime = _WfX25ServiceSetupTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 51),
    _WfX25ServiceSetupTime_Type()
)
wfX25ServiceSetupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceSetupTime.setStatus("mandatory")


class _WfX25ServiceRetryNumber_Type(Integer32):
    """Custom type wfX25ServiceRetryNumber based on Integer32"""
    defaultValue = 1


_WfX25ServiceRetryNumber_Object = MibTableColumn
wfX25ServiceRetryNumber = _WfX25ServiceRetryNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 52),
    _WfX25ServiceRetryNumber_Type()
)
wfX25ServiceRetryNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceRetryNumber.setStatus("mandatory")


class _WfX25BackupInitiation_Type(Integer32):
    """Custom type wfX25BackupInitiation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("last", 2))
    )


_WfX25BackupInitiation_Type.__name__ = "Integer32"
_WfX25BackupInitiation_Object = MibTableColumn
wfX25BackupInitiation = _WfX25BackupInitiation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 53),
    _WfX25BackupInitiation_Type()
)
wfX25BackupInitiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25BackupInitiation.setStatus("mandatory")
_WfX25ServiceEntryName_Type = DisplayString
_WfX25ServiceEntryName_Object = MibTableColumn
wfX25ServiceEntryName = _WfX25ServiceEntryName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 2, 1, 54),
    _WfX25ServiceEntryName_Type()
)
wfX25ServiceEntryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25ServiceEntryName.setStatus("mandatory")
_WfX25VcTable_Object = MibTable
wfX25VcTable = _WfX25VcTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4)
)
if mibBuilder.loadTexts:
    wfX25VcTable.setStatus("mandatory")
_WfX25VcEntry_Object = MibTableRow
wfX25VcEntry = _WfX25VcEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1)
)
wfX25VcEntry.setIndexNames(
    (0, "Wellfleet-X25-MIB", "wfX25VcSlotNum"),
    (0, "Wellfleet-X25-MIB", "wfX25VcConnector"),
    (0, "Wellfleet-X25-MIB", "wfX25VcLineNumber"),
    (0, "Wellfleet-X25-MIB", "wfX25VcLLIndex"),
    (0, "Wellfleet-X25-MIB", "wfX25VcCct"),
    (0, "Wellfleet-X25-MIB", "wfX25VcNumber"),
)
if mibBuilder.loadTexts:
    wfX25VcEntry.setStatus("mandatory")


class _WfX25VcSlotNum_Type(Integer32):
    """Custom type wfX25VcSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfX25VcSlotNum_Type.__name__ = "Integer32"
_WfX25VcSlotNum_Object = MibTableColumn
wfX25VcSlotNum = _WfX25VcSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 1),
    _WfX25VcSlotNum_Type()
)
wfX25VcSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcSlotNum.setStatus("mandatory")


class _WfX25VcConnector_Type(Integer32):
    """Custom type wfX25VcConnector based on Integer32"""
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
        *(("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfX25VcConnector_Type.__name__ = "Integer32"
_WfX25VcConnector_Object = MibTableColumn
wfX25VcConnector = _WfX25VcConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 2),
    _WfX25VcConnector_Type()
)
wfX25VcConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcConnector.setStatus("mandatory")
_WfX25VcLineNumber_Type = Integer32
_WfX25VcLineNumber_Object = MibTableColumn
wfX25VcLineNumber = _WfX25VcLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 3),
    _WfX25VcLineNumber_Type()
)
wfX25VcLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcLineNumber.setStatus("mandatory")
_WfX25VcLLIndex_Type = Integer32
_WfX25VcLLIndex_Object = MibTableColumn
wfX25VcLLIndex = _WfX25VcLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 4),
    _WfX25VcLLIndex_Type()
)
wfX25VcLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcLLIndex.setStatus("mandatory")
_WfX25VcCct_Type = Integer32
_WfX25VcCct_Object = MibTableColumn
wfX25VcCct = _WfX25VcCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 5),
    _WfX25VcCct_Type()
)
wfX25VcCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcCct.setStatus("mandatory")
_WfX25VcNumber_Type = Integer32
_WfX25VcNumber_Object = MibTableColumn
wfX25VcNumber = _WfX25VcNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 6),
    _WfX25VcNumber_Type()
)
wfX25VcNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcNumber.setStatus("mandatory")
_WfX25VcDataTxs_Type = Counter32
_WfX25VcDataTxs_Object = MibTableColumn
wfX25VcDataTxs = _WfX25VcDataTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 7),
    _WfX25VcDataTxs_Type()
)
wfX25VcDataTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcDataTxs.setStatus("mandatory")
_WfX25VcInterruptTxs_Type = Counter32
_WfX25VcInterruptTxs_Object = MibTableColumn
wfX25VcInterruptTxs = _WfX25VcInterruptTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 8),
    _WfX25VcInterruptTxs_Type()
)
wfX25VcInterruptTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcInterruptTxs.setStatus("mandatory")
_WfX25VcResetTxs_Type = Counter32
_WfX25VcResetTxs_Object = MibTableColumn
wfX25VcResetTxs = _WfX25VcResetTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 9),
    _WfX25VcResetTxs_Type()
)
wfX25VcResetTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcResetTxs.setStatus("mandatory")
_WfX25VcRrTxs_Type = Counter32
_WfX25VcRrTxs_Object = MibTableColumn
wfX25VcRrTxs = _WfX25VcRrTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 10),
    _WfX25VcRrTxs_Type()
)
wfX25VcRrTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcRrTxs.setStatus("mandatory")
_WfX25VcRnrTxs_Type = Counter32
_WfX25VcRnrTxs_Object = MibTableColumn
wfX25VcRnrTxs = _WfX25VcRnrTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 11),
    _WfX25VcRnrTxs_Type()
)
wfX25VcRnrTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcRnrTxs.setStatus("mandatory")
_WfX25VcRejectTxs_Type = Counter32
_WfX25VcRejectTxs_Object = MibTableColumn
wfX25VcRejectTxs = _WfX25VcRejectTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 12),
    _WfX25VcRejectTxs_Type()
)
wfX25VcRejectTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcRejectTxs.setStatus("mandatory")
_WfX25VcSegmentTxs_Type = Counter32
_WfX25VcSegmentTxs_Object = MibTableColumn
wfX25VcSegmentTxs = _WfX25VcSegmentTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 13),
    _WfX25VcSegmentTxs_Type()
)
wfX25VcSegmentTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcSegmentTxs.setStatus("mandatory")
_WfX25VcBytesTxs_Type = Counter32
_WfX25VcBytesTxs_Object = MibTableColumn
wfX25VcBytesTxs = _WfX25VcBytesTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 14),
    _WfX25VcBytesTxs_Type()
)
wfX25VcBytesTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcBytesTxs.setStatus("mandatory")
_WfX25VcIntBytesTxs_Type = Counter32
_WfX25VcIntBytesTxs_Object = MibTableColumn
wfX25VcIntBytesTxs = _WfX25VcIntBytesTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 15),
    _WfX25VcIntBytesTxs_Type()
)
wfX25VcIntBytesTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcIntBytesTxs.setStatus("mandatory")
_WfX25VcDataRxs_Type = Counter32
_WfX25VcDataRxs_Object = MibTableColumn
wfX25VcDataRxs = _WfX25VcDataRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 16),
    _WfX25VcDataRxs_Type()
)
wfX25VcDataRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcDataRxs.setStatus("mandatory")
_WfX25VcInterruptRxs_Type = Counter32
_WfX25VcInterruptRxs_Object = MibTableColumn
wfX25VcInterruptRxs = _WfX25VcInterruptRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 17),
    _WfX25VcInterruptRxs_Type()
)
wfX25VcInterruptRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcInterruptRxs.setStatus("mandatory")
_WfX25VcResetRxs_Type = Counter32
_WfX25VcResetRxs_Object = MibTableColumn
wfX25VcResetRxs = _WfX25VcResetRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 18),
    _WfX25VcResetRxs_Type()
)
wfX25VcResetRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcResetRxs.setStatus("mandatory")
_WfX25VcRrRxs_Type = Counter32
_WfX25VcRrRxs_Object = MibTableColumn
wfX25VcRrRxs = _WfX25VcRrRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 19),
    _WfX25VcRrRxs_Type()
)
wfX25VcRrRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcRrRxs.setStatus("mandatory")
_WfX25VcRnrRxs_Type = Counter32
_WfX25VcRnrRxs_Object = MibTableColumn
wfX25VcRnrRxs = _WfX25VcRnrRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 20),
    _WfX25VcRnrRxs_Type()
)
wfX25VcRnrRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcRnrRxs.setStatus("mandatory")
_WfX25VcRejectRxs_Type = Counter32
_WfX25VcRejectRxs_Object = MibTableColumn
wfX25VcRejectRxs = _WfX25VcRejectRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 21),
    _WfX25VcRejectRxs_Type()
)
wfX25VcRejectRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcRejectRxs.setStatus("mandatory")
_WfX25VcSegmentRxs_Type = Counter32
_WfX25VcSegmentRxs_Object = MibTableColumn
wfX25VcSegmentRxs = _WfX25VcSegmentRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 22),
    _WfX25VcSegmentRxs_Type()
)
wfX25VcSegmentRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcSegmentRxs.setStatus("mandatory")
_WfX25VcBytesRxs_Type = Counter32
_WfX25VcBytesRxs_Object = MibTableColumn
wfX25VcBytesRxs = _WfX25VcBytesRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 23),
    _WfX25VcBytesRxs_Type()
)
wfX25VcBytesRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcBytesRxs.setStatus("mandatory")
_WfX25VcIntBytesRxs_Type = Counter32
_WfX25VcIntBytesRxs_Object = MibTableColumn
wfX25VcIntBytesRxs = _WfX25VcIntBytesRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 24),
    _WfX25VcIntBytesRxs_Type()
)
wfX25VcIntBytesRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcIntBytesRxs.setStatus("mandatory")
_WfX25VcApPktsDropped_Type = Counter32
_WfX25VcApPktsDropped_Object = MibTableColumn
wfX25VcApPktsDropped = _WfX25VcApPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 25),
    _WfX25VcApPktsDropped_Type()
)
wfX25VcApPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcApPktsDropped.setStatus("mandatory")
_WfX25VcRemoteX121Addr_Type = DisplayString
_WfX25VcRemoteX121Addr_Object = MibTableColumn
wfX25VcRemoteX121Addr = _WfX25VcRemoteX121Addr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 26),
    _WfX25VcRemoteX121Addr_Type()
)
wfX25VcRemoteX121Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcRemoteX121Addr.setStatus("mandatory")
_WfX25VcBurstQClippedPkts_Type = Counter32
_WfX25VcBurstQClippedPkts_Object = MibTableColumn
wfX25VcBurstQClippedPkts = _WfX25VcBurstQClippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 27),
    _WfX25VcBurstQClippedPkts_Type()
)
wfX25VcBurstQClippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcBurstQClippedPkts.setStatus("mandatory")
_WfX25VcBurstQPktCnt_Type = Counter32
_WfX25VcBurstQPktCnt_Object = MibTableColumn
wfX25VcBurstQPktCnt = _WfX25VcBurstQPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 28),
    _WfX25VcBurstQPktCnt_Type()
)
wfX25VcBurstQPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcBurstQPktCnt.setStatus("mandatory")
_WfX25VcBurstQHighWaterPkts_Type = Gauge32
_WfX25VcBurstQHighWaterPkts_Object = MibTableColumn
wfX25VcBurstQHighWaterPkts = _WfX25VcBurstQHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 29),
    _WfX25VcBurstQHighWaterPkts_Type()
)
wfX25VcBurstQHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcBurstQHighWaterPkts.setStatus("mandatory")
_WfX25VcPktsLargerThanBurstThrCnt_Type = Counter32
_WfX25VcPktsLargerThanBurstThrCnt_Object = MibTableColumn
wfX25VcPktsLargerThanBurstThrCnt = _WfX25VcPktsLargerThanBurstThrCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 30),
    _WfX25VcPktsLargerThanBurstThrCnt_Type()
)
wfX25VcPktsLargerThanBurstThrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcPktsLargerThanBurstThrCnt.setStatus("mandatory")
_WfX25VcPktDrops_Type = Counter32
_WfX25VcPktDrops_Object = MibTableColumn
wfX25VcPktDrops = _WfX25VcPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 31),
    _WfX25VcPktDrops_Type()
)
wfX25VcPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcPktDrops.setStatus("mandatory")
_WfX25VcPlpPktDrops_Type = Counter32
_WfX25VcPlpPktDrops_Object = MibTableColumn
wfX25VcPlpPktDrops = _WfX25VcPlpPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 32),
    _WfX25VcPlpPktDrops_Type()
)
wfX25VcPlpPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcPlpPktDrops.setStatus("mandatory")
_WfX25VcMbsOutstanding_Type = Counter32
_WfX25VcMbsOutstanding_Object = MibTableColumn
wfX25VcMbsOutstanding = _WfX25VcMbsOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 33),
    _WfX25VcMbsOutstanding_Type()
)
wfX25VcMbsOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcMbsOutstanding.setStatus("mandatory")
_WfX25VcMbsOutstandingPostTx_Type = Counter32
_WfX25VcMbsOutstandingPostTx_Object = MibTableColumn
wfX25VcMbsOutstandingPostTx = _WfX25VcMbsOutstandingPostTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 34),
    _WfX25VcMbsOutstandingPostTx_Type()
)
wfX25VcMbsOutstandingPostTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcMbsOutstandingPostTx.setStatus("mandatory")
_WfX25VcMaxTx_Type = Counter32
_WfX25VcMaxTx_Object = MibTableColumn
wfX25VcMaxTx = _WfX25VcMaxTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 35),
    _WfX25VcMaxTx_Type()
)
wfX25VcMaxTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcMaxTx.setStatus("mandatory")
_WfX25VcMbsQueueCnt_Type = Counter32
_WfX25VcMbsQueueCnt_Object = MibTableColumn
wfX25VcMbsQueueCnt = _WfX25VcMbsQueueCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 36),
    _WfX25VcMbsQueueCnt_Type()
)
wfX25VcMbsQueueCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcMbsQueueCnt.setStatus("mandatory")
_WfX25VcMbsQueueCntPostTx_Type = Counter32
_WfX25VcMbsQueueCntPostTx_Object = MibTableColumn
wfX25VcMbsQueueCntPostTx = _WfX25VcMbsQueueCntPostTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 37),
    _WfX25VcMbsQueueCntPostTx_Type()
)
wfX25VcMbsQueueCntPostTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcMbsQueueCntPostTx.setStatus("mandatory")
_WfX25VcTxQueueCnt_Type = Counter32
_WfX25VcTxQueueCnt_Object = MibTableColumn
wfX25VcTxQueueCnt = _WfX25VcTxQueueCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 38),
    _WfX25VcTxQueueCnt_Type()
)
wfX25VcTxQueueCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcTxQueueCnt.setStatus("mandatory")
_WfX25VcTxQueueCntPostTx_Type = Counter32
_WfX25VcTxQueueCntPostTx_Object = MibTableColumn
wfX25VcTxQueueCntPostTx = _WfX25VcTxQueueCntPostTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 4, 1, 39),
    _WfX25VcTxQueueCntPostTx_Type()
)
wfX25VcTxQueueCntPostTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25VcTxQueueCntPostTx.setStatus("mandatory")
_WfLapbPktTable_Object = MibTable
wfLapbPktTable = _WfLapbPktTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5)
)
if mibBuilder.loadTexts:
    wfLapbPktTable.setStatus("mandatory")
_WfLapbPktEntry_Object = MibTableRow
wfLapbPktEntry = _WfLapbPktEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1)
)
wfLapbPktEntry.setIndexNames(
    (0, "Wellfleet-X25-MIB", "wfLapbPktSlotNum"),
    (0, "Wellfleet-X25-MIB", "wfLapbPktConnector"),
    (0, "Wellfleet-X25-MIB", "wfLapbPktLineNumber"),
    (0, "Wellfleet-X25-MIB", "wfLapbPktLLIndex"),
)
if mibBuilder.loadTexts:
    wfLapbPktEntry.setStatus("mandatory")


class _WfLapbPktDelete_Type(Integer32):
    """Custom type wfLapbPktDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfLapbPktDelete_Type.__name__ = "Integer32"
_WfLapbPktDelete_Object = MibTableColumn
wfLapbPktDelete = _WfLapbPktDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 1),
    _WfLapbPktDelete_Type()
)
wfLapbPktDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktDelete.setStatus("mandatory")


class _WfLapbPktDisable_Type(Integer32):
    """Custom type wfLapbPktDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfLapbPktDisable_Type.__name__ = "Integer32"
_WfLapbPktDisable_Object = MibTableColumn
wfLapbPktDisable = _WfLapbPktDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 2),
    _WfLapbPktDisable_Type()
)
wfLapbPktDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktDisable.setStatus("mandatory")
_WfLapbPktSlotNum_Type = Integer32
_WfLapbPktSlotNum_Object = MibTableColumn
wfLapbPktSlotNum = _WfLapbPktSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 3),
    _WfLapbPktSlotNum_Type()
)
wfLapbPktSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktSlotNum.setStatus("mandatory")
_WfLapbPktConnector_Type = Integer32
_WfLapbPktConnector_Object = MibTableColumn
wfLapbPktConnector = _WfLapbPktConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 4),
    _WfLapbPktConnector_Type()
)
wfLapbPktConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktConnector.setStatus("mandatory")
_WfLapbPktLineNumber_Type = Integer32
_WfLapbPktLineNumber_Object = MibTableColumn
wfLapbPktLineNumber = _WfLapbPktLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 5),
    _WfLapbPktLineNumber_Type()
)
wfLapbPktLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktLineNumber.setStatus("mandatory")
_WfLapbPktLLIndex_Type = Integer32
_WfLapbPktLLIndex_Object = MibTableColumn
wfLapbPktLLIndex = _WfLapbPktLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 6),
    _WfLapbPktLLIndex_Type()
)
wfLapbPktLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktLLIndex.setStatus("mandatory")
_WfLapbPktLapbCct_Type = Integer32
_WfLapbPktLapbCct_Object = MibTableColumn
wfLapbPktLapbCct = _WfLapbPktLapbCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 7),
    _WfLapbPktLapbCct_Type()
)
wfLapbPktLapbCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktLapbCct.setStatus("mandatory")
_WfLapbPktLinkId_Type = Integer32
_WfLapbPktLinkId_Object = MibTableColumn
wfLapbPktLinkId = _WfLapbPktLinkId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 8),
    _WfLapbPktLinkId_Type()
)
wfLapbPktLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktLinkId.setStatus("mandatory")


class _WfLapbPktLineState_Type(Integer32):
    """Custom type wfLapbPktLineState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfLapbPktLineState_Type.__name__ = "Integer32"
_WfLapbPktLineState_Object = MibTableColumn
wfLapbPktLineState = _WfLapbPktLineState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 9),
    _WfLapbPktLineState_Type()
)
wfLapbPktLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktLineState.setStatus("mandatory")


class _WfLapbPktSeqSize_Type(Integer32):
    """Custom type wfLapbPktSeqSize based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              128)
        )
    )
    namedValues = NamedValues(
        *(("mod128", 128),
          ("mod8", 8))
    )


_WfLapbPktSeqSize_Type.__name__ = "Integer32"
_WfLapbPktSeqSize_Object = MibTableColumn
wfLapbPktSeqSize = _WfLapbPktSeqSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 10),
    _WfLapbPktSeqSize_Type()
)
wfLapbPktSeqSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktSeqSize.setStatus("mandatory")


class _WfLapbPktMaxWindow_Type(Integer32):
    """Custom type wfLapbPktMaxWindow based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WfLapbPktMaxWindow_Type.__name__ = "Integer32"
_WfLapbPktMaxWindow_Object = MibTableColumn
wfLapbPktMaxWindow = _WfLapbPktMaxWindow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 11),
    _WfLapbPktMaxWindow_Type()
)
wfLapbPktMaxWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktMaxWindow.setStatus("mandatory")


class _WfLapbPktMaxLength_Type(Integer32):
    """Custom type wfLapbPktMaxLength based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("size1024", 10),
          ("size128", 7),
          ("size16", 4),
          ("size2048", 11),
          ("size256", 8),
          ("size32", 5),
          ("size4096", 12),
          ("size512", 9),
          ("size64", 6))
    )


_WfLapbPktMaxLength_Type.__name__ = "Integer32"
_WfLapbPktMaxLength_Object = MibTableColumn
wfLapbPktMaxLength = _WfLapbPktMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 12),
    _WfLapbPktMaxLength_Type()
)
wfLapbPktMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktMaxLength.setStatus("mandatory")


class _WfLapbPktMaxThroughput_Type(Integer32):
    """Custom type wfLapbPktMaxThroughput based on Integer32"""
    defaultValue = 11

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("thrclass1200", 7),
          ("thrclass150", 4),
          ("thrclass19200", 11),
          ("thrclass2400", 8),
          ("thrclass300", 5),
          ("thrclass4800", 9),
          ("thrclass48k", 12),
          ("thrclass600", 6),
          ("thrclass64k", 13),
          ("thrclass75", 3),
          ("thrclass9600", 10))
    )


_WfLapbPktMaxThroughput_Type.__name__ = "Integer32"
_WfLapbPktMaxThroughput_Object = MibTableColumn
wfLapbPktMaxThroughput = _WfLapbPktMaxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 13),
    _WfLapbPktMaxThroughput_Type()
)
wfLapbPktMaxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktMaxThroughput.setStatus("mandatory")


class _WfLapbPktFlowCtl_Type(Integer32):
    """Custom type wfLapbPktFlowCtl based on Integer32"""
    defaultValue = 2

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


_WfLapbPktFlowCtl_Type.__name__ = "Integer32"
_WfLapbPktFlowCtl_Object = MibTableColumn
wfLapbPktFlowCtl = _WfLapbPktFlowCtl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 14),
    _WfLapbPktFlowCtl_Type()
)
wfLapbPktFlowCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktFlowCtl.setStatus("mandatory")


class _WfLapbPktThroughput_Type(Integer32):
    """Custom type wfLapbPktThroughput based on Integer32"""
    defaultValue = 2

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


_WfLapbPktThroughput_Type.__name__ = "Integer32"
_WfLapbPktThroughput_Object = MibTableColumn
wfLapbPktThroughput = _WfLapbPktThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 15),
    _WfLapbPktThroughput_Type()
)
wfLapbPktThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktThroughput.setStatus("mandatory")


class _WfLapbPktUserIdentity_Type(Integer32):
    """Custom type wfLapbPktUserIdentity based on Integer32"""
    defaultValue = 2

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


_WfLapbPktUserIdentity_Type.__name__ = "Integer32"
_WfLapbPktUserIdentity_Object = MibTableColumn
wfLapbPktUserIdentity = _WfLapbPktUserIdentity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 16),
    _WfLapbPktUserIdentity_Type()
)
wfLapbPktUserIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktUserIdentity.setStatus("mandatory")


class _WfLapbPktInCalls_Type(Integer32):
    """Custom type wfLapbPktInCalls based on Integer32"""
    defaultValue = 1

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


_WfLapbPktInCalls_Type.__name__ = "Integer32"
_WfLapbPktInCalls_Object = MibTableColumn
wfLapbPktInCalls = _WfLapbPktInCalls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 17),
    _WfLapbPktInCalls_Type()
)
wfLapbPktInCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktInCalls.setStatus("mandatory")


class _WfLapbPktOutCalls_Type(Integer32):
    """Custom type wfLapbPktOutCalls based on Integer32"""
    defaultValue = 1

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


_WfLapbPktOutCalls_Type.__name__ = "Integer32"
_WfLapbPktOutCalls_Object = MibTableColumn
wfLapbPktOutCalls = _WfLapbPktOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 18),
    _WfLapbPktOutCalls_Type()
)
wfLapbPktOutCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktOutCalls.setStatus("mandatory")


class _WfLapbPktFastAccept_Type(Integer32):
    """Custom type wfLapbPktFastAccept based on Integer32"""
    defaultValue = 2

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


_WfLapbPktFastAccept_Type.__name__ = "Integer32"
_WfLapbPktFastAccept_Object = MibTableColumn
wfLapbPktFastAccept = _WfLapbPktFastAccept_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 19),
    _WfLapbPktFastAccept_Type()
)
wfLapbPktFastAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktFastAccept.setStatus("mandatory")


class _WfLapbPktReverseAccept_Type(Integer32):
    """Custom type wfLapbPktReverseAccept based on Integer32"""
    defaultValue = 2

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


_WfLapbPktReverseAccept_Type.__name__ = "Integer32"
_WfLapbPktReverseAccept_Object = MibTableColumn
wfLapbPktReverseAccept = _WfLapbPktReverseAccept_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 20),
    _WfLapbPktReverseAccept_Type()
)
wfLapbPktReverseAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktReverseAccept.setStatus("mandatory")


class _WfLapbPktFastSelect_Type(Integer32):
    """Custom type wfLapbPktFastSelect based on Integer32"""
    defaultValue = 2

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


_WfLapbPktFastSelect_Type.__name__ = "Integer32"
_WfLapbPktFastSelect_Object = MibTableColumn
wfLapbPktFastSelect = _WfLapbPktFastSelect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 21),
    _WfLapbPktFastSelect_Type()
)
wfLapbPktFastSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktFastSelect.setStatus("mandatory")


class _WfLapbPktReverseCharging_Type(Integer32):
    """Custom type wfLapbPktReverseCharging based on Integer32"""
    defaultValue = 2

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


_WfLapbPktReverseCharging_Type.__name__ = "Integer32"
_WfLapbPktReverseCharging_Object = MibTableColumn
wfLapbPktReverseCharging = _WfLapbPktReverseCharging_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 22),
    _WfLapbPktReverseCharging_Type()
)
wfLapbPktReverseCharging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktReverseCharging.setStatus("mandatory")


class _WfLapbPktCugSelection_Type(Integer32):
    """Custom type wfLapbPktCugSelection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("basic", 16),
          ("extended", 32),
          ("off", 2))
    )


_WfLapbPktCugSelection_Type.__name__ = "Integer32"
_WfLapbPktCugSelection_Object = MibTableColumn
wfLapbPktCugSelection = _WfLapbPktCugSelection_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 23),
    _WfLapbPktCugSelection_Type()
)
wfLapbPktCugSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktCugSelection.setStatus("mandatory")


class _WfLapbPktCugOA_Type(Integer32):
    """Custom type wfLapbPktCugOA based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              64)
        )
    )
    namedValues = NamedValues(
        *(("cugoa", 64),
          ("off", 2))
    )


_WfLapbPktCugOA_Type.__name__ = "Integer32"
_WfLapbPktCugOA_Object = MibTableColumn
wfLapbPktCugOA = _WfLapbPktCugOA_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 24),
    _WfLapbPktCugOA_Type()
)
wfLapbPktCugOA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktCugOA.setStatus("mandatory")


class _WfLapbPktCugBilateral_Type(Integer32):
    """Custom type wfLapbPktCugBilateral based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              128)
        )
    )
    namedValues = NamedValues(
        *(("bilat", 128),
          ("off", 2))
    )


_WfLapbPktCugBilateral_Type.__name__ = "Integer32"
_WfLapbPktCugBilateral_Object = MibTableColumn
wfLapbPktCugBilateral = _WfLapbPktCugBilateral_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 25),
    _WfLapbPktCugBilateral_Type()
)
wfLapbPktCugBilateral.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktCugBilateral.setStatus("mandatory")


class _WfLapbPktRpoaSelection_Type(Integer32):
    """Custom type wfLapbPktRpoaSelection based on Integer32"""
    defaultValue = 2

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


_WfLapbPktRpoaSelection_Type.__name__ = "Integer32"
_WfLapbPktRpoaSelection_Object = MibTableColumn
wfLapbPktRpoaSelection = _WfLapbPktRpoaSelection_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 26),
    _WfLapbPktRpoaSelection_Type()
)
wfLapbPktRpoaSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktRpoaSelection.setStatus("mandatory")


class _WfLapbPktChargeInform_Type(Integer32):
    """Custom type wfLapbPktChargeInform based on Integer32"""
    defaultValue = 2

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


_WfLapbPktChargeInform_Type.__name__ = "Integer32"
_WfLapbPktChargeInform_Object = MibTableColumn
wfLapbPktChargeInform = _WfLapbPktChargeInform_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 27),
    _WfLapbPktChargeInform_Type()
)
wfLapbPktChargeInform.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktChargeInform.setStatus("mandatory")


class _WfLapbPktTransitDelay_Type(Integer32):
    """Custom type wfLapbPktTransitDelay based on Integer32"""
    defaultValue = 2

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


_WfLapbPktTransitDelay_Type.__name__ = "Integer32"
_WfLapbPktTransitDelay_Object = MibTableColumn
wfLapbPktTransitDelay = _WfLapbPktTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 28),
    _WfLapbPktTransitDelay_Type()
)
wfLapbPktTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktTransitDelay.setStatus("mandatory")


class _WfLapbPktFullAddressing_Type(Integer32):
    """Custom type wfLapbPktFullAddressing based on Integer32"""
    defaultValue = 1

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


_WfLapbPktFullAddressing_Type.__name__ = "Integer32"
_WfLapbPktFullAddressing_Object = MibTableColumn
wfLapbPktFullAddressing = _WfLapbPktFullAddressing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 29),
    _WfLapbPktFullAddressing_Type()
)
wfLapbPktFullAddressing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktFullAddressing.setStatus("mandatory")


class _WfLapbPktAccFormat_Type(Integer32):
    """Custom type wfLapbPktAccFormat based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              103,
              255)
        )
    )
    namedValues = NamedValues(
        *(("allext", 255),
          ("basic", 2),
          ("defbas", 103))
    )


_WfLapbPktAccFormat_Type.__name__ = "Integer32"
_WfLapbPktAccFormat_Object = MibTableColumn
wfLapbPktAccFormat = _WfLapbPktAccFormat_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 30),
    _WfLapbPktAccFormat_Type()
)
wfLapbPktAccFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktAccFormat.setStatus("mandatory")


class _WfLapbPktRelFormat_Type(Integer32):
    """Custom type wfLapbPktRelFormat based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              103,
              255)
        )
    )
    namedValues = NamedValues(
        *(("allext", 255),
          ("basic", 2),
          ("defext", 103))
    )


_WfLapbPktRelFormat_Type.__name__ = "Integer32"
_WfLapbPktRelFormat_Object = MibTableColumn
wfLapbPktRelFormat = _WfLapbPktRelFormat_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 31),
    _WfLapbPktRelFormat_Type()
)
wfLapbPktRelFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktRelFormat.setStatus("mandatory")


class _WfLapbPktT1_Type(Integer32):
    """Custom type wfLapbPktT1 based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_WfLapbPktT1_Type.__name__ = "Integer32"
_WfLapbPktT1_Object = MibTableColumn
wfLapbPktT1 = _WfLapbPktT1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 32),
    _WfLapbPktT1_Type()
)
wfLapbPktT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktT1.setStatus("mandatory")


class _WfLapbPktT2_Type(Integer32):
    """Custom type wfLapbPktT2 based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_WfLapbPktT2_Type.__name__ = "Integer32"
_WfLapbPktT2_Object = MibTableColumn
wfLapbPktT2 = _WfLapbPktT2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 33),
    _WfLapbPktT2_Type()
)
wfLapbPktT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktT2.setStatus("mandatory")


class _WfLapbPktT3_Type(Integer32):
    """Custom type wfLapbPktT3 based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 2000),
    )


_WfLapbPktT3_Type.__name__ = "Integer32"
_WfLapbPktT3_Object = MibTableColumn
wfLapbPktT3 = _WfLapbPktT3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 34),
    _WfLapbPktT3_Type()
)
wfLapbPktT3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktT3.setStatus("mandatory")


class _WfLapbPktT4_Type(Integer32):
    """Custom type wfLapbPktT4 based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 2000),
    )


_WfLapbPktT4_Type.__name__ = "Integer32"
_WfLapbPktT4_Object = MibTableColumn
wfLapbPktT4 = _WfLapbPktT4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 35),
    _WfLapbPktT4_Type()
)
wfLapbPktT4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktT4.setStatus("mandatory")


class _WfLapbPktIwcCnt_Type(Integer32):
    """Custom type wfLapbPktIwcCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_WfLapbPktIwcCnt_Type.__name__ = "Integer32"
_WfLapbPktIwcCnt_Object = MibTableColumn
wfLapbPktIwcCnt = _WfLapbPktIwcCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 36),
    _WfLapbPktIwcCnt_Type()
)
wfLapbPktIwcCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktIwcCnt.setStatus("mandatory")


class _WfLapbPktIwcId_Type(Integer32):
    """Custom type wfLapbPktIwcId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WfLapbPktIwcId_Type.__name__ = "Integer32"
_WfLapbPktIwcId_Object = MibTableColumn
wfLapbPktIwcId = _WfLapbPktIwcId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 37),
    _WfLapbPktIwcId_Type()
)
wfLapbPktIwcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktIwcId.setStatus("mandatory")


class _WfLapbPktBwcCnt_Type(Integer32):
    """Custom type wfLapbPktBwcCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_WfLapbPktBwcCnt_Type.__name__ = "Integer32"
_WfLapbPktBwcCnt_Object = MibTableColumn
wfLapbPktBwcCnt = _WfLapbPktBwcCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 38),
    _WfLapbPktBwcCnt_Type()
)
wfLapbPktBwcCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktBwcCnt.setStatus("mandatory")


class _WfLapbPktBwcId_Type(Integer32):
    """Custom type wfLapbPktBwcId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WfLapbPktBwcId_Type.__name__ = "Integer32"
_WfLapbPktBwcId_Object = MibTableColumn
wfLapbPktBwcId = _WfLapbPktBwcId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 39),
    _WfLapbPktBwcId_Type()
)
wfLapbPktBwcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktBwcId.setStatus("mandatory")


class _WfLapbPktOwcCnt_Type(Integer32):
    """Custom type wfLapbPktOwcCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_WfLapbPktOwcCnt_Type.__name__ = "Integer32"
_WfLapbPktOwcCnt_Object = MibTableColumn
wfLapbPktOwcCnt = _WfLapbPktOwcCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 40),
    _WfLapbPktOwcCnt_Type()
)
wfLapbPktOwcCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktOwcCnt.setStatus("mandatory")


class _WfLapbPktOwcId_Type(Integer32):
    """Custom type wfLapbPktOwcId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WfLapbPktOwcId_Type.__name__ = "Integer32"
_WfLapbPktOwcId_Object = MibTableColumn
wfLapbPktOwcId = _WfLapbPktOwcId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 41),
    _WfLapbPktOwcId_Type()
)
wfLapbPktOwcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktOwcId.setStatus("mandatory")


class _WfLapbPktDefWindow_Type(Integer32):
    """Custom type wfLapbPktDefWindow based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WfLapbPktDefWindow_Type.__name__ = "Integer32"
_WfLapbPktDefWindow_Object = MibTableColumn
wfLapbPktDefWindow = _WfLapbPktDefWindow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 42),
    _WfLapbPktDefWindow_Type()
)
wfLapbPktDefWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktDefWindow.setStatus("mandatory")


class _WfLapbPktDefLength_Type(Integer32):
    """Custom type wfLapbPktDefLength based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("size1024", 10),
          ("size128", 7),
          ("size16", 4),
          ("size2048", 11),
          ("size256", 8),
          ("size32", 5),
          ("size4096", 12),
          ("size512", 9),
          ("size64", 6))
    )


_WfLapbPktDefLength_Type.__name__ = "Integer32"
_WfLapbPktDefLength_Object = MibTableColumn
wfLapbPktDefLength = _WfLapbPktDefLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 43),
    _WfLapbPktDefLength_Type()
)
wfLapbPktDefLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktDefLength.setStatus("mandatory")


class _WfLapbPktDefClass_Type(Integer32):
    """Custom type wfLapbPktDefClass based on Integer32"""
    defaultValue = 11

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 13),
    )


_WfLapbPktDefClass_Type.__name__ = "Integer32"
_WfLapbPktDefClass_Object = MibTableColumn
wfLapbPktDefClass = _WfLapbPktDefClass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 44),
    _WfLapbPktDefClass_Type()
)
wfLapbPktDefClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktDefClass.setStatus("mandatory")


class _WfLapbPktDxe_Type(Integer32):
    """Custom type wfLapbPktDxe based on Integer32"""
    defaultValue = 1

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
        *(("x25dce", 3),
          ("x25dte", 2),
          ("x25dtedxe", 4),
          ("x25dtersta", 1))
    )


_WfLapbPktDxe_Type.__name__ = "Integer32"
_WfLapbPktDxe_Object = MibTableColumn
wfLapbPktDxe = _WfLapbPktDxe_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 45),
    _WfLapbPktDxe_Type()
)
wfLapbPktDxe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktDxe.setStatus("mandatory")


class _WfLapbPktConformance_Type(Integer32):
    """Custom type wfLapbPktConformance based on Integer32"""
    defaultValue = 1025

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(257,
              258,
              513,
              514,
              1025,
              1026)
        )
    )
    namedValues = NamedValues(
        *(("dxe1980", 257),
          ("dxe1984", 513),
          ("dxe1988", 1025),
          ("fsel1980", 258),
          ("fsel1984", 514),
          ("fsel1988", 1026))
    )


_WfLapbPktConformance_Type.__name__ = "Integer32"
_WfLapbPktConformance_Object = MibTableColumn
wfLapbPktConformance = _WfLapbPktConformance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 46),
    _WfLapbPktConformance_Type()
)
wfLapbPktConformance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktConformance.setStatus("mandatory")


class _WfLapbPktStandard_Type(Integer32):
    """Custom type wfLapbPktStandard based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("stddod", 32),
          ("stdiso", 16),
          ("stdnone", 1))
    )


_WfLapbPktStandard_Type.__name__ = "Integer32"
_WfLapbPktStandard_Object = MibTableColumn
wfLapbPktStandard = _WfLapbPktStandard_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 47),
    _WfLapbPktStandard_Type()
)
wfLapbPktStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktStandard.setStatus("mandatory")
_WfLapbPktNetaddr_Type = DisplayString
_WfLapbPktNetaddr_Object = MibTableColumn
wfLapbPktNetaddr = _WfLapbPktNetaddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 48),
    _WfLapbPktNetaddr_Type()
)
wfLapbPktNetaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktNetaddr.setStatus("mandatory")


class _WfLapbPktStatistics_Type(Integer32):
    """Custom type wfLapbPktStatistics based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("statsoff", 2),
          ("statson", 1))
    )


_WfLapbPktStatistics_Type.__name__ = "Integer32"
_WfLapbPktStatistics_Object = MibTableColumn
wfLapbPktStatistics = _WfLapbPktStatistics_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 49),
    _WfLapbPktStatistics_Type()
)
wfLapbPktStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktStatistics.setStatus("mandatory")


class _WfLapbPktNetaddrType_Type(Integer32):
    """Custom type wfLapbPktNetaddrType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bfetype", 3),
          ("ddntype", 2),
          ("pdntype", 1))
    )


_WfLapbPktNetaddrType_Type.__name__ = "Integer32"
_WfLapbPktNetaddrType_Object = MibTableColumn
wfLapbPktNetaddrType = _WfLapbPktNetaddrType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 50),
    _WfLapbPktNetaddrType_Type()
)
wfLapbPktNetaddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktNetaddrType.setStatus("mandatory")
_WfLapbPktDDNIpAddr_Type = IpAddress
_WfLapbPktDDNIpAddr_Object = MibTableColumn
wfLapbPktDDNIpAddr = _WfLapbPktDDNIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 51),
    _WfLapbPktDDNIpAddr_Type()
)
wfLapbPktDDNIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktDDNIpAddr.setStatus("mandatory")
_WfLapbPktPDNX121Addr_Type = DisplayString
_WfLapbPktPDNX121Addr_Object = MibTableColumn
wfLapbPktPDNX121Addr = _WfLapbPktPDNX121Addr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 52),
    _WfLapbPktPDNX121Addr_Type()
)
wfLapbPktPDNX121Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktPDNX121Addr.setStatus("mandatory")


class _WfLapbPktTxT5_Type(Integer32):
    """Custom type wfLapbPktTxT5 based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8000),
    )


_WfLapbPktTxT5_Type.__name__ = "Integer32"
_WfLapbPktTxT5_Object = MibTableColumn
wfLapbPktTxT5 = _WfLapbPktTxT5_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 53),
    _WfLapbPktTxT5_Type()
)
wfLapbPktTxT5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktTxT5.setStatus("mandatory")


class _WfLapbPktUseDfltService_Type(Integer32):
    """Custom type wfLapbPktUseDfltService based on Integer32"""
    defaultValue = 2

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


_WfLapbPktUseDfltService_Type.__name__ = "Integer32"
_WfLapbPktUseDfltService_Object = MibTableColumn
wfLapbPktUseDfltService = _WfLapbPktUseDfltService_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 54),
    _WfLapbPktUseDfltService_Type()
)
wfLapbPktUseDfltService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktUseDfltService.setStatus("mandatory")


class _WfLapbPktPVCCnt_Type(Integer32):
    """Custom type wfLapbPktPVCCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_WfLapbPktPVCCnt_Type.__name__ = "Integer32"
_WfLapbPktPVCCnt_Object = MibTableColumn
wfLapbPktPVCCnt = _WfLapbPktPVCCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 55),
    _WfLapbPktPVCCnt_Type()
)
wfLapbPktPVCCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktPVCCnt.setStatus("mandatory")


class _WfLapbPktPVCLowLcn_Type(Integer32):
    """Custom type wfLapbPktPVCLowLcn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WfLapbPktPVCLowLcn_Type.__name__ = "Integer32"
_WfLapbPktPVCLowLcn_Object = MibTableColumn
wfLapbPktPVCLowLcn = _WfLapbPktPVCLowLcn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 56),
    _WfLapbPktPVCLowLcn_Type()
)
wfLapbPktPVCLowLcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktPVCLowLcn.setStatus("mandatory")


class _WfLapbPktClientTimer_Type(Integer32):
    """Custom type wfLapbPktClientTimer based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_WfLapbPktClientTimer_Type.__name__ = "Integer32"
_WfLapbPktClientTimer_Object = MibTableColumn
wfLapbPktClientTimer = _WfLapbPktClientTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 57),
    _WfLapbPktClientTimer_Type()
)
wfLapbPktClientTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktClientTimer.setStatus("mandatory")


class _WfLapbPktPduSize_Type(Integer32):
    """Custom type wfLapbPktPduSize based on Integer32"""
    defaultValue = 1600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1600, 4096),
    )


_WfLapbPktPduSize_Type.__name__ = "Integer32"
_WfLapbPktPduSize_Object = MibTableColumn
wfLapbPktPduSize = _WfLapbPktPduSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 58),
    _WfLapbPktPduSize_Type()
)
wfLapbPktPduSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktPduSize.setStatus("mandatory")


class _WfLapbPktTranspacCauseCodeEnable_Type(Integer32):
    """Custom type wfLapbPktTranspacCauseCodeEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfLapbPktTranspacCauseCodeEnable_Type.__name__ = "Integer32"
_WfLapbPktTranspacCauseCodeEnable_Object = MibTableColumn
wfLapbPktTranspacCauseCodeEnable = _WfLapbPktTranspacCauseCodeEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 59),
    _WfLapbPktTranspacCauseCodeEnable_Type()
)
wfLapbPktTranspacCauseCodeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktTranspacCauseCodeEnable.setStatus("mandatory")


class _WfLapbPktTxMbsQueueThreshold_Type(Integer32):
    """Custom type wfLapbPktTxMbsQueueThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_WfLapbPktTxMbsQueueThreshold_Type.__name__ = "Integer32"
_WfLapbPktTxMbsQueueThreshold_Object = MibTableColumn
wfLapbPktTxMbsQueueThreshold = _WfLapbPktTxMbsQueueThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 60),
    _WfLapbPktTxMbsQueueThreshold_Type()
)
wfLapbPktTxMbsQueueThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktTxMbsQueueThreshold.setStatus("mandatory")


class _WfLapbPktBackupDebugLvl_Type(Integer32):
    """Custom type wfLapbPktBackupDebugLvl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("debug", 4),
          ("one", 1))
    )


_WfLapbPktBackupDebugLvl_Type.__name__ = "Integer32"
_WfLapbPktBackupDebugLvl_Object = MibTableColumn
wfLapbPktBackupDebugLvl = _WfLapbPktBackupDebugLvl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 61),
    _WfLapbPktBackupDebugLvl_Type()
)
wfLapbPktBackupDebugLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktBackupDebugLvl.setStatus("mandatory")


class _WfLapbPktBackupEnable_Type(Integer32):
    """Custom type wfLapbPktBackupEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfLapbPktBackupEnable_Type.__name__ = "Integer32"
_WfLapbPktBackupEnable_Object = MibTableColumn
wfLapbPktBackupEnable = _WfLapbPktBackupEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 5, 1, 62),
    _WfLapbPktBackupEnable_Type()
)
wfLapbPktBackupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbPktBackupEnable.setStatus("mandatory")
_WfLapbPktStatsTable_Object = MibTable
wfLapbPktStatsTable = _WfLapbPktStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6)
)
if mibBuilder.loadTexts:
    wfLapbPktStatsTable.setStatus("mandatory")
_WfLapbPktStatsEntry_Object = MibTableRow
wfLapbPktStatsEntry = _WfLapbPktStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1)
)
wfLapbPktStatsEntry.setIndexNames(
    (0, "Wellfleet-X25-MIB", "wfLapbPktStatsSlotNum"),
    (0, "Wellfleet-X25-MIB", "wfLapbPktStatsConnector"),
    (0, "Wellfleet-X25-MIB", "wfLapbPktStatsLineNumber"),
    (0, "Wellfleet-X25-MIB", "wfLapbPktStatsLLIndex"),
)
if mibBuilder.loadTexts:
    wfLapbPktStatsEntry.setStatus("mandatory")
_WfLapbPktStatsSlotNum_Type = Integer32
_WfLapbPktStatsSlotNum_Object = MibTableColumn
wfLapbPktStatsSlotNum = _WfLapbPktStatsSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 1),
    _WfLapbPktStatsSlotNum_Type()
)
wfLapbPktStatsSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsSlotNum.setStatus("mandatory")
_WfLapbPktStatsConnector_Type = Integer32
_WfLapbPktStatsConnector_Object = MibTableColumn
wfLapbPktStatsConnector = _WfLapbPktStatsConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 2),
    _WfLapbPktStatsConnector_Type()
)
wfLapbPktStatsConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsConnector.setStatus("mandatory")
_WfLapbPktStatsLineNumber_Type = Integer32
_WfLapbPktStatsLineNumber_Object = MibTableColumn
wfLapbPktStatsLineNumber = _WfLapbPktStatsLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 3),
    _WfLapbPktStatsLineNumber_Type()
)
wfLapbPktStatsLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsLineNumber.setStatus("mandatory")
_WfLapbPktStatsLLIndex_Type = Integer32
_WfLapbPktStatsLLIndex_Object = MibTableColumn
wfLapbPktStatsLLIndex = _WfLapbPktStatsLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 4),
    _WfLapbPktStatsLLIndex_Type()
)
wfLapbPktStatsLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsLLIndex.setStatus("mandatory")
_WfLapbPktStatsCct_Type = Integer32
_WfLapbPktStatsCct_Object = MibTableColumn
wfLapbPktStatsCct = _WfLapbPktStatsCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 5),
    _WfLapbPktStatsCct_Type()
)
wfLapbPktStatsCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsCct.setStatus("mandatory")
_WfLapbPktStatsLineAddress_Type = DisplayString
_WfLapbPktStatsLineAddress_Object = MibTableColumn
wfLapbPktStatsLineAddress = _WfLapbPktStatsLineAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 6),
    _WfLapbPktStatsLineAddress_Type()
)
wfLapbPktStatsLineAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsLineAddress.setStatus("mandatory")
_WfLapbPktStatsMaxVcs_Type = Counter32
_WfLapbPktStatsMaxVcs_Object = MibTableColumn
wfLapbPktStatsMaxVcs = _WfLapbPktStatsMaxVcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 7),
    _WfLapbPktStatsMaxVcs_Type()
)
wfLapbPktStatsMaxVcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsMaxVcs.setStatus("mandatory")
_WfLapbPktStatsActiveVcs_Type = Counter32
_WfLapbPktStatsActiveVcs_Object = MibTableColumn
wfLapbPktStatsActiveVcs = _WfLapbPktStatsActiveVcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 8),
    _WfLapbPktStatsActiveVcs_Type()
)
wfLapbPktStatsActiveVcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsActiveVcs.setStatus("mandatory")
_WfLapbPktStatsActiveMax_Type = Counter32
_WfLapbPktStatsActiveMax_Object = MibTableColumn
wfLapbPktStatsActiveMax = _WfLapbPktStatsActiveMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 9),
    _WfLapbPktStatsActiveMax_Type()
)
wfLapbPktStatsActiveMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsActiveMax.setStatus("mandatory")
_WfLapbPktStatsTotalConnections_Type = Counter32
_WfLapbPktStatsTotalConnections_Object = MibTableColumn
wfLapbPktStatsTotalConnections = _WfLapbPktStatsTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 10),
    _WfLapbPktStatsTotalConnections_Type()
)
wfLapbPktStatsTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsTotalConnections.setStatus("mandatory")
_WfLapbPktStatsFailedConnections_Type = Counter32
_WfLapbPktStatsFailedConnections_Object = MibTableColumn
wfLapbPktStatsFailedConnections = _WfLapbPktStatsFailedConnections_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 11),
    _WfLapbPktStatsFailedConnections_Type()
)
wfLapbPktStatsFailedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsFailedConnections.setStatus("mandatory")
_WfLapbPktStatsNormalDisconnects_Type = Counter32
_WfLapbPktStatsNormalDisconnects_Object = MibTableColumn
wfLapbPktStatsNormalDisconnects = _WfLapbPktStatsNormalDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 12),
    _WfLapbPktStatsNormalDisconnects_Type()
)
wfLapbPktStatsNormalDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsNormalDisconnects.setStatus("mandatory")
_WfLapbPktStatsAbnormalDisconnects_Type = Counter32
_WfLapbPktStatsAbnormalDisconnects_Object = MibTableColumn
wfLapbPktStatsAbnormalDisconnects = _WfLapbPktStatsAbnormalDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 13),
    _WfLapbPktStatsAbnormalDisconnects_Type()
)
wfLapbPktStatsAbnormalDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsAbnormalDisconnects.setStatus("mandatory")
_WfLapbPktStatsDataTxs_Type = Counter32
_WfLapbPktStatsDataTxs_Object = MibTableColumn
wfLapbPktStatsDataTxs = _WfLapbPktStatsDataTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 14),
    _WfLapbPktStatsDataTxs_Type()
)
wfLapbPktStatsDataTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsDataTxs.setStatus("mandatory")
_WfLapbPktStatsInterruptTxs_Type = Counter32
_WfLapbPktStatsInterruptTxs_Object = MibTableColumn
wfLapbPktStatsInterruptTxs = _WfLapbPktStatsInterruptTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 15),
    _WfLapbPktStatsInterruptTxs_Type()
)
wfLapbPktStatsInterruptTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsInterruptTxs.setStatus("mandatory")
_WfLapbPktStatsResetTxs_Type = Counter32
_WfLapbPktStatsResetTxs_Object = MibTableColumn
wfLapbPktStatsResetTxs = _WfLapbPktStatsResetTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 16),
    _WfLapbPktStatsResetTxs_Type()
)
wfLapbPktStatsResetTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsResetTxs.setStatus("mandatory")
_WfLapbPktStatsRrTxs_Type = Counter32
_WfLapbPktStatsRrTxs_Object = MibTableColumn
wfLapbPktStatsRrTxs = _WfLapbPktStatsRrTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 17),
    _WfLapbPktStatsRrTxs_Type()
)
wfLapbPktStatsRrTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsRrTxs.setStatus("mandatory")
_WfLapbPktStatsRnrTxs_Type = Counter32
_WfLapbPktStatsRnrTxs_Object = MibTableColumn
wfLapbPktStatsRnrTxs = _WfLapbPktStatsRnrTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 18),
    _WfLapbPktStatsRnrTxs_Type()
)
wfLapbPktStatsRnrTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsRnrTxs.setStatus("mandatory")
_WfLapbPktStatsRejectTxs_Type = Counter32
_WfLapbPktStatsRejectTxs_Object = MibTableColumn
wfLapbPktStatsRejectTxs = _WfLapbPktStatsRejectTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 19),
    _WfLapbPktStatsRejectTxs_Type()
)
wfLapbPktStatsRejectTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsRejectTxs.setStatus("mandatory")
_WfLapbPktStatsRestartTxs_Type = Counter32
_WfLapbPktStatsRestartTxs_Object = MibTableColumn
wfLapbPktStatsRestartTxs = _WfLapbPktStatsRestartTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 20),
    _WfLapbPktStatsRestartTxs_Type()
)
wfLapbPktStatsRestartTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsRestartTxs.setStatus("mandatory")
_WfLapbPktStatsDiagTxs_Type = Counter32
_WfLapbPktStatsDiagTxs_Object = MibTableColumn
wfLapbPktStatsDiagTxs = _WfLapbPktStatsDiagTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 21),
    _WfLapbPktStatsDiagTxs_Type()
)
wfLapbPktStatsDiagTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsDiagTxs.setStatus("mandatory")
_WfLapbPktStatsSegmentTxs_Type = Counter32
_WfLapbPktStatsSegmentTxs_Object = MibTableColumn
wfLapbPktStatsSegmentTxs = _WfLapbPktStatsSegmentTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 22),
    _WfLapbPktStatsSegmentTxs_Type()
)
wfLapbPktStatsSegmentTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsSegmentTxs.setStatus("mandatory")
_WfLapbPktStatsBytesTxs_Type = Counter32
_WfLapbPktStatsBytesTxs_Object = MibTableColumn
wfLapbPktStatsBytesTxs = _WfLapbPktStatsBytesTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 23),
    _WfLapbPktStatsBytesTxs_Type()
)
wfLapbPktStatsBytesTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsBytesTxs.setStatus("mandatory")
_WfLapbPktStatsIntBytesTxs_Type = Counter32
_WfLapbPktStatsIntBytesTxs_Object = MibTableColumn
wfLapbPktStatsIntBytesTxs = _WfLapbPktStatsIntBytesTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 24),
    _WfLapbPktStatsIntBytesTxs_Type()
)
wfLapbPktStatsIntBytesTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsIntBytesTxs.setStatus("mandatory")
_WfLapbPktStatsDataRxs_Type = Counter32
_WfLapbPktStatsDataRxs_Object = MibTableColumn
wfLapbPktStatsDataRxs = _WfLapbPktStatsDataRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 25),
    _WfLapbPktStatsDataRxs_Type()
)
wfLapbPktStatsDataRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsDataRxs.setStatus("mandatory")
_WfLapbPktStatsInterruptRxs_Type = Counter32
_WfLapbPktStatsInterruptRxs_Object = MibTableColumn
wfLapbPktStatsInterruptRxs = _WfLapbPktStatsInterruptRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 26),
    _WfLapbPktStatsInterruptRxs_Type()
)
wfLapbPktStatsInterruptRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsInterruptRxs.setStatus("mandatory")
_WfLapbPktStatsResetRxs_Type = Counter32
_WfLapbPktStatsResetRxs_Object = MibTableColumn
wfLapbPktStatsResetRxs = _WfLapbPktStatsResetRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 27),
    _WfLapbPktStatsResetRxs_Type()
)
wfLapbPktStatsResetRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsResetRxs.setStatus("mandatory")
_WfLapbPktStatsRrRxs_Type = Counter32
_WfLapbPktStatsRrRxs_Object = MibTableColumn
wfLapbPktStatsRrRxs = _WfLapbPktStatsRrRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 28),
    _WfLapbPktStatsRrRxs_Type()
)
wfLapbPktStatsRrRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsRrRxs.setStatus("mandatory")
_WfLapbPktStatsRnrRxs_Type = Counter32
_WfLapbPktStatsRnrRxs_Object = MibTableColumn
wfLapbPktStatsRnrRxs = _WfLapbPktStatsRnrRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 29),
    _WfLapbPktStatsRnrRxs_Type()
)
wfLapbPktStatsRnrRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsRnrRxs.setStatus("mandatory")
_WfLapbPktStatsRejectRxs_Type = Counter32
_WfLapbPktStatsRejectRxs_Object = MibTableColumn
wfLapbPktStatsRejectRxs = _WfLapbPktStatsRejectRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 30),
    _WfLapbPktStatsRejectRxs_Type()
)
wfLapbPktStatsRejectRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsRejectRxs.setStatus("mandatory")
_WfLapbPktStatsRestartRxs_Type = Counter32
_WfLapbPktStatsRestartRxs_Object = MibTableColumn
wfLapbPktStatsRestartRxs = _WfLapbPktStatsRestartRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 31),
    _WfLapbPktStatsRestartRxs_Type()
)
wfLapbPktStatsRestartRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsRestartRxs.setStatus("mandatory")
_WfLapbPktStatsDiagRxs_Type = Counter32
_WfLapbPktStatsDiagRxs_Object = MibTableColumn
wfLapbPktStatsDiagRxs = _WfLapbPktStatsDiagRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 32),
    _WfLapbPktStatsDiagRxs_Type()
)
wfLapbPktStatsDiagRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsDiagRxs.setStatus("mandatory")
_WfLapbPktStatsSegmentRxs_Type = Counter32
_WfLapbPktStatsSegmentRxs_Object = MibTableColumn
wfLapbPktStatsSegmentRxs = _WfLapbPktStatsSegmentRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 33),
    _WfLapbPktStatsSegmentRxs_Type()
)
wfLapbPktStatsSegmentRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsSegmentRxs.setStatus("mandatory")
_WfLapbPktStatsBytesRxs_Type = Counter32
_WfLapbPktStatsBytesRxs_Object = MibTableColumn
wfLapbPktStatsBytesRxs = _WfLapbPktStatsBytesRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 34),
    _WfLapbPktStatsBytesRxs_Type()
)
wfLapbPktStatsBytesRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsBytesRxs.setStatus("mandatory")
_WfLapbPktStatsIntBytesRxs_Type = Counter32
_WfLapbPktStatsIntBytesRxs_Object = MibTableColumn
wfLapbPktStatsIntBytesRxs = _WfLapbPktStatsIntBytesRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 35),
    _WfLapbPktStatsIntBytesRxs_Type()
)
wfLapbPktStatsIntBytesRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsIntBytesRxs.setStatus("mandatory")
_WfLapbPktStatsOnOffSwitch_Type = Integer32
_WfLapbPktStatsOnOffSwitch_Object = MibTableColumn
wfLapbPktStatsOnOffSwitch = _WfLapbPktStatsOnOffSwitch_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 6, 1, 36),
    _WfLapbPktStatsOnOffSwitch_Type()
)
wfLapbPktStatsOnOffSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbPktStatsOnOffSwitch.setStatus("mandatory")
_WfX25PvcServiceTable_Object = MibTable
wfX25PvcServiceTable = _WfX25PvcServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 7)
)
if mibBuilder.loadTexts:
    wfX25PvcServiceTable.setStatus("mandatory")
_WfX25PvcServiceEntry_Object = MibTableRow
wfX25PvcServiceEntry = _WfX25PvcServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 7, 1)
)
wfX25PvcServiceEntry.setIndexNames(
    (0, "Wellfleet-X25-MIB", "wfX25SlotNum"),
    (0, "Wellfleet-X25-MIB", "wfX25Connector"),
    (0, "Wellfleet-X25-MIB", "wfX25LineNumber"),
    (0, "Wellfleet-X25-MIB", "wfX25LLIndex"),
    (0, "Wellfleet-X25-MIB", "wfX25PvcServiceCct"),
    (0, "Wellfleet-X25-MIB", "wfX25PvcServiceIndex"),
)
if mibBuilder.loadTexts:
    wfX25PvcServiceEntry.setStatus("mandatory")


class _WfX25PvcDelete_Type(Integer32):
    """Custom type wfX25PvcDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfX25PvcDelete_Type.__name__ = "Integer32"
_WfX25PvcDelete_Object = MibTableColumn
wfX25PvcDelete = _WfX25PvcDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 7, 1, 1),
    _WfX25PvcDelete_Type()
)
wfX25PvcDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PvcDelete.setStatus("mandatory")


class _WfX25PvcDisable_Type(Integer32):
    """Custom type wfX25PvcDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfX25PvcDisable_Type.__name__ = "Integer32"
_WfX25PvcDisable_Object = MibTableColumn
wfX25PvcDisable = _WfX25PvcDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 7, 1, 2),
    _WfX25PvcDisable_Type()
)
wfX25PvcDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PvcDisable.setStatus("mandatory")
_WfX25SlotNum_Type = Integer32
_WfX25SlotNum_Object = MibTableColumn
wfX25SlotNum = _WfX25SlotNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 7, 1, 3),
    _WfX25SlotNum_Type()
)
wfX25SlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25SlotNum.setStatus("mandatory")
_WfX25Connector_Type = Integer32
_WfX25Connector_Object = MibTableColumn
wfX25Connector = _WfX25Connector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 7, 1, 4),
    _WfX25Connector_Type()
)
wfX25Connector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25Connector.setStatus("mandatory")
_WfX25LineNumber_Type = Integer32
_WfX25LineNumber_Object = MibTableColumn
wfX25LineNumber = _WfX25LineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 7, 1, 5),
    _WfX25LineNumber_Type()
)
wfX25LineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25LineNumber.setStatus("mandatory")
_WfX25LLIndex_Type = Integer32
_WfX25LLIndex_Object = MibTableColumn
wfX25LLIndex = _WfX25LLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 7, 1, 6),
    _WfX25LLIndex_Type()
)
wfX25LLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25LLIndex.setStatus("mandatory")
_WfX25PvcServiceCct_Type = Integer32
_WfX25PvcServiceCct_Object = MibTableColumn
wfX25PvcServiceCct = _WfX25PvcServiceCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 7, 1, 7),
    _WfX25PvcServiceCct_Type()
)
wfX25PvcServiceCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PvcServiceCct.setStatus("mandatory")
_WfX25PvcServiceIndex_Type = Integer32
_WfX25PvcServiceIndex_Object = MibTableColumn
wfX25PvcServiceIndex = _WfX25PvcServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 7, 1, 8),
    _WfX25PvcServiceIndex_Type()
)
wfX25PvcServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PvcServiceIndex.setStatus("mandatory")


class _WfX25PvcServiceType_Type(Integer32):
    """Custom type wfX25PvcServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("ddntype", 2),
          ("ipextype", 16),
          ("npttype", 8),
          ("pdntype", 1),
          ("ptoptype", 4),
          ("qllctype", 32))
    )


_WfX25PvcServiceType_Type.__name__ = "Integer32"
_WfX25PvcServiceType_Object = MibTableColumn
wfX25PvcServiceType = _WfX25PvcServiceType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 7, 1, 9),
    _WfX25PvcServiceType_Type()
)
wfX25PvcServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PvcServiceType.setStatus("mandatory")


class _WfX25PvcRxDefWindow_Type(Integer32):
    """Custom type wfX25PvcRxDefWindow based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WfX25PvcRxDefWindow_Type.__name__ = "Integer32"
_WfX25PvcRxDefWindow_Object = MibTableColumn
wfX25PvcRxDefWindow = _WfX25PvcRxDefWindow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 7, 1, 10),
    _WfX25PvcRxDefWindow_Type()
)
wfX25PvcRxDefWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PvcRxDefWindow.setStatus("mandatory")


class _WfX25PvcTxDefWindow_Type(Integer32):
    """Custom type wfX25PvcTxDefWindow based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WfX25PvcTxDefWindow_Type.__name__ = "Integer32"
_WfX25PvcTxDefWindow_Object = MibTableColumn
wfX25PvcTxDefWindow = _WfX25PvcTxDefWindow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 7, 1, 11),
    _WfX25PvcTxDefWindow_Type()
)
wfX25PvcTxDefWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PvcTxDefWindow.setStatus("mandatory")


class _WfX25PvcRxDefLength_Type(Integer32):
    """Custom type wfX25PvcRxDefLength based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("size1024", 10),
          ("size128", 7),
          ("size16", 4),
          ("size2048", 11),
          ("size256", 8),
          ("size32", 5),
          ("size4096", 12),
          ("size512", 9),
          ("size64", 6))
    )


_WfX25PvcRxDefLength_Type.__name__ = "Integer32"
_WfX25PvcRxDefLength_Object = MibTableColumn
wfX25PvcRxDefLength = _WfX25PvcRxDefLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 7, 1, 12),
    _WfX25PvcRxDefLength_Type()
)
wfX25PvcRxDefLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PvcRxDefLength.setStatus("mandatory")


class _WfX25PvcTxDefLength_Type(Integer32):
    """Custom type wfX25PvcTxDefLength based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("size1024", 10),
          ("size128", 7),
          ("size16", 4),
          ("size2048", 11),
          ("size256", 8),
          ("size32", 5),
          ("size4096", 12),
          ("size512", 9),
          ("size64", 6))
    )


_WfX25PvcTxDefLength_Type.__name__ = "Integer32"
_WfX25PvcTxDefLength_Object = MibTableColumn
wfX25PvcTxDefLength = _WfX25PvcTxDefLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 7, 1, 13),
    _WfX25PvcTxDefLength_Type()
)
wfX25PvcTxDefLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PvcTxDefLength.setStatus("mandatory")


class _WfX25PvcRxDefClass_Type(Integer32):
    """Custom type wfX25PvcRxDefClass based on Integer32"""
    defaultValue = 11

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("thrclass1200", 7),
          ("thrclass150", 4),
          ("thrclass19200", 11),
          ("thrclass2400", 8),
          ("thrclass300", 5),
          ("thrclass4800", 9),
          ("thrclass48k", 12),
          ("thrclass600", 6),
          ("thrclass64k", 13),
          ("thrclass75", 3),
          ("thrclass9600", 10))
    )


_WfX25PvcRxDefClass_Type.__name__ = "Integer32"
_WfX25PvcRxDefClass_Object = MibTableColumn
wfX25PvcRxDefClass = _WfX25PvcRxDefClass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 7, 1, 14),
    _WfX25PvcRxDefClass_Type()
)
wfX25PvcRxDefClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PvcRxDefClass.setStatus("mandatory")


class _WfX25PvcTxDefClass_Type(Integer32):
    """Custom type wfX25PvcTxDefClass based on Integer32"""
    defaultValue = 11

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("thrclass1200", 7),
          ("thrclass150", 4),
          ("thrclass19200", 11),
          ("thrclass2400", 8),
          ("thrclass300", 5),
          ("thrclass4800", 9),
          ("thrclass48k", 12),
          ("thrclass600", 6),
          ("thrclass64k", 13),
          ("thrclass75", 3),
          ("thrclass9600", 10))
    )


_WfX25PvcTxDefClass_Type.__name__ = "Integer32"
_WfX25PvcTxDefClass_Object = MibTableColumn
wfX25PvcTxDefClass = _WfX25PvcTxDefClass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 7, 1, 15),
    _WfX25PvcTxDefClass_Type()
)
wfX25PvcTxDefClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PvcTxDefClass.setStatus("mandatory")
_WfX25QllcAddrMapTable_Object = MibTable
wfX25QllcAddrMapTable = _WfX25QllcAddrMapTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 8)
)
if mibBuilder.loadTexts:
    wfX25QllcAddrMapTable.setStatus("mandatory")
_WfX25QllcAddrMapEntry_Object = MibTableRow
wfX25QllcAddrMapEntry = _WfX25QllcAddrMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 8, 1)
)
wfX25QllcAddrMapEntry.setIndexNames(
    (0, "Wellfleet-X25-MIB", "wfX25QllcAddrMapCct"),
    (0, "Wellfleet-X25-MIB", "wfX25QllcAddrMapIndex"),
)
if mibBuilder.loadTexts:
    wfX25QllcAddrMapEntry.setStatus("mandatory")


class _WfX25QllcAddrMapDelete_Type(Integer32):
    """Custom type wfX25QllcAddrMapDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfX25QllcAddrMapDelete_Type.__name__ = "Integer32"
_WfX25QllcAddrMapDelete_Object = MibTableColumn
wfX25QllcAddrMapDelete = _WfX25QllcAddrMapDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 8, 1, 1),
    _WfX25QllcAddrMapDelete_Type()
)
wfX25QllcAddrMapDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25QllcAddrMapDelete.setStatus("mandatory")


class _WfX25QllcAddrMapDisable_Type(Integer32):
    """Custom type wfX25QllcAddrMapDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfX25QllcAddrMapDisable_Type.__name__ = "Integer32"
_WfX25QllcAddrMapDisable_Object = MibTableColumn
wfX25QllcAddrMapDisable = _WfX25QllcAddrMapDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 8, 1, 2),
    _WfX25QllcAddrMapDisable_Type()
)
wfX25QllcAddrMapDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25QllcAddrMapDisable.setStatus("mandatory")


class _WfX25QllcAddrMapState_Type(Integer32):
    """Custom type wfX25QllcAddrMapState based on Integer32"""
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
        *(("active", 1),
          ("notactive", 2),
          ("notpresent", 3))
    )


_WfX25QllcAddrMapState_Type.__name__ = "Integer32"
_WfX25QllcAddrMapState_Object = MibTableColumn
wfX25QllcAddrMapState = _WfX25QllcAddrMapState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 8, 1, 3),
    _WfX25QllcAddrMapState_Type()
)
wfX25QllcAddrMapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25QllcAddrMapState.setStatus("mandatory")


class _WfX25QllcAddrMapCct_Type(Integer32):
    """Custom type wfX25QllcAddrMapCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfX25QllcAddrMapCct_Type.__name__ = "Integer32"
_WfX25QllcAddrMapCct_Object = MibTableColumn
wfX25QllcAddrMapCct = _WfX25QllcAddrMapCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 8, 1, 4),
    _WfX25QllcAddrMapCct_Type()
)
wfX25QllcAddrMapCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25QllcAddrMapCct.setStatus("mandatory")


class _WfX25QllcAddrMapIndex_Type(Integer32):
    """Custom type wfX25QllcAddrMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_WfX25QllcAddrMapIndex_Type.__name__ = "Integer32"
_WfX25QllcAddrMapIndex_Object = MibTableColumn
wfX25QllcAddrMapIndex = _WfX25QllcAddrMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 8, 1, 5),
    _WfX25QllcAddrMapIndex_Type()
)
wfX25QllcAddrMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25QllcAddrMapIndex.setStatus("mandatory")
_WfX25QllcAddrMapPartnerX121_Type = DisplayString
_WfX25QllcAddrMapPartnerX121_Object = MibTableColumn
wfX25QllcAddrMapPartnerX121 = _WfX25QllcAddrMapPartnerX121_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 8, 1, 6),
    _WfX25QllcAddrMapPartnerX121_Type()
)
wfX25QllcAddrMapPartnerX121.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25QllcAddrMapPartnerX121.setStatus("mandatory")
_WfX25QllcAddrMapAdjacentX121_Type = DisplayString
_WfX25QllcAddrMapAdjacentX121_Object = MibTableColumn
wfX25QllcAddrMapAdjacentX121 = _WfX25QllcAddrMapAdjacentX121_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 8, 1, 7),
    _WfX25QllcAddrMapAdjacentX121_Type()
)
wfX25QllcAddrMapAdjacentX121.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25QllcAddrMapAdjacentX121.setStatus("mandatory")


class _WfX25QllcAddrMapPid_Type(Integer32):
    """Custom type wfX25QllcAddrMapPid based on Integer32"""
    defaultValue = 195

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_WfX25QllcAddrMapPid_Type.__name__ = "Integer32"
_WfX25QllcAddrMapPid_Object = MibTableColumn
wfX25QllcAddrMapPid = _WfX25QllcAddrMapPid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 8, 1, 8),
    _WfX25QllcAddrMapPid_Type()
)
wfX25QllcAddrMapPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25QllcAddrMapPid.setStatus("mandatory")
_WfX25QllcAddrMapPartnerMac_Type = OctetString
_WfX25QllcAddrMapPartnerMac_Object = MibTableColumn
wfX25QllcAddrMapPartnerMac = _WfX25QllcAddrMapPartnerMac_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 8, 1, 9),
    _WfX25QllcAddrMapPartnerMac_Type()
)
wfX25QllcAddrMapPartnerMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25QllcAddrMapPartnerMac.setStatus("mandatory")


class _WfX25QllcAddrMapPartnerSap_Type(Integer32):
    """Custom type wfX25QllcAddrMapPartnerSap based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_WfX25QllcAddrMapPartnerSap_Type.__name__ = "Integer32"
_WfX25QllcAddrMapPartnerSap_Object = MibTableColumn
wfX25QllcAddrMapPartnerSap = _WfX25QllcAddrMapPartnerSap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 8, 1, 10),
    _WfX25QllcAddrMapPartnerSap_Type()
)
wfX25QllcAddrMapPartnerSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25QllcAddrMapPartnerSap.setStatus("mandatory")


class _WfX25QllcAddrMapAdjacentMac_Type(OctetString):
    """Custom type wfX25QllcAddrMapAdjacentMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfX25QllcAddrMapAdjacentMac_Type.__name__ = "OctetString"
_WfX25QllcAddrMapAdjacentMac_Object = MibTableColumn
wfX25QllcAddrMapAdjacentMac = _WfX25QllcAddrMapAdjacentMac_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 8, 1, 11),
    _WfX25QllcAddrMapAdjacentMac_Type()
)
wfX25QllcAddrMapAdjacentMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25QllcAddrMapAdjacentMac.setStatus("mandatory")


class _WfX25QllcAddrMapAdjacentSap_Type(Integer32):
    """Custom type wfX25QllcAddrMapAdjacentSap based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_WfX25QllcAddrMapAdjacentSap_Type.__name__ = "Integer32"
_WfX25QllcAddrMapAdjacentSap_Object = MibTableColumn
wfX25QllcAddrMapAdjacentSap = _WfX25QllcAddrMapAdjacentSap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 8, 1, 12),
    _WfX25QllcAddrMapAdjacentSap_Type()
)
wfX25QllcAddrMapAdjacentSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25QllcAddrMapAdjacentSap.setStatus("mandatory")


class _WfX25QllcAddrMapOptions_Type(Integer32):
    """Custom type wfX25QllcAddrMapOptions based on Integer32"""
    defaultValue = 0


_WfX25QllcAddrMapOptions_Object = MibTableColumn
wfX25QllcAddrMapOptions = _WfX25QllcAddrMapOptions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 8, 1, 13),
    _WfX25QllcAddrMapOptions_Type()
)
wfX25QllcAddrMapOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25QllcAddrMapOptions.setStatus("mandatory")


class _WfX25QllcAddrMapTrace_Type(Integer32):
    """Custom type wfX25QllcAddrMapTrace based on Integer32"""
    defaultValue = 0


_WfX25QllcAddrMapTrace_Object = MibTableColumn
wfX25QllcAddrMapTrace = _WfX25QllcAddrMapTrace_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 8, 1, 14),
    _WfX25QllcAddrMapTrace_Type()
)
wfX25QllcAddrMapTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25QllcAddrMapTrace.setStatus("mandatory")


class _WfX25QllcAddrMapPuType_Type(Integer32):
    """Custom type wfX25QllcAddrMapPuType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pu20", 2),
          ("pu21", 1))
    )


_WfX25QllcAddrMapPuType_Type.__name__ = "Integer32"
_WfX25QllcAddrMapPuType_Object = MibTableColumn
wfX25QllcAddrMapPuType = _WfX25QllcAddrMapPuType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 8, 1, 15),
    _WfX25QllcAddrMapPuType_Type()
)
wfX25QllcAddrMapPuType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25QllcAddrMapPuType.setStatus("obsolete")


class _WfX25QllcAddrMapGenXid_Type(Integer32):
    """Custom type wfX25QllcAddrMapGenXid based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfX25QllcAddrMapGenXid_Type.__name__ = "Integer32"
_WfX25QllcAddrMapGenXid_Object = MibTableColumn
wfX25QllcAddrMapGenXid = _WfX25QllcAddrMapGenXid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 8, 1, 16),
    _WfX25QllcAddrMapGenXid_Type()
)
wfX25QllcAddrMapGenXid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25QllcAddrMapGenXid.setStatus("mandatory")


class _WfX25QllcAddrMapNodeId_Type(OctetString):
    """Custom type wfX25QllcAddrMapNodeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfX25QllcAddrMapNodeId_Type.__name__ = "OctetString"
_WfX25QllcAddrMapNodeId_Object = MibTableColumn
wfX25QllcAddrMapNodeId = _WfX25QllcAddrMapNodeId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 8, 1, 17),
    _WfX25QllcAddrMapNodeId_Type()
)
wfX25QllcAddrMapNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25QllcAddrMapNodeId.setStatus("obsolete")
_WfX25QllcAddrMapName_Type = DisplayString
_WfX25QllcAddrMapName_Object = MibTableColumn
wfX25QllcAddrMapName = _WfX25QllcAddrMapName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4, 8, 1, 18),
    _WfX25QllcAddrMapName_Type()
)
wfX25QllcAddrMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25QllcAddrMapName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-X25-MIB",
    **{"wfX25": wfX25,
       "wfX25Delete": wfX25Delete,
       "wfX25Disable": wfX25Disable,
       "wfX25State": wfX25State,
       "wfX25ServiceTable": wfX25ServiceTable,
       "wfX25ServiceEntry": wfX25ServiceEntry,
       "wfX25ServiceDelete": wfX25ServiceDelete,
       "wfX25ServiceDisable": wfX25ServiceDisable,
       "wfX25ServiceSlot": wfX25ServiceSlot,
       "wfX25ServiceConnector": wfX25ServiceConnector,
       "wfX25ServiceLineNumber": wfX25ServiceLineNumber,
       "wfX25ServiceLLIndex": wfX25ServiceLLIndex,
       "wfX25ServiceCct": wfX25ServiceCct,
       "wfX25ServiceIndex": wfX25ServiceIndex,
       "wfX25ServiceType": wfX25ServiceType,
       "wfX25ServiceConnRef": wfX25ServiceConnRef,
       "wfX25ServiceConnId": wfX25ServiceConnId,
       "wfX25ServiceRemoteX121Addr": wfX25ServiceRemoteX121Addr,
       "wfX25ServiceRemoteIpAddr": wfX25ServiceRemoteIpAddr,
       "wfX25ServiceBCast": wfX25ServiceBCast,
       "wfX25ServiceMaxConn": wfX25ServiceMaxConn,
       "wfX25ServicePrecedence": wfX25ServicePrecedence,
       "wfX25ServiceMaxIdle": wfX25ServiceMaxIdle,
       "wfX25ServiceCallRetry": wfX25ServiceCallRetry,
       "wfX25ServiceFlowFacility": wfX25ServiceFlowFacility,
       "wfX25ServiceWinSize": wfX25ServiceWinSize,
       "wfX25ServicePktSize": wfX25ServicePktSize,
       "wfX25ServiceFastSelRequest": wfX25ServiceFastSelRequest,
       "wfX25ServiceFastSelAccept": wfX25ServiceFastSelAccept,
       "wfX25ServiceRevChRequest": wfX25ServiceRevChRequest,
       "wfX25ServiceRevChAccept": wfX25ServiceRevChAccept,
       "wfX25ServiceCugFormat": wfX25ServiceCugFormat,
       "wfX25ServiceCugType": wfX25ServiceCugType,
       "wfX25ServiceCugNum": wfX25ServiceCugNum,
       "wfX25ServiceUserFacility": wfX25ServiceUserFacility,
       "wfX25ServiceValid": wfX25ServiceValid,
       "wfX25ServiceBFE": wfX25ServiceBFE,
       "wfX25ServiceForceCugZero": wfX25ServiceForceCugZero,
       "wfX25ServiceWcpEnable": wfX25ServiceWcpEnable,
       "wfX25ServiceMUX": wfX25ServiceMUX,
       "wfX25ServicePtopCallRequest": wfX25ServicePtopCallRequest,
       "wfX25ServiceVcType": wfX25ServiceVcType,
       "wfX25ServicePvcLcn": wfX25ServicePvcLcn,
       "wfX25ServiceMacPoolStart": wfX25ServiceMacPoolStart,
       "wfX25ServiceMacPoolSize": wfX25ServiceMacPoolSize,
       "wfX25ServiceWindowTimeout": wfX25ServiceWindowTimeout,
       "wfX25ServiceVcBurstThroughput": wfX25ServiceVcBurstThroughput,
       "wfX25ServiceVcBurstQDepth": wfX25ServiceVcBurstQDepth,
       "wfX25ServiceVcPriority": wfX25ServiceVcPriority,
       "wfX25ServiceVcBurstQClippedPkts": wfX25ServiceVcBurstQClippedPkts,
       "wfX25ServiceVcBurstQPktCnt": wfX25ServiceVcBurstQPktCnt,
       "wfX25ServiceVcBurstQHighWaterPkts": wfX25ServiceVcBurstQHighWaterPkts,
       "wfX25ServiceVcPktDrops": wfX25ServiceVcPktDrops,
       "wfX25ServicePlpPktDrops": wfX25ServicePlpPktDrops,
       "wfX25ServiceBurstThrPerVc": wfX25ServiceBurstThrPerVc,
       "wfX25ServiceBackupRecoveryDelay": wfX25ServiceBackupRecoveryDelay,
       "wfX25ServiceSetupTime": wfX25ServiceSetupTime,
       "wfX25ServiceRetryNumber": wfX25ServiceRetryNumber,
       "wfX25BackupInitiation": wfX25BackupInitiation,
       "wfX25ServiceEntryName": wfX25ServiceEntryName,
       "wfX25VcTable": wfX25VcTable,
       "wfX25VcEntry": wfX25VcEntry,
       "wfX25VcSlotNum": wfX25VcSlotNum,
       "wfX25VcConnector": wfX25VcConnector,
       "wfX25VcLineNumber": wfX25VcLineNumber,
       "wfX25VcLLIndex": wfX25VcLLIndex,
       "wfX25VcCct": wfX25VcCct,
       "wfX25VcNumber": wfX25VcNumber,
       "wfX25VcDataTxs": wfX25VcDataTxs,
       "wfX25VcInterruptTxs": wfX25VcInterruptTxs,
       "wfX25VcResetTxs": wfX25VcResetTxs,
       "wfX25VcRrTxs": wfX25VcRrTxs,
       "wfX25VcRnrTxs": wfX25VcRnrTxs,
       "wfX25VcRejectTxs": wfX25VcRejectTxs,
       "wfX25VcSegmentTxs": wfX25VcSegmentTxs,
       "wfX25VcBytesTxs": wfX25VcBytesTxs,
       "wfX25VcIntBytesTxs": wfX25VcIntBytesTxs,
       "wfX25VcDataRxs": wfX25VcDataRxs,
       "wfX25VcInterruptRxs": wfX25VcInterruptRxs,
       "wfX25VcResetRxs": wfX25VcResetRxs,
       "wfX25VcRrRxs": wfX25VcRrRxs,
       "wfX25VcRnrRxs": wfX25VcRnrRxs,
       "wfX25VcRejectRxs": wfX25VcRejectRxs,
       "wfX25VcSegmentRxs": wfX25VcSegmentRxs,
       "wfX25VcBytesRxs": wfX25VcBytesRxs,
       "wfX25VcIntBytesRxs": wfX25VcIntBytesRxs,
       "wfX25VcApPktsDropped": wfX25VcApPktsDropped,
       "wfX25VcRemoteX121Addr": wfX25VcRemoteX121Addr,
       "wfX25VcBurstQClippedPkts": wfX25VcBurstQClippedPkts,
       "wfX25VcBurstQPktCnt": wfX25VcBurstQPktCnt,
       "wfX25VcBurstQHighWaterPkts": wfX25VcBurstQHighWaterPkts,
       "wfX25VcPktsLargerThanBurstThrCnt": wfX25VcPktsLargerThanBurstThrCnt,
       "wfX25VcPktDrops": wfX25VcPktDrops,
       "wfX25VcPlpPktDrops": wfX25VcPlpPktDrops,
       "wfX25VcMbsOutstanding": wfX25VcMbsOutstanding,
       "wfX25VcMbsOutstandingPostTx": wfX25VcMbsOutstandingPostTx,
       "wfX25VcMaxTx": wfX25VcMaxTx,
       "wfX25VcMbsQueueCnt": wfX25VcMbsQueueCnt,
       "wfX25VcMbsQueueCntPostTx": wfX25VcMbsQueueCntPostTx,
       "wfX25VcTxQueueCnt": wfX25VcTxQueueCnt,
       "wfX25VcTxQueueCntPostTx": wfX25VcTxQueueCntPostTx,
       "wfLapbPktTable": wfLapbPktTable,
       "wfLapbPktEntry": wfLapbPktEntry,
       "wfLapbPktDelete": wfLapbPktDelete,
       "wfLapbPktDisable": wfLapbPktDisable,
       "wfLapbPktSlotNum": wfLapbPktSlotNum,
       "wfLapbPktConnector": wfLapbPktConnector,
       "wfLapbPktLineNumber": wfLapbPktLineNumber,
       "wfLapbPktLLIndex": wfLapbPktLLIndex,
       "wfLapbPktLapbCct": wfLapbPktLapbCct,
       "wfLapbPktLinkId": wfLapbPktLinkId,
       "wfLapbPktLineState": wfLapbPktLineState,
       "wfLapbPktSeqSize": wfLapbPktSeqSize,
       "wfLapbPktMaxWindow": wfLapbPktMaxWindow,
       "wfLapbPktMaxLength": wfLapbPktMaxLength,
       "wfLapbPktMaxThroughput": wfLapbPktMaxThroughput,
       "wfLapbPktFlowCtl": wfLapbPktFlowCtl,
       "wfLapbPktThroughput": wfLapbPktThroughput,
       "wfLapbPktUserIdentity": wfLapbPktUserIdentity,
       "wfLapbPktInCalls": wfLapbPktInCalls,
       "wfLapbPktOutCalls": wfLapbPktOutCalls,
       "wfLapbPktFastAccept": wfLapbPktFastAccept,
       "wfLapbPktReverseAccept": wfLapbPktReverseAccept,
       "wfLapbPktFastSelect": wfLapbPktFastSelect,
       "wfLapbPktReverseCharging": wfLapbPktReverseCharging,
       "wfLapbPktCugSelection": wfLapbPktCugSelection,
       "wfLapbPktCugOA": wfLapbPktCugOA,
       "wfLapbPktCugBilateral": wfLapbPktCugBilateral,
       "wfLapbPktRpoaSelection": wfLapbPktRpoaSelection,
       "wfLapbPktChargeInform": wfLapbPktChargeInform,
       "wfLapbPktTransitDelay": wfLapbPktTransitDelay,
       "wfLapbPktFullAddressing": wfLapbPktFullAddressing,
       "wfLapbPktAccFormat": wfLapbPktAccFormat,
       "wfLapbPktRelFormat": wfLapbPktRelFormat,
       "wfLapbPktT1": wfLapbPktT1,
       "wfLapbPktT2": wfLapbPktT2,
       "wfLapbPktT3": wfLapbPktT3,
       "wfLapbPktT4": wfLapbPktT4,
       "wfLapbPktIwcCnt": wfLapbPktIwcCnt,
       "wfLapbPktIwcId": wfLapbPktIwcId,
       "wfLapbPktBwcCnt": wfLapbPktBwcCnt,
       "wfLapbPktBwcId": wfLapbPktBwcId,
       "wfLapbPktOwcCnt": wfLapbPktOwcCnt,
       "wfLapbPktOwcId": wfLapbPktOwcId,
       "wfLapbPktDefWindow": wfLapbPktDefWindow,
       "wfLapbPktDefLength": wfLapbPktDefLength,
       "wfLapbPktDefClass": wfLapbPktDefClass,
       "wfLapbPktDxe": wfLapbPktDxe,
       "wfLapbPktConformance": wfLapbPktConformance,
       "wfLapbPktStandard": wfLapbPktStandard,
       "wfLapbPktNetaddr": wfLapbPktNetaddr,
       "wfLapbPktStatistics": wfLapbPktStatistics,
       "wfLapbPktNetaddrType": wfLapbPktNetaddrType,
       "wfLapbPktDDNIpAddr": wfLapbPktDDNIpAddr,
       "wfLapbPktPDNX121Addr": wfLapbPktPDNX121Addr,
       "wfLapbPktTxT5": wfLapbPktTxT5,
       "wfLapbPktUseDfltService": wfLapbPktUseDfltService,
       "wfLapbPktPVCCnt": wfLapbPktPVCCnt,
       "wfLapbPktPVCLowLcn": wfLapbPktPVCLowLcn,
       "wfLapbPktClientTimer": wfLapbPktClientTimer,
       "wfLapbPktPduSize": wfLapbPktPduSize,
       "wfLapbPktTranspacCauseCodeEnable": wfLapbPktTranspacCauseCodeEnable,
       "wfLapbPktTxMbsQueueThreshold": wfLapbPktTxMbsQueueThreshold,
       "wfLapbPktBackupDebugLvl": wfLapbPktBackupDebugLvl,
       "wfLapbPktBackupEnable": wfLapbPktBackupEnable,
       "wfLapbPktStatsTable": wfLapbPktStatsTable,
       "wfLapbPktStatsEntry": wfLapbPktStatsEntry,
       "wfLapbPktStatsSlotNum": wfLapbPktStatsSlotNum,
       "wfLapbPktStatsConnector": wfLapbPktStatsConnector,
       "wfLapbPktStatsLineNumber": wfLapbPktStatsLineNumber,
       "wfLapbPktStatsLLIndex": wfLapbPktStatsLLIndex,
       "wfLapbPktStatsCct": wfLapbPktStatsCct,
       "wfLapbPktStatsLineAddress": wfLapbPktStatsLineAddress,
       "wfLapbPktStatsMaxVcs": wfLapbPktStatsMaxVcs,
       "wfLapbPktStatsActiveVcs": wfLapbPktStatsActiveVcs,
       "wfLapbPktStatsActiveMax": wfLapbPktStatsActiveMax,
       "wfLapbPktStatsTotalConnections": wfLapbPktStatsTotalConnections,
       "wfLapbPktStatsFailedConnections": wfLapbPktStatsFailedConnections,
       "wfLapbPktStatsNormalDisconnects": wfLapbPktStatsNormalDisconnects,
       "wfLapbPktStatsAbnormalDisconnects": wfLapbPktStatsAbnormalDisconnects,
       "wfLapbPktStatsDataTxs": wfLapbPktStatsDataTxs,
       "wfLapbPktStatsInterruptTxs": wfLapbPktStatsInterruptTxs,
       "wfLapbPktStatsResetTxs": wfLapbPktStatsResetTxs,
       "wfLapbPktStatsRrTxs": wfLapbPktStatsRrTxs,
       "wfLapbPktStatsRnrTxs": wfLapbPktStatsRnrTxs,
       "wfLapbPktStatsRejectTxs": wfLapbPktStatsRejectTxs,
       "wfLapbPktStatsRestartTxs": wfLapbPktStatsRestartTxs,
       "wfLapbPktStatsDiagTxs": wfLapbPktStatsDiagTxs,
       "wfLapbPktStatsSegmentTxs": wfLapbPktStatsSegmentTxs,
       "wfLapbPktStatsBytesTxs": wfLapbPktStatsBytesTxs,
       "wfLapbPktStatsIntBytesTxs": wfLapbPktStatsIntBytesTxs,
       "wfLapbPktStatsDataRxs": wfLapbPktStatsDataRxs,
       "wfLapbPktStatsInterruptRxs": wfLapbPktStatsInterruptRxs,
       "wfLapbPktStatsResetRxs": wfLapbPktStatsResetRxs,
       "wfLapbPktStatsRrRxs": wfLapbPktStatsRrRxs,
       "wfLapbPktStatsRnrRxs": wfLapbPktStatsRnrRxs,
       "wfLapbPktStatsRejectRxs": wfLapbPktStatsRejectRxs,
       "wfLapbPktStatsRestartRxs": wfLapbPktStatsRestartRxs,
       "wfLapbPktStatsDiagRxs": wfLapbPktStatsDiagRxs,
       "wfLapbPktStatsSegmentRxs": wfLapbPktStatsSegmentRxs,
       "wfLapbPktStatsBytesRxs": wfLapbPktStatsBytesRxs,
       "wfLapbPktStatsIntBytesRxs": wfLapbPktStatsIntBytesRxs,
       "wfLapbPktStatsOnOffSwitch": wfLapbPktStatsOnOffSwitch,
       "wfX25PvcServiceTable": wfX25PvcServiceTable,
       "wfX25PvcServiceEntry": wfX25PvcServiceEntry,
       "wfX25PvcDelete": wfX25PvcDelete,
       "wfX25PvcDisable": wfX25PvcDisable,
       "wfX25SlotNum": wfX25SlotNum,
       "wfX25Connector": wfX25Connector,
       "wfX25LineNumber": wfX25LineNumber,
       "wfX25LLIndex": wfX25LLIndex,
       "wfX25PvcServiceCct": wfX25PvcServiceCct,
       "wfX25PvcServiceIndex": wfX25PvcServiceIndex,
       "wfX25PvcServiceType": wfX25PvcServiceType,
       "wfX25PvcRxDefWindow": wfX25PvcRxDefWindow,
       "wfX25PvcTxDefWindow": wfX25PvcTxDefWindow,
       "wfX25PvcRxDefLength": wfX25PvcRxDefLength,
       "wfX25PvcTxDefLength": wfX25PvcTxDefLength,
       "wfX25PvcRxDefClass": wfX25PvcRxDefClass,
       "wfX25PvcTxDefClass": wfX25PvcTxDefClass,
       "wfX25QllcAddrMapTable": wfX25QllcAddrMapTable,
       "wfX25QllcAddrMapEntry": wfX25QllcAddrMapEntry,
       "wfX25QllcAddrMapDelete": wfX25QllcAddrMapDelete,
       "wfX25QllcAddrMapDisable": wfX25QllcAddrMapDisable,
       "wfX25QllcAddrMapState": wfX25QllcAddrMapState,
       "wfX25QllcAddrMapCct": wfX25QllcAddrMapCct,
       "wfX25QllcAddrMapIndex": wfX25QllcAddrMapIndex,
       "wfX25QllcAddrMapPartnerX121": wfX25QllcAddrMapPartnerX121,
       "wfX25QllcAddrMapAdjacentX121": wfX25QllcAddrMapAdjacentX121,
       "wfX25QllcAddrMapPid": wfX25QllcAddrMapPid,
       "wfX25QllcAddrMapPartnerMac": wfX25QllcAddrMapPartnerMac,
       "wfX25QllcAddrMapPartnerSap": wfX25QllcAddrMapPartnerSap,
       "wfX25QllcAddrMapAdjacentMac": wfX25QllcAddrMapAdjacentMac,
       "wfX25QllcAddrMapAdjacentSap": wfX25QllcAddrMapAdjacentSap,
       "wfX25QllcAddrMapOptions": wfX25QllcAddrMapOptions,
       "wfX25QllcAddrMapTrace": wfX25QllcAddrMapTrace,
       "wfX25QllcAddrMapPuType": wfX25QllcAddrMapPuType,
       "wfX25QllcAddrMapGenXid": wfX25QllcAddrMapGenXid,
       "wfX25QllcAddrMapNodeId": wfX25QllcAddrMapNodeId,
       "wfX25QllcAddrMapName": wfX25QllcAddrMapName}
)
