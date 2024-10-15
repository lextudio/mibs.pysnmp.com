# SNMP MIB module (CISCO-UNITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:34 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoUnityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 385)
)
ciscoUnityMIB.setRevisions(
        ("2005-12-12 00:00",
         "2004-01-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoUnityIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class CiscoUnityServerStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("running", 3),
          ("starting", 2),
          ("stopped", 1),
          ("stopping", 4))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoUnityMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoUnityMIBNotifs = _CiscoUnityMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 0)
)
_CiscoUnityMIBObjects_ObjectIdentity = ObjectIdentity
ciscoUnityMIBObjects = _CiscoUnityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1)
)
_CiscoUnityGeneralInfo_ObjectIdentity = ObjectIdentity
ciscoUnityGeneralInfo = _CiscoUnityGeneralInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1)
)
_CiscoUnityTable_Object = MibTable
ciscoUnityTable = _CiscoUnityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoUnityTable.setStatus("current")
_CiscoUnityEntry_Object = MibTableRow
ciscoUnityEntry = _CiscoUnityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 1, 1)
)
ciscoUnityEntry.setIndexNames(
    (0, "CISCO-UNITY-MIB", "ciscoUnityIndex"),
)
if mibBuilder.loadTexts:
    ciscoUnityEntry.setStatus("current")
_CiscoUnityIndex_Type = CiscoUnityIndex
_CiscoUnityIndex_Object = MibTableColumn
ciscoUnityIndex = _CiscoUnityIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 1, 1, 1),
    _CiscoUnityIndex_Type()
)
ciscoUnityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoUnityIndex.setStatus("current")
_CiscoUnityName_Type = SnmpAdminString
_CiscoUnityName_Object = MibTableColumn
ciscoUnityName = _CiscoUnityName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 1, 1, 2),
    _CiscoUnityName_Type()
)
ciscoUnityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityName.setStatus("current")


class _CiscoUnityVersion_Type(SnmpAdminString):
    """Custom type ciscoUnityVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CiscoUnityVersion_Type.__name__ = "SnmpAdminString"
_CiscoUnityVersion_Object = MibTableColumn
ciscoUnityVersion = _CiscoUnityVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 1, 1, 3),
    _CiscoUnityVersion_Type()
)
ciscoUnityVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityVersion.setStatus("current")
_CiscoUnityPortTable_Object = MibTable
ciscoUnityPortTable = _CiscoUnityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoUnityPortTable.setStatus("current")
_CiscoUnityPortEntry_Object = MibTableRow
ciscoUnityPortEntry = _CiscoUnityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1)
)
ciscoUnityPortEntry.setIndexNames(
    (0, "CISCO-UNITY-MIB", "ciscoUnityPortIndex"),
)
if mibBuilder.loadTexts:
    ciscoUnityPortEntry.setStatus("current")
_CiscoUnityPortIndex_Type = CiscoUnityIndex
_CiscoUnityPortIndex_Object = MibTableColumn
ciscoUnityPortIndex = _CiscoUnityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 1),
    _CiscoUnityPortIndex_Type()
)
ciscoUnityPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoUnityPortIndex.setStatus("current")


class _CiscoUnityPortNumber_Type(Unsigned32):
    """Custom type ciscoUnityPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiscoUnityPortNumber_Type.__name__ = "Unsigned32"
_CiscoUnityPortNumber_Object = MibTableColumn
ciscoUnityPortNumber = _CiscoUnityPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 2),
    _CiscoUnityPortNumber_Type()
)
ciscoUnityPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityPortNumber.setStatus("current")


class _CiscoUnityPortIntegration_Type(SnmpAdminString):
    """Custom type ciscoUnityPortIntegration based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CiscoUnityPortIntegration_Type.__name__ = "SnmpAdminString"
_CiscoUnityPortIntegration_Object = MibTableColumn
ciscoUnityPortIntegration = _CiscoUnityPortIntegration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 3),
    _CiscoUnityPortIntegration_Type()
)
ciscoUnityPortIntegration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityPortIntegration.setStatus("current")


class _CiscoUnityPortExtension_Type(SnmpAdminString):
    """Custom type ciscoUnityPortExtension based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CiscoUnityPortExtension_Type.__name__ = "SnmpAdminString"
