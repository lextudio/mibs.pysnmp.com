# SNMP MIB module (SIP-REGISTRAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SIP-REGISTRAR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:52:24 2024
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

(applIndex,) = mibBuilder.importSymbols(
    "NETWORK-SERVICES-MIB",
    "applIndex")

(sipMIB,) = mibBuilder.importSymbols(
    "SIP-MIB-SMI",
    "sipMIB")

(SipServerActions,) = mibBuilder.importSymbols(
    "SIP-TC",
    "SipServerActions")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

sipRegistrarMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SipRegCfg_ObjectIdentity = ObjectIdentity
sipRegCfg = _SipRegCfg_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1)
)
_SipRegCfgTable_Object = MibTable
sipRegCfgTable = _SipRegCfgTable_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 1)
)
if mibBuilder.loadTexts:
    sipRegCfgTable.setStatus("current")
_SipRegCfgEntry_Object = MibTableRow
sipRegCfgEntry = _SipRegCfgEntry_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 1, 1)
)
sipRegCfgEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    sipRegCfgEntry.setStatus("current")
_SipRegAllowThirdParty_Type = TruthValue
_SipRegAllowThirdParty_Object = MibTableColumn
sipRegAllowThirdParty = _SipRegAllowThirdParty_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 1, 1, 1),
    _SipRegAllowThirdParty_Type()
)
sipRegAllowThirdParty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegAllowThirdParty.setStatus("current")


class _SipRegContactDfltExpiryDuration_Type(Unsigned32):
    """Custom type sipRegContactDfltExpiryDuration based on Unsigned32"""
    defaultValue = 3600


_SipRegContactDfltExpiryDuration_Object = MibTableColumn
sipRegContactDfltExpiryDuration = _SipRegContactDfltExpiryDuration_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 1, 1, 2),
    _SipRegContactDfltExpiryDuration_Type()
)
sipRegContactDfltExpiryDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegContactDfltExpiryDuration.setStatus("current")
if mibBuilder.loadTexts:
    sipRegContactDfltExpiryDuration.setUnits("seconds")
_SipRegContactDfltExpiryDate_Type = DateAndTime
_SipRegContactDfltExpiryDate_Object = MibTableColumn
sipRegContactDfltExpiryDate = _SipRegContactDfltExpiryDate_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 1, 1, 3),
    _SipRegContactDfltExpiryDate_Type()
)
sipRegContactDfltExpiryDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegContactDfltExpiryDate.setStatus("current")


class _SipRegMaxContactExpiryDate_Type(Unsigned32):
    """Custom type sipRegMaxContactExpiryDate based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SipRegMaxContactExpiryDate_Type.__name__ = "Unsigned32"
_SipRegMaxContactExpiryDate_Object = MibTableColumn
sipRegMaxContactExpiryDate = _SipRegMaxContactExpiryDate_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 1, 1, 4),
    _SipRegMaxContactExpiryDate_Type()
)
sipRegMaxContactExpiryDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegMaxContactExpiryDate.setStatus("current")
if mibBuilder.loadTexts:
    sipRegMaxContactExpiryDate.setUnits("seconds")
_SipRegRespHasContacts_Type = TruthValue
_SipRegRespHasContacts_Object = MibTableColumn
sipRegRespHasContacts = _SipRegRespHasContacts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 1, 1, 5),
    _SipRegRespHasContacts_Type()
)
sipRegRespHasContacts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegRespHasContacts.setStatus("current")


class _SipRegMaxUsers_Type(Unsigned32):
    """Custom type sipRegMaxUsers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SipRegMaxUsers_Type.__name__ = "Unsigned32"
_SipRegMaxUsers_Object = MibTableColumn
sipRegMaxUsers = _SipRegMaxUsers_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 1, 1, 6),
    _SipRegMaxUsers_Type()
)
sipRegMaxUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRegMaxUsers.setStatus("current")


