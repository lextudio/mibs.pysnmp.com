# SNMP MIB module (IPX-INTERFACE-MANAGEMENT-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPX-INTERFACE-MANAGEMENT-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:34 2024
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

(cjnMgmt,) = mibBuilder.importSymbols(
    "Cajun-ROOT",
    "cjnMgmt")

(NetNumber,) = mibBuilder.importSymbols(
    "IPX-PRIVATE-MIB",
    "NetNumber")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cjnIpxIfMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CjnIpxIfGroup_ObjectIdentity = ObjectIdentity
cjnIpxIfGroup = _CjnIpxIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 2, 1)
)
_CjnIpxIfNextIndex_Type = Integer32
_CjnIpxIfNextIndex_Object = MibScalar
cjnIpxIfNextIndex = _CjnIpxIfNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 2, 1, 1),
    _CjnIpxIfNextIndex_Type()
)
cjnIpxIfNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxIfNextIndex.setStatus("current")
_CjnIpxIfNumber_Type = Integer32
_CjnIpxIfNumber_Object = MibScalar
cjnIpxIfNumber = _CjnIpxIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 2, 1, 2),
    _CjnIpxIfNumber_Type()
)
cjnIpxIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxIfNumber.setStatus("current")
_CjnIpxIfTable_Object = MibTable
cjnIpxIfTable = _CjnIpxIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cjnIpxIfTable.setStatus("current")
_CjnIpxIfEntry_Object = MibTableRow
cjnIpxIfEntry = _CjnIpxIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 2, 1, 3, 1)
)
cjnIpxIfEntry.setIndexNames(
    (0, "IPX-INTERFACE-MANAGEMENT-PRIVATE-MIB", "cjnIpxIfIndex"),
)
if mibBuilder.loadTexts:
    cjnIpxIfEntry.setStatus("current")
_CjnIpxIfIndex_Type = Integer32
_CjnIpxIfIndex_Object = MibTableColumn
cjnIpxIfIndex = _CjnIpxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 2, 1, 3, 1, 1),
    _CjnIpxIfIndex_Type()
)
cjnIpxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxIfIndex.setStatus("current")
_CjnIpxIfRowStatus_Type = RowStatus
_CjnIpxIfRowStatus_Object = MibTableColumn
cjnIpxIfRowStatus = _CjnIpxIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 2, 1, 3, 1, 2),
    _CjnIpxIfRowStatus_Type()
)
cjnIpxIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxIfRowStatus.setStatus("current")
_CjnIpxIfNetNumber_Type = NetNumber
_CjnIpxIfNetNumber_Object = MibTableColumn
cjnIpxIfNetNumber = _CjnIpxIfNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 2, 1, 3, 1, 3),
    _CjnIpxIfNetNumber_Type()
)
cjnIpxIfNetNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxIfNetNumber.setStatus("current")


class _CjnIpxIfEncapsType_Type(Integer32):
    """Custom type cjnIpxIfEncapsType based on Integer32"""
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
        *(("ethernet8022", 2),
          ("ethernet8023", 4),
          ("ethernetSNAP", 3),
          ("ethernetV2", 1))
    )


_CjnIpxIfEncapsType_Type.__name__ = "Integer32"
_CjnIpxIfEncapsType_Object = MibTableColumn
cjnIpxIfEncapsType = _CjnIpxIfEncapsType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 2, 1, 3, 1, 4),
    _CjnIpxIfEncapsType_Type()
)
cjnIpxIfEncapsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxIfEncapsType.setStatus("current")
_CjnIpxIfVlanIfIndex_Type = Integer32
_CjnIpxIfVlanIfIndex_Object = MibTableColumn
cjnIpxIfVlanIfIndex = _CjnIpxIfVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 2, 1, 3, 1, 5),
    _CjnIpxIfVlanIfIndex_Type()
)
cjnIpxIfVlanIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxIfVlanIfIndex.setStatus("current")


