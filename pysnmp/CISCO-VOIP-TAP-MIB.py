# SNMP MIB module (CISCO-VOIP-TAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VOIP-TAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:31 2024
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

(cTap2MediationContentId,
 cTap2StreamIndex) = mibBuilder.importSymbols(
    "CISCO-TAP2-MIB",
    "cTap2MediationContentId",
    "cTap2StreamIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoVoIpTapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 716)
)
ciscoVoIpTapMIB.setRevisions(
        ("2009-10-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CvoipWarrantId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )



class CvoipSubscriberId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoVoIpTapMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoVoIpTapMIBNotifs = _CiscoVoIpTapMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 716, 0)
)
_CiscoVoIpTapMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVoIpTapMIBObjects = _CiscoVoIpTapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 716, 1)
)
_CvoiptapStreamEncodePacket_ObjectIdentity = ObjectIdentity
cvoiptapStreamEncodePacket = _CvoiptapStreamEncodePacket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1)
)


class _CvoiptapStreamCapabilities_Type(Bits):
    """Custom type cvoiptapStreamCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("tapEnable", 0),
          ("uri", 2),
          ("usernameOrNumber", 1))
    )

_CvoiptapStreamCapabilities_Type.__name__ = "Bits"
_CvoiptapStreamCapabilities_Object = MibScalar
cvoiptapStreamCapabilities = _CvoiptapStreamCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 1),
    _CvoiptapStreamCapabilities_Type()
)
cvoiptapStreamCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvoiptapStreamCapabilities.setStatus("current")
_CvoiptapStreamTable_Object = MibTable
cvoiptapStreamTable = _CvoiptapStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cvoiptapStreamTable.setStatus("current")
_CvoiptapStreamEntry_Object = MibTableRow
cvoiptapStreamEntry = _CvoiptapStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1)
)
cvoiptapStreamEntry.setIndexNames(
    (0, "CISCO-TAP2-MIB", "cTap2MediationContentId"),
    (0, "CISCO-TAP2-MIB", "cTap2StreamIndex"),
)
if mibBuilder.loadTexts:
    cvoiptapStreamEntry.setStatus("current")
_CvoiptapStreamId_Type = CvoipWarrantId
_CvoiptapStreamId_Object = MibTableColumn
cvoiptapStreamId = _CvoiptapStreamId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 1),
    _CvoiptapStreamId_Type()
)
cvoiptapStreamId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvoiptapStreamId.setStatus("current")


class _CvoiptapStreamType_Type(Integer32):
    """Custom type cvoiptapStreamType based on Integer32"""
    defaultValue = 4

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
        *(("intercept", 4),
          ("pen", 1),
          ("penAndTrace", 3),
          ("trace", 2))
    )


_CvoiptapStreamType_Type.__name__ = "Integer32"
_CvoiptapStreamType_Object = MibTableColumn
cvoiptapStreamType = _CvoiptapStreamType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 2),
    _CvoiptapStreamType_Type()
)
cvoiptapStreamType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvoiptapStreamType.setStatus("current")
_CvoiptapStreamMatch_Type = CvoipSubscriberId
_CvoiptapStreamMatch_Object = MibTableColumn
cvoiptapStreamMatch = _CvoiptapStreamMatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 3),
    _CvoiptapStreamMatch_Type()
)
cvoiptapStreamMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvoiptapStreamMatch.setStatus("current")


class _CvoiptapStreamMatchType_Type(Integer32):
    """Custom type cvoiptapStreamMatchType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uri", 2),
          ("usernameOrNumber", 1))
    )


_CvoiptapStreamMatchType_Type.__name__ = "Integer32"
_CvoiptapStreamMatchType_Object = MibTableColumn
cvoiptapStreamMatchType = _CvoiptapStreamMatchType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 4),
    _CvoiptapStreamMatchType_Type()
)
cvoiptapStreamMatchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvoiptapStreamMatchType.setStatus("current")
_CvoiptapStreamCCMediationDevice_Type = Integer32
_CvoiptapStreamCCMediationDevice_Object = MibTableColumn
cvoiptapStreamCCMediationDevice = _CvoiptapStreamCCMediationDevice_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 5),
    _CvoiptapStreamCCMediationDevice_Type()
)
cvoiptapStreamCCMediationDevice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvoiptapStreamCCMediationDevice.setStatus("current")
_CvoiptapStreamRowStatus_Type = RowStatus
_CvoiptapStreamRowStatus_Object = MibTableColumn
cvoiptapStreamRowStatus = _CvoiptapStreamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 6),
    _CvoiptapStreamRowStatus_Type()
)
cvoiptapStreamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvoiptapStreamRowStatus.setStatus("current")
_CiscoVoIpTapMIBConform_ObjectIdentity = ObjectIdentity
ciscoVoIpTapMIBConform = _CiscoVoIpTapMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 716, 2)
)
_CiscoVoIpTapMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVoIpTapMIBCompliances = _CiscoVoIpTapMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 716, 2, 1)
)
_CiscoVoIpTapMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVoIpTapMIBGroups = _CiscoVoIpTapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 716, 2, 2)
)

# Managed Objects groups

ciscoVoIpTapStreamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 716, 2, 2, 1)
)
ciscoVoIpTapStreamGroup.setObjects(
      *(("CISCO-VOIP-TAP-MIB", "cvoiptapStreamCapabilities"),
        ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamId"),
        ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamType"),
        ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamMatch"),
        ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamMatchType"),
        ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamCCMediationDevice"),
        ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoVoIpTapStreamGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVoIpTapMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 716, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoVoIpTapMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VOIP-TAP-MIB",
    **{"CvoipWarrantId": CvoipWarrantId,
       "CvoipSubscriberId": CvoipSubscriberId,
       "ciscoVoIpTapMIB": ciscoVoIpTapMIB,
       "ciscoVoIpTapMIBNotifs": ciscoVoIpTapMIBNotifs,
       "ciscoVoIpTapMIBObjects": ciscoVoIpTapMIBObjects,
       "cvoiptapStreamEncodePacket": cvoiptapStreamEncodePacket,
       "cvoiptapStreamCapabilities": cvoiptapStreamCapabilities,
       "cvoiptapStreamTable": cvoiptapStreamTable,
       "cvoiptapStreamEntry": cvoiptapStreamEntry,
       "cvoiptapStreamId": cvoiptapStreamId,
       "cvoiptapStreamType": cvoiptapStreamType,
       "cvoiptapStreamMatch": cvoiptapStreamMatch,
       "cvoiptapStreamMatchType": cvoiptapStreamMatchType,
       "cvoiptapStreamCCMediationDevice": cvoiptapStreamCCMediationDevice,
       "cvoiptapStreamRowStatus": cvoiptapStreamRowStatus,
       "ciscoVoIpTapMIBConform": ciscoVoIpTapMIBConform,
       "ciscoVoIpTapMIBCompliances": ciscoVoIpTapMIBCompliances,
       "ciscoVoIpTapMIBCompliance": ciscoVoIpTapMIBCompliance,
       "ciscoVoIpTapMIBGroups": ciscoVoIpTapMIBGroups,
       "ciscoVoIpTapStreamGroup": ciscoVoIpTapStreamGroup}
)