_CiscoUnityPortExtension_Object = MibTableColumn
ciscoUnityPortExtension = _CiscoUnityPortExtension_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 4),
    _CiscoUnityPortExtension_Type()
)
ciscoUnityPortExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityPortExtension.setStatus("current")
_CiscoUnityPortEnabled_Type = TruthValue
_CiscoUnityPortEnabled_Object = MibTableColumn
ciscoUnityPortEnabled = _CiscoUnityPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 5),
    _CiscoUnityPortEnabled_Type()
)
ciscoUnityPortEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityPortEnabled.setStatus("current")
_CiscoUnityPortAnswerCalls_Type = TruthValue
_CiscoUnityPortAnswerCalls_Object = MibTableColumn
ciscoUnityPortAnswerCalls = _CiscoUnityPortAnswerCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 6),
    _CiscoUnityPortAnswerCalls_Type()
)
ciscoUnityPortAnswerCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityPortAnswerCalls.setStatus("current")
_CiscoUnityPortMessageNotif_Type = TruthValue
_CiscoUnityPortMessageNotif_Object = MibTableColumn
ciscoUnityPortMessageNotif = _CiscoUnityPortMessageNotif_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 7),
    _CiscoUnityPortMessageNotif_Type()
)
ciscoUnityPortMessageNotif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityPortMessageNotif.setStatus("current")
_CiscoUnityPortDialoutMWI_Type = TruthValue
_CiscoUnityPortDialoutMWI_Object = MibTableColumn
ciscoUnityPortDialoutMWI = _CiscoUnityPortDialoutMWI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 8),
    _CiscoUnityPortDialoutMWI_Type()
)
ciscoUnityPortDialoutMWI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityPortDialoutMWI.setStatus("current")
_CiscoUnityPortAMISDelivery_Type = TruthValue
_CiscoUnityPortAMISDelivery_Object = MibTableColumn
ciscoUnityPortAMISDelivery = _CiscoUnityPortAMISDelivery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 9),
    _CiscoUnityPortAMISDelivery_Type()
)
ciscoUnityPortAMISDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityPortAMISDelivery.setStatus("current")
_CiscoUnityPortTRAPConnection_Type = TruthValue
_CiscoUnityPortTRAPConnection_Object = MibTableColumn
ciscoUnityPortTRAPConnection = _CiscoUnityPortTRAPConnection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 10),
    _CiscoUnityPortTRAPConnection_Type()
)
ciscoUnityPortTRAPConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityPortTRAPConnection.setStatus("current")
_CiscoUnityPortActivity_Type = SnmpAdminString
_CiscoUnityPortActivity_Object = MibTableColumn
ciscoUnityPortActivity = _CiscoUnityPortActivity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 11),
    _CiscoUnityPortActivity_Type()
)
ciscoUnityPortActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityPortActivity.setStatus("current")


class _CiscoUnityPortObjectId_Type(SnmpAdminString):
    """Custom type ciscoUnityPortObjectId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_CiscoUnityPortObjectId_Type.__name__ = "SnmpAdminString"
_CiscoUnityPortObjectId_Object = MibTableColumn
ciscoUnityPortObjectId = _CiscoUnityPortObjectId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 12),
    _CiscoUnityPortObjectId_Type()
)
ciscoUnityPortObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityPortObjectId.setStatus("current")
_CiscoUnityGlobalInfo_ObjectIdentity = ObjectIdentity
ciscoUnityGlobalInfo = _CiscoUnityGlobalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2)
)
_CiscoUnityServerState_Type = CiscoUnityServerStatus
_CiscoUnityServerState_Object = MibScalar
ciscoUnityServerState = _CiscoUnityServerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 1),
    _CiscoUnityServerState_Type()
)
ciscoUnityServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityServerState.setStatus("current")


class _CiscoUnityPorts_Type(Unsigned32):
    """Custom type ciscoUnityPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiscoUnityPorts_Type.__name__ = "Unsigned32"
_CiscoUnityPorts_Object = MibScalar
ciscoUnityPorts = _CiscoUnityPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 2),
    _CiscoUnityPorts_Type()
)
ciscoUnityPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityPorts.setStatus("current")


class _CiscoUnityPortsActive_Type(Unsigned32):
    """Custom type ciscoUnityPortsActive based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiscoUnityPortsActive_Type.__name__ = "Unsigned32"
_CiscoUnityPortsActive_Object = MibScalar
ciscoUnityPortsActive = _CiscoUnityPortsActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 3),
    _CiscoUnityPortsActive_Type()
)
ciscoUnityPortsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityPortsActive.setStatus("current")


class _CiscoUnityPortsInbound_Type(Unsigned32):
    """Custom type ciscoUnityPortsInbound based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiscoUnityPortsInbound_Type.__name__ = "Unsigned32"
