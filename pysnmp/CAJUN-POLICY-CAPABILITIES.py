# SNMP MIB module (CAJUN-POLICY-CAPABILITIES) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CAJUN-POLICY-CAPABILITIES
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:21 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

lucent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2)
)
_CajunRulesMIB_ObjectIdentity = ObjectIdentity
cajunRulesMIB = _CajunRulesMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42)
)
_PolicyCapabilityMIB_ObjectIdentity = ObjectIdentity
policyCapabilityMIB = _PolicyCapabilityMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1)
)
_LucentDevicePolicyCapabilities_ObjectIdentity = ObjectIdentity
lucentDevicePolicyCapabilities = _LucentDevicePolicyCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1)
)
_LucentDevicePolicyCapabilityTable_Object = MibTable
lucentDevicePolicyCapabilityTable = _LucentDevicePolicyCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lucentDevicePolicyCapabilityTable.setStatus("current")
_LucentDevicePolicyCapabilityEntry_Object = MibTableRow
lucentDevicePolicyCapabilityEntry = _LucentDevicePolicyCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1)
)
lucentDevicePolicyCapabilityEntry.setIndexNames(
    (0, "CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityIndex"),
)
if mibBuilder.loadTexts:
    lucentDevicePolicyCapabilityEntry.setStatus("current")


class _LucentDevicePolicyCapabilityIndex_Type(Integer32):
    """Custom type lucentDevicePolicyCapabilityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_LucentDevicePolicyCapabilityIndex_Type.__name__ = "Integer32"
_LucentDevicePolicyCapabilityIndex_Object = MibTableColumn
lucentDevicePolicyCapabilityIndex = _LucentDevicePolicyCapabilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1, 1),
    _LucentDevicePolicyCapabilityIndex_Type()
)
lucentDevicePolicyCapabilityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentDevicePolicyCapabilityIndex.setStatus("current")


class _LucentDevicePolicyCapabilityType_Type(Integer32):
    """Custom type lucentDevicePolicyCapabilityType based on Integer32"""
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
        *(("cli", 6),
          ("cops", 2),
          ("diameter", 3),
          ("ldap", 1),
          ("other", 7),
          ("radius", 5),
          ("snmp", 4))
    )


_LucentDevicePolicyCapabilityType_Type.__name__ = "Integer32"
_LucentDevicePolicyCapabilityType_Object = MibTableColumn
lucentDevicePolicyCapabilityType = _LucentDevicePolicyCapabilityType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1, 2),
    _LucentDevicePolicyCapabilityType_Type()
)
lucentDevicePolicyCapabilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentDevicePolicyCapabilityType.setStatus("current")
_LucentDevicePolicyCapabilityDescription_Type = DisplayString
_LucentDevicePolicyCapabilityDescription_Object = MibTableColumn
lucentDevicePolicyCapabilityDescription = _LucentDevicePolicyCapabilityDescription_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1, 3),
    _LucentDevicePolicyCapabilityDescription_Type()
)
lucentDevicePolicyCapabilityDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentDevicePolicyCapabilityDescription.setStatus("current")


class _LucentDevicePolicyCapabilityInformation_Type(OctetString):
    """Custom type lucentDevicePolicyCapabilityInformation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LucentDevicePolicyCapabilityInformation_Type.__name__ = "OctetString"
_LucentDevicePolicyCapabilityInformation_Object = MibTableColumn
lucentDevicePolicyCapabilityInformation = _LucentDevicePolicyCapabilityInformation_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1, 4),
    _LucentDevicePolicyCapabilityInformation_Type()
)
lucentDevicePolicyCapabilityInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentDevicePolicyCapabilityInformation.setStatus("current")


