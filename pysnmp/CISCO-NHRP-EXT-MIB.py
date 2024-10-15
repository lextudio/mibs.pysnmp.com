# SNMP MIB module (CISCO-NHRP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-NHRP-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:13 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

(nhrpCacheNbmaAddr,
 nhrpCacheNbmaAddrType,
 nhrpCacheNbmaSubaddr,
 nhrpCacheNextHopInternetworkAddr,
 nhrpCacheType,
 nhrpClientHoldTime,
 nhrpClientIndex,
 nhrpClientInternetworkAddr,
 nhrpClientInternetworkAddrType,
 nhrpClientNbmaAddr,
 nhrpClientNbmaAddrType,
 nhrpClientNbmaSubaddr,
 nhrpClientNhsInUse,
 nhrpClientNhsInternetworkAddr,
 nhrpClientNhsInternetworkAddrType,
 nhrpClientNhsNbmaAddr,
 nhrpClientNhsNbmaAddrType,
 nhrpClientNhsNbmaSubaddr,
 nhrpClientRegUniqueness,
 nhrpClientStatEntry,
 nhrpServerCacheUniqueness,
 nhrpServerIndex,
 nhrpServerInternetworkAddr,
 nhrpServerInternetworkAddrType,
 nhrpServerNbmaAddr,
 nhrpServerNbmaAddrType,
 nhrpServerNbmaSubaddr,
 nhrpServerNhcInUse,
 nhrpServerNhcInternetworkAddr,
 nhrpServerNhcInternetworkAddrType,
 nhrpServerNhcNbmaAddr,
 nhrpServerNhcNbmaAddrType,
 nhrpServerNhcNbmaSubaddr,
 nhrpServerNhcPrefixLength,
 nhrpServerStatEntry) = mibBuilder.importSymbols(
    "NHRP-MIB",
    "nhrpCacheNbmaAddr",
    "nhrpCacheNbmaAddrType",
    "nhrpCacheNbmaSubaddr",
    "nhrpCacheNextHopInternetworkAddr",
    "nhrpCacheType",
    "nhrpClientHoldTime",
    "nhrpClientIndex",
    "nhrpClientInternetworkAddr",
    "nhrpClientInternetworkAddrType",
    "nhrpClientNbmaAddr",
    "nhrpClientNbmaAddrType",
    "nhrpClientNbmaSubaddr",
    "nhrpClientNhsInUse",
    "nhrpClientNhsInternetworkAddr",
    "nhrpClientNhsInternetworkAddrType",
    "nhrpClientNhsNbmaAddr",
    "nhrpClientNhsNbmaAddrType",
    "nhrpClientNhsNbmaSubaddr",
    "nhrpClientRegUniqueness",
    "nhrpClientStatEntry",
    "nhrpServerCacheUniqueness",
    "nhrpServerIndex",
    "nhrpServerInternetworkAddr",
    "nhrpServerInternetworkAddrType",
    "nhrpServerNbmaAddr",
    "nhrpServerNbmaAddrType",
    "nhrpServerNbmaSubaddr",
    "nhrpServerNhcInUse",
    "nhrpServerNhcInternetworkAddr",
    "nhrpServerNhcInternetworkAddrType",
    "nhrpServerNhcNbmaAddr",
    "nhrpServerNhcNbmaAddrType",
    "nhrpServerNhcNbmaSubaddr",
    "nhrpServerNhcPrefixLength",
    "nhrpServerStatEntry")

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

ciscoNhrpExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 680)
)
ciscoNhrpExtMIB.setRevisions(
        ("2008-11-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoNhrpErrorCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              256)
        )
    )
    namedValues = NamedValues(
        *(("addressUnreachable", 6),
          ("adminProhibited", 4),
          ("authFailure", 11),
          ("bindingNotUnique", 13),
          ("hopCountExceeded", 15),
          ("insufficientResources", 5),
          ("invalidExtension", 9),
          ("invalidResReply", 10),
          ("loopDetected", 3),
          ("noAddressBinding", 12),
          ("other", 256),
          ("protocolError", 7),
          ("sduSizeExceeded", 8),
          ("uniqueInternetworkAddrRegd", 14),
          ("unrecogExtension", 1))
    )



class CiscoNextHopDownReasonCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("administrative", 1),
          ("external", 6),
          ("normalExpiry", 5),
          ("other", 7),
          ("purgeReceived", 4),
          ("registrationFailure", 2),
          ("resolutionFailure", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CneNotifs_ObjectIdentity = ObjectIdentity
cneNotifs = _CneNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 0)
)
_CneObjects_ObjectIdentity = ObjectIdentity
cneObjects = _CneObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 1)
)
_CneGeneralObjects_ObjectIdentity = ObjectIdentity
cneGeneralObjects = _CneGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 1)
)
_CneNextHopDownReason_Type = CiscoNextHopDownReasonCode
_CneNextHopDownReason_Object = MibScalar
cneNextHopDownReason = _CneNextHopDownReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 1, 1),
    _CneNextHopDownReason_Type()
)
cneNextHopDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cneNextHopDownReason.setStatus("current")
_CneNHRPException_Type = CiscoNhrpErrorCode
_CneNHRPException_Object = MibScalar
cneNHRPException = _CneNHRPException_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 1, 2),
    _CneNHRPException_Type()
)
cneNHRPException.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cneNHRPException.setStatus("current")
_CneClientObjects_ObjectIdentity = ObjectIdentity
cneClientObjects = _CneClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 2)
)
_CneClientStatExtTable_Object = MibTable
cneClientStatExtTable = _CneClientStatExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cneClientStatExtTable.setStatus("current")
_CneClientStatExtEntry_Object = MibTableRow
cneClientStatExtEntry = _CneClientStatExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cneClientStatExtEntry.setStatus("current")
_CneClientStatRedirectRx_Type = Counter32
_CneClientStatRedirectRx_Object = MibTableColumn
cneClientStatRedirectRx = _CneClientStatRedirectRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 2, 1, 1, 1),
    _CneClientStatRedirectRx_Type()
)
cneClientStatRedirectRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cneClientStatRedirectRx.setStatus("current")
_CneServerObjects_ObjectIdentity = ObjectIdentity
cneServerObjects = _CneServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 3)
)
_CneServerStatExtTable_Object = MibTable
cneServerStatExtTable = _CneServerStatExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cneServerStatExtTable.setStatus("current")
_CneServerStatExtEntry_Object = MibTableRow
cneServerStatExtEntry = _CneServerStatExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cneServerStatExtEntry.setStatus("current")
_CneServerStatRedirectTx_Type = Counter32
_CneServerStatRedirectTx_Object = MibTableColumn
cneServerStatRedirectTx = _CneServerStatRedirectTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 3, 1, 1, 1),
    _CneServerStatRedirectTx_Type()
)
cneServerStatRedirectTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cneServerStatRedirectTx.setStatus("current")
_CneNotificationControlObjects_ObjectIdentity = ObjectIdentity
cneNotificationControlObjects = _CneNotificationControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 4)
)


class _CneNotifEnable_Type(Bits):
    """Custom type cneNotifEnable based on Bits"""
    defaultBinValue = "1111001"

    namedValues = NamedValues(
        *(("nextHopPeerDown", 5),
          ("nextHopPeerUp", 4),
          ("nextHopRegClientDown", 3),
          ("nextHopRegClientUp", 2),
          ("nextHopRegServerDown", 1),
          ("nextHopRegServerUp", 0),
          ("rateLimitExceeded", 6))
    )

_CneNotifEnable_Type.__name__ = "Bits"
_CneNotifEnable_Object = MibScalar
cneNotifEnable = _CneNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 4, 1),
    _CneNotifEnable_Type()
)
cneNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cneNotifEnable.setStatus("current")
_CneConform_ObjectIdentity = ObjectIdentity
cneConform = _CneConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 2)
)
_CneCompliances_ObjectIdentity = ObjectIdentity
cneCompliances = _CneCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 1)
)
_CneGroups_ObjectIdentity = ObjectIdentity
cneGroups = _CneGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2)
)
nhrpClientStatEntry.registerAugmentions(
    ("CISCO-NHRP-EXT-MIB",
     "cneClientStatExtEntry")
)
cneClientStatExtEntry.setIndexNames(*nhrpClientStatEntry.getIndexNames())
nhrpServerStatEntry.registerAugmentions(
    ("CISCO-NHRP-EXT-MIB",
     "cneServerStatExtEntry")
)
cneServerStatExtEntry.setIndexNames(*nhrpServerStatEntry.getIndexNames())

