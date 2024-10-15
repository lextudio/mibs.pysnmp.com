# SNMP MIB module (EQLINTERNAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQLINTERNAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:04 2024
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

(UTFString,) = mibBuilder.importSymbols(
    "EQLGROUP-MIB",
    "UTFString")

(equalLogic,) = mibBuilder.importSymbols(
    "EQUALLOGIC-SMI",
    "equalLogic")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

eqlInternalModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 27)
)
eqlInternalModule.setRevisions(
        ("2013-01-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EqlInternalObjects_ObjectIdentity = ObjectIdentity
eqlInternalObjects = _EqlInternalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 27, 1)
)
_EqlMonitorTable_Object = MibTable
eqlMonitorTable = _EqlMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 27, 1, 1)
)
if mibBuilder.loadTexts:
    eqlMonitorTable.setStatus("current")
_EqlMonitorEntry_Object = MibTableRow
eqlMonitorEntry = _EqlMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1)
)
eqlMonitorEntry.setIndexNames(
    (0, "EQLINTERNAL-MIB", "eqlMonitorIndex"),
)
if mibBuilder.loadTexts:
    eqlMonitorEntry.setStatus("current")
_EqlMonitorIndex_Type = Unsigned32
_EqlMonitorIndex_Object = MibTableColumn
eqlMonitorIndex = _EqlMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 1),
    _EqlMonitorIndex_Type()
)
eqlMonitorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlMonitorIndex.setStatus("current")
_EqlMonitorRowStatus_Type = RowStatus
_EqlMonitorRowStatus_Object = MibTableColumn
eqlMonitorRowStatus = _EqlMonitorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 2),
    _EqlMonitorRowStatus_Type()
)
eqlMonitorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMonitorRowStatus.setStatus("current")


class _EqlMonitorUUID_Type(OctetString):
    """Custom type eqlMonitorUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlMonitorUUID_Type.__name__ = "OctetString"
_EqlMonitorUUID_Object = MibTableColumn
eqlMonitorUUID = _EqlMonitorUUID_Object(
    (1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 3),
    _EqlMonitorUUID_Type()
)
eqlMonitorUUID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMonitorUUID.setStatus("current")


class _EqlMonitorServerName_Type(UTFString):
    """Custom type eqlMonitorServerName based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqlMonitorServerName_Type.__name__ = "UTFString"
_EqlMonitorServerName_Object = MibTableColumn
eqlMonitorServerName = _EqlMonitorServerName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 4),
    _EqlMonitorServerName_Type()
)
eqlMonitorServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMonitorServerName.setStatus("current")


class _EqlMonitorDomainName_Type(UTFString):
    """Custom type eqlMonitorDomainName based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqlMonitorDomainName_Type.__name__ = "UTFString"
_EqlMonitorDomainName_Object = MibTableColumn
eqlMonitorDomainName = _EqlMonitorDomainName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 5),
    _EqlMonitorDomainName_Type()
)
eqlMonitorDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMonitorDomainName.setStatus("current")
_EqlMonitorInetAddressType_Type = InetAddressType
_EqlMonitorInetAddressType_Object = MibTableColumn
eqlMonitorInetAddressType = _EqlMonitorInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 6),
    _EqlMonitorInetAddressType_Type()
)
eqlMonitorInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMonitorInetAddressType.setStatus("current")
_EqlMonitorInetAddress_Type = InetAddress
_EqlMonitorInetAddress_Object = MibTableColumn
eqlMonitorInetAddress = _EqlMonitorInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 7),
    _EqlMonitorInetAddress_Type()
)
eqlMonitorInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMonitorInetAddress.setStatus("current")


class _EqlMonitorSupportAssist_Type(Integer32):
    """Custom type eqlMonitorSupportAssist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("supportAssistCommunicatingWithDell", 3),
          ("supportAssistEnabled", 2),
          ("supportAssistInstalledNotEnabled", 1),
          ("supportAssistNone", 0))
    )