class _SipRegCurrentUsers_Type(Gauge32):
    """Custom type sipRegCurrentUsers based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SipRegCurrentUsers_Type.__name__ = "Gauge32"
_SipRegCurrentUsers_Object = MibTableColumn
sipRegCurrentUsers = _SipRegCurrentUsers_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 1, 1, 7),
    _SipRegCurrentUsers_Type()
)
sipRegCurrentUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRegCurrentUsers.setStatus("current")
_SipRegUserTable_Object = MibTable
sipRegUserTable = _SipRegUserTable_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 2)
)
if mibBuilder.loadTexts:
    sipRegUserTable.setStatus("current")
_SipRegUserEntry_Object = MibTableRow
sipRegUserEntry = _SipRegUserEntry_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 2, 1)
)
sipRegUserEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "SIP-REGISTRAR-MIB", "sipUserIndex"),
)
if mibBuilder.loadTexts:
    sipRegUserEntry.setStatus("current")


class _SipUserIndex_Type(Unsigned32):
    """Custom type sipUserIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SipUserIndex_Type.__name__ = "Unsigned32"
_SipUserIndex_Object = MibTableColumn
sipUserIndex = _SipUserIndex_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 2, 1, 1),
    _SipUserIndex_Type()
)
sipUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipUserIndex.setStatus("current")
_SipUserUri_Type = SnmpAdminString
_SipUserUri_Object = MibTableColumn
sipUserUri = _SipUserUri_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 2, 1, 2),
    _SipUserUri_Type()
)
sipUserUri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipUserUri.setStatus("current")


class _SipUserPassword_Type(OctetString):
    """Custom type sipUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SipUserPassword_Type.__name__ = "OctetString"
_SipUserPassword_Object = MibTableColumn
sipUserPassword = _SipUserPassword_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 2, 1, 3),
    _SipUserPassword_Type()
)
sipUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipUserPassword.setStatus("current")
_SipUserAuthenticationFailures_Type = Counter32
_SipUserAuthenticationFailures_Object = MibTableColumn
sipUserAuthenticationFailures = _SipUserAuthenticationFailures_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 2, 1, 4),
    _SipUserAuthenticationFailures_Type()
)
sipUserAuthenticationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipUserAuthenticationFailures.setStatus("current")
_SipUserTableRowStatus_Type = RowStatus
_SipUserTableRowStatus_Object = MibTableColumn
sipUserTableRowStatus = _SipUserTableRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 2, 1, 5),
    _SipUserTableRowStatus_Type()
)
sipUserTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipUserTableRowStatus.setStatus("current")
_SipContactTable_Object = MibTable
sipContactTable = _SipContactTable_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 3)
)
if mibBuilder.loadTexts:
    sipContactTable.setStatus("current")
_SipContactEntry_Object = MibTableRow
sipContactEntry = _SipContactEntry_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 3, 1)
)
sipContactEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "SIP-REGISTRAR-MIB", "sipUserIndex"),
    (0, "SIP-REGISTRAR-MIB", "sipContactIndex"),
)
if mibBuilder.loadTexts:
    sipContactEntry.setStatus("current")


class _SipContactIndex_Type(Unsigned32):
    """Custom type sipContactIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SipContactIndex_Type.__name__ = "Unsigned32"
_SipContactIndex_Object = MibTableColumn
sipContactIndex = _SipContactIndex_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 3, 1, 1),
    _SipContactIndex_Type()
)
sipContactIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipContactIndex.setStatus("current")
_SipContactDisplayName_Type = SnmpAdminString
_SipContactDisplayName_Object = MibTableColumn
sipContactDisplayName = _SipContactDisplayName_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 3, 1, 2),
    _SipContactDisplayName_Type()
)
sipContactDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipContactDisplayName.setStatus("current")
_SipContactURI_Type = SnmpAdminString
_SipContactURI_Object = MibTableColumn
sipContactURI = _SipContactURI_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 3, 1, 3),
    _SipContactURI_Type()
)
sipContactURI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipContactURI.setStatus("current")
_SipContactLastUpdated_Type = TimeStamp
_SipContactLastUpdated_Object = MibTableColumn
sipContactLastUpdated = _SipContactLastUpdated_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 3, 1, 4),
    _SipContactLastUpdated_Type()
)
sipContactLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipContactLastUpdated.setStatus("current")
_SipContactExpiry_Type = DateAndTime
_SipContactExpiry_Object = MibTableColumn
sipContactExpiry = _SipContactExpiry_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 3, 1, 5),
    _SipContactExpiry_Type()
)
sipContactExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipContactExpiry.setStatus("current")


