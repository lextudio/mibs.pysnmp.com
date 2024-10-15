# SNMP MIB module (CISCO-WAN-CODEC-GEN-PARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-CODEC-GEN-PARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:00 2024
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

ciscoWanCodecGenParmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 21)
)
ciscoWanCodecGenParmMIB.setRevisions(
        ("2004-03-17 00:00",
         "2004-01-30 00:00",
         "2003-05-23 00:00",
         "2001-09-10 00:00",
         "2001-08-21 15:00",
         "2001-08-02 15:00",
         "2001-06-15 15:00",
         "2001-03-20 15:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoWanCodecGenParmMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWanCodecGenParmMIBObjects = _CiscoWanCodecGenParmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 21, 1)
)
_VismCodecGenParmGrp_ObjectIdentity = ObjectIdentity
vismCodecGenParmGrp = _VismCodecGenParmGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 21, 1, 1)
)
_VismCodecGenParmTable_Object = MibTable
vismCodecGenParmTable = _VismCodecGenParmTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 21, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vismCodecGenParmTable.setStatus("current")
_VismCodecGenParmEntry_Object = MibTableRow
vismCodecGenParmEntry = _VismCodecGenParmEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 21, 1, 1, 1, 1)
)
vismCodecGenParmEntry.setIndexNames(
    (0, "CISCO-WAN-CODEC-GEN-PARM-MIB", "vismCodecIndex"),
)
if mibBuilder.loadTexts:
    vismCodecGenParmEntry.setStatus("current")


class _VismCodecIndex_Type(Integer32):
    """Custom type vismCodecIndex based on Integer32"""
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


_VismCodecIndex_Type.__name__ = "Integer32"
_VismCodecIndex_Object = MibTableColumn
vismCodecIndex = _VismCodecIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 21, 1, 1, 1, 1, 1),
    _VismCodecIndex_Type()
)
vismCodecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vismCodecIndex.setStatus("current")


class _VismCodecJitterDelayMode_Type(Integer32):
    """Custom type vismCodecJitterDelayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("fixed", 1),
          ("fixedWithTimeStamp", 3))
    )


_VismCodecJitterDelayMode_Type.__name__ = "Integer32"
_VismCodecJitterDelayMode_Object = MibTableColumn
vismCodecJitterDelayMode = _VismCodecJitterDelayMode_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 21, 1, 1, 1, 1, 2),
    _VismCodecJitterDelayMode_Type()
)
vismCodecJitterDelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCodecJitterDelayMode.setStatus("current")


class _VismCodecJitterInitialDelay_Type(Integer32):
    """Custom type vismCodecJitterInitialDelay based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              55,
              60,
              65,
              70,
              75,
              80,
              85,
              90,
              95,
              100)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("eighteen", 18),
          ("eighty", 80),
          ("eightyfive", 85),
          ("eleven", 11),
          ("fifteen", 15),
          ("fifty", 50),
          ("fiftyfive", 55),
          ("five", 5),
          ("fortyeight", 48),
          ("fortyfive", 45),
          ("fortyfour", 44),
          ("fortynine", 49),
          ("fortyone", 41),
          ("fortyseven", 47),
          ("fortysix", 46),
          ("fortythree", 43),
          ("fortytwo", 42),
          ("four", 4),
          ("fourteen", 14),
          ("fourty", 40),
          ("hundred", 100),
          ("nine", 9),
          ("nineteen", 19),
          ("ninetyfive", 95),
          ("ninty", 90),
          ("seven", 7),
          ("seventeen", 17),
          ("seventy", 70),
          ("seventyfive", 75),
          ("six", 6),
          ("sixteen", 16),
          ("sixty", 60),
          ("sixtyfive", 65),
          ("ten", 10),
          ("thirteen", 13),
          ("thirty", 30),
          ("thirtyeight", 38),
          ("thirtyfive", 35),
          ("thirtyfour", 34),
          ("thirtynine", 39),
          ("thirtyone", 31),
          ("thirtyseven", 37),
          ("thirtysix", 36),
          ("thirtythree", 33),
          ("thirtytwo", 32),
          ("three", 3),
          ("twelve", 12),
          ("twenty", 20),
          ("twentyeight", 28),
          ("twentyfive", 25),
          ("twentyfour", 24),
          ("twentynine", 29),
          ("twentyone", 21),
          ("twentyseven", 27),
          ("twentysix", 26),
          ("twentythree", 23),
          ("twentytwo", 22),
          ("two", 2),
          ("zero", 1))
    )


_VismCodecJitterInitialDelay_Type.__name__ = "Integer32"
_VismCodecJitterInitialDelay_Object = MibTableColumn
vismCodecJitterInitialDelay = _VismCodecJitterInitialDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 21, 1, 1, 1, 1, 3),
    _VismCodecJitterInitialDelay_Type()
)
vismCodecJitterInitialDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCodecJitterInitialDelay.setStatus("current")
_VismCodecGenParmNotificationPrefix_ObjectIdentity = ObjectIdentity
vismCodecGenParmNotificationPrefix = _VismCodecGenParmNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 21, 2)
)
_VismCodecGenParmNotifications_ObjectIdentity = ObjectIdentity
vismCodecGenParmNotifications = _VismCodecGenParmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 21, 2, 0)
)
_VismCodecGenParmMIBConformance_ObjectIdentity = ObjectIdentity
vismCodecGenParmMIBConformance = _VismCodecGenParmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 21, 3)
)
_VismCodecGenParmMIBCompliances_ObjectIdentity = ObjectIdentity
vismCodecGenParmMIBCompliances = _VismCodecGenParmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 21, 3, 1)
)
_VismCodecGenParmMIBGroups_ObjectIdentity = ObjectIdentity
vismCodecGenParmMIBGroups = _VismCodecGenParmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 21, 3, 2)
)

# Managed Objects groups

vismCodecGenParmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 21, 3, 2, 1)
)
vismCodecGenParmGroup.setObjects(
      *(("CISCO-WAN-CODEC-GEN-PARM-MIB", "vismCodecJitterDelayMode"),
        ("CISCO-WAN-CODEC-GEN-PARM-MIB", "vismCodecJitterInitialDelay"))
)
if mibBuilder.loadTexts:
    vismCodecGenParmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vismCodecGenParmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 21, 3, 1, 1)
)
if mibBuilder.loadTexts:
    vismCodecGenParmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-CODEC-GEN-PARM-MIB",
    **{"ciscoWanCodecGenParmMIB": ciscoWanCodecGenParmMIB,
       "ciscoWanCodecGenParmMIBObjects": ciscoWanCodecGenParmMIBObjects,
       "vismCodecGenParmGrp": vismCodecGenParmGrp,
       "vismCodecGenParmTable": vismCodecGenParmTable,
       "vismCodecGenParmEntry": vismCodecGenParmEntry,
       "vismCodecIndex": vismCodecIndex,
       "vismCodecJitterDelayMode": vismCodecJitterDelayMode,
       "vismCodecJitterInitialDelay": vismCodecJitterInitialDelay,
       "vismCodecGenParmNotificationPrefix": vismCodecGenParmNotificationPrefix,
       "vismCodecGenParmNotifications": vismCodecGenParmNotifications,
       "vismCodecGenParmMIBConformance": vismCodecGenParmMIBConformance,
       "vismCodecGenParmMIBCompliances": vismCodecGenParmMIBCompliances,
       "vismCodecGenParmMIBCompliance": vismCodecGenParmMIBCompliance,
       "vismCodecGenParmMIBGroups": vismCodecGenParmMIBGroups,
       "vismCodecGenParmGroup": vismCodecGenParmGroup}
)
