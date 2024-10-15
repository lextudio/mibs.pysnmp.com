# SNMP MIB module (CISCO-WAN-AAL2-PROFILES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-AAL2-PROFILES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:44 2024
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

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

ciscoWanAal2ProfilesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 17)
)
ciscoWanAal2ProfilesMIB.setRevisions(
        ("2005-09-01 00:00",
         "2004-04-09 00:00",
         "2003-10-10 00:00",
         "2003-08-14 00:00",
         "2003-05-23 00:00",
         "2001-09-10 00:00",
         "2001-08-24 15:00",
         "2001-01-19 15:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoWanAal2ProfilesMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWanAal2ProfilesMIBObjects = _CiscoWanAal2ProfilesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 17, 1)
)
_Aal2ProfilesGrp_ObjectIdentity = ObjectIdentity
aal2ProfilesGrp = _Aal2ProfilesGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 17, 1, 1)
)
_Aal2ProfilesGrpTable_Object = MibTable
aal2ProfilesGrpTable = _Aal2ProfilesGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 17, 1, 1, 1)
)
if mibBuilder.loadTexts:
    aal2ProfilesGrpTable.setStatus("current")
_Aal2ProfilesGrpEntry_Object = MibTableRow
aal2ProfilesGrpEntry = _Aal2ProfilesGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 17, 1, 1, 1, 1)
)
aal2ProfilesGrpEntry.setIndexNames(
    (0, "CISCO-WAN-AAL2-PROFILES-MIB", "aal2ProfileType"),
    (0, "CISCO-WAN-AAL2-PROFILES-MIB", "aal2ProfileNumber"),
)
if mibBuilder.loadTexts:
    aal2ProfilesGrpEntry.setStatus("current")


class _Aal2ProfileType_Type(Integer32):
    """Custom type aal2ProfileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("custom", 3),
          ("itu", 1))
    )


_Aal2ProfileType_Type.__name__ = "Integer32"
_Aal2ProfileType_Object = MibTableColumn
aal2ProfileType = _Aal2ProfileType_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 17, 1, 1, 1, 1, 1),
    _Aal2ProfileType_Type()
)
aal2ProfileType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aal2ProfileType.setStatus("current")


class _Aal2ProfileNumber_Type(Integer32):
    """Custom type aal2ProfileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              7,
              8,
              12,
              100,
              101,
              110,
              200,
              201,
              210)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("one", 1),
          ("oneHundred", 100),
          ("oneHundredOne", 101),
          ("oneHundredTen", 110),
          ("seven", 7),
          ("three", 3),
          ("twelve", 12),
          ("two", 2),
          ("twoHundred", 200),
          ("twoHundredOne", 201),
          ("twoHundredTen", 210))
    )


_Aal2ProfileNumber_Type.__name__ = "Integer32"
_Aal2ProfileNumber_Object = MibTableColumn
aal2ProfileNumber = _Aal2ProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 17, 1, 1, 1, 1, 2),
    _Aal2ProfileNumber_Type()
)
aal2ProfileNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aal2ProfileNumber.setStatus("current")


class _Aal2ProfilePreference_Type(Integer32):
    """Custom type aal2ProfilePreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Aal2ProfilePreference_Type.__name__ = "Integer32"
_Aal2ProfilePreference_Object = MibTableColumn
aal2ProfilePreference = _Aal2ProfilePreference_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 17, 1, 1, 1, 1, 3),
    _Aal2ProfilePreference_Type()
)
aal2ProfilePreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2ProfilePreference.setStatus("current")


class _Aal2ProfileVoiceCodec_Type(Integer32):
    """Custom type aal2ProfileVoiceCodec based on Integer32"""
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
              8,
              9,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("clearChannel", 6),
          ("g711a", 2),
          ("g711u", 1),
          ("g723ah", 12),
          ("g723al", 14),
          ("g723h", 11),
          ("g723l", 13),
          ("g726r16000", 7),
          ("g726r24000", 8),
          ("g726r32000", 3),
          ("g726r40000", 9),
          ("g729a", 4),
          ("g729ab", 5),
          ("lossless", 15))
    )


_Aal2ProfileVoiceCodec_Type.__name__ = "Integer32"
_Aal2ProfileVoiceCodec_Object = MibTableColumn
aal2ProfileVoiceCodec = _Aal2ProfileVoiceCodec_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 17, 1, 1, 1, 1, 4),
    _Aal2ProfileVoiceCodec_Type()
)
aal2ProfileVoiceCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2ProfileVoiceCodec.setStatus("current")


class _Aal2ProfileVoicePktPeriod_Type(Integer32):
    """Custom type aal2ProfileVoicePktPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              10,
              20,
              30,
              40)
        )
    )
    namedValues = NamedValues(
        *(("five", 5),
          ("fourty", 40),
          ("ten", 10),
          ("thirty", 30),
          ("twenty", 20))
    )


_Aal2ProfileVoicePktPeriod_Type.__name__ = "Integer32"
_Aal2ProfileVoicePktPeriod_Object = MibTableColumn
aal2ProfileVoicePktPeriod = _Aal2ProfileVoicePktPeriod_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 17, 1, 1, 1, 1, 5),
    _Aal2ProfileVoicePktPeriod_Type()
)
aal2ProfileVoicePktPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2ProfileVoicePktPeriod.setStatus("current")
if mibBuilder.loadTexts:
    aal2ProfileVoicePktPeriod.setUnits("milli seconds")