class _SipContactPreference_Type(OctetString):
    """Custom type sipContactPreference based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SipContactPreference_Type.__name__ = "OctetString"
_SipContactPreference_Object = MibTableColumn
sipContactPreference = _SipContactPreference_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 3, 1, 6),
    _SipContactPreference_Type()
)
sipContactPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipContactPreference.setStatus("current")
_SipContactAction_Type = SipServerActions
_SipContactAction_Object = MibTableColumn
sipContactAction = _SipContactAction_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 3, 1, 7),
    _SipContactAction_Type()
)
sipContactAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipContactAction.setStatus("current")
_SipContactRetryAfter_Type = DateAndTime
_SipContactRetryAfter_Object = MibTableColumn
sipContactRetryAfter = _SipContactRetryAfter_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 1, 3, 1, 8),
    _SipContactRetryAfter_Type()
)
sipContactRetryAfter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipContactRetryAfter.setStatus("current")
_SipRegStats_ObjectIdentity = ObjectIdentity
sipRegStats = _SipRegStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 5, 2)
)
_SipRegStatsTable_Object = MibTable
sipRegStatsTable = _SipRegStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 2, 1)
)
if mibBuilder.loadTexts:
    sipRegStatsTable.setStatus("current")
_SipRegStatsEntry_Object = MibTableRow
sipRegStatsEntry = _SipRegStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 2, 1, 1)
)
sipRegStatsEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    sipRegStatsEntry.setStatus("current")
_SipRegAcceptedRegistrations_Type = Counter32
_SipRegAcceptedRegistrations_Object = MibTableColumn
sipRegAcceptedRegistrations = _SipRegAcceptedRegistrations_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 2, 1, 1, 1),
    _SipRegAcceptedRegistrations_Type()
)
sipRegAcceptedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRegAcceptedRegistrations.setStatus("current")
_SipRegRejectedRegistrations_Type = Counter32
_SipRegRejectedRegistrations_Object = MibTableColumn
sipRegRejectedRegistrations = _SipRegRejectedRegistrations_Object(
    (1, 3, 6, 1, 2, 1, 9998, 5, 2, 1, 1, 2),
    _SipRegRejectedRegistrations_Type()
)
sipRegRejectedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRegRejectedRegistrations.setStatus("current")
_SipRegMIBNotif_ObjectIdentity = ObjectIdentity
sipRegMIBNotif = _SipRegMIBNotif_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 5, 3)
)
_SipRegMIBConformance_ObjectIdentity = ObjectIdentity
sipRegMIBConformance = _SipRegMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 5, 4)
)
_SipRegMIBCompliances_ObjectIdentity = ObjectIdentity
sipRegMIBCompliances = _SipRegMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 5, 4, 1)
)
_SipRegMIBGroups_ObjectIdentity = ObjectIdentity
sipRegMIBGroups = _SipRegMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 5, 4, 2)
)

# Managed Objects groups

sipRegistrarConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 9998, 5, 4, 2, 1)
)
sipRegistrarConfigGroup.setObjects(
      *(("SIP-REGISTRAR-MIB", "sipRegAllowThirdParty"),
        ("SIP-REGISTRAR-MIB", "sipRegContactDfltExpiryDuration"),
        ("SIP-REGISTRAR-MIB", "sipRegContactDfltExpiryDate"),
        ("SIP-REGISTRAR-MIB", "sipRegMaxContactExpiryDate"),
        ("SIP-REGISTRAR-MIB", "sipRegRespHasContacts"),
        ("SIP-REGISTRAR-MIB", "sipRegMaxUsers"),
        ("SIP-REGISTRAR-MIB", "sipRegCurrentUsers"),
        ("SIP-REGISTRAR-MIB", "sipUserUri"),
        ("SIP-REGISTRAR-MIB", "sipUserPassword"),
        ("SIP-REGISTRAR-MIB", "sipUserAuthenticationFailures"),
        ("SIP-REGISTRAR-MIB", "sipUserTableRowStatus"),
        ("SIP-REGISTRAR-MIB", "sipContactDisplayName"),
        ("SIP-REGISTRAR-MIB", "sipContactURI"),
        ("SIP-REGISTRAR-MIB", "sipContactLastUpdated"),
        ("SIP-REGISTRAR-MIB", "sipContactExpiry"),
        ("SIP-REGISTRAR-MIB", "sipContactPreference"),
        ("SIP-REGISTRAR-MIB", "sipContactAction"),
        ("SIP-REGISTRAR-MIB", "sipContactRetryAfter"))
)
if mibBuilder.loadTexts:
    sipRegistrarConfigGroup.setStatus("current")

sipRegistrarStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 9998, 5, 4, 2, 2)
)
sipRegistrarStatsGroup.setObjects(
      *(("SIP-REGISTRAR-MIB", "sipRegAcceptedRegistrations"),
        ("SIP-REGISTRAR-MIB", "sipRegRejectedRegistrations"))
)
if mibBuilder.loadTexts:
    sipRegistrarStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sipRegCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 9998, 5, 4, 1, 1)
)
if mibBuilder.loadTexts:
    sipRegCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIP-REGISTRAR-MIB",
    **{"sipRegistrarMIB": sipRegistrarMIB,
       "sipRegCfg": sipRegCfg,
       "sipRegCfgTable": sipRegCfgTable,
       "sipRegCfgEntry": sipRegCfgEntry,
       "sipRegAllowThirdParty": sipRegAllowThirdParty,
       "sipRegContactDfltExpiryDuration": sipRegContactDfltExpiryDuration,
       "sipRegContactDfltExpiryDate": sipRegContactDfltExpiryDate,
       "sipRegMaxContactExpiryDate": sipRegMaxContactExpiryDate,
       "sipRegRespHasContacts": sipRegRespHasContacts,
       "sipRegMaxUsers": sipRegMaxUsers,
       "sipRegCurrentUsers": sipRegCurrentUsers,
       "sipRegUserTable": sipRegUserTable,
       "sipRegUserEntry": sipRegUserEntry,
       "sipUserIndex": sipUserIndex,
       "sipUserUri": sipUserUri,
       "sipUserPassword": sipUserPassword,
       "sipUserAuthenticationFailures": sipUserAuthenticationFailures,
       "sipUserTableRowStatus": sipUserTableRowStatus,
       "sipContactTable": sipContactTable,
       "sipContactEntry": sipContactEntry,
       "sipContactIndex": sipContactIndex,
       "sipContactDisplayName": sipContactDisplayName,
       "sipContactURI": sipContactURI,
       "sipContactLastUpdated": sipContactLastUpdated,
       "sipContactExpiry": sipContactExpiry,
       "sipContactPreference": sipContactPreference,
       "sipContactAction": sipContactAction,
       "sipContactRetryAfter": sipContactRetryAfter,
       "sipRegStats": sipRegStats,
       "sipRegStatsTable": sipRegStatsTable,
       "sipRegStatsEntry": sipRegStatsEntry,
       "sipRegAcceptedRegistrations": sipRegAcceptedRegistrations,
       "sipRegRejectedRegistrations": sipRegRejectedRegistrations,
       "sipRegMIBNotif": sipRegMIBNotif,
       "sipRegMIBConformance": sipRegMIBConformance,
       "sipRegMIBCompliances": sipRegMIBCompliances,
       "sipRegCompliance": sipRegCompliance,
       "sipRegMIBGroups": sipRegMIBGroups,
       "sipRegistrarConfigGroup": sipRegistrarConfigGroup,
       "sipRegistrarStatsGroup": sipRegistrarStatsGroup}
)
