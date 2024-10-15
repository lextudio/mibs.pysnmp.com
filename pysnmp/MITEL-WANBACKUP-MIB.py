# SNMP MIB module (MITEL-WANBACKUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MITEL-WANBACKUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:31 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

mitelIpGrpBackupWANGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6)
)
mitelIpGrpBackupWANGroup.setRevisions(
        ("2003-03-24 11:03",
         "1999-03-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mitel_ObjectIdentity = ObjectIdentity
mitel = _Mitel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027)
)
_MitelProprietary_ObjectIdentity = ObjectIdentity
mitelProprietary = _MitelProprietary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4)
)
_MitelPropIpNetworking_ObjectIdentity = ObjectIdentity
mitelPropIpNetworking = _MitelPropIpNetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8)
)
_MitelIpNetRouter_ObjectIdentity = ObjectIdentity
mitelIpNetRouter = _MitelIpNetRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1)
)
_MitelRouterIpGroup_ObjectIdentity = ObjectIdentity
mitelRouterIpGroup = _MitelRouterIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1)
)
_MitelBackupWANDestIndex_Type = Integer32
_MitelBackupWANDestIndex_Object = MibScalar
mitelBackupWANDestIndex = _MitelBackupWANDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6, 1),
    _MitelBackupWANDestIndex_Type()
)
mitelBackupWANDestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBackupWANDestIndex.setStatus("current")


class _MitelBackupWANEnable_Type(Integer32):
    """Custom type mitelBackupWANEnable based on Integer32"""
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


_MitelBackupWANEnable_Type.__name__ = "Integer32"
_MitelBackupWANEnable_Object = MibScalar
mitelBackupWANEnable = _MitelBackupWANEnable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6, 2),
    _MitelBackupWANEnable_Type()
)
mitelBackupWANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelBackupWANEnable.setStatus("current")


class _MitelBackupWANPollFreq_Type(Integer32):
    """Custom type mitelBackupWANPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_MitelBackupWANPollFreq_Type.__name__ = "Integer32"
_MitelBackupWANPollFreq_Object = MibScalar
mitelBackupWANPollFreq = _MitelBackupWANPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6, 3),
    _MitelBackupWANPollFreq_Type()
)
mitelBackupWANPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelBackupWANPollFreq.setStatus("current")


class _MitelBackupWANLinkStatus_Type(Integer32):
    """Custom type mitelBackupWANLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("down", 2))
    )


_MitelBackupWANLinkStatus_Type.__name__ = "Integer32"
_MitelBackupWANLinkStatus_Object = MibScalar
mitelBackupWANLinkStatus = _MitelBackupWANLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6, 4),
    _MitelBackupWANLinkStatus_Type()
)
mitelBackupWANLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBackupWANLinkStatus.setStatus("current")
_MitelBackupWANServerTable_Object = MibTable
mitelBackupWANServerTable = _MitelBackupWANServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6, 5)
)
if mibBuilder.loadTexts:
    mitelBackupWANServerTable.setStatus("current")
_MitelBackupWANServerEntry_Object = MibTableRow
mitelBackupWANServerEntry = _MitelBackupWANServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6, 5, 1)
)
mitelBackupWANServerEntry.setIndexNames(
    (0, "MITEL-WANBACKUP-MIB", "mitelBackupWANServerIPAddr"),
)
if mibBuilder.loadTexts:
    mitelBackupWANServerEntry.setStatus("current")
_MitelBackupWANServerIPAddr_Type = IpAddress
_MitelBackupWANServerIPAddr_Object = MibTableColumn
mitelBackupWANServerIPAddr = _MitelBackupWANServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6, 5, 1, 1),
    _MitelBackupWANServerIPAddr_Type()
)
mitelBackupWANServerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelBackupWANServerIPAddr.setStatus("current")
_MitelBackupWANServerSubnetAddr_Type = IpAddress
_MitelBackupWANServerSubnetAddr_Object = MibTableColumn
mitelBackupWANServerSubnetAddr = _MitelBackupWANServerSubnetAddr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6, 5, 1, 2),
    _MitelBackupWANServerSubnetAddr_Type()
)
mitelBackupWANServerSubnetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelBackupWANServerSubnetAddr.setStatus("current")


class _MitelBackupWANServerPrimary_Type(Integer32):
    """Custom type mitelBackupWANServerPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_MitelBackupWANServerPrimary_Type.__name__ = "Integer32"
_MitelBackupWANServerPrimary_Object = MibTableColumn
mitelBackupWANServerPrimary = _MitelBackupWANServerPrimary_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6, 5, 1, 3),
    _MitelBackupWANServerPrimary_Type()
)
mitelBackupWANServerPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelBackupWANServerPrimary.setStatus("current")
_MitelBackupWANServerStatus_Type = RowStatus
_MitelBackupWANServerStatus_Object = MibTableColumn
mitelBackupWANServerStatus = _MitelBackupWANServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6, 5, 1, 4),
    _MitelBackupWANServerStatus_Type()
)
mitelBackupWANServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mitelBackupWANServerStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-WANBACKUP-MIB",
    **{"mitel": mitel,
       "mitelProprietary": mitelProprietary,
       "mitelPropIpNetworking": mitelPropIpNetworking,
       "mitelIpNetRouter": mitelIpNetRouter,
       "mitelRouterIpGroup": mitelRouterIpGroup,
       "mitelIpGrpBackupWANGroup": mitelIpGrpBackupWANGroup,
       "mitelBackupWANDestIndex": mitelBackupWANDestIndex,
       "mitelBackupWANEnable": mitelBackupWANEnable,
       "mitelBackupWANPollFreq": mitelBackupWANPollFreq,
       "mitelBackupWANLinkStatus": mitelBackupWANLinkStatus,
       "mitelBackupWANServerTable": mitelBackupWANServerTable,
       "mitelBackupWANServerEntry": mitelBackupWANServerEntry,
       "mitelBackupWANServerIPAddr": mitelBackupWANServerIPAddr,
       "mitelBackupWANServerSubnetAddr": mitelBackupWANServerSubnetAddr,
       "mitelBackupWANServerPrimary": mitelBackupWANServerPrimary,
       "mitelBackupWANServerStatus": mitelBackupWANServerStatus}
)
