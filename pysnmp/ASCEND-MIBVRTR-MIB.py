# SNMP MIB module (ASCEND-MIBVRTR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBVRTR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:34 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibvRouterProfile_ObjectIdentity = ObjectIdentity
mibvRouterProfile = _MibvRouterProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 139)
)
_MibvRouterProfileTable_Object = MibTable
mibvRouterProfileTable = _MibvRouterProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 1)
)
if mibBuilder.loadTexts:
    mibvRouterProfileTable.setStatus("mandatory")
_MibvRouterProfileEntry_Object = MibTableRow
mibvRouterProfileEntry = _MibvRouterProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 1, 1)
)
mibvRouterProfileEntry.setIndexNames(
    (0, "ASCEND-MIBVRTR-MIB", "vRouterProfile-Name"),
)
if mibBuilder.loadTexts:
    mibvRouterProfileEntry.setStatus("mandatory")
_VRouterProfile_Name_Type = DisplayString
_VRouterProfile_Name_Object = MibScalar
vRouterProfile_Name = _VRouterProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 1, 1, 1),
    _VRouterProfile_Name_Type()
)
vRouterProfile_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouterProfile_Name.setStatus("mandatory")


class _VRouterProfile_Active_Type(Integer32):
    """Custom type vRouterProfile_Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_VRouterProfile_Active_Type.__name__ = "Integer32"
_VRouterProfile_Active_Object = MibScalar
vRouterProfile_Active = _VRouterProfile_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 1, 1, 2),
    _VRouterProfile_Active_Type()
)
vRouterProfile_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouterProfile_Active.setStatus("mandatory")
_VRouterProfile_VrouterIpAddr_Type = IpAddress
_VRouterProfile_VrouterIpAddr_Object = MibScalar
vRouterProfile_VrouterIpAddr = _VRouterProfile_VrouterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 1, 1, 3),
    _VRouterProfile_VrouterIpAddr_Type()
)
vRouterProfile_VrouterIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouterProfile_VrouterIpAddr.setStatus("mandatory")


class _VRouterProfile_PoolSummary_Type(Integer32):
    """Custom type vRouterProfile_PoolSummary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_VRouterProfile_PoolSummary_Type.__name__ = "Integer32"
_VRouterProfile_PoolSummary_Object = MibScalar
vRouterProfile_PoolSummary = _VRouterProfile_PoolSummary_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 1, 1, 4),
    _VRouterProfile_PoolSummary_Type()
)
vRouterProfile_PoolSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouterProfile_PoolSummary.setStatus("mandatory")


class _VRouterProfile_RipPolicy_Type(Integer32):
    """Custom type vRouterProfile_RipPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("poisonRvrs", 2),
          ("splitHorzn", 1))
    )


_VRouterProfile_RipPolicy_Type.__name__ = "Integer32"
_VRouterProfile_RipPolicy_Object = MibScalar
vRouterProfile_RipPolicy = _VRouterProfile_RipPolicy_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 1, 1, 5),
    _VRouterProfile_RipPolicy_Type()
)
vRouterProfile_RipPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouterProfile_RipPolicy.setStatus("mandatory")


class _VRouterProfile_SummarizeRipRoutes_Type(Integer32):
    """Custom type vRouterProfile_SummarizeRipRoutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_VRouterProfile_SummarizeRipRoutes_Type.__name__ = "Integer32"
_VRouterProfile_SummarizeRipRoutes_Object = MibScalar
vRouterProfile_SummarizeRipRoutes = _VRouterProfile_SummarizeRipRoutes_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 1, 1, 6),
    _VRouterProfile_SummarizeRipRoutes_Type()
)
vRouterProfile_SummarizeRipRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouterProfile_SummarizeRipRoutes.setStatus("mandatory")


