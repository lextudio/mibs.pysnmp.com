# SNMP MIB module (CISCO-SECURE-SHELL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SECURE-SHELL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:03 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoSecureShellMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 339)
)
ciscoSecureShellMIB.setRevisions(
        ("2005-06-01 00:00",
         "2004-04-05 00:00",
         "2003-09-18 00:00",
         "2002-10-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CssVersions(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoSecureShellMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSecureShellMIBObjects = _CiscoSecureShellMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1)
)
_CssConfiguration_ObjectIdentity = ObjectIdentity
cssConfiguration = _CssConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1)
)


class _CssServiceActivation_Type(TruthValue):
    """Custom type cssServiceActivation based on TruthValue"""


_CssServiceActivation_Object = MibScalar
cssServiceActivation = _CssServiceActivation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 1),
    _CssServiceActivation_Type()
)
cssServiceActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssServiceActivation.setStatus("current")
_CssKeyTable_Object = MibTable
cssKeyTable = _CssKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cssKeyTable.setStatus("current")
_CssKeyEntry_Object = MibTableRow
cssKeyEntry = _CssKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2, 1)
)
cssKeyEntry.setIndexNames(
    (0, "CISCO-SECURE-SHELL-MIB", "cssKeyIndex"),
)
if mibBuilder.loadTexts:
    cssKeyEntry.setStatus("current")


class _CssKeyIndex_Type(Integer32):
    """Custom type cssKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dsa", 3),
          ("rsa", 1),
          ("rsa1", 2))
    )


_CssKeyIndex_Type.__name__ = "Integer32"
_CssKeyIndex_Object = MibTableColumn
cssKeyIndex = _CssKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2, 1, 1),
    _CssKeyIndex_Type()
)
cssKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssKeyIndex.setStatus("current")


class _CssKeyNBits_Type(Integer32):
    """Custom type cssKeyNBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 2048),
    )


_CssKeyNBits_Type.__name__ = "Integer32"
_CssKeyNBits_Object = MibTableColumn
cssKeyNBits = _CssKeyNBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2, 1, 2),
    _CssKeyNBits_Type()
)
cssKeyNBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cssKeyNBits.setStatus("current")
_CssKeyOverWrite_Type = TruthValue
_CssKeyOverWrite_Object = MibTableColumn
cssKeyOverWrite = _CssKeyOverWrite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2, 1, 3),
    _CssKeyOverWrite_Type()
)
cssKeyOverWrite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cssKeyOverWrite.setStatus("current")
_CssKeyLastCreationTime_Type = TimeStamp
_CssKeyLastCreationTime_Object = MibTableColumn
cssKeyLastCreationTime = _CssKeyLastCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2, 1, 4),
    _CssKeyLastCreationTime_Type()
)
cssKeyLastCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssKeyLastCreationTime.setStatus("current")
_CssKeyRowStatus_Type = RowStatus
_CssKeyRowStatus_Object = MibTableColumn
cssKeyRowStatus = _CssKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2, 1, 5),
    _CssKeyRowStatus_Type()
)
cssKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cssKeyRowStatus.setStatus("current")


class _CssKeyString_Type(DisplayString):
    """Custom type cssKeyString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CssKeyString_Type.__name__ = "DisplayString"
_CssKeyString_Object = MibTableColumn
cssKeyString = _CssKeyString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2, 1, 6),
    _CssKeyString_Type()
)
cssKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssKeyString.setStatus("current")
_CssServiceCapability_Type = CssVersions
_CssServiceCapability_Object = MibScalar
cssServiceCapability = _CssServiceCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 3),
    _CssServiceCapability_Type()
)
cssServiceCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssServiceCapability.setStatus("current")
_CssServiceMode_Type = CssVersions
_CssServiceMode_Object = MibScalar
cssServiceMode = _CssServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 4),
    _CssServiceMode_Type()
)
cssServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssServiceMode.setStatus("current")


class _CssKeyGenerationStatus_Type(Integer32):
    """Custom type cssKeyGenerationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("inProgress", 1),
          ("successful", 2))
    )