class _LucentDevicePolicyCapabilityState_Type(Integer32):
    """Custom type lucentDevicePolicyCapabilityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("other", 3))
    )


_LucentDevicePolicyCapabilityState_Type.__name__ = "Integer32"
_LucentDevicePolicyCapabilityState_Object = MibTableColumn
lucentDevicePolicyCapabilityState = _LucentDevicePolicyCapabilityState_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1, 5),
    _LucentDevicePolicyCapabilityState_Type()
)
lucentDevicePolicyCapabilityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentDevicePolicyCapabilityState.setStatus("current")


class _LucentDevicePolicyCapabilityRetrievalStatus_Type(Integer32):
    """Custom type lucentDevicePolicyCapabilityRetrievalStatus based on Integer32"""
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
        *(("failedExecution", 3),
          ("failedRetrieval", 2),
          ("inProgress", 4),
          ("success", 1))
    )


_LucentDevicePolicyCapabilityRetrievalStatus_Type.__name__ = "Integer32"
_LucentDevicePolicyCapabilityRetrievalStatus_Object = MibTableColumn
lucentDevicePolicyCapabilityRetrievalStatus = _LucentDevicePolicyCapabilityRetrievalStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1, 6),
    _LucentDevicePolicyCapabilityRetrievalStatus_Type()
)
lucentDevicePolicyCapabilityRetrievalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentDevicePolicyCapabilityRetrievalStatus.setStatus("current")


class _LucentDevicePolicyCapabilityExecutionOption_Type(Integer32):
    """Custom type lucentDevicePolicyCapabilityExecutionOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignoreErrors", 2),
          ("stopOnError", 1))
    )


_LucentDevicePolicyCapabilityExecutionOption_Type.__name__ = "Integer32"
_LucentDevicePolicyCapabilityExecutionOption_Object = MibTableColumn
lucentDevicePolicyCapabilityExecutionOption = _LucentDevicePolicyCapabilityExecutionOption_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1, 7),
    _LucentDevicePolicyCapabilityExecutionOption_Type()
)
lucentDevicePolicyCapabilityExecutionOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentDevicePolicyCapabilityExecutionOption.setStatus("current")
_LucentDevicePolicyTime_Type = DateAndTime
_LucentDevicePolicyTime_Object = MibScalar
lucentDevicePolicyTime = _LucentDevicePolicyTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 2),
    _LucentDevicePolicyTime_Type()
)
lucentDevicePolicyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentDevicePolicyTime.setStatus("current")
_LucentDevicePolicyLDAPObjects_ObjectIdentity = ObjectIdentity
lucentDevicePolicyLDAPObjects = _LucentDevicePolicyLDAPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2)
)
_LucentDevicePolicyLDAPServerIP_Type = IpAddress
_LucentDevicePolicyLDAPServerIP_Object = MibScalar
lucentDevicePolicyLDAPServerIP = _LucentDevicePolicyLDAPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 1),
    _LucentDevicePolicyLDAPServerIP_Type()
)
lucentDevicePolicyLDAPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentDevicePolicyLDAPServerIP.setStatus("current")
_LucentDevicePolicyLDAPServerPort_Type = Integer32
_LucentDevicePolicyLDAPServerPort_Object = MibScalar
lucentDevicePolicyLDAPServerPort = _LucentDevicePolicyLDAPServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 2),
    _LucentDevicePolicyLDAPServerPort_Type()
)
lucentDevicePolicyLDAPServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentDevicePolicyLDAPServerPort.setStatus("current")
_LucentDevicePolicySecondaryLDAPServerIP_Type = IpAddress
_LucentDevicePolicySecondaryLDAPServerIP_Object = MibScalar
lucentDevicePolicySecondaryLDAPServerIP = _LucentDevicePolicySecondaryLDAPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 3),
    _LucentDevicePolicySecondaryLDAPServerIP_Type()
)
lucentDevicePolicySecondaryLDAPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentDevicePolicySecondaryLDAPServerIP.setStatus("current")
_LucentDevicePolicySecondaryLDAPServerPort_Type = Integer32
_LucentDevicePolicySecondaryLDAPServerPort_Object = MibScalar
lucentDevicePolicySecondaryLDAPServerPort = _LucentDevicePolicySecondaryLDAPServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 4),
    _LucentDevicePolicySecondaryLDAPServerPort_Type()
)
lucentDevicePolicySecondaryLDAPServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentDevicePolicySecondaryLDAPServerPort.setStatus("current")