_CiscoUnityPortsInbound_Object = MibScalar
ciscoUnityPortsInbound = _CiscoUnityPortsInbound_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 4),
    _CiscoUnityPortsInbound_Type()
)
ciscoUnityPortsInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityPortsInbound.setStatus("current")


class _CiscoUnityPortsInboundActive_Type(Unsigned32):
    """Custom type ciscoUnityPortsInboundActive based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiscoUnityPortsInboundActive_Type.__name__ = "Unsigned32"
_CiscoUnityPortsInboundActive_Object = MibScalar
ciscoUnityPortsInboundActive = _CiscoUnityPortsInboundActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 5),
    _CiscoUnityPortsInboundActive_Type()
)
ciscoUnityPortsInboundActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityPortsInboundActive.setStatus("current")


class _CiscoUnityPortsOutbound_Type(Unsigned32):
    """Custom type ciscoUnityPortsOutbound based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiscoUnityPortsOutbound_Type.__name__ = "Unsigned32"
_CiscoUnityPortsOutbound_Object = MibScalar
ciscoUnityPortsOutbound = _CiscoUnityPortsOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 6),
    _CiscoUnityPortsOutbound_Type()
)
ciscoUnityPortsOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityPortsOutbound.setStatus("current")


class _CiscoUnityPortsOutboundActive_Type(Unsigned32):
    """Custom type ciscoUnityPortsOutboundActive based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiscoUnityPortsOutboundActive_Type.__name__ = "Unsigned32"
_CiscoUnityPortsOutboundActive_Object = MibScalar
ciscoUnityPortsOutboundActive = _CiscoUnityPortsOutboundActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 7),
    _CiscoUnityPortsOutboundActive_Type()
)
ciscoUnityPortsOutboundActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityPortsOutboundActive.setStatus("current")


class _CiscoUnityLicLanguagesMax_Type(Unsigned32):
    """Custom type ciscoUnityLicLanguagesMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiscoUnityLicLanguagesMax_Type.__name__ = "Unsigned32"
_CiscoUnityLicLanguagesMax_Object = MibScalar
ciscoUnityLicLanguagesMax = _CiscoUnityLicLanguagesMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 8),
    _CiscoUnityLicLanguagesMax_Type()
)
ciscoUnityLicLanguagesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityLicLanguagesMax.setStatus("current")


class _CiscoUnityLicTTSSessionsMax_Type(Unsigned32):
    """Custom type ciscoUnityLicTTSSessionsMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiscoUnityLicTTSSessionsMax_Type.__name__ = "Unsigned32"
_CiscoUnityLicTTSSessionsMax_Object = MibScalar
ciscoUnityLicTTSSessionsMax = _CiscoUnityLicTTSSessionsMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 9),
    _CiscoUnityLicTTSSessionsMax_Type()
)
ciscoUnityLicTTSSessionsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityLicTTSSessionsMax.setStatus("current")


class _CiscoUnityLicSubscribersMax_Type(Unsigned32):
    """Custom type ciscoUnityLicSubscribersMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoUnityLicSubscribersMax_Type.__name__ = "Unsigned32"
_CiscoUnityLicSubscribersMax_Object = MibScalar
ciscoUnityLicSubscribersMax = _CiscoUnityLicSubscribersMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 10),
    _CiscoUnityLicSubscribersMax_Type()
)
ciscoUnityLicSubscribersMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityLicSubscribersMax.setStatus("current")


class _CiscoUnityLicUMSubscribersMax_Type(Unsigned32):
    """Custom type ciscoUnityLicUMSubscribersMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoUnityLicUMSubscribersMax_Type.__name__ = "Unsigned32"
_CiscoUnityLicUMSubscribersMax_Object = MibScalar
ciscoUnityLicUMSubscribersMax = _CiscoUnityLicUMSubscribersMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 11),
    _CiscoUnityLicUMSubscribersMax_Type()
)
ciscoUnityLicUMSubscribersMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityLicUMSubscribersMax.setStatus("current")


class _CiscoUnityLicVMISubscribersMax_Type(Unsigned32):
    """Custom type ciscoUnityLicVMISubscribersMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoUnityLicVMISubscribersMax_Type.__name__ = "Unsigned32"