class _Aal2ProfileVoiceVAD_Type(Integer32):
    """Custom type aal2ProfileVoiceVAD based on Integer32"""
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
        *(("off", 1),
          ("on", 2),
          ("sid723", 5),
          ("sid729", 4),
          ("sidGenric", 3))
    )


_Aal2ProfileVoiceVAD_Type.__name__ = "Integer32"
_Aal2ProfileVoiceVAD_Object = MibTableColumn
aal2ProfileVoiceVAD = _Aal2ProfileVoiceVAD_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 17, 1, 1, 1, 1, 6),
    _Aal2ProfileVoiceVAD_Type()
)
aal2ProfileVoiceVAD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2ProfileVoiceVAD.setStatus("current")


class _Aal2ProfileVBDCodec_Type(Integer32):
    """Custom type aal2ProfileVBDCodec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              8,
              9,
              11,
              13,
              15)
        )
    )
    namedValues = NamedValues(
        *(("clearChannel", 6),
          ("g711a", 2),
          ("g711u", 1),
          ("g723h", 11),
          ("g723l", 13),
          ("g726r16000", 7),
          ("g726r24000", 8),
          ("g726r32000", 3),
          ("g726r40000", 9),
          ("lossless", 15))
    )


_Aal2ProfileVBDCodec_Type.__name__ = "Integer32"
_Aal2ProfileVBDCodec_Object = MibTableColumn
aal2ProfileVBDCodec = _Aal2ProfileVBDCodec_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 17, 1, 1, 1, 1, 7),
    _Aal2ProfileVBDCodec_Type()
)
aal2ProfileVBDCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2ProfileVBDCodec.setStatus("current")


class _Aal2ProfileVBDPktPeriod_Type(Integer32):
    """Custom type aal2ProfileVBDPktPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              10,
              30)
        )
    )
    namedValues = NamedValues(
        *(("five", 5),
          ("ten", 10),
          ("thirty", 30))
    )


_Aal2ProfileVBDPktPeriod_Type.__name__ = "Integer32"
_Aal2ProfileVBDPktPeriod_Object = MibTableColumn
aal2ProfileVBDPktPeriod = _Aal2ProfileVBDPktPeriod_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 17, 1, 1, 1, 1, 8),
    _Aal2ProfileVBDPktPeriod_Type()
)
aal2ProfileVBDPktPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2ProfileVBDPktPeriod.setStatus("current")
if mibBuilder.loadTexts:
    aal2ProfileVBDPktPeriod.setUnits("milli seconds")
_Aal2ProfileMIBConformance_ObjectIdentity = ObjectIdentity
aal2ProfileMIBConformance = _Aal2ProfileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 17, 2)
)
_Aal2ProfileMIBCompliances_ObjectIdentity = ObjectIdentity
aal2ProfileMIBCompliances = _Aal2ProfileMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 17, 2, 1)
)
_Aal2ProfileMIBGroups_ObjectIdentity = ObjectIdentity
aal2ProfileMIBGroups = _Aal2ProfileMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 17, 2, 2)
)

# Managed Objects groups

aal2ProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 17, 2, 2, 1)
)
aal2ProfileGroup.setObjects(
      *(("CISCO-WAN-AAL2-PROFILES-MIB", "aal2ProfilePreference"),
        ("CISCO-WAN-AAL2-PROFILES-MIB", "aal2ProfileVoiceCodec"),
        ("CISCO-WAN-AAL2-PROFILES-MIB", "aal2ProfileVoicePktPeriod"),
        ("CISCO-WAN-AAL2-PROFILES-MIB", "aal2ProfileVoiceVAD"),
        ("CISCO-WAN-AAL2-PROFILES-MIB", "aal2ProfileVBDCodec"),
        ("CISCO-WAN-AAL2-PROFILES-MIB", "aal2ProfileVBDPktPeriod"))
)
if mibBuilder.loadTexts:
    aal2ProfileGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aal2ProfileMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 17, 2, 1, 1)
)
if mibBuilder.loadTexts:
    aal2ProfileMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-AAL2-PROFILES-MIB",
    **{"ciscoWanAal2ProfilesMIB": ciscoWanAal2ProfilesMIB,
       "ciscoWanAal2ProfilesMIBObjects": ciscoWanAal2ProfilesMIBObjects,
       "aal2ProfilesGrp": aal2ProfilesGrp,
       "aal2ProfilesGrpTable": aal2ProfilesGrpTable,
       "aal2ProfilesGrpEntry": aal2ProfilesGrpEntry,
       "aal2ProfileType": aal2ProfileType,
       "aal2ProfileNumber": aal2ProfileNumber,
       "aal2ProfilePreference": aal2ProfilePreference,
       "aal2ProfileVoiceCodec": aal2ProfileVoiceCodec,
       "aal2ProfileVoicePktPeriod": aal2ProfileVoicePktPeriod,
       "aal2ProfileVoiceVAD": aal2ProfileVoiceVAD,
       "aal2ProfileVBDCodec": aal2ProfileVBDCodec,
       "aal2ProfileVBDPktPeriod": aal2ProfileVBDPktPeriod,
       "aal2ProfileMIBConformance": aal2ProfileMIBConformance,
       "aal2ProfileMIBCompliances": aal2ProfileMIBCompliances,
       "aal2ProfileMIBCompliance": aal2ProfileMIBCompliance,
       "aal2ProfileMIBGroups": aal2ProfileMIBGroups,
       "aal2ProfileGroup": aal2ProfileGroup}
)
