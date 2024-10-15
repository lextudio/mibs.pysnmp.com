# SNMP MIB module (CLAB-ANI-NID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CLAB-ANI-NID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:37 2024
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

(clabCommonMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabCommonMibs")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

clabAniNidMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8)
)
clabAniNidMib.setRevisions(
        ("2016-11-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ClabAniNidNotifications_ObjectIdentity = ObjectIdentity
clabAniNidNotifications = _ClabAniNidNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 0)
)
_ClabAniNidMibObjects_ObjectIdentity = ObjectIdentity
clabAniNidMibObjects = _ClabAniNidMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1)
)
_ClabAniNidCfgObjects_ObjectIdentity = ObjectIdentity
clabAniNidCfgObjects = _ClabAniNidCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 1)
)
_ClabAniNidCfgID_Type = SnmpAdminString
_ClabAniNidCfgID_Object = MibScalar
clabAniNidCfgID = _ClabAniNidCfgID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 1, 1),
    _ClabAniNidCfgID_Type()
)
clabAniNidCfgID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabAniNidCfgID.setStatus("current")


class _ClabAniNidCfgPtpMcastMac_Type(Integer32):
    """Custom type clabAniNidCfgPtpMcastMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwardable", 1),
          ("nonforwardable", 2))
    )


_ClabAniNidCfgPtpMcastMac_Type.__name__ = "Integer32"
_ClabAniNidCfgPtpMcastMac_Object = MibScalar
clabAniNidCfgPtpMcastMac = _ClabAniNidCfgPtpMcastMac_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 1, 2),
    _ClabAniNidCfgPtpMcastMac_Type()
)
clabAniNidCfgPtpMcastMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabAniNidCfgPtpMcastMac.setStatus("current")
_ClabAniNidCfgTelnetEnabled_Type = TruthValue
_ClabAniNidCfgTelnetEnabled_Object = MibScalar
clabAniNidCfgTelnetEnabled = _ClabAniNidCfgTelnetEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 1, 3),
    _ClabAniNidCfgTelnetEnabled_Type()
)
clabAniNidCfgTelnetEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabAniNidCfgTelnetEnabled.setStatus("current")
_ClabAniNidCfgTftpEnabled_Type = TruthValue
_ClabAniNidCfgTftpEnabled_Object = MibScalar
clabAniNidCfgTftpEnabled = _ClabAniNidCfgTftpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 1, 4),
    _ClabAniNidCfgTftpEnabled_Type()
)
clabAniNidCfgTftpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabAniNidCfgTftpEnabled.setStatus("current")


class _ClabAniNidCfgClientAuthStatus_Type(Integer32):
    """Custom type clabAniNidCfgClientAuthStatus based on Integer32"""
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
        *(("authenticated", 1),
          ("authenticationFailed", 2),
          ("noAvailableServers", 3),
          ("unknown", 0))
    )


_ClabAniNidCfgClientAuthStatus_Type.__name__ = "Integer32"
_ClabAniNidCfgClientAuthStatus_Object = MibScalar
clabAniNidCfgClientAuthStatus = _ClabAniNidCfgClientAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 1, 5),
    _ClabAniNidCfgClientAuthStatus_Type()
)
clabAniNidCfgClientAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabAniNidCfgClientAuthStatus.setStatus("current")


class _ClabAniNidCfgAuthServerServiceType_Type(Integer32):
    """Custom type clabAniNidCfgAuthServerServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("tacacs", 2),
          ("unknown", 0))
    )