_CiscoUnityLicVMISubscribersMax_Object = MibScalar
ciscoUnityLicVMISubscribersMax = _CiscoUnityLicVMISubscribersMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 12),
    _CiscoUnityLicVMISubscribersMax_Type()
)
ciscoUnityLicVMISubscribersMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityLicVMISubscribersMax.setStatus("current")


class _CiscoUnityLicVoicePortsMax_Type(Unsigned32):
    """Custom type ciscoUnityLicVoicePortsMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiscoUnityLicVoicePortsMax_Type.__name__ = "Unsigned32"
_CiscoUnityLicVoicePortsMax_Object = MibScalar
ciscoUnityLicVoicePortsMax = _CiscoUnityLicVoicePortsMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 13),
    _CiscoUnityLicVoicePortsMax_Type()
)
ciscoUnityLicVoicePortsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityLicVoicePortsMax.setStatus("current")


class _CiscoUnityLicBridgeSessionsMax_Type(Unsigned32):
    """Custom type ciscoUnityLicBridgeSessionsMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiscoUnityLicBridgeSessionsMax_Type.__name__ = "Unsigned32"
_CiscoUnityLicBridgeSessionsMax_Object = MibScalar
ciscoUnityLicBridgeSessionsMax = _CiscoUnityLicBridgeSessionsMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 14),
    _CiscoUnityLicBridgeSessionsMax_Type()
)
ciscoUnityLicBridgeSessionsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityLicBridgeSessionsMax.setStatus("current")
_CiscoUnityLicAMISIsLicensed_Type = TruthValue
_CiscoUnityLicAMISIsLicensed_Object = MibScalar
ciscoUnityLicAMISIsLicensed = _CiscoUnityLicAMISIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 15),
    _CiscoUnityLicAMISIsLicensed_Type()
)
ciscoUnityLicAMISIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityLicAMISIsLicensed.setStatus("current")
_CiscoUnityLicMaxMsgRecLenIsLic_Type = TruthValue
_CiscoUnityLicMaxMsgRecLenIsLic_Object = MibScalar
ciscoUnityLicMaxMsgRecLenIsLic = _CiscoUnityLicMaxMsgRecLenIsLic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 16),
    _CiscoUnityLicMaxMsgRecLenIsLic_Type()
)
ciscoUnityLicMaxMsgRecLenIsLic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityLicMaxMsgRecLenIsLic.setStatus("current")
_CiscoUnityLicPoolingIsEnabled_Type = TruthValue
_CiscoUnityLicPoolingIsEnabled_Object = MibScalar
ciscoUnityLicPoolingIsEnabled = _CiscoUnityLicPoolingIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 17),
    _CiscoUnityLicPoolingIsEnabled_Type()
)
ciscoUnityLicPoolingIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityLicPoolingIsEnabled.setStatus("current")
_CiscoUnityLicVPIMIsLicensed_Type = TruthValue
_CiscoUnityLicVPIMIsLicensed_Object = MibScalar
ciscoUnityLicVPIMIsLicensed = _CiscoUnityLicVPIMIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 18),
    _CiscoUnityLicVPIMIsLicensed_Type()
)
ciscoUnityLicVPIMIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityLicVPIMIsLicensed.setStatus("current")
_CiscoUnityLicPrimaryServerIsLic_Type = TruthValue
_CiscoUnityLicPrimaryServerIsLic_Object = MibScalar
ciscoUnityLicPrimaryServerIsLic = _CiscoUnityLicPrimaryServerIsLic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 19),
    _CiscoUnityLicPrimaryServerIsLic_Type()
)
ciscoUnityLicPrimaryServerIsLic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityLicPrimaryServerIsLic.setStatus("current")
_CiscoUnityLicSecondServerIsLic_Type = TruthValue
_CiscoUnityLicSecondServerIsLic_Object = MibScalar
ciscoUnityLicSecondServerIsLic = _CiscoUnityLicSecondServerIsLic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 20),
    _CiscoUnityLicSecondServerIsLic_Type()
)
ciscoUnityLicSecondServerIsLic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityLicSecondServerIsLic.setStatus("current")


class _CiscoUnityLicUtilSecondServer_Type(Unsigned32):
    """Custom type ciscoUnityLicUtilSecondServer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CiscoUnityLicUtilSecondServer_Type.__name__ = "Unsigned32"
_CiscoUnityLicUtilSecondServer_Object = MibScalar
ciscoUnityLicUtilSecondServer = _CiscoUnityLicUtilSecondServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 21),
    _CiscoUnityLicUtilSecondServer_Type()
)
ciscoUnityLicUtilSecondServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityLicUtilSecondServer.setStatus("current")


class _CiscoUnityLicUtilSubs_Type(Unsigned32):
    """Custom type ciscoUnityLicUtilSubs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoUnityLicUtilSubs_Type.__name__ = "Unsigned32"