class _CjnIpxIfName_Type(DisplayString):
    """Custom type cjnIpxIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CjnIpxIfName_Type.__name__ = "DisplayString"
_CjnIpxIfName_Object = MibTableColumn
cjnIpxIfName = _CjnIpxIfName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 2, 1, 3, 1, 6),
    _CjnIpxIfName_Type()
)
cjnIpxIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxIfName.setStatus("current")


class _CjnIpxIfTicks_Type(Integer32):
    """Custom type cjnIpxIfTicks based on Integer32"""
    defaultValue = 1


_CjnIpxIfTicks_Object = MibTableColumn
cjnIpxIfTicks = _CjnIpxIfTicks_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 2, 1, 3, 1, 7),
    _CjnIpxIfTicks_Type()
)
cjnIpxIfTicks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxIfTicks.setStatus("current")


class _CjnIpxIfType20RbcastMode_Type(Integer32):
    """Custom type cjnIpxIfType20RbcastMode based on Integer32"""
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
        *(("both", 4),
          ("disabled", 1),
          ("inbound", 2),
          ("outbound", 3))
    )


_CjnIpxIfType20RbcastMode_Type.__name__ = "Integer32"
_CjnIpxIfType20RbcastMode_Object = MibTableColumn
cjnIpxIfType20RbcastMode = _CjnIpxIfType20RbcastMode_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 2, 1, 3, 1, 8),
    _CjnIpxIfType20RbcastMode_Type()
)
cjnIpxIfType20RbcastMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxIfType20RbcastMode.setStatus("current")


class _CjnIpxIfAdminStatus_Type(Integer32):
    """Custom type cjnIpxIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_CjnIpxIfAdminStatus_Type.__name__ = "Integer32"
_CjnIpxIfAdminStatus_Object = MibTableColumn
cjnIpxIfAdminStatus = _CjnIpxIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 2, 1, 3, 1, 9),
    _CjnIpxIfAdminStatus_Type()
)
cjnIpxIfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxIfAdminStatus.setStatus("current")


class _CjnIpxIfOperStatus_Type(Integer32):
    """Custom type cjnIpxIfOperStatus based on Integer32"""
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
          ("lowerLayerDown", 4),
          ("testing", 3),
          ("up", 1))
    )


_CjnIpxIfOperStatus_Type.__name__ = "Integer32"
_CjnIpxIfOperStatus_Object = MibTableColumn
cjnIpxIfOperStatus = _CjnIpxIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 2, 1, 3, 1, 10),
    _CjnIpxIfOperStatus_Type()
)
cjnIpxIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxIfOperStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPX-INTERFACE-MANAGEMENT-PRIVATE-MIB",
    **{"cjnIpxIfMgmt": cjnIpxIfMgmt,
       "cjnIpxIfGroup": cjnIpxIfGroup,
       "cjnIpxIfNextIndex": cjnIpxIfNextIndex,
       "cjnIpxIfNumber": cjnIpxIfNumber,
       "cjnIpxIfTable": cjnIpxIfTable,
       "cjnIpxIfEntry": cjnIpxIfEntry,
       "cjnIpxIfIndex": cjnIpxIfIndex,
       "cjnIpxIfRowStatus": cjnIpxIfRowStatus,
       "cjnIpxIfNetNumber": cjnIpxIfNetNumber,
       "cjnIpxIfEncapsType": cjnIpxIfEncapsType,
       "cjnIpxIfVlanIfIndex": cjnIpxIfVlanIfIndex,
       "cjnIpxIfName": cjnIpxIfName,
       "cjnIpxIfTicks": cjnIpxIfTicks,
       "cjnIpxIfType20RbcastMode": cjnIpxIfType20RbcastMode,
       "cjnIpxIfAdminStatus": cjnIpxIfAdminStatus,
       "cjnIpxIfOperStatus": cjnIpxIfOperStatus}
)
