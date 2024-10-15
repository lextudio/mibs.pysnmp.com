# SNMP MIB module (CXFLT-IPX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXFLT-IPX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:23 2024
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

(cxFltIpx,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxFltIpx")

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



class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CxFltIpxAddrTable_Object = MibTable
cxFltIpxAddrTable = _CxFltIpxAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22, 1)
)
if mibBuilder.loadTexts:
    cxFltIpxAddrTable.setStatus("mandatory")
_CxFltIpxAddrEntry_Object = MibTableRow
cxFltIpxAddrEntry = _CxFltIpxAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22, 1, 1)
)
cxFltIpxAddrEntry.setIndexNames(
    (0, "CXFLT-IPX-MIB", "cxFltIpxIndex"),
)
if mibBuilder.loadTexts:
    cxFltIpxAddrEntry.setStatus("mandatory")


class _CxFltIpxIndex_Type(Integer32):
    """Custom type cxFltIpxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CxFltIpxIndex_Type.__name__ = "Integer32"
_CxFltIpxIndex_Object = MibTableColumn
cxFltIpxIndex = _CxFltIpxIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22, 1, 1, 1),
    _CxFltIpxIndex_Type()
)
cxFltIpxIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFltIpxIndex.setStatus("mandatory")
_CxFltIpxSrcAddr_Type = NetNumber
_CxFltIpxSrcAddr_Object = MibTableColumn
cxFltIpxSrcAddr = _CxFltIpxSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22, 1, 1, 2),
    _CxFltIpxSrcAddr_Type()
)
cxFltIpxSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFltIpxSrcAddr.setStatus("mandatory")
_CxFltIpxDstAddr_Type = NetNumber
_CxFltIpxDstAddr_Object = MibTableColumn
cxFltIpxDstAddr = _CxFltIpxDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22, 1, 1, 3),
    _CxFltIpxDstAddr_Type()
)
cxFltIpxDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFltIpxDstAddr.setStatus("mandatory")


class _CxFltIpxParameter_Type(Integer32):
    """Custom type cxFltIpxParameter based on Integer32"""
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


_CxFltIpxParameter_Type.__name__ = "Integer32"
_CxFltIpxParameter_Object = MibTableColumn
cxFltIpxParameter = _CxFltIpxParameter_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22, 1, 1, 4),
    _CxFltIpxParameter_Type()
)
cxFltIpxParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFltIpxParameter.setStatus("mandatory")


class _CxFltIpxRowStatus_Type(Integer32):
    """Custom type cxFltIpxRowStatus based on Integer32"""
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


_CxFltIpxRowStatus_Type.__name__ = "Integer32"
_CxFltIpxRowStatus_Object = MibTableColumn
cxFltIpxRowStatus = _CxFltIpxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22, 1, 1, 5),
    _CxFltIpxRowStatus_Type()
)
cxFltIpxRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFltIpxRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXFLT-IPX-MIB",
    **{"NetNumber": NetNumber,
       "cxFltIpxAddrTable": cxFltIpxAddrTable,
       "cxFltIpxAddrEntry": cxFltIpxAddrEntry,
       "cxFltIpxIndex": cxFltIpxIndex,
       "cxFltIpxSrcAddr": cxFltIpxSrcAddr,
       "cxFltIpxDstAddr": cxFltIpxDstAddr,
       "cxFltIpxParameter": cxFltIpxParameter,
       "cxFltIpxRowStatus": cxFltIpxRowStatus}
)