_CiscoUnityLicUtilSubs_Object = MibScalar
ciscoUnityLicUtilSubs = _CiscoUnityLicUtilSubs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 22),
    _CiscoUnityLicUtilSubs_Type()
)
ciscoUnityLicUtilSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityLicUtilSubs.setStatus("current")


class _CiscoUnityLicUtilVMISubs_Type(Unsigned32):
    """Custom type ciscoUnityLicUtilVMISubs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoUnityLicUtilVMISubs_Type.__name__ = "Unsigned32"
_CiscoUnityLicUtilVMISubs_Object = MibScalar
ciscoUnityLicUtilVMISubs = _CiscoUnityLicUtilVMISubs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 23),
    _CiscoUnityLicUtilVMISubs_Type()
)
ciscoUnityLicUtilVMISubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUnityLicUtilVMISubs.setStatus("current")
_CiscoUnityNotificationsInfo_ObjectIdentity = ObjectIdentity
ciscoUnityNotificationsInfo = _CiscoUnityNotificationsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 3)
)


class _CiscoUnityEventType_Type(Integer32):
    """Custom type ciscoUnityEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("informational", 3),
          ("warning", 2))
    )


_CiscoUnityEventType_Type.__name__ = "Integer32"
_CiscoUnityEventType_Object = MibScalar
ciscoUnityEventType = _CiscoUnityEventType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 3, 1),
    _CiscoUnityEventType_Type()
)
ciscoUnityEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciscoUnityEventType.setStatus("current")
_CiscoUnityEventSource_Type = SnmpAdminString
_CiscoUnityEventSource_Object = MibScalar
ciscoUnityEventSource = _CiscoUnityEventSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 3, 2),
    _CiscoUnityEventSource_Type()
)
ciscoUnityEventSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciscoUnityEventSource.setStatus("current")
_CiscoUnityEventCategory_Type = SnmpAdminString
_CiscoUnityEventCategory_Object = MibScalar
ciscoUnityEventCategory = _CiscoUnityEventCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 3, 3),
    _CiscoUnityEventCategory_Type()
)
ciscoUnityEventCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciscoUnityEventCategory.setStatus("current")