_EqlMonitorSupportAssist_Type.__name__ = "Integer32"
_EqlMonitorSupportAssist_Object = MibTableColumn
eqlMonitorSupportAssist = _EqlMonitorSupportAssist_Object(
    (1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 8),
    _EqlMonitorSupportAssist_Type()
)
eqlMonitorSupportAssist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMonitorSupportAssist.setStatus("current")
_EqlMonitorTimestamp_Type = Counter32
_EqlMonitorTimestamp_Object = MibTableColumn
eqlMonitorTimestamp = _EqlMonitorTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 9),
    _EqlMonitorTimestamp_Type()
)
eqlMonitorTimestamp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMonitorTimestamp.setStatus("current")
_EqlMonitorSupportAssistTimestamp_Type = Counter32
_EqlMonitorSupportAssistTimestamp_Object = MibTableColumn
eqlMonitorSupportAssistTimestamp = _EqlMonitorSupportAssistTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 10),
    _EqlMonitorSupportAssistTimestamp_Type()
)
eqlMonitorSupportAssistTimestamp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMonitorSupportAssistTimestamp.setStatus("current")
_EqlMonitorLicensingTimestamp_Type = Counter32
_EqlMonitorLicensingTimestamp_Object = MibTableColumn
eqlMonitorLicensingTimestamp = _EqlMonitorLicensingTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 11),
    _EqlMonitorLicensingTimestamp_Type()
)
eqlMonitorLicensingTimestamp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMonitorLicensingTimestamp.setStatus("current")


class _EqlMonitorDescription_Type(UTFString):
    """Custom type eqlMonitorDescription based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqlMonitorDescription_Type.__name__ = "UTFString"
_EqlMonitorDescription_Object = MibTableColumn
eqlMonitorDescription = _EqlMonitorDescription_Object(
    (1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 12),
    _EqlMonitorDescription_Type()
)
eqlMonitorDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMonitorDescription.setStatus("current")
_EqlMonitorStatusTable_Object = MibTable
eqlMonitorStatusTable = _EqlMonitorStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 27, 1, 2)
)
if mibBuilder.loadTexts:
    eqlMonitorStatusTable.setStatus("current")
_EqlMonitorStatusEntry_Object = MibTableRow
eqlMonitorStatusEntry = _EqlMonitorStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 27, 1, 2, 1)
)
eqlMonitorStatusEntry.setIndexNames(
    (0, "EQLINTERNAL-MIB", "eqlMonitorIndex"),
)
if mibBuilder.loadTexts:
    eqlMonitorStatusEntry.setStatus("current")


class _EqlMonitorStatusReminder_Type(Integer32):
    """Custom type eqlMonitorStatusReminder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("monitoringCurrent", 1),
          ("monitoringExpired", 0))
    )


_EqlMonitorStatusReminder_Type.__name__ = "Integer32"
_EqlMonitorStatusReminder_Object = MibTableColumn
eqlMonitorStatusReminder = _EqlMonitorStatusReminder_Object(
    (1, 3, 6, 1, 4, 1, 12740, 27, 1, 2, 1, 1),
    _EqlMonitorStatusReminder_Type()
)
eqlMonitorStatusReminder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMonitorStatusReminder.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQLINTERNAL-MIB",
    **{"eqlInternalModule": eqlInternalModule,
       "eqlInternalObjects": eqlInternalObjects,
       "eqlMonitorTable": eqlMonitorTable,
       "eqlMonitorEntry": eqlMonitorEntry,
       "eqlMonitorIndex": eqlMonitorIndex,
       "eqlMonitorRowStatus": eqlMonitorRowStatus,
       "eqlMonitorUUID": eqlMonitorUUID,
       "eqlMonitorServerName": eqlMonitorServerName,
       "eqlMonitorDomainName": eqlMonitorDomainName,
       "eqlMonitorInetAddressType": eqlMonitorInetAddressType,
       "eqlMonitorInetAddress": eqlMonitorInetAddress,
       "eqlMonitorSupportAssist": eqlMonitorSupportAssist,
       "eqlMonitorTimestamp": eqlMonitorTimestamp,
       "eqlMonitorSupportAssistTimestamp": eqlMonitorSupportAssistTimestamp,
       "eqlMonitorLicensingTimestamp": eqlMonitorLicensingTimestamp,
       "eqlMonitorDescription": eqlMonitorDescription,
       "eqlMonitorStatusTable": eqlMonitorStatusTable,
       "eqlMonitorStatusEntry": eqlMonitorStatusEntry,
       "eqlMonitorStatusReminder": eqlMonitorStatusReminder}
)
