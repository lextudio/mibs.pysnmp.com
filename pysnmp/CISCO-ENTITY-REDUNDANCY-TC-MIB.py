# SNMP MIB module (CISCO-ENTITY-REDUNDANCY-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENTITY-REDUNDANCY-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:41 2024
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

ciscoEntityRedunTcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 494)
)
ciscoEntityRedunTcMIB.setRevisions(
        ("2005-10-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CeRedunType(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("aps", 3),
          ("cmts", 7),
          ("externalSwitch", 5),
          ("featureCard", 4),
          ("other", 1),
          ("slotPair", 6),
          ("yCable", 2))
    )



class CeRedunScope(Integer32, TextualConvention):
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
        *(("local", 2),
          ("other", 1),
          ("remoteChassis", 3),
          ("remoteSystem", 4))
    )



class CeRedunArch(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("loadSharing", 6),
          ("mToN", 5),
          ("onePlusOne", 3),
          ("oneToN", 4),
          ("oneToOne", 2),
          ("other", 1))
    )



class CeRedunSwitchCommand(Integer32, TextualConvention):
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
        *(("clear", 2),
          ("forcedSwitchAway", 4),
          ("lockoutProtection", 5),
          ("manualSwitchAway", 3),
          ("noCmdInEffect", 1))
    )



class CeRedunMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )



class CeRedunMbrStatus(Bits, TextualConvention):
    status = "current"


class CeRedunStateCategories(Integer32, TextualConvention):
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("active", 14),
          ("activeConfigInitialize", 9),
          ("activeFromStandbyTransition", 11),
          ("activeImageInitialize", 8),
          ("activeOther", 7),
          ("activeReconciliation", 12),
          ("activeRunStateInitialize", 10),
          ("activeWait", 13),
          ("disabled", 2),
          ("failed", 4),
          ("inactive", 3),
          ("initializing", 5),
          ("negotiation", 6),
          ("other", 1),
          ("standbyColdFinal", 21),
          ("standbyConfigInitialize", 17),
          ("standbyHotFinal", 23),
          ("standbyImageInitialize", 16),
          ("standbyOther", 15),
          ("standbyReconciliation", 19),
          ("standbyRunStateInitialize", 18),
          ("standbySwitchingToActive", 24),
          ("standbyWait", 20),
          ("standbyWarmFinal", 22))
    )



class CeRedunReasonCategories(Integer32, TextualConvention):
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("activeMbrDisabled", 9),
          ("activeMbrFailed", 7),
          ("activeMbrRemoved", 8),
          ("notKnown", 3),
          ("other", 1),
          ("remoteRequest", 11),
          ("revertiveSwitchover", 10),
          ("unsupported", 2),
          ("userForced", 5),
          ("userLockout", 6),
          ("userManual", 4))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENTITY-REDUNDANCY-TC-MIB",
    **{"CeRedunType": CeRedunType,
       "CeRedunScope": CeRedunScope,
       "CeRedunArch": CeRedunArch,
       "CeRedunSwitchCommand": CeRedunSwitchCommand,
       "CeRedunMode": CeRedunMode,
       "CeRedunMbrStatus": CeRedunMbrStatus,
       "CeRedunStateCategories": CeRedunStateCategories,
       "CeRedunReasonCategories": CeRedunReasonCategories,
       "ciscoEntityRedunTcMIB": ciscoEntityRedunTcMIB}
)