_ClabAniNidCfgAuthServerServiceType_Type.__name__ = "Integer32"
_ClabAniNidCfgAuthServerServiceType_Object = MibScalar
clabAniNidCfgAuthServerServiceType = _ClabAniNidCfgAuthServerServiceType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 1, 6),
    _ClabAniNidCfgAuthServerServiceType_Type()
)
clabAniNidCfgAuthServerServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabAniNidCfgAuthServerServiceType.setStatus("current")
_ClabAniNidCfgPrimaryServerIpAddressType_Type = InetAddressType
_ClabAniNidCfgPrimaryServerIpAddressType_Object = MibScalar
clabAniNidCfgPrimaryServerIpAddressType = _ClabAniNidCfgPrimaryServerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 1, 7),
    _ClabAniNidCfgPrimaryServerIpAddressType_Type()
)
clabAniNidCfgPrimaryServerIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabAniNidCfgPrimaryServerIpAddressType.setStatus("current")
_ClabAniNidCfgPrimaryServerIpAddress_Type = InetAddress
_ClabAniNidCfgPrimaryServerIpAddress_Object = MibScalar
clabAniNidCfgPrimaryServerIpAddress = _ClabAniNidCfgPrimaryServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 1, 8),
    _ClabAniNidCfgPrimaryServerIpAddress_Type()
)
clabAniNidCfgPrimaryServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabAniNidCfgPrimaryServerIpAddress.setStatus("current")
_ClabAniNidCfgPrimaryServerPort_Type = InetPortNumber
_ClabAniNidCfgPrimaryServerPort_Object = MibScalar
clabAniNidCfgPrimaryServerPort = _ClabAniNidCfgPrimaryServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 1, 9),
    _ClabAniNidCfgPrimaryServerPort_Type()
)
clabAniNidCfgPrimaryServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabAniNidCfgPrimaryServerPort.setStatus("current")
_ClabAniNidCfgSecondaryServerIpAddressType_Type = InetAddressType
_ClabAniNidCfgSecondaryServerIpAddressType_Object = MibScalar
clabAniNidCfgSecondaryServerIpAddressType = _ClabAniNidCfgSecondaryServerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 1, 10),
    _ClabAniNidCfgSecondaryServerIpAddressType_Type()
)
clabAniNidCfgSecondaryServerIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabAniNidCfgSecondaryServerIpAddressType.setStatus("current")
_ClabAniNidCfgSecondaryServerIpAddress_Type = InetAddress
_ClabAniNidCfgSecondaryServerIpAddress_Object = MibScalar
clabAniNidCfgSecondaryServerIpAddress = _ClabAniNidCfgSecondaryServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 1, 11),
    _ClabAniNidCfgSecondaryServerIpAddress_Type()
)
clabAniNidCfgSecondaryServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabAniNidCfgSecondaryServerIpAddress.setStatus("current")
_ClabAniNidCfgSecondaryServerPort_Type = InetPortNumber
_ClabAniNidCfgSecondaryServerPort_Object = MibScalar
clabAniNidCfgSecondaryServerPort = _ClabAniNidCfgSecondaryServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 1, 12),
    _ClabAniNidCfgSecondaryServerPort_Type()
)
clabAniNidCfgSecondaryServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabAniNidCfgSecondaryServerPort.setStatus("current")
_ClabAniNidStatusObjects_ObjectIdentity = ObjectIdentity
clabAniNidStatusObjects = _ClabAniNidStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 2)
)
_ClabAniNidStatusAuthHistoryMaxTableSize_Type = Unsigned32
_ClabAniNidStatusAuthHistoryMaxTableSize_Object = MibScalar
clabAniNidStatusAuthHistoryMaxTableSize = _ClabAniNidStatusAuthHistoryMaxTableSize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 2, 1),
    _ClabAniNidStatusAuthHistoryMaxTableSize_Type()
)
clabAniNidStatusAuthHistoryMaxTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabAniNidStatusAuthHistoryMaxTableSize.setStatus("current")
_ClabAniNidStatusAuthHistoryTable_Object = MibTable
clabAniNidStatusAuthHistoryTable = _ClabAniNidStatusAuthHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 2, 2)
)
if mibBuilder.loadTexts:
    clabAniNidStatusAuthHistoryTable.setStatus("current")
_ClabAniNidStatusAuthHistoryEntry_Object = MibTableRow
clabAniNidStatusAuthHistoryEntry = _ClabAniNidStatusAuthHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 2, 2, 1)
)
clabAniNidStatusAuthHistoryEntry.setIndexNames(
    (0, "CLAB-ANI-NID-MIB", "clabAniNidStatusAuthHistoryInitiationTime"),
)
if mibBuilder.loadTexts:
    clabAniNidStatusAuthHistoryEntry.setStatus("current")
_ClabAniNidStatusAuthHistoryInitiationTime_Type = TimeTicks
_ClabAniNidStatusAuthHistoryInitiationTime_Object = MibTableColumn
clabAniNidStatusAuthHistoryInitiationTime = _ClabAniNidStatusAuthHistoryInitiationTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 2, 2, 1, 1),
    _ClabAniNidStatusAuthHistoryInitiationTime_Type()
)
clabAniNidStatusAuthHistoryInitiationTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabAniNidStatusAuthHistoryInitiationTime.setStatus("current")


