# SNMP MIB module (CL-PKTC-EUE-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CL-PKTC-EUE-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:29 2024
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

(pktcEUEMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "pktcEUEMibs")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pktcEUETCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PktcEUETCID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )



class PktcEUETCIDType(Integer32, TextualConvention):
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("gruu", 2),
          ("macaddress", 7),
          ("other", 1),
          ("packetcableIdentity", 8),
          ("privateIdentity", 4),
          ("publicIdentity", 3),
          ("publicPrivatePair", 5),
          ("username", 6))
    )



class PktcEUETCActStatus(TruthValue, TextualConvention):
    status = "current"


class PktcEUETCActStatusInfo(SnmpAdminString, TextualConvention):
    status = "current"
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )



class PktcEUETCUsrElementIndexType(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class PktcEUETCAppOrgIdentifier(Unsigned32, TextualConvention):
    status = "current"


class PktcEUETCAppIdentifier(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )



class PktcEUETCUsrAppIndexType(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )



class PktcEUETCCredsType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("certificate", 5),
          ("none", 2),
          ("other", 1),
          ("password", 3),
          ("preSharedKey", 4))
    )



class PktcEUETCCreds(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8192),
    )



# MIB Managed Objects in the order of their OIDs

_PktcEUETCNotifications_ObjectIdentity = ObjectIdentity
pktcEUETCNotifications = _PktcEUETCNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 0)
)
_PktcEUETCObjects_ObjectIdentity = ObjectIdentity
pktcEUETCObjects = _PktcEUETCObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1)
)
_PktcEUETCUsageObjs_ObjectIdentity = ObjectIdentity
pktcEUETCUsageObjs = _PktcEUETCUsageObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1)
)
_PktcEUETCSampleID_Type = PktcEUETCID
_PktcEUETCSampleID_Object = MibScalar
pktcEUETCSampleID = _PktcEUETCSampleID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 2),
    _PktcEUETCSampleID_Type()
)
pktcEUETCSampleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUETCSampleID.setStatus("obsolete")
_PktcEUETCSampleIDType_Type = PktcEUETCIDType
_PktcEUETCSampleIDType_Object = MibScalar
pktcEUETCSampleIDType = _PktcEUETCSampleIDType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 3),
    _PktcEUETCSampleIDType_Type()
)
pktcEUETCSampleIDType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUETCSampleIDType.setStatus("obsolete")
_PktcEUETCSampleActStatus_Type = PktcEUETCActStatus
_PktcEUETCSampleActStatus_Object = MibScalar
pktcEUETCSampleActStatus = _PktcEUETCSampleActStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 4),
    _PktcEUETCSampleActStatus_Type()
)
pktcEUETCSampleActStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUETCSampleActStatus.setStatus("obsolete")
_PktcEUETCSampleUsrRef_Type = PktcEUETCUsrElementIndexType
_PktcEUETCSampleUsrRef_Object = MibScalar
pktcEUETCSampleUsrRef = _PktcEUETCSampleUsrRef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 5),
    _PktcEUETCSampleUsrRef_Type()
)
pktcEUETCSampleUsrRef.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUETCSampleUsrRef.setStatus("obsolete")
_PktcEUETCSampleCredsType_Type = PktcEUETCCredsType
_PktcEUETCSampleCredsType_Object = MibScalar
pktcEUETCSampleCredsType = _PktcEUETCSampleCredsType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 6),
    _PktcEUETCSampleCredsType_Type()
)
pktcEUETCSampleCredsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUETCSampleCredsType.setStatus("obsolete")
_PktcEUETCSampleCreds_Type = PktcEUETCCreds
_PktcEUETCSampleCreds_Object = MibScalar
pktcEUETCSampleCreds = _PktcEUETCSampleCreds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 7),
    _PktcEUETCSampleCreds_Type()
)
pktcEUETCSampleCreds.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUETCSampleCreds.setStatus("obsolete")
_PktcEUETCSampleAppRef_Type = PktcEUETCUsrAppIndexType
_PktcEUETCSampleAppRef_Object = MibScalar
pktcEUETCSampleAppRef = _PktcEUETCSampleAppRef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 8),
    _PktcEUETCSampleAppRef_Type()
)
pktcEUETCSampleAppRef.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUETCSampleAppRef.setStatus("obsolete")
_PktcEUETCSampleActStatusInfo_Type = PktcEUETCActStatusInfo
_PktcEUETCSampleActStatusInfo_Object = MibScalar
pktcEUETCSampleActStatusInfo = _PktcEUETCSampleActStatusInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 9),
    _PktcEUETCSampleActStatusInfo_Type()
)
pktcEUETCSampleActStatusInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUETCSampleActStatusInfo.setStatus("obsolete")
_PktcEUETCAppIdentifier_Type = PktcEUETCAppIdentifier
_PktcEUETCAppIdentifier_Object = MibScalar
pktcEUETCAppIdentifier = _PktcEUETCAppIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 10),
    _PktcEUETCAppIdentifier_Type()
)
pktcEUETCAppIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUETCAppIdentifier.setStatus("obsolete")
_PktcEUETCAppOrgIdentifier_Type = PktcEUETCAppOrgIdentifier
_PktcEUETCAppOrgIdentifier_Object = MibScalar
pktcEUETCAppOrgIdentifier = _PktcEUETCAppOrgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 11),
    _PktcEUETCAppOrgIdentifier_Type()
)
pktcEUETCAppOrgIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUETCAppOrgIdentifier.setStatus("obsolete")
_PktcEUETCConformance_ObjectIdentity = ObjectIdentity
pktcEUETCConformance = _PktcEUETCConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 2)
)
_PktcEUETCCompliances_ObjectIdentity = ObjectIdentity
pktcEUETCCompliances = _PktcEUETCCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 2, 1)
)
_PktcEUETCGroups_ObjectIdentity = ObjectIdentity
pktcEUETCGroups = _PktcEUETCGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pktcEUETCMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pktcEUETCMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CL-PKTC-EUE-TC-MIB",
    **{"PktcEUETCID": PktcEUETCID,
       "PktcEUETCIDType": PktcEUETCIDType,
       "PktcEUETCActStatus": PktcEUETCActStatus,
       "PktcEUETCActStatusInfo": PktcEUETCActStatusInfo,
       "PktcEUETCUsrElementIndexType": PktcEUETCUsrElementIndexType,
       "PktcEUETCAppOrgIdentifier": PktcEUETCAppOrgIdentifier,
       "PktcEUETCAppIdentifier": PktcEUETCAppIdentifier,
       "PktcEUETCUsrAppIndexType": PktcEUETCUsrAppIndexType,
       "PktcEUETCCredsType": PktcEUETCCredsType,
       "PktcEUETCCreds": PktcEUETCCreds,
       "pktcEUETCMIB": pktcEUETCMIB,
       "pktcEUETCNotifications": pktcEUETCNotifications,
       "pktcEUETCObjects": pktcEUETCObjects,
       "pktcEUETCUsageObjs": pktcEUETCUsageObjs,
       "pktcEUETCSampleID": pktcEUETCSampleID,
       "pktcEUETCSampleIDType": pktcEUETCSampleIDType,
       "pktcEUETCSampleActStatus": pktcEUETCSampleActStatus,
       "pktcEUETCSampleUsrRef": pktcEUETCSampleUsrRef,
       "pktcEUETCSampleCredsType": pktcEUETCSampleCredsType,
       "pktcEUETCSampleCreds": pktcEUETCSampleCreds,
       "pktcEUETCSampleAppRef": pktcEUETCSampleAppRef,
       "pktcEUETCSampleActStatusInfo": pktcEUETCSampleActStatusInfo,
       "pktcEUETCAppIdentifier": pktcEUETCAppIdentifier,
       "pktcEUETCAppOrgIdentifier": pktcEUETCAppOrgIdentifier,
       "pktcEUETCConformance": pktcEUETCConformance,
       "pktcEUETCCompliances": pktcEUETCCompliances,
       "pktcEUETCMIBCompliance": pktcEUETCMIBCompliance,
       "pktcEUETCGroups": pktcEUETCGroups}
)
