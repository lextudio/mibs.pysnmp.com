# SNMP MIB module (CXFLT-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXFLT-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:22 2024
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

(cxFltIp,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxFltIp")

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

_CxFltIpAddrTable_Object = MibTable
cxFltIpAddrTable = _CxFltIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 21, 1)
)
if mibBuilder.loadTexts:
    cxFltIpAddrTable.setStatus("mandatory")
_CxFltIpAddrEntry_Object = MibTableRow
cxFltIpAddrEntry = _CxFltIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 21, 1, 1)
)
cxFltIpAddrEntry.setIndexNames(
    (0, "CXFLT-IP-MIB", "cxFltIpIndex"),
)
if mibBuilder.loadTexts:
    cxFltIpAddrEntry.setStatus("mandatory")


class _CxFltIpIndex_Type(Integer32):
    """Custom type cxFltIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CxFltIpIndex_Type.__name__ = "Integer32"
_CxFltIpIndex_Object = MibTableColumn
cxFltIpIndex = _CxFltIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 21, 1, 1, 1),
    _CxFltIpIndex_Type()
)
cxFltIpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFltIpIndex.setStatus("mandatory")
_CxFltIpSrcAddr_Type = IpAddress
_CxFltIpSrcAddr_Object = MibTableColumn
cxFltIpSrcAddr = _CxFltIpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 21, 1, 1, 2),
    _CxFltIpSrcAddr_Type()
)
cxFltIpSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFltIpSrcAddr.setStatus("mandatory")
_CxFltIpSrcNetMask_Type = IpAddress
_CxFltIpSrcNetMask_Object = MibTableColumn
cxFltIpSrcNetMask = _CxFltIpSrcNetMask_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 21, 1, 1, 3),
    _CxFltIpSrcNetMask_Type()
)
cxFltIpSrcNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFltIpSrcNetMask.setStatus("mandatory")
_CxFltIpDstAddr_Type = IpAddress
_CxFltIpDstAddr_Object = MibTableColumn
cxFltIpDstAddr = _CxFltIpDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 21, 1, 1, 4),
    _CxFltIpDstAddr_Type()
)
cxFltIpDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFltIpDstAddr.setStatus("mandatory")
_CxFltIpDstNetMask_Type = IpAddress
_CxFltIpDstNetMask_Object = MibTableColumn
cxFltIpDstNetMask = _CxFltIpDstNetMask_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 21, 1, 1, 5),
    _CxFltIpDstNetMask_Type()
)
cxFltIpDstNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFltIpDstNetMask.setStatus("mandatory")


class _CxFltIpParameter_Type(Integer32):
    """Custom type cxFltIpParameter based on Integer32"""
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
        *(("discard", 1),
          ("forward", 2),
          ("priority-high", 4),
          ("priority-low", 3))
    )


_CxFltIpParameter_Type.__name__ = "Integer32"
_CxFltIpParameter_Object = MibTableColumn
cxFltIpParameter = _CxFltIpParameter_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 21, 1, 1, 6),
    _CxFltIpParameter_Type()
)
cxFltIpParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFltIpParameter.setStatus("mandatory")


class _CxFltIpRowStatus_Type(Integer32):
    """Custom type cxFltIpRowStatus based on Integer32"""
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


_CxFltIpRowStatus_Type.__name__ = "Integer32"
_CxFltIpRowStatus_Object = MibTableColumn
cxFltIpRowStatus = _CxFltIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 21, 1, 1, 7),
    _CxFltIpRowStatus_Type()
)
cxFltIpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFltIpRowStatus.setStatus("mandatory")


class _CxFltIpProtType_Type(Integer32):
    """Custom type cxFltIpProtType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CxFltIpProtType_Type.__name__ = "Integer32"
_CxFltIpProtType_Object = MibTableColumn
cxFltIpProtType = _CxFltIpProtType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 21, 1, 1, 8),
    _CxFltIpProtType_Type()
)
cxFltIpProtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFltIpProtType.setStatus("mandatory")


class _CxFltIpProtPortNum_Type(Integer32):
    """Custom type cxFltIpProtPortNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CxFltIpProtPortNum_Type.__name__ = "Integer32"
_CxFltIpProtPortNum_Object = MibTableColumn
cxFltIpProtPortNum = _CxFltIpProtPortNum_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 21, 1, 1, 9),
    _CxFltIpProtPortNum_Type()
)
cxFltIpProtPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFltIpProtPortNum.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXFLT-IP-MIB",
    **{"cxFltIpAddrTable": cxFltIpAddrTable,
       "cxFltIpAddrEntry": cxFltIpAddrEntry,
       "cxFltIpIndex": cxFltIpIndex,
       "cxFltIpSrcAddr": cxFltIpSrcAddr,
       "cxFltIpSrcNetMask": cxFltIpSrcNetMask,
       "cxFltIpDstAddr": cxFltIpDstAddr,
       "cxFltIpDstNetMask": cxFltIpDstNetMask,
       "cxFltIpParameter": cxFltIpParameter,
       "cxFltIpRowStatus": cxFltIpRowStatus,
       "cxFltIpProtType": cxFltIpProtType,
       "cxFltIpProtPortNum": cxFltIpProtPortNum}
)
