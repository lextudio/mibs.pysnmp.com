# SNMP MIB module (CXFLT-IPXSAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXFLT-IPXSAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:24 2024
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

(cxIpx,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxIpx")

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

_CxFltIpxSapTable_Object = MibTable
cxFltIpxSapTable = _CxFltIpxSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 3)
)
if mibBuilder.loadTexts:
    cxFltIpxSapTable.setStatus("mandatory")
_CxFltIpxSapEntry_Object = MibTableRow
cxFltIpxSapEntry = _CxFltIpxSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 3, 1)
)
cxFltIpxSapEntry.setIndexNames(
    (0, "CXFLT-IPXSAP-MIB", "cxFltIpxSapIndex"),
)
if mibBuilder.loadTexts:
    cxFltIpxSapEntry.setStatus("mandatory")


class _CxFltIpxSapIndex_Type(Integer32):
    """Custom type cxFltIpxSapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CxFltIpxSapIndex_Type.__name__ = "Integer32"
_CxFltIpxSapIndex_Object = MibTableColumn
cxFltIpxSapIndex = _CxFltIpxSapIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 3, 1, 1),
    _CxFltIpxSapIndex_Type()
)
cxFltIpxSapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxFltIpxSapIndex.setStatus("mandatory")


class _CxFltIpxSapType_Type(Integer32):
    """Custom type cxFltIpxSapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CxFltIpxSapType_Type.__name__ = "Integer32"
_CxFltIpxSapType_Object = MibTableColumn
cxFltIpxSapType = _CxFltIpxSapType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 3, 1, 2),
    _CxFltIpxSapType_Type()
)
cxFltIpxSapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFltIpxSapType.setStatus("mandatory")


class _CxFltIpxSapName_Type(DisplayString):
    """Custom type cxFltIpxSapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_CxFltIpxSapName_Type.__name__ = "DisplayString"
_CxFltIpxSapName_Object = MibTableColumn
cxFltIpxSapName = _CxFltIpxSapName_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 3, 1, 3),
    _CxFltIpxSapName_Type()
)
cxFltIpxSapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFltIpxSapName.setStatus("mandatory")


class _CxFltIpxSapStatus_Type(Integer32):
    """Custom type cxFltIpxSapStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("nodiscard", 2))
    )


_CxFltIpxSapStatus_Type.__name__ = "Integer32"
_CxFltIpxSapStatus_Object = MibTableColumn
cxFltIpxSapStatus = _CxFltIpxSapStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 3, 1, 4),
    _CxFltIpxSapStatus_Type()
)
cxFltIpxSapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFltIpxSapStatus.setStatus("mandatory")


class _CxFltIpxSapRowStatus_Type(Integer32):
    """Custom type cxFltIpxSapRowStatus based on Integer32"""
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


_CxFltIpxSapRowStatus_Type.__name__ = "Integer32"
_CxFltIpxSapRowStatus_Object = MibTableColumn
cxFltIpxSapRowStatus = _CxFltIpxSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 3, 1, 5),
    _CxFltIpxSapRowStatus_Type()
)
cxFltIpxSapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFltIpxSapRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXFLT-IPXSAP-MIB",
    **{"cxFltIpxSapTable": cxFltIpxSapTable,
       "cxFltIpxSapEntry": cxFltIpxSapEntry,
       "cxFltIpxSapIndex": cxFltIpxSapIndex,
       "cxFltIpxSapType": cxFltIpxSapType,
       "cxFltIpxSapName": cxFltIpxSapName,
       "cxFltIpxSapStatus": cxFltIpxSapStatus,
       "cxFltIpxSapRowStatus": cxFltIpxSapRowStatus}
)
