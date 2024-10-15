# SNMP MIB module (Juniper-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:35 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

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

juniTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 1)
)
juniTextualConventions.setRevisions(
        ("2005-12-21 20:13",
         "2005-11-18 22:30",
         "2004-12-03 22:12",
         "2003-11-12 22:31",
         "2002-09-16 21:44",
         "2002-04-04 16:35",
         "2001-03-08 22:26",
         "1999-12-12 00:00",
         "1999-07-14 00:00",
         "1998-11-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniEnable(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )



class JuniName(OctetString, TextualConvention):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class JuniVrfName(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class JuniNextIfIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class JuniIpAddrLessIf(IpAddress, TextualConvention):
    status = "current"


class JuniTimeSlotMap(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class JuniAcctngAdminType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )



class JuniAcctngOperType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notSupported", 2))
    )



class JuniLogSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notice", 5),
          ("off", -1),
          ("warning", 4))
    )



class JuniSetMap(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class JuniInterfaceDescrFormat(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("industryCommon", 1),
          ("proprietary", 0))
    )



class JuniInterfaceLocation(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class JuniInterfaceLocationType(Integer32, TextualConvention):
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
        *(("adapterPort", 3),
          ("slotAdapterPort", 2),
          ("slotPort", 1),
          ("unknown", 0))
    )



class JuniInterfaceLocationValue(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class JuniVrfGroupName(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class JuniTimeFilter(TimeTicks, TextualConvention):
    status = "current"


class JuniNibbleConfig(Integer32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-TC",
    **{"JuniEnable": JuniEnable,
       "JuniName": JuniName,
       "JuniVrfName": JuniVrfName,
       "JuniNextIfIndex": JuniNextIfIndex,
       "JuniIpAddrLessIf": JuniIpAddrLessIf,
       "JuniTimeSlotMap": JuniTimeSlotMap,
       "JuniAcctngAdminType": JuniAcctngAdminType,
       "JuniAcctngOperType": JuniAcctngOperType,
       "JuniLogSeverity": JuniLogSeverity,
       "JuniSetMap": JuniSetMap,
       "JuniInterfaceDescrFormat": JuniInterfaceDescrFormat,
       "JuniInterfaceLocation": JuniInterfaceLocation,
       "JuniInterfaceLocationType": JuniInterfaceLocationType,
       "JuniInterfaceLocationValue": JuniInterfaceLocationValue,
       "JuniVrfGroupName": JuniVrfGroupName,
       "JuniTimeFilter": JuniTimeFilter,
       "JuniNibbleConfig": JuniNibbleConfig,
       "juniTextualConventions": juniTextualConventions}
)
