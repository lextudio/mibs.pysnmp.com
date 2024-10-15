# SNMP MIB module (COLUBRIS-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COLUBRIS-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:09 2024
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

(colubrisModules,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisModules")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

colubrisTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 4, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ColubrisAuthenticationMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("localAndProfile", 3),
          ("profile", 2))
    )



class ColubrisUsersAuthenticationMode(Integer32, TextualConvention):
    status = "current"
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
        *(("local", 1),
          ("localAndProfile", 3),
          ("none", 0),
          ("profile", 2))
    )



class ColubrisUsersAuthenticationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("html", 3),
          ("ieee802dot1x", 2),
          ("mac", 1))
    )



class ColubrisNotificationEnable(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )



class ColubrisProfileIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class ColubrisProfileIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ColubrisServerIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class ColubrisServerIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ColubrisSSID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class ColubrisSSIDOrNone(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class ColubrisSecurity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot1x", 3),
          ("ieee802dot1xWithWep", 4),
          ("none", 1),
          ("unknown", 0),
          ("wep", 2),
          ("wpa", 5),
          ("wpaPsk", 6))
    )



class ColubrisPriorityQueue(Integer32, TextualConvention):
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
        *(("high", 3),
          ("low", 1),
          ("normal", 2),
          ("veryHigh", 4))
    )



class ColubrisDataRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("rate11Meg", 7),
          ("rate12Meg", 8),
          ("rate18Meg", 9),
          ("rate1Meg", 2),
          ("rate24Meg", 10),
          ("rate2Meg", 3),
          ("rate36Meg", 11),
          ("rate48Meg", 12),
          ("rate54Meg", 13),
          ("rate5dot5Meg", 4),
          ("rate6Meg", 5),
          ("rate9Meg", 6),
          ("rateHighestAvailable", 14),
          ("rateLowestAvailable", 1),
          ("unknown", 0))
    )



class ColubrisRadioType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ar2317", 6),
          ("cm6", 1),
          ("cm9", 2),
          ("mb82", 5),
          ("sunfish", 3),
          ("xb114", 7))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-TC",
    **{"ColubrisAuthenticationMode": ColubrisAuthenticationMode,
       "ColubrisUsersAuthenticationMode": ColubrisUsersAuthenticationMode,
       "ColubrisUsersAuthenticationType": ColubrisUsersAuthenticationType,
       "ColubrisNotificationEnable": ColubrisNotificationEnable,
       "ColubrisProfileIndex": ColubrisProfileIndex,
       "ColubrisProfileIndexOrZero": ColubrisProfileIndexOrZero,
       "ColubrisServerIndex": ColubrisServerIndex,
       "ColubrisServerIndexOrZero": ColubrisServerIndexOrZero,
       "ColubrisSSID": ColubrisSSID,
       "ColubrisSSIDOrNone": ColubrisSSIDOrNone,
       "ColubrisSecurity": ColubrisSecurity,
       "ColubrisPriorityQueue": ColubrisPriorityQueue,
       "ColubrisDataRate": ColubrisDataRate,
       "ColubrisRadioType": ColubrisRadioType,
       "colubrisTextualConventions": colubrisTextualConventions}
)