_CssKeyGenerationStatus_Type.__name__ = "Integer32"
_CssKeyGenerationStatus_Object = MibScalar
cssKeyGenerationStatus = _CssKeyGenerationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 5),
    _CssKeyGenerationStatus_Type()
)
cssKeyGenerationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssKeyGenerationStatus.setStatus("current")
_CssSessionInfo_ObjectIdentity = ObjectIdentity
cssSessionInfo = _CssSessionInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2)
)
_CssSessionTable_Object = MibTable
cssSessionTable = _CssSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cssSessionTable.setStatus("current")
_CssSessionEntry_Object = MibTableRow
cssSessionEntry = _CssSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1)
)
cssSessionEntry.setIndexNames(
    (0, "CISCO-SECURE-SHELL-MIB", "cssSessionID"),
)
if mibBuilder.loadTexts:
    cssSessionEntry.setStatus("current")
_CssSessionID_Type = Unsigned32
_CssSessionID_Object = MibTableColumn
cssSessionID = _CssSessionID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1, 1),
    _CssSessionID_Type()
)
cssSessionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssSessionID.setStatus("current")


class _CssSessionVersion_Type(Integer32):
    """Custom type cssSessionVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_CssSessionVersion_Type.__name__ = "Integer32"
_CssSessionVersion_Object = MibTableColumn
cssSessionVersion = _CssSessionVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1, 2),
    _CssSessionVersion_Type()
)
cssSessionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssSessionVersion.setStatus("current")


class _CssSessionState_Type(Integer32):
    """Custom type cssSessionState based on Integer32"""
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
        *(("sshSessionAuthenticated", 3),
          ("sshSessionClosed", 7),
          ("sshSessionDisconnected", 6),
          ("sshSessionDisconnecting", 5),
          ("sshSessionKeysExchanged", 2),
          ("sshSessionOpen", 4),
          ("sshSessionVersionOk", 1))
    )


_CssSessionState_Type.__name__ = "Integer32"
_CssSessionState_Object = MibTableColumn
cssSessionState = _CssSessionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1, 3),
    _CssSessionState_Type()
)
cssSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssSessionState.setStatus("current")
_CssSessionPID_Type = Unsigned32
_CssSessionPID_Object = MibTableColumn
cssSessionPID = _CssSessionPID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1, 4),
    _CssSessionPID_Type()
)
cssSessionPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssSessionPID.setStatus("current")
_CssSessionUserID_Type = SnmpAdminString
_CssSessionUserID_Object = MibTableColumn
cssSessionUserID = _CssSessionUserID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1, 5),
    _CssSessionUserID_Type()
)
cssSessionUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssSessionUserID.setStatus("current")
_CssSessionHostAddrType_Type = InetAddressType
_CssSessionHostAddrType_Object = MibTableColumn
cssSessionHostAddrType = _CssSessionHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1, 6),
    _CssSessionHostAddrType_Type()
)
cssSessionHostAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssSessionHostAddrType.setStatus("current")
_CssSessionHostAddr_Type = InetAddress
_CssSessionHostAddr_Object = MibTableColumn
cssSessionHostAddr = _CssSessionHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1, 7),
    _CssSessionHostAddr_Type()
)
cssSessionHostAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssSessionHostAddr.setStatus("current")
_CiscoSecureShellMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSecureShellMIBConformance = _CiscoSecureShellMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 2)
)
_CiscoSecureShellMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSecureShellMIBCompliances = _CiscoSecureShellMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 1)
)
_CiscoSecureShellMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSecureShellMIBGroups = _CiscoSecureShellMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 2)
)

# Managed Objects groups

cssConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 2, 1)
)
cssConfigurationGroup.setObjects(
      *(("CISCO-SECURE-SHELL-MIB", "cssServiceActivation"),
        ("CISCO-SECURE-SHELL-MIB", "cssKeyNBits"),
        ("CISCO-SECURE-SHELL-MIB", "cssKeyOverWrite"),
        ("CISCO-SECURE-SHELL-MIB", "cssKeyLastCreationTime"),
        ("CISCO-SECURE-SHELL-MIB", "cssKeyRowStatus"))
)
if mibBuilder.loadTexts:
    cssConfigurationGroup.setStatus("deprecated")

cssConfigurationGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 2, 2)
)
cssConfigurationGroupRev1.setObjects(
      *(("CISCO-SECURE-SHELL-MIB", "cssServiceActivation"),
        ("CISCO-SECURE-SHELL-MIB", "cssKeyNBits"),
        ("CISCO-SECURE-SHELL-MIB", "cssKeyOverWrite"),
        ("CISCO-SECURE-SHELL-MIB", "cssKeyLastCreationTime"),
        ("CISCO-SECURE-SHELL-MIB", "cssKeyString"),
        ("CISCO-SECURE-SHELL-MIB", "cssKeyRowStatus"))
)
if mibBuilder.loadTexts:
    cssConfigurationGroupRev1.setStatus("current")

cssServiceModeCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 2, 3)
)
cssServiceModeCfgGroup.setObjects(
      *(("CISCO-SECURE-SHELL-MIB", "cssServiceCapability"),
        ("CISCO-SECURE-SHELL-MIB", "cssServiceMode"))
)
if mibBuilder.loadTexts:
    cssServiceModeCfgGroup.setStatus("current")

cssSessionInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 2, 4)
)
cssSessionInfoGroup.setObjects(
      *(("CISCO-SECURE-SHELL-MIB", "cssSessionVersion"),
        ("CISCO-SECURE-SHELL-MIB", "cssSessionState"),
        ("CISCO-SECURE-SHELL-MIB", "cssSessionPID"),
        ("CISCO-SECURE-SHELL-MIB", "cssSessionUserID"),
        ("CISCO-SECURE-SHELL-MIB", "cssSessionHostAddrType"),
        ("CISCO-SECURE-SHELL-MIB", "cssSessionHostAddr"))
)
if mibBuilder.loadTexts:
    cssSessionInfoGroup.setStatus("current")

cssConfigurationGroupSupp1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 2, 5)
)
cssConfigurationGroupSupp1.setObjects(
    ("CISCO-SECURE-SHELL-MIB", "cssKeyGenerationStatus")
)
if mibBuilder.loadTexts:
    cssConfigurationGroupSupp1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSecureShellMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSecureShellMIBCompliance.setStatus(
        "deprecated"
    )

ciscoSecureShellMIBComplianceRv1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoSecureShellMIBComplianceRv1.setStatus(
        "deprecated"
    )

ciscoSecureShellMIBComplianceRv2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoSecureShellMIBComplianceRv2.setStatus(
        "deprecated"
    )

ciscoSecureShellMIBComplianceRv3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoSecureShellMIBComplianceRv3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SECURE-SHELL-MIB",
    **{"CssVersions": CssVersions,
       "ciscoSecureShellMIB": ciscoSecureShellMIB,
       "ciscoSecureShellMIBObjects": ciscoSecureShellMIBObjects,
       "cssConfiguration": cssConfiguration,
       "cssServiceActivation": cssServiceActivation,
       "cssKeyTable": cssKeyTable,
       "cssKeyEntry": cssKeyEntry,
       "cssKeyIndex": cssKeyIndex,
       "cssKeyNBits": cssKeyNBits,
       "cssKeyOverWrite": cssKeyOverWrite,
       "cssKeyLastCreationTime": cssKeyLastCreationTime,
       "cssKeyRowStatus": cssKeyRowStatus,
       "cssKeyString": cssKeyString,
       "cssServiceCapability": cssServiceCapability,
       "cssServiceMode": cssServiceMode,
       "cssKeyGenerationStatus": cssKeyGenerationStatus,
       "cssSessionInfo": cssSessionInfo,
       "cssSessionTable": cssSessionTable,
       "cssSessionEntry": cssSessionEntry,
       "cssSessionID": cssSessionID,
       "cssSessionVersion": cssSessionVersion,
       "cssSessionState": cssSessionState,
       "cssSessionPID": cssSessionPID,
       "cssSessionUserID": cssSessionUserID,
       "cssSessionHostAddrType": cssSessionHostAddrType,
       "cssSessionHostAddr": cssSessionHostAddr,
       "ciscoSecureShellMIBConformance": ciscoSecureShellMIBConformance,
       "ciscoSecureShellMIBCompliances": ciscoSecureShellMIBCompliances,
       "ciscoSecureShellMIBCompliance": ciscoSecureShellMIBCompliance,
       "ciscoSecureShellMIBComplianceRv1": ciscoSecureShellMIBComplianceRv1,
       "ciscoSecureShellMIBComplianceRv2": ciscoSecureShellMIBComplianceRv2,
       "ciscoSecureShellMIBComplianceRv3": ciscoSecureShellMIBComplianceRv3,
       "ciscoSecureShellMIBGroups": ciscoSecureShellMIBGroups,
       "cssConfigurationGroup": cssConfigurationGroup,
       "cssConfigurationGroupRev1": cssConfigurationGroupRev1,
       "cssServiceModeCfgGroup": cssServiceModeCfgGroup,
       "cssSessionInfoGroup": cssSessionInfoGroup,
       "cssConfigurationGroupSupp1": cssConfigurationGroupSupp1}
)