class _ClabAniNidStatusAuthHistoryResults_Type(Integer32):
    """Custom type clabAniNidStatusAuthHistoryResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failedRc1", 2),
          ("failedRc2", 3),
          ("failedRc3", 4),
          ("success", 1),
          ("unknown", 0))
    )


_ClabAniNidStatusAuthHistoryResults_Type.__name__ = "Integer32"
_ClabAniNidStatusAuthHistoryResults_Object = MibTableColumn
clabAniNidStatusAuthHistoryResults = _ClabAniNidStatusAuthHistoryResults_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 2, 2, 1, 2),
    _ClabAniNidStatusAuthHistoryResults_Type()
)
clabAniNidStatusAuthHistoryResults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabAniNidStatusAuthHistoryResults.setStatus("current")


class _ClabAniNidStatusAuthHistoryServer_Type(Integer32):
    """Custom type clabAniNidStatusAuthHistoryServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1))
    )


_ClabAniNidStatusAuthHistoryServer_Type.__name__ = "Integer32"
_ClabAniNidStatusAuthHistoryServer_Object = MibTableColumn
clabAniNidStatusAuthHistoryServer = _ClabAniNidStatusAuthHistoryServer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 2, 2, 1, 3),
    _ClabAniNidStatusAuthHistoryServer_Type()
)
clabAniNidStatusAuthHistoryServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabAniNidStatusAuthHistoryServer.setStatus("current")
_ClabAniNidStatusReportCircuitTable_Object = MibTable
clabAniNidStatusReportCircuitTable = _ClabAniNidStatusReportCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 2, 3)
)
if mibBuilder.loadTexts:
    clabAniNidStatusReportCircuitTable.setStatus("current")
_ClabAniNidStatusReportCircuitEntry_Object = MibTableRow
clabAniNidStatusReportCircuitEntry = _ClabAniNidStatusReportCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 2, 3, 1)
)
clabAniNidStatusReportCircuitEntry.setIndexNames(
    (0, "CLAB-ANI-NID-MIB", "clabAniNidStatusReportCircuitIndex"),
)
if mibBuilder.loadTexts:
    clabAniNidStatusReportCircuitEntry.setStatus("current")


