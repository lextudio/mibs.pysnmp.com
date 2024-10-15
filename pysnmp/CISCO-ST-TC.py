# SNMP MIB module (CISCO-ST-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ST-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:38 2024
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

(ciscoModules,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoModules")

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

storageTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 12, 4)
)
storageTextualConventions.setRevisions(
        ("2012-08-08 00:00",
         "2011-07-26 00:00",
         "2010-12-24 00:00",
         "2008-05-16 00:00",
         "2005-12-17 00:00",
         "2004-05-18 00:00",
         "2003-09-26 00:00",
         "2003-08-07 00:00",
         "2002-10-04 00:00",
         "2002-09-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VsanIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class DomainId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 239),
    )



class DomainIdOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 239),
    )



class FcAddressId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class FcNameId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class FcNameIdOrZero(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
    )



class FcClassOfServices(Bits, TextualConvention):
    status = "current"


class FcPortTypes(Integer32, TextualConvention):
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("bPort", 5),
          ("ePort", 4),
          ("fPort", 2),
          ("flPort", 3),
          ("fvPort", 13),
          ("fxPort", 6),
          ("nPort", 9),
          ("nlPort", 10),
          ("npPort", 16),
          ("nxPort", 11),
          ("portOperDown", 14),
          ("sdPort", 7),
          ("stPort", 15),
          ("tePort", 12),
          ("tfPort", 17),
          ("tlPort", 8),
          ("tnpPort", 18))
    )



class FcPortTxTypes(Integer32, TextualConvention):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("electrical", 5),
          ("longWaveLaser", 2),
          ("longWaveLaserCostReduced", 4),
          ("shortWaveLaser", 3),
          ("tenGigBaseEr", 8),
          ("tenGigBaseEw", 12),
          ("tenGigBaseLr", 7),
          ("tenGigBaseLw", 11),
          ("tenGigBaseLx4", 9),
          ("tenGigBaseSr", 6),
          ("tenGigBaseSw", 10),
          ("unknown", 1))
    )



class FcPortModuleTypes(Integer32, TextualConvention):
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("embedded", 4),
          ("gbic", 3),
          ("gbicWithSerialID", 6),
          ("gbicWithoutSerialID", 7),
          ("glm", 5),
          ("other", 2),
          ("qsfp", 19),
          ("sfpDwdm", 18),
          ("sfpWithSerialID", 8),
          ("sfpWithoutSerialID", 9),
          ("unknown", 1),
          ("x2Dwdm", 20),
          ("x2Medium", 12),
          ("x2Short", 11),
          ("x2Tall", 13),
          ("xenpak", 17),
          ("xfp", 10),
          ("xpakMedium", 15),
          ("xpakShort", 14),
          ("xpakTall", 16))
    )



class FcIfSpeed(Integer32, TextualConvention):
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
        *(("auto", 1),
          ("autoMaxEightG", 9),
          ("autoMaxFourG", 7),
          ("autoMaxSixteenG", 11),
          ("autoMaxTwoG", 5),
          ("eightG", 6),
          ("fourG", 4),
          ("oneG", 2),
          ("sixteenG", 10),
          ("tenG", 8),
          ("twoG", 3))
    )



class PortMemberList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class FcAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
        ValueSizeConstraint(8, 8),
    )



class FcAddressType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fcid", 2),
          ("wwn", 1))
    )



class InterfaceOperMode(Integer32, TextualConvention):
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("bPort", 5),
          ("ePort", 4),
          ("evPort", 18),
          ("fPort", 2),
          ("flPort", 3),
          ("fvPort", 13),
          ("fxPort", 6),
          ("ipsPort", 17),
          ("mgmtPort", 16),
          ("nPort", 9),
          ("nlPort", 10),
          ("npPort", 19),
          ("nxPort", 11),
          ("portOperDown", 14),
          ("sdPort", 7),
          ("stPort", 15),
          ("tePort", 12),
          ("tfPort", 20),
          ("tlPort", 8),
          ("tnpPort", 21))
    )



class FcIfServiceStateType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2))
    )



class FcIfSfpDiagLevelType(Integer32, TextualConvention):
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
        *(("highAlarm", 6),
          ("highWarning", 5),
          ("lowAlarm", 4),
          ("lowWarning", 3),
          ("normal", 2),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ST-TC",
    **{"VsanIndex": VsanIndex,
       "DomainId": DomainId,
       "DomainIdOrZero": DomainIdOrZero,
       "FcAddressId": FcAddressId,
       "FcNameId": FcNameId,
       "FcNameIdOrZero": FcNameIdOrZero,
       "FcClassOfServices": FcClassOfServices,
       "FcPortTypes": FcPortTypes,
       "FcPortTxTypes": FcPortTxTypes,
       "FcPortModuleTypes": FcPortModuleTypes,
       "FcIfSpeed": FcIfSpeed,
       "PortMemberList": PortMemberList,
       "FcAddress": FcAddress,
       "FcAddressType": FcAddressType,
       "InterfaceOperMode": InterfaceOperMode,
       "FcIfServiceStateType": FcIfServiceStateType,
       "FcIfSfpDiagLevelType": FcIfSfpDiagLevelType,
       "storageTextualConventions": storageTextualConventions}
)
