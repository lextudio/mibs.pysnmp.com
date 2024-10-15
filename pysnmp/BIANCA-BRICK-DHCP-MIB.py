# SNMP MIB module (BIANCA-BRICK-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-DHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:23 2024
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


# MODULE-IDENTITY


# Types definitions



class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""




class Date(Integer32):
    """Custom type Date based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Biboip_ObjectIdentity = ObjectIdentity
biboip = _Biboip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 5)
)
_IpDhcpTable_Object = MibTable
ipDhcpTable = _IpDhcpTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 8)
)
if mibBuilder.loadTexts:
    ipDhcpTable.setStatus("mandatory")
_IpDhcpEntry_Object = MibTableRow
ipDhcpEntry = _IpDhcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 8, 1)
)
ipDhcpEntry.setIndexNames(
    (0, "BIANCA-BRICK-DHCP-MIB", "ipDhcpIfIndex"),
)
if mibBuilder.loadTexts:
    ipDhcpEntry.setStatus("mandatory")
_IpDhcpIfIndex_Type = Integer32
_IpDhcpIfIndex_Object = MibTableColumn
ipDhcpIfIndex = _IpDhcpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 8, 1, 1),
    _IpDhcpIfIndex_Type()
)
ipDhcpIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDhcpIfIndex.setStatus("mandatory")


class _IpDhcpState_Type(Integer32):
    """Custom type ipDhcpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("on", 1))
    )


_IpDhcpState_Type.__name__ = "Integer32"
_IpDhcpState_Object = MibTableColumn
ipDhcpState = _IpDhcpState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 8, 1, 2),
    _IpDhcpState_Type()
)
ipDhcpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDhcpState.setStatus("mandatory")
_IpDhcpFirst_Type = IpAddress
_IpDhcpFirst_Object = MibTableColumn
ipDhcpFirst = _IpDhcpFirst_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 8, 1, 3),
    _IpDhcpFirst_Type()
)
ipDhcpFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDhcpFirst.setStatus("mandatory")
_IpDhcpRange_Type = Integer32
_IpDhcpRange_Object = MibTableColumn
ipDhcpRange = _IpDhcpRange_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 8, 1, 4),
    _IpDhcpRange_Type()
)
ipDhcpRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDhcpRange.setStatus("mandatory")
_IpDhcpLease_Type = Integer32
_IpDhcpLease_Object = MibTableColumn
ipDhcpLease = _IpDhcpLease_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 8, 1, 5),
    _IpDhcpLease_Type()
)
ipDhcpLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDhcpLease.setStatus("mandatory")
_IpDhcpPhys_Type = PhysAddress
_IpDhcpPhys_Object = MibTableColumn
ipDhcpPhys = _IpDhcpPhys_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 8, 1, 6),
    _IpDhcpPhys_Type()
)
ipDhcpPhys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDhcpPhys.setStatus("mandatory")


class _IpDhcpNodeType_Type(Integer32):
    """Custom type ipDhcpNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bnode", 2),
          ("hnode", 5),
          ("mnode", 4),
          ("none", 1),
          ("pnode", 3))
    )


_IpDhcpNodeType_Type.__name__ = "Integer32"
_IpDhcpNodeType_Object = MibTableColumn
ipDhcpNodeType = _IpDhcpNodeType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 8, 1, 7),
    _IpDhcpNodeType_Type()
)
ipDhcpNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDhcpNodeType.setStatus("mandatory")
_IpDhcpGateway_Type = IpAddress
_IpDhcpGateway_Object = MibTableColumn
ipDhcpGateway = _IpDhcpGateway_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 8, 1, 8),
    _IpDhcpGateway_Type()
)
ipDhcpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDhcpGateway.setStatus("mandatory")
_IpDhcpInUseTable_Object = MibTable
ipDhcpInUseTable = _IpDhcpInUseTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 9)
)
if mibBuilder.loadTexts:
    ipDhcpInUseTable.setStatus("mandatory")
_IpDhcpInUseEntry_Object = MibTableRow
ipDhcpInUseEntry = _IpDhcpInUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 9, 1)
)
ipDhcpInUseEntry.setIndexNames(
    (0, "BIANCA-BRICK-DHCP-MIB", "ipDhcpInUseAddress"),
)
if mibBuilder.loadTexts:
    ipDhcpInUseEntry.setStatus("mandatory")
_IpDhcpInUseAddress_Type = IpAddress
_IpDhcpInUseAddress_Object = MibTableColumn
ipDhcpInUseAddress = _IpDhcpInUseAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 9, 1, 1),
    _IpDhcpInUseAddress_Type()
)
ipDhcpInUseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDhcpInUseAddress.setStatus("mandatory")
_IpDhcpInUsePhys_Type = PhysAddress
_IpDhcpInUsePhys_Object = MibTableColumn
ipDhcpInUsePhys = _IpDhcpInUsePhys_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 9, 1, 2),
    _IpDhcpInUsePhys_Type()
)
ipDhcpInUsePhys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDhcpInUsePhys.setStatus("mandatory")
_IpDhcpInUseExpires_Type = Date
_IpDhcpInUseExpires_Object = MibTableColumn
ipDhcpInUseExpires = _IpDhcpInUseExpires_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 9, 1, 3),
    _IpDhcpInUseExpires_Type()
)
ipDhcpInUseExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDhcpInUseExpires.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-DHCP-MIB",
    **{"PhysAddress": PhysAddress,
       "Date": Date,
       "org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "biboip": biboip,
       "ipDhcpTable": ipDhcpTable,
       "ipDhcpEntry": ipDhcpEntry,
       "ipDhcpIfIndex": ipDhcpIfIndex,
       "ipDhcpState": ipDhcpState,
       "ipDhcpFirst": ipDhcpFirst,
       "ipDhcpRange": ipDhcpRange,
       "ipDhcpLease": ipDhcpLease,
       "ipDhcpPhys": ipDhcpPhys,
       "ipDhcpNodeType": ipDhcpNodeType,
       "ipDhcpGateway": ipDhcpGateway,
       "ipDhcpInUseTable": ipDhcpInUseTable,
       "ipDhcpInUseEntry": ipDhcpInUseEntry,
       "ipDhcpInUseAddress": ipDhcpInUseAddress,
       "ipDhcpInUsePhys": ipDhcpInUsePhys,
       "ipDhcpInUseExpires": ipDhcpInUseExpires}
)