class _VRouterProfile_RipTrigger_Type(Integer32):
    """Custom type vRouterProfile_RipTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_VRouterProfile_RipTrigger_Type.__name__ = "Integer32"
_VRouterProfile_RipTrigger_Object = MibScalar
vRouterProfile_RipTrigger = _VRouterProfile_RipTrigger_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 1, 1, 7),
    _VRouterProfile_RipTrigger_Type()
)
vRouterProfile_RipTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouterProfile_RipTrigger.setStatus("mandatory")
_VRouterProfile_DomainName_Type = DisplayString
_VRouterProfile_DomainName_Object = MibScalar
vRouterProfile_DomainName = _VRouterProfile_DomainName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 1, 1, 8),
    _VRouterProfile_DomainName_Type()
)
vRouterProfile_DomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouterProfile_DomainName.setStatus("mandatory")
_VRouterProfile_SecDomainName_Type = DisplayString
_VRouterProfile_SecDomainName_Object = MibScalar
vRouterProfile_SecDomainName = _VRouterProfile_SecDomainName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 1, 1, 9),
    _VRouterProfile_SecDomainName_Type()
)
vRouterProfile_SecDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouterProfile_SecDomainName.setStatus("mandatory")
_VRouterProfile_DnsPrimaryServer_Type = IpAddress
_VRouterProfile_DnsPrimaryServer_Object = MibScalar
vRouterProfile_DnsPrimaryServer = _VRouterProfile_DnsPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 1, 1, 10),
    _VRouterProfile_DnsPrimaryServer_Type()
)
vRouterProfile_DnsPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouterProfile_DnsPrimaryServer.setStatus("mandatory")
_VRouterProfile_DnsSecondaryServer_Type = IpAddress
_VRouterProfile_DnsSecondaryServer_Object = MibScalar
vRouterProfile_DnsSecondaryServer = _VRouterProfile_DnsSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 1, 1, 11),
    _VRouterProfile_DnsSecondaryServer_Type()
)
vRouterProfile_DnsSecondaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouterProfile_DnsSecondaryServer.setStatus("mandatory")
_VRouterProfile_ClientPrimaryDnsServer_Type = IpAddress
_VRouterProfile_ClientPrimaryDnsServer_Object = MibScalar
vRouterProfile_ClientPrimaryDnsServer = _VRouterProfile_ClientPrimaryDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 1, 1, 12),
    _VRouterProfile_ClientPrimaryDnsServer_Type()
)
vRouterProfile_ClientPrimaryDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouterProfile_ClientPrimaryDnsServer.setStatus("mandatory")
_VRouterProfile_ClientSecondaryDnsServer_Type = IpAddress
_VRouterProfile_ClientSecondaryDnsServer_Object = MibScalar
vRouterProfile_ClientSecondaryDnsServer = _VRouterProfile_ClientSecondaryDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 1, 1, 13),
    _VRouterProfile_ClientSecondaryDnsServer_Type()
)
vRouterProfile_ClientSecondaryDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouterProfile_ClientSecondaryDnsServer.setStatus("mandatory")


class _VRouterProfile_AllowAsClientDnsInfo_Type(Integer32):
    """Custom type vRouterProfile_AllowAsClientDnsInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_VRouterProfile_AllowAsClientDnsInfo_Type.__name__ = "Integer32"
_VRouterProfile_AllowAsClientDnsInfo_Object = MibScalar
vRouterProfile_AllowAsClientDnsInfo = _VRouterProfile_AllowAsClientDnsInfo_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 1, 1, 14),
    _VRouterProfile_AllowAsClientDnsInfo_Type()
)
vRouterProfile_AllowAsClientDnsInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouterProfile_AllowAsClientDnsInfo.setStatus("mandatory")