class _ClabAniNidStatusReportCircuitIndex_Type(Unsigned32):
    """Custom type clabAniNidStatusReportCircuitIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClabAniNidStatusReportCircuitIndex_Type.__name__ = "Unsigned32"
_ClabAniNidStatusReportCircuitIndex_Object = MibTableColumn
clabAniNidStatusReportCircuitIndex = _ClabAniNidStatusReportCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 2, 3, 1, 1),
    _ClabAniNidStatusReportCircuitIndex_Type()
)
clabAniNidStatusReportCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabAniNidStatusReportCircuitIndex.setStatus("current")
_ClabAniNidStatusReportCircuitIdentifier_Type = SnmpAdminString
_ClabAniNidStatusReportCircuitIdentifier_Object = MibTableColumn
clabAniNidStatusReportCircuitIdentifier = _ClabAniNidStatusReportCircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 2, 3, 1, 2),
    _ClabAniNidStatusReportCircuitIdentifier_Type()
)
clabAniNidStatusReportCircuitIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabAniNidStatusReportCircuitIdentifier.setStatus("current")
_ClabAniNidStatusReportCircuitTargetIdentifier_Type = SnmpAdminString
_ClabAniNidStatusReportCircuitTargetIdentifier_Object = MibTableColumn
clabAniNidStatusReportCircuitTargetIdentifier = _ClabAniNidStatusReportCircuitTargetIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 1, 2, 3, 1, 3),
    _ClabAniNidStatusReportCircuitTargetIdentifier_Type()
)
clabAniNidStatusReportCircuitTargetIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabAniNidStatusReportCircuitTargetIdentifier.setStatus("current")
_ClabAniNidMibConformance_ObjectIdentity = ObjectIdentity
clabAniNidMibConformance = _ClabAniNidMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 99)
)
_ClabAniNidMibCompliances_ObjectIdentity = ObjectIdentity
clabAniNidMibCompliances = _ClabAniNidMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 99, 1)
)
_ClabAniNidMibGroups_ObjectIdentity = ObjectIdentity
clabAniNidMibGroups = _ClabAniNidMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 99, 2)
)

# Managed Objects groups

clabAniNidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 99, 2, 1)
)
clabAniNidGroup.setObjects(
      *(("CLAB-ANI-NID-MIB", "clabAniNidCfgID"),
        ("CLAB-ANI-NID-MIB", "clabAniNidCfgPtpMcastMac"),
        ("CLAB-ANI-NID-MIB", "clabAniNidCfgTelnetEnabled"),
        ("CLAB-ANI-NID-MIB", "clabAniNidCfgTftpEnabled"),
        ("CLAB-ANI-NID-MIB", "clabAniNidCfgClientAuthStatus"),
        ("CLAB-ANI-NID-MIB", "clabAniNidCfgAuthServerServiceType"),
        ("CLAB-ANI-NID-MIB", "clabAniNidCfgPrimaryServerIpAddressType"),
        ("CLAB-ANI-NID-MIB", "clabAniNidCfgPrimaryServerIpAddress"),
        ("CLAB-ANI-NID-MIB", "clabAniNidCfgPrimaryServerPort"),
        ("CLAB-ANI-NID-MIB", "clabAniNidCfgSecondaryServerIpAddressType"),
        ("CLAB-ANI-NID-MIB", "clabAniNidCfgSecondaryServerIpAddress"),
        ("CLAB-ANI-NID-MIB", "clabAniNidCfgSecondaryServerPort"),
        ("CLAB-ANI-NID-MIB", "clabAniNidStatusAuthHistoryMaxTableSize"),
        ("CLAB-ANI-NID-MIB", "clabAniNidStatusAuthHistoryResults"),
        ("CLAB-ANI-NID-MIB", "clabAniNidStatusAuthHistoryServer"),
        ("CLAB-ANI-NID-MIB", "clabAniNidStatusReportCircuitIndex"),
        ("CLAB-ANI-NID-MIB", "clabAniNidStatusReportCircuitIdentifier"),
        ("CLAB-ANI-NID-MIB", "clabAniNidStatusReportCircuitTargetIdentifier"))
)
if mibBuilder.loadTexts:
    clabAniNidGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

clabAniNidCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 4, 8, 99, 1, 1)
)
if mibBuilder.loadTexts:
    clabAniNidCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CLAB-ANI-NID-MIB",
    **{"clabAniNidMib": clabAniNidMib,
       "clabAniNidNotifications": clabAniNidNotifications,
       "clabAniNidMibObjects": clabAniNidMibObjects,
       "clabAniNidCfgObjects": clabAniNidCfgObjects,
       "clabAniNidCfgID": clabAniNidCfgID,
       "clabAniNidCfgPtpMcastMac": clabAniNidCfgPtpMcastMac,
       "clabAniNidCfgTelnetEnabled": clabAniNidCfgTelnetEnabled,
       "clabAniNidCfgTftpEnabled": clabAniNidCfgTftpEnabled,
       "clabAniNidCfgClientAuthStatus": clabAniNidCfgClientAuthStatus,
       "clabAniNidCfgAuthServerServiceType": clabAniNidCfgAuthServerServiceType,
       "clabAniNidCfgPrimaryServerIpAddressType": clabAniNidCfgPrimaryServerIpAddressType,
       "clabAniNidCfgPrimaryServerIpAddress": clabAniNidCfgPrimaryServerIpAddress,
       "clabAniNidCfgPrimaryServerPort": clabAniNidCfgPrimaryServerPort,
       "clabAniNidCfgSecondaryServerIpAddressType": clabAniNidCfgSecondaryServerIpAddressType,
       "clabAniNidCfgSecondaryServerIpAddress": clabAniNidCfgSecondaryServerIpAddress,
       "clabAniNidCfgSecondaryServerPort": clabAniNidCfgSecondaryServerPort,
       "clabAniNidStatusObjects": clabAniNidStatusObjects,
       "clabAniNidStatusAuthHistoryMaxTableSize": clabAniNidStatusAuthHistoryMaxTableSize,
       "clabAniNidStatusAuthHistoryTable": clabAniNidStatusAuthHistoryTable,
       "clabAniNidStatusAuthHistoryEntry": clabAniNidStatusAuthHistoryEntry,
       "clabAniNidStatusAuthHistoryInitiationTime": clabAniNidStatusAuthHistoryInitiationTime,
       "clabAniNidStatusAuthHistoryResults": clabAniNidStatusAuthHistoryResults,
       "clabAniNidStatusAuthHistoryServer": clabAniNidStatusAuthHistoryServer,
       "clabAniNidStatusReportCircuitTable": clabAniNidStatusReportCircuitTable,
       "clabAniNidStatusReportCircuitEntry": clabAniNidStatusReportCircuitEntry,
       "clabAniNidStatusReportCircuitIndex": clabAniNidStatusReportCircuitIndex,
       "clabAniNidStatusReportCircuitIdentifier": clabAniNidStatusReportCircuitIdentifier,
       "clabAniNidStatusReportCircuitTargetIdentifier": clabAniNidStatusReportCircuitTargetIdentifier,
       "clabAniNidMibConformance": clabAniNidMibConformance,
       "clabAniNidMibCompliances": clabAniNidMibCompliances,
       "clabAniNidCompliance": clabAniNidCompliance,
       "clabAniNidMibGroups": clabAniNidMibGroups,
       "clabAniNidGroup": clabAniNidGroup}
)