class _LucentDevicePolicyBadLDAPObject_Type(OctetString):
    """Custom type lucentDevicePolicyBadLDAPObject based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LucentDevicePolicyBadLDAPObject_Type.__name__ = "OctetString"
_LucentDevicePolicyBadLDAPObject_Object = MibScalar
lucentDevicePolicyBadLDAPObject = _LucentDevicePolicyBadLDAPObject_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 5),
    _LucentDevicePolicyBadLDAPObject_Type()
)
lucentDevicePolicyBadLDAPObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentDevicePolicyBadLDAPObject.setStatus("current")
_LucentDevicePolicyBadLDAPDescription_Type = DisplayString
_LucentDevicePolicyBadLDAPDescription_Object = MibScalar
lucentDevicePolicyBadLDAPDescription = _LucentDevicePolicyBadLDAPDescription_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 6),
    _LucentDevicePolicyBadLDAPDescription_Type()
)
lucentDevicePolicyBadLDAPDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentDevicePolicyBadLDAPDescription.setStatus("current")
_LucentDevicePolicyCapabilityLastChange_Type = TimeTicks
_LucentDevicePolicyCapabilityLastChange_Object = MibScalar
lucentDevicePolicyCapabilityLastChange = _LucentDevicePolicyCapabilityLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 7),
    _LucentDevicePolicyCapabilityLastChange_Type()
)
lucentDevicePolicyCapabilityLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentDevicePolicyCapabilityLastChange.setStatus("current")
_LucentDevicePolicyCapabilityProducerSignal_Type = Integer32
_LucentDevicePolicyCapabilityProducerSignal_Object = MibScalar
lucentDevicePolicyCapabilityProducerSignal = _LucentDevicePolicyCapabilityProducerSignal_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 8),
    _LucentDevicePolicyCapabilityProducerSignal_Type()
)
lucentDevicePolicyCapabilityProducerSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentDevicePolicyCapabilityProducerSignal.setStatus("current")
_LucentDevicePolicyCapabilityConsumerSignal_Type = Integer32
_LucentDevicePolicyCapabilityConsumerSignal_Object = MibScalar
lucentDevicePolicyCapabilityConsumerSignal = _LucentDevicePolicyCapabilityConsumerSignal_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 9),
    _LucentDevicePolicyCapabilityConsumerSignal_Type()
)
lucentDevicePolicyCapabilityConsumerSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentDevicePolicyCapabilityConsumerSignal.setStatus("current")
_LucentDevicePolicyLDAPSearchBase_Type = DisplayString
_LucentDevicePolicyLDAPSearchBase_Object = MibScalar
lucentDevicePolicyLDAPSearchBase = _LucentDevicePolicyLDAPSearchBase_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 10),
    _LucentDevicePolicyLDAPSearchBase_Type()
)
lucentDevicePolicyLDAPSearchBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentDevicePolicyLDAPSearchBase.setStatus("current")
_LucentDevicePolicyCapabilityMIBConformance_ObjectIdentity = ObjectIdentity
lucentDevicePolicyCapabilityMIBConformance = _LucentDevicePolicyCapabilityMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 11)
)
_LucentDevicePolicyCapabilityMIBCompliances_ObjectIdentity = ObjectIdentity
lucentDevicePolicyCapabilityMIBCompliances = _LucentDevicePolicyCapabilityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 12)
)
_LucentDevicePolicyMIBGroups_ObjectIdentity = ObjectIdentity
lucentDevicePolicyMIBGroups = _LucentDevicePolicyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 13)
)
_LucentPolicyCapabilityEvents_ObjectIdentity = ObjectIdentity
lucentPolicyCapabilityEvents = _LucentPolicyCapabilityEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 21)
)
_LucentPolicyCapabilityEventsV2_ObjectIdentity = ObjectIdentity
lucentPolicyCapabilityEventsV2 = _LucentPolicyCapabilityEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 21, 1)
)
if mibBuilder.loadTexts:
    lucentPolicyCapabilityEventsV2.setStatus("current")

# Managed Objects groups

lucentDevicePolicyCapabilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 13, 1)
)
lucentDevicePolicyCapabilityGroup.setObjects(
      *(("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityIndex"),
        ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityType"),
        ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityDescription"),
        ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityInformation"),
        ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityState"),
        ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyTime"))
)
if mibBuilder.loadTexts:
    lucentDevicePolicyCapabilityGroup.setStatus("current")

lucentDevicePolicyCapabilityLDAPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 13, 2)
)
lucentDevicePolicyCapabilityLDAPGroup.setObjects(
      *(("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyLDAPServerIP"),
        ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyLDAPServerPort"),
        ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicySecondaryLDAPServerIP"),
        ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicySecondaryLDAPServerPort"),
        ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyBadLDAPObject"),
        ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyBadLDAPDescription"),
        ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityLastChange"),
        ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityProducerSignal"),
        ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityConsumerSignal"),
        ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyLDAPSearchBase"))
)
if mibBuilder.loadTexts:
    lucentDevicePolicyCapabilityLDAPGroup.setStatus("current")


# Notification objects

lucentBadLDAPObject = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 21, 1, 1)
)
lucentBadLDAPObject.setObjects(
      *(("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyLDAPServerIP"),
        ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyLDAPServerPort"),
        ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyBadLDAPObject"),
        ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyBadLDAPDescription"))
)
if mibBuilder.loadTexts:
    lucentBadLDAPObject.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

lucentDevicePolicyCapabilityBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 12, 1)
)
if mibBuilder.loadTexts:
    lucentDevicePolicyCapabilityBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAJUN-POLICY-CAPABILITIES",
    **{"lucent": lucent,
       "mibs": mibs,
       "cajunRulesMIB": cajunRulesMIB,
       "policyCapabilityMIB": policyCapabilityMIB,
       "lucentDevicePolicyCapabilities": lucentDevicePolicyCapabilities,
       "lucentDevicePolicyCapabilityTable": lucentDevicePolicyCapabilityTable,
       "lucentDevicePolicyCapabilityEntry": lucentDevicePolicyCapabilityEntry,
       "lucentDevicePolicyCapabilityIndex": lucentDevicePolicyCapabilityIndex,
       "lucentDevicePolicyCapabilityType": lucentDevicePolicyCapabilityType,
       "lucentDevicePolicyCapabilityDescription": lucentDevicePolicyCapabilityDescription,
       "lucentDevicePolicyCapabilityInformation": lucentDevicePolicyCapabilityInformation,
       "lucentDevicePolicyCapabilityState": lucentDevicePolicyCapabilityState,
       "lucentDevicePolicyCapabilityRetrievalStatus": lucentDevicePolicyCapabilityRetrievalStatus,
       "lucentDevicePolicyCapabilityExecutionOption": lucentDevicePolicyCapabilityExecutionOption,
       "lucentDevicePolicyTime": lucentDevicePolicyTime,
       "lucentDevicePolicyLDAPObjects": lucentDevicePolicyLDAPObjects,
       "lucentDevicePolicyLDAPServerIP": lucentDevicePolicyLDAPServerIP,
       "lucentDevicePolicyLDAPServerPort": lucentDevicePolicyLDAPServerPort,
       "lucentDevicePolicySecondaryLDAPServerIP": lucentDevicePolicySecondaryLDAPServerIP,
       "lucentDevicePolicySecondaryLDAPServerPort": lucentDevicePolicySecondaryLDAPServerPort,
       "lucentDevicePolicyBadLDAPObject": lucentDevicePolicyBadLDAPObject,
       "lucentDevicePolicyBadLDAPDescription": lucentDevicePolicyBadLDAPDescription,
       "lucentDevicePolicyCapabilityLastChange": lucentDevicePolicyCapabilityLastChange,
       "lucentDevicePolicyCapabilityProducerSignal": lucentDevicePolicyCapabilityProducerSignal,
       "lucentDevicePolicyCapabilityConsumerSignal": lucentDevicePolicyCapabilityConsumerSignal,
       "lucentDevicePolicyLDAPSearchBase": lucentDevicePolicyLDAPSearchBase,
       "lucentDevicePolicyCapabilityMIBConformance": lucentDevicePolicyCapabilityMIBConformance,
       "lucentDevicePolicyCapabilityMIBCompliances": lucentDevicePolicyCapabilityMIBCompliances,
       "lucentDevicePolicyCapabilityBasicCompliance": lucentDevicePolicyCapabilityBasicCompliance,
       "lucentDevicePolicyMIBGroups": lucentDevicePolicyMIBGroups,
       "lucentDevicePolicyCapabilityGroup": lucentDevicePolicyCapabilityGroup,
       "lucentDevicePolicyCapabilityLDAPGroup": lucentDevicePolicyCapabilityLDAPGroup,
       "lucentPolicyCapabilityEvents": lucentPolicyCapabilityEvents,
       "lucentPolicyCapabilityEventsV2": lucentPolicyCapabilityEventsV2,
       "lucentBadLDAPObject": lucentBadLDAPObject}
)