# Managed Objects groups

cneGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2, 1)
)
cneGeneralGroup.setObjects(
      *(("CISCO-NHRP-EXT-MIB", "cneNHRPException"),
        ("CISCO-NHRP-EXT-MIB", "cneNextHopDownReason"))
)
if mibBuilder.loadTexts:
    cneGeneralGroup.setStatus("current")

cneClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2, 2)
)
cneClientGroup.setObjects(
    ("CISCO-NHRP-EXT-MIB", "cneClientStatRedirectRx")
)
if mibBuilder.loadTexts:
    cneClientGroup.setStatus("current")

cneServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2, 3)
)
cneServerGroup.setObjects(
    ("CISCO-NHRP-EXT-MIB", "cneServerStatRedirectTx")
)
if mibBuilder.loadTexts:
    cneServerGroup.setStatus("current")

cneNotificationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2, 4)
)
cneNotificationControlGroup.setObjects(
    ("CISCO-NHRP-EXT-MIB", "cneNotifEnable")
)
if mibBuilder.loadTexts:
    cneNotificationControlGroup.setStatus("current")


# Notification objects

cneNotifNextHopRegServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 0, 1)
)
cneNotifNextHopRegServerUp.setObjects(
      *(("NHRP-MIB", "nhrpClientInternetworkAddrType"),
        ("NHRP-MIB", "nhrpClientInternetworkAddr"),
        ("NHRP-MIB", "nhrpClientNbmaAddrType"),
        ("NHRP-MIB", "nhrpClientNbmaAddr"),
        ("NHRP-MIB", "nhrpClientNbmaSubaddr"),
        ("NHRP-MIB", "nhrpClientNhsInternetworkAddrType"),
        ("NHRP-MIB", "nhrpClientNhsInternetworkAddr"),
        ("NHRP-MIB", "nhrpClientNhsNbmaAddrType"),
        ("NHRP-MIB", "nhrpClientNhsNbmaAddr"),
        ("NHRP-MIB", "nhrpClientNhsNbmaSubaddr"),
        ("NHRP-MIB", "nhrpClientHoldTime"),
        ("NHRP-MIB", "nhrpClientRegUniqueness"),
        ("NHRP-MIB", "nhrpClientNhsInUse"))
)
if mibBuilder.loadTexts:
    cneNotifNextHopRegServerUp.setStatus(
        "current"
    )

cneNotifNextHopRegServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 0, 2)
)
cneNotifNextHopRegServerDown.setObjects(
      *(("NHRP-MIB", "nhrpClientInternetworkAddrType"),
        ("NHRP-MIB", "nhrpClientInternetworkAddr"),
        ("NHRP-MIB", "nhrpClientNbmaAddrType"),
        ("NHRP-MIB", "nhrpClientNbmaAddr"),
        ("NHRP-MIB", "nhrpClientNbmaSubaddr"),
        ("NHRP-MIB", "nhrpClientNhsInternetworkAddrType"),
        ("NHRP-MIB", "nhrpClientNhsInternetworkAddr"),
        ("NHRP-MIB", "nhrpClientNhsNbmaAddrType"),
        ("NHRP-MIB", "nhrpClientNhsNbmaAddr"),
        ("NHRP-MIB", "nhrpClientNhsNbmaSubaddr"),
        ("CISCO-NHRP-EXT-MIB", "cneNextHopDownReason"),
        ("CISCO-NHRP-EXT-MIB", "cneNHRPException"))
)
if mibBuilder.loadTexts:
    cneNotifNextHopRegServerDown.setStatus(
        "current"
    )

cneNotifNextHopRegClientUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 0, 3)
)
cneNotifNextHopRegClientUp.setObjects(
      *(("NHRP-MIB", "nhrpServerInternetworkAddrType"),
        ("NHRP-MIB", "nhrpServerInternetworkAddr"),
        ("NHRP-MIB", "nhrpServerNbmaAddrType"),
        ("NHRP-MIB", "nhrpServerNbmaAddr"),
        ("NHRP-MIB", "nhrpServerNbmaSubaddr"),
        ("NHRP-MIB", "nhrpServerNhcInternetworkAddrType"),
        ("NHRP-MIB", "nhrpServerNhcInternetworkAddr"),
        ("NHRP-MIB", "nhrpServerNhcNbmaAddrType"),
        ("NHRP-MIB", "nhrpServerNhcNbmaAddr"),
        ("NHRP-MIB", "nhrpServerNhcNbmaSubaddr"),
        ("NHRP-MIB", "nhrpServerNhcPrefixLength"),
        ("NHRP-MIB", "nhrpServerNhcInUse"),
        ("NHRP-MIB", "nhrpServerCacheUniqueness"))
)
if mibBuilder.loadTexts:
    cneNotifNextHopRegClientUp.setStatus(
        "current"
    )

cneNotifNextHopRegClientDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 0, 4)
)
cneNotifNextHopRegClientDown.setObjects(
      *(("NHRP-MIB", "nhrpServerInternetworkAddrType"),
        ("NHRP-MIB", "nhrpServerInternetworkAddr"),
        ("NHRP-MIB", "nhrpServerNbmaAddrType"),
        ("NHRP-MIB", "nhrpServerNbmaAddr"),
        ("NHRP-MIB", "nhrpServerNbmaSubaddr"),
        ("NHRP-MIB", "nhrpServerNhcInternetworkAddrType"),
        ("NHRP-MIB", "nhrpServerNhcInternetworkAddr"),
        ("NHRP-MIB", "nhrpServerNhcNbmaAddrType"),
        ("NHRP-MIB", "nhrpServerNhcNbmaAddr"),
        ("NHRP-MIB", "nhrpServerNhcNbmaSubaddr"),
        ("NHRP-MIB", "nhrpServerNhcPrefixLength"),
        ("NHRP-MIB", "nhrpServerCacheUniqueness"),
        ("CISCO-NHRP-EXT-MIB", "cneNextHopDownReason"),
        ("CISCO-NHRP-EXT-MIB", "cneNHRPException"))
)
if mibBuilder.loadTexts:
    cneNotifNextHopRegClientDown.setStatus(
        "current"
    )

cneNotifNextHopPeerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 0, 5)
)
cneNotifNextHopPeerUp.setObjects(
      *(("NHRP-MIB", "nhrpClientInternetworkAddrType"),
        ("NHRP-MIB", "nhrpClientInternetworkAddr"),
        ("NHRP-MIB", "nhrpClientNbmaAddrType"),
        ("NHRP-MIB", "nhrpClientNbmaAddr"),
        ("NHRP-MIB", "nhrpClientNbmaSubaddr"),
        ("NHRP-MIB", "nhrpCacheNextHopInternetworkAddr"),
        ("NHRP-MIB", "nhrpCacheNbmaAddrType"),
        ("NHRP-MIB", "nhrpCacheNbmaAddr"),
        ("NHRP-MIB", "nhrpCacheNbmaSubaddr"),
        ("NHRP-MIB", "nhrpCacheType"))
)
if mibBuilder.loadTexts:
    cneNotifNextHopPeerUp.setStatus(
        "current"
    )

cneNotifNextHopPeerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 0, 6)
)
cneNotifNextHopPeerDown.setObjects(
      *(("NHRP-MIB", "nhrpClientInternetworkAddrType"),
        ("NHRP-MIB", "nhrpClientInternetworkAddr"),
        ("NHRP-MIB", "nhrpClientNbmaAddrType"),
        ("NHRP-MIB", "nhrpClientNbmaAddr"),
        ("NHRP-MIB", "nhrpClientNbmaSubaddr"),
        ("NHRP-MIB", "nhrpCacheNextHopInternetworkAddr"),
        ("NHRP-MIB", "nhrpCacheNbmaAddrType"),
        ("NHRP-MIB", "nhrpCacheNbmaAddr"),
        ("NHRP-MIB", "nhrpCacheNbmaSubaddr"),
        ("CISCO-NHRP-EXT-MIB", "cneNextHopDownReason"),
        ("CISCO-NHRP-EXT-MIB", "cneNHRPException"))
)
if mibBuilder.loadTexts:
    cneNotifNextHopPeerDown.setStatus(
        "current"
    )

cneNotifRateLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 0, 7)
)
cneNotifRateLimitExceeded.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    cneNotifRateLimitExceeded.setStatus(
        "current"
    )


# Notifications groups

cneGeneralNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2, 5)
)
cneGeneralNotificationGroup.setObjects(
      *(("CISCO-NHRP-EXT-MIB", "cneNotifRateLimitExceeded"),
        ("CISCO-NHRP-EXT-MIB", "cneNotifNextHopPeerUp"),
        ("CISCO-NHRP-EXT-MIB", "cneNotifNextHopPeerDown"))
)
if mibBuilder.loadTexts:
    cneGeneralNotificationGroup.setStatus(
        "current"
    )

cneClientNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2, 6)
)
cneClientNotificationGroup.setObjects(
      *(("CISCO-NHRP-EXT-MIB", "cneNotifNextHopRegServerUp"),
        ("CISCO-NHRP-EXT-MIB", "cneNotifNextHopRegServerDown"))
)
if mibBuilder.loadTexts:
    cneClientNotificationGroup.setStatus(
        "current"
    )

cneServerNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2, 7)
)
cneServerNotificationGroup.setObjects(
      *(("CISCO-NHRP-EXT-MIB", "cneNotifNextHopRegClientUp"),
        ("CISCO-NHRP-EXT-MIB", "cneNotifNextHopRegClientDown"))
)
if mibBuilder.loadTexts:
    cneServerNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cneCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cneCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-NHRP-EXT-MIB",
    **{"CiscoNhrpErrorCode": CiscoNhrpErrorCode,
       "CiscoNextHopDownReasonCode": CiscoNextHopDownReasonCode,
       "ciscoNhrpExtMIB": ciscoNhrpExtMIB,
       "cneNotifs": cneNotifs,
       "cneNotifNextHopRegServerUp": cneNotifNextHopRegServerUp,
       "cneNotifNextHopRegServerDown": cneNotifNextHopRegServerDown,
       "cneNotifNextHopRegClientUp": cneNotifNextHopRegClientUp,
       "cneNotifNextHopRegClientDown": cneNotifNextHopRegClientDown,
       "cneNotifNextHopPeerUp": cneNotifNextHopPeerUp,
       "cneNotifNextHopPeerDown": cneNotifNextHopPeerDown,
       "cneNotifRateLimitExceeded": cneNotifRateLimitExceeded,
       "cneObjects": cneObjects,
       "cneGeneralObjects": cneGeneralObjects,
       "cneNextHopDownReason": cneNextHopDownReason,
       "cneNHRPException": cneNHRPException,
       "cneClientObjects": cneClientObjects,
       "cneClientStatExtTable": cneClientStatExtTable,
       "cneClientStatExtEntry": cneClientStatExtEntry,
       "cneClientStatRedirectRx": cneClientStatRedirectRx,
       "cneServerObjects": cneServerObjects,
       "cneServerStatExtTable": cneServerStatExtTable,
       "cneServerStatExtEntry": cneServerStatExtEntry,
       "cneServerStatRedirectTx": cneServerStatRedirectTx,
       "cneNotificationControlObjects": cneNotificationControlObjects,
       "cneNotifEnable": cneNotifEnable,
       "cneConform": cneConform,
       "cneCompliances": cneCompliances,
       "cneCompliance": cneCompliance,
       "cneGroups": cneGroups,
       "cneGeneralGroup": cneGeneralGroup,
       "cneClientGroup": cneClientGroup,
       "cneServerGroup": cneServerGroup,
       "cneNotificationControlGroup": cneNotificationControlGroup,
       "cneGeneralNotificationGroup": cneGeneralNotificationGroup,
       "cneClientNotificationGroup": cneClientNotificationGroup,
       "cneServerNotificationGroup": cneServerNotificationGroup}
)
