# SNMP MIB module (RMONitor-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RMONitor-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:06 2024
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



class OwnerString(DisplayString):
    """Custom type OwnerString based on DisplayString"""




class EntryStatus(Integer32):
    """Custom type EntryStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mib_2_ObjectIdentity = ObjectIdentity
mib_2 = _Mib_2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1)
)
_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_Rmonitor_ObjectIdentity = ObjectIdentity
rmonitor = _Rmonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 45)
)
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 1)
)
_AuthTable_Object = MibTable
authTable = _AuthTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 1, 1)
)
if mibBuilder.loadTexts:
    authTable.setStatus("mandatory")
_AuthEntry_Object = MibTableRow
authEntry = _AuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 1, 1, 1)
)
authEntry.setIndexNames(
    (0, "RMONitor-MIB", "authCommunity"),
)
if mibBuilder.loadTexts:
    authEntry.setStatus("mandatory")
_AuthCommunity_Type = OctetString
_AuthCommunity_Object = MibTableColumn
authCommunity = _AuthCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 1, 1, 1, 1),
    _AuthCommunity_Type()
)
authCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authCommunity.setStatus("mandatory")


class _AuthTypeAccess_Type(Integer32):
    """Custom type authTypeAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("monitor", 2),
          ("not-applicable", 3),
          ("primary", 4))
    )


_AuthTypeAccess_Type.__name__ = "Integer32"
_AuthTypeAccess_Object = MibTableColumn
authTypeAccess = _AuthTypeAccess_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 1, 1, 1, 2),
    _AuthTypeAccess_Type()
)
authTypeAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authTypeAccess.setStatus("mandatory")


class _AuthActions_Type(Integer32):
    """Custom type authActions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("delete", 3),
          ("not-applicable", 1))
    )


_AuthActions_Type.__name__ = "Integer32"
_AuthActions_Object = MibTableColumn
authActions = _AuthActions_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 1, 1, 1, 3),
    _AuthActions_Type()
)
authActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authActions.setStatus("mandatory")
_SubscriptTable_Object = MibTable
subscriptTable = _SubscriptTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 1, 2)
)
if mibBuilder.loadTexts:
    subscriptTable.setStatus("mandatory")
_SubscriptEntry_Object = MibTableRow
subscriptEntry = _SubscriptEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 1, 2, 1)
)
subscriptEntry.setIndexNames(
    (0, "RMONitor-MIB", "subscriptIpAddress"),
)
if mibBuilder.loadTexts:
    subscriptEntry.setStatus("mandatory")
_SubscriptIpAddress_Type = IpAddress
_SubscriptIpAddress_Object = MibTableColumn
subscriptIpAddress = _SubscriptIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 1, 2, 1, 1),
    _SubscriptIpAddress_Type()
)
subscriptIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriptIpAddress.setStatus("mandatory")
_SubscriptCommunity_Type = DisplayString
_SubscriptCommunity_Object = MibTableColumn
subscriptCommunity = _SubscriptCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 1, 2, 1, 2),
    _SubscriptCommunity_Type()
)
subscriptCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriptCommunity.setStatus("mandatory")


class _SubscriptActions_Type(Integer32):
    """Custom type subscriptActions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("delete", 3),
          ("not-applicable", 1))
    )


_SubscriptActions_Type.__name__ = "Integer32"
_SubscriptActions_Object = MibTableColumn
subscriptActions = _SubscriptActions_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 1, 2, 1, 3),
    _SubscriptActions_Type()
)
subscriptActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriptActions.setStatus("mandatory")
_AuthFailTable_Object = MibTable
authFailTable = _AuthFailTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 1, 3)
)
if mibBuilder.loadTexts:
    authFailTable.setStatus("mandatory")
_AuthFailEntry_Object = MibTableRow
authFailEntry = _AuthFailEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 1, 3, 1)
)
authFailEntry.setIndexNames(
    (0, "RMONitor-MIB", "authFailIndex"),
)
if mibBuilder.loadTexts:
    authFailEntry.setStatus("mandatory")
_AuthFailIndex_Type = Integer32
_AuthFailIndex_Object = MibTableColumn
authFailIndex = _AuthFailIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 1, 3, 1, 1),
    _AuthFailIndex_Type()
)
authFailIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authFailIndex.setStatus("mandatory")
_AuthFailIPAddress_Type = IpAddress
_AuthFailIPAddress_Object = MibTableColumn
authFailIPAddress = _AuthFailIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 1, 3, 1, 2),
    _AuthFailIPAddress_Type()
)
authFailIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authFailIPAddress.setStatus("mandatory")
_AuthFailCommunity_Type = DisplayString
_AuthFailCommunity_Object = MibTableColumn
authFailCommunity = _AuthFailCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 1, 3, 1, 3),
    _AuthFailCommunity_Type()
)
authFailCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authFailCommunity.setStatus("mandatory")
_Protocols_ObjectIdentity = ObjectIdentity
protocols = _Protocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 2)
)
_ProtocolDistControlTable_Object = MibTable
protocolDistControlTable = _ProtocolDistControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 2, 1)
)
if mibBuilder.loadTexts:
    protocolDistControlTable.setStatus("mandatory")
_ProtocolDistControlEntry_Object = MibTableRow
protocolDistControlEntry = _ProtocolDistControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 2, 1, 1)
)
protocolDistControlEntry.setIndexNames(
    (0, "RMONitor-MIB", "protocolDistControlIndex"),
)
if mibBuilder.loadTexts:
    protocolDistControlEntry.setStatus("mandatory")