class _VRouterProfile_IpxRoutingEnabled_Type(Integer32):
    """Custom type vRouterProfile_IpxRoutingEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_VRouterProfile_IpxRoutingEnabled_Type.__name__ = "Integer32"
_VRouterProfile_IpxRoutingEnabled_Object = MibScalar
vRouterProfile_IpxRoutingEnabled = _VRouterProfile_IpxRoutingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 1, 1, 15),
    _VRouterProfile_IpxRoutingEnabled_Type()
)
vRouterProfile_IpxRoutingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouterProfile_IpxRoutingEnabled.setStatus("mandatory")
_VRouterProfile_IpxDialinPool_Type = DisplayString
_VRouterProfile_IpxDialinPool_Object = MibScalar
vRouterProfile_IpxDialinPool = _VRouterProfile_IpxDialinPool_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 1, 1, 16),
    _VRouterProfile_IpxDialinPool_Type()
)
vRouterProfile_IpxDialinPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouterProfile_IpxDialinPool.setStatus("mandatory")


class _VRouterProfile_Action_o_Type(Integer32):
    """Custom type vRouterProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_VRouterProfile_Action_o_Type.__name__ = "Integer32"
_VRouterProfile_Action_o_Object = MibScalar
vRouterProfile_Action_o = _VRouterProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 1, 1, 17),
    _VRouterProfile_Action_o_Type()
)
vRouterProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouterProfile_Action_o.setStatus("mandatory")


