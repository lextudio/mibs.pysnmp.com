# SNMP MIB module (ADTRAN-AOS-VRRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-AOS-VRRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:16 2024
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

(adGenAOSConformance,
 adGenAOSRouter) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSConformance",
    "adGenAOSRouter")

(adIdentity,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

adGenAOSVrrpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 2, 3)
)
adGenAOSVrrpMib.setRevisions(
        ("2014-07-29 00:00",
         "2014-04-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAOSVrrp_ObjectIdentity = ObjectIdentity
adGenAOSVrrp = _AdGenAOSVrrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3)
)
_AdGenAOSVrrpTrap_ObjectIdentity = ObjectIdentity
adGenAOSVrrpTrap = _AdGenAOSVrrpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 0)
)
_AdGenAOSVrrpTrapCntl_ObjectIdentity = ObjectIdentity
adGenAOSVrrpTrapCntl = _AdGenAOSVrrpTrapCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 1)
)


class _AdGenAOSVrrpMasterTrapCntl_Type(Integer32):
    """Custom type adGenAOSVrrpMasterTrapCntl based on Integer32"""
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


_AdGenAOSVrrpMasterTrapCntl_Type.__name__ = "Integer32"
_AdGenAOSVrrpMasterTrapCntl_Object = MibScalar
adGenAOSVrrpMasterTrapCntl = _AdGenAOSVrrpMasterTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 1, 1),
    _AdGenAOSVrrpMasterTrapCntl_Type()
)
adGenAOSVrrpMasterTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSVrrpMasterTrapCntl.setStatus("current")
_AdGenAOSVrrpTable_Object = MibTable
adGenAOSVrrpTable = _AdGenAOSVrrpTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2)
)
if mibBuilder.loadTexts:
    adGenAOSVrrpTable.setStatus("current")
_AdGenAOSVrrpEntry_Object = MibTableRow
adGenAOSVrrpEntry = _AdGenAOSVrrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2, 1)
)
adGenAOSVrrpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpVersion"),
    (0, "ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpId"),
    (0, "ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpInetAddrType"),
)
if mibBuilder.loadTexts:
    adGenAOSVrrpEntry.setStatus("current")


class _AdGenAOSVrrpVersion_Type(Integer32):
    """Custom type adGenAOSVrrpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v2", 2),
          ("v3", 3))
    )


_AdGenAOSVrrpVersion_Type.__name__ = "Integer32"
_AdGenAOSVrrpVersion_Object = MibTableColumn
adGenAOSVrrpVersion = _AdGenAOSVrrpVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2, 1, 1),
    _AdGenAOSVrrpVersion_Type()
)
adGenAOSVrrpVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenAOSVrrpVersion.setStatus("current")


class _AdGenAOSVrrpId_Type(Integer32):
    """Custom type adGenAOSVrrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenAOSVrrpId_Type.__name__ = "Integer32"
_AdGenAOSVrrpId_Object = MibTableColumn
adGenAOSVrrpId = _AdGenAOSVrrpId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2, 1, 2),
    _AdGenAOSVrrpId_Type()
)
adGenAOSVrrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenAOSVrrpId.setStatus("current")
_AdGenAOSVrrpInetAddrType_Type = InetAddressType
_AdGenAOSVrrpInetAddrType_Object = MibTableColumn
adGenAOSVrrpInetAddrType = _AdGenAOSVrrpInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2, 1, 3),
    _AdGenAOSVrrpInetAddrType_Type()
)
adGenAOSVrrpInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenAOSVrrpInetAddrType.setStatus("current")
_AdGenAOSVrrpInetAddr_Type = InetAddress
_AdGenAOSVrrpInetAddr_Object = MibTableColumn
adGenAOSVrrpInetAddr = _AdGenAOSVrrpInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2, 1, 4),
    _AdGenAOSVrrpInetAddr_Type()
)
adGenAOSVrrpInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSVrrpInetAddr.setStatus("current")


class _AdGenAOSVrrpOperStatus_Type(Integer32):
    """Custom type adGenAOSVrrpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("initialize", 1),
          ("master", 3))
    )


_AdGenAOSVrrpOperStatus_Type.__name__ = "Integer32"
_AdGenAOSVrrpOperStatus_Object = MibTableColumn
adGenAOSVrrpOperStatus = _AdGenAOSVrrpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2, 1, 5),
    _AdGenAOSVrrpOperStatus_Type()
)
adGenAOSVrrpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSVrrpOperStatus.setStatus("current")


class _AdGenAOSVrrpPriority_Type(Integer32):
    """Custom type adGenAOSVrrpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenAOSVrrpPriority_Type.__name__ = "Integer32"