_ProtocolDistControlIndex_Type = Integer32
_ProtocolDistControlIndex_Object = MibTableColumn
protocolDistControlIndex = _ProtocolDistControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 2, 1, 1, 1),
    _ProtocolDistControlIndex_Type()
)
protocolDistControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolDistControlIndex.setStatus("mandatory")
_ProtocolDistControlDataSource_Type = ObjectIdentifier
_ProtocolDistControlDataSource_Object = MibTableColumn
protocolDistControlDataSource = _ProtocolDistControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 2, 1, 1, 2),
    _ProtocolDistControlDataSource_Type()
)
protocolDistControlDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolDistControlDataSource.setStatus("mandatory")
_ProtocolDistControlLastDeleteTime_Type = TimeTicks
_ProtocolDistControlLastDeleteTime_Object = MibTableColumn
protocolDistControlLastDeleteTime = _ProtocolDistControlLastDeleteTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 2, 1, 1, 3),
    _ProtocolDistControlLastDeleteTime_Type()
)
protocolDistControlLastDeleteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolDistControlLastDeleteTime.setStatus("mandatory")
_ProtocolDistControlOwner_Type = OwnerString
_ProtocolDistControlOwner_Object = MibTableColumn
protocolDistControlOwner = _ProtocolDistControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 2, 1, 1, 4),
    _ProtocolDistControlOwner_Type()
)
protocolDistControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolDistControlOwner.setStatus("mandatory")
_ProtocolDistControlStatus_Type = EntryStatus
_ProtocolDistControlStatus_Object = MibTableColumn
protocolDistControlStatus = _ProtocolDistControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 2, 1, 1, 5),
    _ProtocolDistControlStatus_Type()
)
protocolDistControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolDistControlStatus.setStatus("mandatory")
_ProtocolDistTable_Object = MibTable
protocolDistTable = _ProtocolDistTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 2, 2)
)
if mibBuilder.loadTexts:
    protocolDistTable.setStatus("mandatory")
_ProtocolDistEntry_Object = MibTableRow
protocolDistEntry = _ProtocolDistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 2, 2, 1)
)
protocolDistEntry.setIndexNames(
    (0, "RMONitor-MIB", "protocolDistIndex"),
    (0, "RMONitor-MIB", "protocolDistEthertype"),
)
if mibBuilder.loadTexts:
    protocolDistEntry.setStatus("mandatory")
_ProtocolDistIndex_Type = Integer32
_ProtocolDistIndex_Object = MibTableColumn
protocolDistIndex = _ProtocolDistIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 2, 2, 1, 1),
    _ProtocolDistIndex_Type()
)
protocolDistIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolDistIndex.setStatus("mandatory")


class _ProtocolDistEthertype_Type(OctetString):
    """Custom type protocolDistEthertype based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ProtocolDistEthertype_Type.__name__ = "OctetString"
_ProtocolDistEthertype_Object = MibTableColumn
protocolDistEthertype = _ProtocolDistEthertype_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 2, 2, 1, 2),
    _ProtocolDistEthertype_Type()
)
protocolDistEthertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolDistEthertype.setStatus("mandatory")
_ProtocolDistPkts_Type = Counter32
_ProtocolDistPkts_Object = MibTableColumn
protocolDistPkts = _ProtocolDistPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 2, 2, 1, 3),
    _ProtocolDistPkts_Type()
)
protocolDistPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolDistPkts.setStatus("mandatory")
_ProtocolDistOctets_Type = Counter32
_ProtocolDistOctets_Object = MibTableColumn
protocolDistOctets = _ProtocolDistOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 45, 2, 2, 1, 4),
    _ProtocolDistOctets_Type()
)
protocolDistOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolDistOctets.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RMONitor-MIB",
    **{"OwnerString": OwnerString,
       "EntryStatus": EntryStatus,
       "mib-2": mib_2,
       "ibm": ibm,
       "ibmProd": ibmProd,
       "rmonitor": rmonitor,
       "security": security,
       "authTable": authTable,
       "authEntry": authEntry,
       "authCommunity": authCommunity,
       "authTypeAccess": authTypeAccess,
       "authActions": authActions,
       "subscriptTable": subscriptTable,
       "subscriptEntry": subscriptEntry,
       "subscriptIpAddress": subscriptIpAddress,
       "subscriptCommunity": subscriptCommunity,
       "subscriptActions": subscriptActions,
       "authFailTable": authFailTable,
       "authFailEntry": authFailEntry,
       "authFailIndex": authFailIndex,
       "authFailIPAddress": authFailIPAddress,
       "authFailCommunity": authFailCommunity,
       "protocols": protocols,
       "protocolDistControlTable": protocolDistControlTable,
       "protocolDistControlEntry": protocolDistControlEntry,
       "protocolDistControlIndex": protocolDistControlIndex,
       "protocolDistControlDataSource": protocolDistControlDataSource,
       "protocolDistControlLastDeleteTime": protocolDistControlLastDeleteTime,
       "protocolDistControlOwner": protocolDistControlOwner,
       "protocolDistControlStatus": protocolDistControlStatus,
       "protocolDistTable": protocolDistTable,
       "protocolDistEntry": protocolDistEntry,
       "protocolDistIndex": protocolDistIndex,
       "protocolDistEthertype": protocolDistEthertype,
       "protocolDistPkts": protocolDistPkts,
       "protocolDistOctets": protocolDistOctets}
)