class _VRouterProfile_ShareGlobalPool_Type(Integer32):
    """Custom type vRouterProfile_ShareGlobalPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_VRouterProfile_ShareGlobalPool_Type.__name__ = "Integer32"
_VRouterProfile_ShareGlobalPool_Object = MibScalar
vRouterProfile_ShareGlobalPool = _VRouterProfile_ShareGlobalPool_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 1, 1, 18),
    _VRouterProfile_ShareGlobalPool_Type()
)
vRouterProfile_ShareGlobalPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouterProfile_ShareGlobalPool.setStatus("mandatory")
_MibvRouterProfile_PoolNameTable_Object = MibTable
mibvRouterProfile_PoolNameTable = _MibvRouterProfile_PoolNameTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 2)
)
if mibBuilder.loadTexts:
    mibvRouterProfile_PoolNameTable.setStatus("mandatory")
_MibvRouterProfile_PoolNameEntry_Object = MibTableRow
mibvRouterProfile_PoolNameEntry = _MibvRouterProfile_PoolNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 2, 1)
)
mibvRouterProfile_PoolNameEntry.setIndexNames(
    (0, "ASCEND-MIBVRTR-MIB", "vRouterProfile-PoolName-Name"),
    (0, "ASCEND-MIBVRTR-MIB", "vRouterProfile-PoolName-Index-o"),
)
if mibBuilder.loadTexts:
    mibvRouterProfile_PoolNameEntry.setStatus("mandatory")
_VRouterProfile_PoolName_Name_Type = DisplayString
_VRouterProfile_PoolName_Name_Object = MibScalar
vRouterProfile_PoolName_Name = _VRouterProfile_PoolName_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 2, 1, 1),
    _VRouterProfile_PoolName_Name_Type()
)
vRouterProfile_PoolName_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouterProfile_PoolName_Name.setStatus("mandatory")
_VRouterProfile_PoolName_Index_o_Type = Integer32
_VRouterProfile_PoolName_Index_o_Object = MibScalar
vRouterProfile_PoolName_Index_o = _VRouterProfile_PoolName_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 2, 1, 2),
    _VRouterProfile_PoolName_Index_o_Type()
)
vRouterProfile_PoolName_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouterProfile_PoolName_Index_o.setStatus("mandatory")
_VRouterProfile_PoolName_Type = DisplayString
_VRouterProfile_PoolName_Object = MibScalar
vRouterProfile_PoolName = _VRouterProfile_PoolName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 2, 1, 3),
    _VRouterProfile_PoolName_Type()
)
vRouterProfile_PoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouterProfile_PoolName.setStatus("mandatory")
_MibvRouterProfile_AssignCountTable_Object = MibTable
mibvRouterProfile_AssignCountTable = _MibvRouterProfile_AssignCountTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 3)
)
if mibBuilder.loadTexts:
    mibvRouterProfile_AssignCountTable.setStatus("mandatory")
_MibvRouterProfile_AssignCountEntry_Object = MibTableRow
mibvRouterProfile_AssignCountEntry = _MibvRouterProfile_AssignCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 3, 1)
)
mibvRouterProfile_AssignCountEntry.setIndexNames(
    (0, "ASCEND-MIBVRTR-MIB", "vRouterProfile-AssignCount-Name"),
    (0, "ASCEND-MIBVRTR-MIB", "vRouterProfile-AssignCount-Index-o"),
)
if mibBuilder.loadTexts:
    mibvRouterProfile_AssignCountEntry.setStatus("mandatory")
_VRouterProfile_AssignCount_Name_Type = DisplayString
_VRouterProfile_AssignCount_Name_Object = MibScalar
vRouterProfile_AssignCount_Name = _VRouterProfile_AssignCount_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 3, 1, 1),
    _VRouterProfile_AssignCount_Name_Type()
)
vRouterProfile_AssignCount_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouterProfile_AssignCount_Name.setStatus("mandatory")
_VRouterProfile_AssignCount_Index_o_Type = Integer32
_VRouterProfile_AssignCount_Index_o_Object = MibScalar
vRouterProfile_AssignCount_Index_o = _VRouterProfile_AssignCount_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 3, 1, 2),
    _VRouterProfile_AssignCount_Index_o_Type()
)
vRouterProfile_AssignCount_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouterProfile_AssignCount_Index_o.setStatus("mandatory")
_VRouterProfile_AssignCount_Type = Integer32
_VRouterProfile_AssignCount_Object = MibScalar
vRouterProfile_AssignCount = _VRouterProfile_AssignCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 3, 1, 3),
    _VRouterProfile_AssignCount_Type()
)
vRouterProfile_AssignCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouterProfile_AssignCount.setStatus("mandatory")
_MibvRouterProfile_PoolBaseAddressTable_Object = MibTable
mibvRouterProfile_PoolBaseAddressTable = _MibvRouterProfile_PoolBaseAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 4)
)
if mibBuilder.loadTexts:
    mibvRouterProfile_PoolBaseAddressTable.setStatus("mandatory")
_MibvRouterProfile_PoolBaseAddressEntry_Object = MibTableRow
mibvRouterProfile_PoolBaseAddressEntry = _MibvRouterProfile_PoolBaseAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 4, 1)
)
mibvRouterProfile_PoolBaseAddressEntry.setIndexNames(
    (0, "ASCEND-MIBVRTR-MIB", "vRouterProfile-PoolBaseAddress-Name"),
    (0, "ASCEND-MIBVRTR-MIB", "vRouterProfile-PoolBaseAddress-Index-o"),
)
if mibBuilder.loadTexts:
    mibvRouterProfile_PoolBaseAddressEntry.setStatus("mandatory")
_VRouterProfile_PoolBaseAddress_Name_Type = DisplayString
_VRouterProfile_PoolBaseAddress_Name_Object = MibScalar
vRouterProfile_PoolBaseAddress_Name = _VRouterProfile_PoolBaseAddress_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 4, 1, 1),
    _VRouterProfile_PoolBaseAddress_Name_Type()
)
vRouterProfile_PoolBaseAddress_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouterProfile_PoolBaseAddress_Name.setStatus("mandatory")
_VRouterProfile_PoolBaseAddress_Index_o_Type = Integer32
_VRouterProfile_PoolBaseAddress_Index_o_Object = MibScalar
vRouterProfile_PoolBaseAddress_Index_o = _VRouterProfile_PoolBaseAddress_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 4, 1, 2),
    _VRouterProfile_PoolBaseAddress_Index_o_Type()
)
vRouterProfile_PoolBaseAddress_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouterProfile_PoolBaseAddress_Index_o.setStatus("mandatory")
_VRouterProfile_PoolBaseAddress_Type = IpAddress
_VRouterProfile_PoolBaseAddress_Object = MibScalar
vRouterProfile_PoolBaseAddress = _VRouterProfile_PoolBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 139, 4, 1, 3),
    _VRouterProfile_PoolBaseAddress_Type()
)
vRouterProfile_PoolBaseAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRouterProfile_PoolBaseAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBVRTR-MIB",
    **{"DisplayString": DisplayString,
       "mibvRouterProfile": mibvRouterProfile,
       "mibvRouterProfileTable": mibvRouterProfileTable,
       "mibvRouterProfileEntry": mibvRouterProfileEntry,
       "vRouterProfile-Name": vRouterProfile_Name,
       "vRouterProfile-Active": vRouterProfile_Active,
       "vRouterProfile-VrouterIpAddr": vRouterProfile_VrouterIpAddr,
       "vRouterProfile-PoolSummary": vRouterProfile_PoolSummary,
       "vRouterProfile-RipPolicy": vRouterProfile_RipPolicy,
       "vRouterProfile-SummarizeRipRoutes": vRouterProfile_SummarizeRipRoutes,
       "vRouterProfile-RipTrigger": vRouterProfile_RipTrigger,
       "vRouterProfile-DomainName": vRouterProfile_DomainName,
       "vRouterProfile-SecDomainName": vRouterProfile_SecDomainName,
       "vRouterProfile-DnsPrimaryServer": vRouterProfile_DnsPrimaryServer,
       "vRouterProfile-DnsSecondaryServer": vRouterProfile_DnsSecondaryServer,
       "vRouterProfile-ClientPrimaryDnsServer": vRouterProfile_ClientPrimaryDnsServer,
       "vRouterProfile-ClientSecondaryDnsServer": vRouterProfile_ClientSecondaryDnsServer,
       "vRouterProfile-AllowAsClientDnsInfo": vRouterProfile_AllowAsClientDnsInfo,
       "vRouterProfile-IpxRoutingEnabled": vRouterProfile_IpxRoutingEnabled,
       "vRouterProfile-IpxDialinPool": vRouterProfile_IpxDialinPool,
       "vRouterProfile-Action-o": vRouterProfile_Action_o,
       "vRouterProfile-ShareGlobalPool": vRouterProfile_ShareGlobalPool,
       "mibvRouterProfile-PoolNameTable": mibvRouterProfile_PoolNameTable,
       "mibvRouterProfile-PoolNameEntry": mibvRouterProfile_PoolNameEntry,
       "vRouterProfile-PoolName-Name": vRouterProfile_PoolName_Name,
       "vRouterProfile-PoolName-Index-o": vRouterProfile_PoolName_Index_o,
       "vRouterProfile-PoolName": vRouterProfile_PoolName,
       "mibvRouterProfile-AssignCountTable": mibvRouterProfile_AssignCountTable,
       "mibvRouterProfile-AssignCountEntry": mibvRouterProfile_AssignCountEntry,
       "vRouterProfile-AssignCount-Name": vRouterProfile_AssignCount_Name,
       "vRouterProfile-AssignCount-Index-o": vRouterProfile_AssignCount_Index_o,
       "vRouterProfile-AssignCount": vRouterProfile_AssignCount,
       "mibvRouterProfile-PoolBaseAddressTable": mibvRouterProfile_PoolBaseAddressTable,
       "mibvRouterProfile-PoolBaseAddressEntry": mibvRouterProfile_PoolBaseAddressEntry,
       "vRouterProfile-PoolBaseAddress-Name": vRouterProfile_PoolBaseAddress_Name,
       "vRouterProfile-PoolBaseAddress-Index-o": vRouterProfile_PoolBaseAddress_Index_o,
       "vRouterProfile-PoolBaseAddress": vRouterProfile_PoolBaseAddress}
)
