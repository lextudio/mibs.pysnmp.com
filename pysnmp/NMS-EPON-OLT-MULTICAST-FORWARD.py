# SNMP MIB module (NMS-EPON-OLT-MULTICAST-FORWARD) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-EPON-OLT-MULTICAST-FORWARD
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:43 2024
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

(nmsEPONGroup,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsEPONGroup")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmsEponOltMulticastForward_ObjectIdentity = ObjectIdentity
nmsEponOltMulticastForward = _NmsEponOltMulticastForward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 4)
)
_NmseponoltmulticastforwardTable_Object = MibTable
nmseponoltmulticastforwardTable = _NmseponoltmulticastforwardTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 4, 1)
)
if mibBuilder.loadTexts:
    nmseponoltmulticastforwardTable.setStatus("mandatory")
_NmsEponOltMulticastForwardEntry_Object = MibTableRow
nmsEponOltMulticastForwardEntry = _NmsEponOltMulticastForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 4, 1, 1)
)
nmsEponOltMulticastForwardEntry.setIndexNames(
    (0, "NMS-EPON-OLT-MULTICAST-FORWARD", "oltVlanId"),
    (0, "NMS-EPON-OLT-MULTICAST-FORWARD", "oltMcIpAddress"),
    (0, "NMS-EPON-OLT-MULTICAST-FORWARD", "oltLlidDiid"),
)
if mibBuilder.loadTexts:
    nmsEponOltMulticastForwardEntry.setStatus("mandatory")


class _OltVlanId_Type(Integer32):
    """Custom type oltVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_OltVlanId_Type.__name__ = "Integer32"
_OltVlanId_Object = MibTableColumn
oltVlanId = _OltVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 4, 1, 1, 1),
    _OltVlanId_Type()
)
oltVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltVlanId.setStatus("mandatory")
_OltMcIpAddress_Type = IpAddress
_OltMcIpAddress_Object = MibTableColumn
oltMcIpAddress = _OltMcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 4, 1, 1, 2),
    _OltMcIpAddress_Type()
)
oltMcIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltMcIpAddress.setStatus("mandatory")
_OltMcMacAddress_Type = MacAddress
_OltMcMacAddress_Object = MibTableColumn
oltMcMacAddress = _OltMcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 4, 1, 1, 3),
    _OltMcMacAddress_Type()
)
oltMcMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltMcMacAddress.setStatus("mandatory")


class _OltMcType_Type(Integer32):
    """Custom type oltMcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 0))
    )


_OltMcType_Type.__name__ = "Integer32"
_OltMcType_Object = MibTableColumn
oltMcType = _OltMcType_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 4, 1, 1, 4),
    _OltMcType_Type()
)
oltMcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltMcType.setStatus("mandatory")
_OltLlidDiid_Type = Integer32
_OltLlidDiid_Object = MibTableColumn
oltLlidDiid = _OltLlidDiid_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 4, 1, 1, 5),
    _OltLlidDiid_Type()
)
oltLlidDiid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltLlidDiid.setStatus("mandatory")
_OltExpiryTime_Type = TimeTicks
_OltExpiryTime_Object = MibTableColumn
oltExpiryTime = _OltExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 4, 1, 1, 6),
    _OltExpiryTime_Type()
)
oltExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltExpiryTime.setStatus("mandatory")
_OltForwardRowStatus_Type = RowStatus
_OltForwardRowStatus_Object = MibTableColumn
oltForwardRowStatus = _OltForwardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 4, 1, 1, 7),
    _OltForwardRowStatus_Type()
)
oltForwardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oltForwardRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-EPON-OLT-MULTICAST-FORWARD",
    **{"nmsEponOltMulticastForward": nmsEponOltMulticastForward,
       "nmseponoltmulticastforwardTable": nmseponoltmulticastforwardTable,
       "nmsEponOltMulticastForwardEntry": nmsEponOltMulticastForwardEntry,
       "oltVlanId": oltVlanId,
       "oltMcIpAddress": oltMcIpAddress,
       "oltMcMacAddress": oltMcMacAddress,
       "oltMcType": oltMcType,
       "oltLlidDiid": oltLlidDiid,
       "oltExpiryTime": oltExpiryTime,
       "oltForwardRowStatus": oltForwardRowStatus}
)