_AdGenAOSVrrpPriority_Object = MibTableColumn
adGenAOSVrrpPriority = _AdGenAOSVrrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2, 1, 6),
    _AdGenAOSVrrpPriority_Type()
)
adGenAOSVrrpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSVrrpPriority.setStatus("current")
_AdGenAOSVrrpConformance_ObjectIdentity = ObjectIdentity
adGenAOSVrrpConformance = _AdGenAOSVrrpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20)
)
_AdGenAOSVrrpGroups_ObjectIdentity = ObjectIdentity
adGenAOSVrrpGroups = _AdGenAOSVrrpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 1)
)
_AdGenAOSVrrpCompliances_ObjectIdentity = ObjectIdentity
adGenAOSVrrpCompliances = _AdGenAOSVrrpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 2)
)

# Managed Objects groups

adGenAOSVrrpObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 1, 1)
)
adGenAOSVrrpObjectGroup.setObjects(
      *(("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpInetAddr"),
        ("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpPriority"))
)
if mibBuilder.loadTexts:
    adGenAOSVrrpObjectGroup.setStatus("current")

adGenAOSVrrpTrapCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 1, 2)
)
adGenAOSVrrpTrapCfgGroup.setObjects(
    ("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpMasterTrapCntl")
)
if mibBuilder.loadTexts:
    adGenAOSVrrpTrapCfgGroup.setStatus("current")

adGenAOSVrrpTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 1, 3)
)
adGenAOSVrrpTrapGroup.setObjects(
    ("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpOperStatus")
)
if mibBuilder.loadTexts:
    adGenAOSVrrpTrapGroup.setStatus("current")


# Notification objects

adGenAOSVrrpMasterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 0, 1)
)
adGenAOSVrrpMasterTrap.setObjects(
    ("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpOperStatus")
)
if mibBuilder.loadTexts:
    adGenAOSVrrpMasterTrap.setStatus(
        "current"
    )


# Notifications groups

adGenAOSVrrpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 1, 4)
)
adGenAOSVrrpNotificationGroup.setObjects(
    ("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpMasterTrap")
)
if mibBuilder.loadTexts:
    adGenAOSVrrpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

adGenAOSVrrpFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 2, 1)
)
if mibBuilder.loadTexts:
    adGenAOSVrrpFullCompliance.setStatus(
        "current"
    )

adGenAOSVrrpReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 2, 2)
)
if mibBuilder.loadTexts:
    adGenAOSVrrpReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS-VRRP-MIB",
    **{"adGenAOSVrrp": adGenAOSVrrp,
       "adGenAOSVrrpTrap": adGenAOSVrrpTrap,
       "adGenAOSVrrpMasterTrap": adGenAOSVrrpMasterTrap,
       "adGenAOSVrrpTrapCntl": adGenAOSVrrpTrapCntl,
       "adGenAOSVrrpMasterTrapCntl": adGenAOSVrrpMasterTrapCntl,
       "adGenAOSVrrpTable": adGenAOSVrrpTable,
       "adGenAOSVrrpEntry": adGenAOSVrrpEntry,
       "adGenAOSVrrpVersion": adGenAOSVrrpVersion,
       "adGenAOSVrrpId": adGenAOSVrrpId,
       "adGenAOSVrrpInetAddrType": adGenAOSVrrpInetAddrType,
       "adGenAOSVrrpInetAddr": adGenAOSVrrpInetAddr,
       "adGenAOSVrrpOperStatus": adGenAOSVrrpOperStatus,
       "adGenAOSVrrpPriority": adGenAOSVrrpPriority,
       "adGenAOSVrrpConformance": adGenAOSVrrpConformance,
       "adGenAOSVrrpGroups": adGenAOSVrrpGroups,
       "adGenAOSVrrpObjectGroup": adGenAOSVrrpObjectGroup,
       "adGenAOSVrrpTrapCfgGroup": adGenAOSVrrpTrapCfgGroup,
       "adGenAOSVrrpTrapGroup": adGenAOSVrrpTrapGroup,
       "adGenAOSVrrpNotificationGroup": adGenAOSVrrpNotificationGroup,
       "adGenAOSVrrpCompliances": adGenAOSVrrpCompliances,
       "adGenAOSVrrpFullCompliance": adGenAOSVrrpFullCompliance,
       "adGenAOSVrrpReadOnlyCompliance": adGenAOSVrrpReadOnlyCompliance,
       "adGenAOSVrrpMib": adGenAOSVrrpMib}
)