class _CiscoUnityEventId_Type(Unsigned32):
    """Custom type ciscoUnityEventId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoUnityEventId_Type.__name__ = "Unsigned32"
_CiscoUnityEventId_Object = MibScalar
ciscoUnityEventId = _CiscoUnityEventId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 3, 4),
    _CiscoUnityEventId_Type()
)
ciscoUnityEventId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciscoUnityEventId.setStatus("current")
_CiscoUnityEventDate_Type = DateAndTime
_CiscoUnityEventDate_Object = MibScalar
ciscoUnityEventDate = _CiscoUnityEventDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 3, 5),
    _CiscoUnityEventDate_Type()
)
ciscoUnityEventDate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciscoUnityEventDate.setStatus("current")
_CiscoUnityEventUser_Type = SnmpAdminString
_CiscoUnityEventUser_Object = MibScalar
ciscoUnityEventUser = _CiscoUnityEventUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 3, 6),
    _CiscoUnityEventUser_Type()
)
ciscoUnityEventUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciscoUnityEventUser.setStatus("current")
_CiscoUnityEventComputer_Type = SnmpAdminString
_CiscoUnityEventComputer_Object = MibScalar
ciscoUnityEventComputer = _CiscoUnityEventComputer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 3, 7),
    _CiscoUnityEventComputer_Type()
)
ciscoUnityEventComputer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciscoUnityEventComputer.setStatus("current")
_CiscoUnityEventDescription_Type = SnmpAdminString
_CiscoUnityEventDescription_Object = MibScalar
ciscoUnityEventDescription = _CiscoUnityEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 3, 8),
    _CiscoUnityEventDescription_Type()
)
ciscoUnityEventDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciscoUnityEventDescription.setStatus("current")
_CiscoUnityEventEMSNotes_Type = SnmpAdminString
_CiscoUnityEventEMSNotes_Object = MibScalar
ciscoUnityEventEMSNotes = _CiscoUnityEventEMSNotes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 3, 9),
    _CiscoUnityEventEMSNotes_Type()
)
ciscoUnityEventEMSNotes.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciscoUnityEventEMSNotes.setStatus("current")
_CiscoUnityMIBConform_ObjectIdentity = ObjectIdentity
ciscoUnityMIBConform = _CiscoUnityMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 2)
)
_CiscoUnityMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoUnityMIBCompliances = _CiscoUnityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 2, 1)
)
_CiscoUnityMIBGroups_ObjectIdentity = ObjectIdentity
ciscoUnityMIBGroups = _CiscoUnityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 2, 2)
)

# Managed Objects groups

ciscoUnityInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 2, 2, 1)
)
ciscoUnityInfoGroup.setObjects(
      *(("CISCO-UNITY-MIB", "ciscoUnityName"),
        ("CISCO-UNITY-MIB", "ciscoUnityVersion"),
        ("CISCO-UNITY-MIB", "ciscoUnityServerState"),
        ("CISCO-UNITY-MIB", "ciscoUnityPorts"),
        ("CISCO-UNITY-MIB", "ciscoUnityPortsActive"),
        ("CISCO-UNITY-MIB", "ciscoUnityPortsInbound"),
        ("CISCO-UNITY-MIB", "ciscoUnityPortsInboundActive"),
        ("CISCO-UNITY-MIB", "ciscoUnityPortsOutbound"),
        ("CISCO-UNITY-MIB", "ciscoUnityPortsOutboundActive"))
)
if mibBuilder.loadTexts:
    ciscoUnityInfoGroup.setStatus("current")

ciscoUnityPortInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 2, 2, 2)
)
ciscoUnityPortInfoGroup.setObjects(
      *(("CISCO-UNITY-MIB", "ciscoUnityPortNumber"),
        ("CISCO-UNITY-MIB", "ciscoUnityPortIntegration"),
        ("CISCO-UNITY-MIB", "ciscoUnityPortExtension"),
        ("CISCO-UNITY-MIB", "ciscoUnityPortEnabled"),
        ("CISCO-UNITY-MIB", "ciscoUnityPortAnswerCalls"),
        ("CISCO-UNITY-MIB", "ciscoUnityPortMessageNotif"),
        ("CISCO-UNITY-MIB", "ciscoUnityPortDialoutMWI"),
        ("CISCO-UNITY-MIB", "ciscoUnityPortAMISDelivery"),
        ("CISCO-UNITY-MIB", "ciscoUnityPortTRAPConnection"))
)
if mibBuilder.loadTexts:
    ciscoUnityPortInfoGroup.setStatus("current")

ciscoUnityNotificationsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 2, 2, 3)
)
ciscoUnityNotificationsInfoGroup.setObjects(
      *(("CISCO-UNITY-MIB", "ciscoUnityEventType"),
        ("CISCO-UNITY-MIB", "ciscoUnityEventSource"),
        ("CISCO-UNITY-MIB", "ciscoUnityEventCategory"),
        ("CISCO-UNITY-MIB", "ciscoUnityEventId"),
        ("CISCO-UNITY-MIB", "ciscoUnityEventDate"),
        ("CISCO-UNITY-MIB", "ciscoUnityEventUser"),
        ("CISCO-UNITY-MIB", "ciscoUnityEventComputer"),
        ("CISCO-UNITY-MIB", "ciscoUnityEventDescription"),
        ("CISCO-UNITY-MIB", "ciscoUnityEventEMSNotes"))
)
if mibBuilder.loadTexts:
    ciscoUnityNotificationsInfoGroup.setStatus("current")

ciscoUnityLicInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 2, 2, 5)
)
ciscoUnityLicInfoGroup.setObjects(
      *(("CISCO-UNITY-MIB", "ciscoUnityLicLanguagesMax"),
        ("CISCO-UNITY-MIB", "ciscoUnityLicTTSSessionsMax"),
        ("CISCO-UNITY-MIB", "ciscoUnityLicSubscribersMax"),
        ("CISCO-UNITY-MIB", "ciscoUnityLicUMSubscribersMax"),
        ("CISCO-UNITY-MIB", "ciscoUnityLicVMISubscribersMax"),
        ("CISCO-UNITY-MIB", "ciscoUnityLicVoicePortsMax"),
        ("CISCO-UNITY-MIB", "ciscoUnityLicBridgeSessionsMax"),
        ("CISCO-UNITY-MIB", "ciscoUnityLicAMISIsLicensed"),
        ("CISCO-UNITY-MIB", "ciscoUnityLicMaxMsgRecLenIsLic"),
        ("CISCO-UNITY-MIB", "ciscoUnityLicPoolingIsEnabled"),
        ("CISCO-UNITY-MIB", "ciscoUnityLicVPIMIsLicensed"),
        ("CISCO-UNITY-MIB", "ciscoUnityLicPrimaryServerIsLic"),
        ("CISCO-UNITY-MIB", "ciscoUnityLicSecondServerIsLic"),
        ("CISCO-UNITY-MIB", "ciscoUnityLicUtilSecondServer"),
        ("CISCO-UNITY-MIB", "ciscoUnityLicUtilSubs"),
        ("CISCO-UNITY-MIB", "ciscoUnityLicUtilVMISubs"))
)
if mibBuilder.loadTexts:
    ciscoUnityLicInfoGroup.setStatus("current")

ciscoUnityPortInfoGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 2, 2, 6)
)
ciscoUnityPortInfoGroup2.setObjects(
    ("CISCO-UNITY-MIB", "ciscoUnityPortActivity")
)
if mibBuilder.loadTexts:
    ciscoUnityPortInfoGroup2.setStatus("current")

ciscoUnityPortInfoGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 2, 2, 7)
)
ciscoUnityPortInfoGroup3.setObjects(
    ("CISCO-UNITY-MIB", "ciscoUnityPortObjectId")
)
if mibBuilder.loadTexts:
    ciscoUnityPortInfoGroup3.setStatus("current")


# Notification objects

ciscoUnityMonitoredEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 0, 1)
)
ciscoUnityMonitoredEvent.setObjects(
      *(("CISCO-UNITY-MIB", "ciscoUnityEventType"),
        ("CISCO-UNITY-MIB", "ciscoUnityEventSource"),
        ("CISCO-UNITY-MIB", "ciscoUnityEventCategory"),
        ("CISCO-UNITY-MIB", "ciscoUnityEventId"),
        ("CISCO-UNITY-MIB", "ciscoUnityEventDate"),
        ("CISCO-UNITY-MIB", "ciscoUnityEventUser"),
        ("CISCO-UNITY-MIB", "ciscoUnityEventComputer"),
        ("CISCO-UNITY-MIB", "ciscoUnityEventDescription"),
        ("CISCO-UNITY-MIB", "ciscoUnityEventEMSNotes"))
)
if mibBuilder.loadTexts:
    ciscoUnityMonitoredEvent.setStatus(
        "current"
    )


# Notifications groups

ciscoUnityNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 2, 2, 4)
)
ciscoUnityNotificationsGroup.setObjects(
    ("CISCO-UNITY-MIB", "ciscoUnityMonitoredEvent")
)
if mibBuilder.loadTexts:
    ciscoUnityNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoUnityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoUnityMIBCompliance.setStatus(
        "deprecated"
    )

ciscoUnityMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 385, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoUnityMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNITY-MIB",
    **{"CiscoUnityIndex": CiscoUnityIndex,
       "CiscoUnityServerStatus": CiscoUnityServerStatus,
       "ciscoUnityMIB": ciscoUnityMIB,
       "ciscoUnityMIBNotifs": ciscoUnityMIBNotifs,
       "ciscoUnityMonitoredEvent": ciscoUnityMonitoredEvent,
       "ciscoUnityMIBObjects": ciscoUnityMIBObjects,
       "ciscoUnityGeneralInfo": ciscoUnityGeneralInfo,
       "ciscoUnityTable": ciscoUnityTable,
       "ciscoUnityEntry": ciscoUnityEntry,
       "ciscoUnityIndex": ciscoUnityIndex,
       "ciscoUnityName": ciscoUnityName,
       "ciscoUnityVersion": ciscoUnityVersion,
       "ciscoUnityPortTable": ciscoUnityPortTable,
       "ciscoUnityPortEntry": ciscoUnityPortEntry,
       "ciscoUnityPortIndex": ciscoUnityPortIndex,
       "ciscoUnityPortNumber": ciscoUnityPortNumber,
       "ciscoUnityPortIntegration": ciscoUnityPortIntegration,
       "ciscoUnityPortExtension": ciscoUnityPortExtension,
       "ciscoUnityPortEnabled": ciscoUnityPortEnabled,
       "ciscoUnityPortAnswerCalls": ciscoUnityPortAnswerCalls,
       "ciscoUnityPortMessageNotif": ciscoUnityPortMessageNotif,
       "ciscoUnityPortDialoutMWI": ciscoUnityPortDialoutMWI,
       "ciscoUnityPortAMISDelivery": ciscoUnityPortAMISDelivery,
       "ciscoUnityPortTRAPConnection": ciscoUnityPortTRAPConnection,
       "ciscoUnityPortActivity": ciscoUnityPortActivity,
       "ciscoUnityPortObjectId": ciscoUnityPortObjectId,
       "ciscoUnityGlobalInfo": ciscoUnityGlobalInfo,
       "ciscoUnityServerState": ciscoUnityServerState,
       "ciscoUnityPorts": ciscoUnityPorts,
       "ciscoUnityPortsActive": ciscoUnityPortsActive,
       "ciscoUnityPortsInbound": ciscoUnityPortsInbound,
       "ciscoUnityPortsInboundActive": ciscoUnityPortsInboundActive,
       "ciscoUnityPortsOutbound": ciscoUnityPortsOutbound,
       "ciscoUnityPortsOutboundActive": ciscoUnityPortsOutboundActive,
       "ciscoUnityLicLanguagesMax": ciscoUnityLicLanguagesMax,
       "ciscoUnityLicTTSSessionsMax": ciscoUnityLicTTSSessionsMax,
       "ciscoUnityLicSubscribersMax": ciscoUnityLicSubscribersMax,
       "ciscoUnityLicUMSubscribersMax": ciscoUnityLicUMSubscribersMax,
       "ciscoUnityLicVMISubscribersMax": ciscoUnityLicVMISubscribersMax,
       "ciscoUnityLicVoicePortsMax": ciscoUnityLicVoicePortsMax,
       "ciscoUnityLicBridgeSessionsMax": ciscoUnityLicBridgeSessionsMax,
       "ciscoUnityLicAMISIsLicensed": ciscoUnityLicAMISIsLicensed,
       "ciscoUnityLicMaxMsgRecLenIsLic": ciscoUnityLicMaxMsgRecLenIsLic,
       "ciscoUnityLicPoolingIsEnabled": ciscoUnityLicPoolingIsEnabled,
       "ciscoUnityLicVPIMIsLicensed": ciscoUnityLicVPIMIsLicensed,
       "ciscoUnityLicPrimaryServerIsLic": ciscoUnityLicPrimaryServerIsLic,
       "ciscoUnityLicSecondServerIsLic": ciscoUnityLicSecondServerIsLic,
       "ciscoUnityLicUtilSecondServer": ciscoUnityLicUtilSecondServer,
       "ciscoUnityLicUtilSubs": ciscoUnityLicUtilSubs,
       "ciscoUnityLicUtilVMISubs": ciscoUnityLicUtilVMISubs,
       "ciscoUnityNotificationsInfo": ciscoUnityNotificationsInfo,
       "ciscoUnityEventType": ciscoUnityEventType,
       "ciscoUnityEventSource": ciscoUnityEventSource,
       "ciscoUnityEventCategory": ciscoUnityEventCategory,
       "ciscoUnityEventId": ciscoUnityEventId,
       "ciscoUnityEventDate": ciscoUnityEventDate,
       "ciscoUnityEventUser": ciscoUnityEventUser,
       "ciscoUnityEventComputer": ciscoUnityEventComputer,
       "ciscoUnityEventDescription": ciscoUnityEventDescription,
       "ciscoUnityEventEMSNotes": ciscoUnityEventEMSNotes,
       "ciscoUnityMIBConform": ciscoUnityMIBConform,
       "ciscoUnityMIBCompliances": ciscoUnityMIBCompliances,
       "ciscoUnityMIBCompliance": ciscoUnityMIBCompliance,
       "ciscoUnityMIBComplianceRev1": ciscoUnityMIBComplianceRev1,
       "ciscoUnityMIBGroups": ciscoUnityMIBGroups,
       "ciscoUnityInfoGroup": ciscoUnityInfoGroup,
       "ciscoUnityPortInfoGroup": ciscoUnityPortInfoGroup,
       "ciscoUnityNotificationsInfoGroup": ciscoUnityNotificationsInfoGroup,
       "ciscoUnityNotificationsGroup": ciscoUnityNotificationsGroup,
       "ciscoUnityLicInfoGroup": ciscoUnityLicInfoGroup,
       "ciscoUnityPortInfoGroup2": ciscoUnityPortInfoGroup2,
       "ciscoUnityPortInfoGroup3": ciscoUnityPortInfoGroup3}
)
