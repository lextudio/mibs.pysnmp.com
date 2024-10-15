# SNMP MIB module (SONUS-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:49 2024
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

(sonusModules,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusModules")


# MODULE-IDENTITY

sonusTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HwTypeID(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              50)
        )
    )
    namedValues = NamedValues(
        *(("cna01", 29),
          ("cna02", 49),
          ("cna03", 30),
          ("cna05", 50),
          ("cna06", 42),
          ("cna10", 24),
          ("cna20", 34),
          ("cna21", 35),
          ("cna25", 45),
          ("cna30", 25),
          ("cna33", 23),
          ("cna61", 39),
          ("cns10", 18),
          ("cns20", 31),
          ("cns25", 44),
          ("cns30", 19),
          ("cns31", 43),
          ("cns61", 38),
          ("fanTray", 27),
          ("mna10", 21),
          ("mns10", 16),
          ("mta01", 20),
          ("mta10", 28),
          ("mta20", 40),
          ("mta21", 41),
          ("none", 1),
          ("pna10", 22),
          ("pna21", 36),
          ("pna23", 37),
          ("pna30", 47),
          ("pns10", 17),
          ("pns20", 32),
          ("pns30", 46),
          ("sonicPlane", 26),
          ("sonicPlane2", 48),
          ("sps60", 33),
          ("undefined", 15),
          ("unknown", 14))
    )



class ServerTypeID(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              17,
              18,
              19,
              31,
              32,
              38,
              43,
              44,
              46)
        )
    )
    namedValues = NamedValues(
        *(("cns10", 18),
          ("cns20", 31),
          ("cns25", 44),
          ("cns30", 19),
          ("cns31", 43),
          ("cns61", 38),
          ("mns10", 16),
          ("pns10", 17),
          ("pns20", 32),
          ("pns30", 46))
    )



class AdapterTypeID(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              21,
              22,
              23,
              24,
              25,
              29,
              30,
              34,
              35,
              36,
              39,
              42,
              45,
              47,
              49,
              50)
        )
    )
    namedValues = NamedValues(
        *(("cna01", 29),
          ("cna02", 49),
          ("cna03", 30),
          ("cna05", 50),
          ("cna06", 42),
          ("cna10", 24),
          ("cna20", 34),
          ("cna21", 35),
          ("cna25", 45),
          ("cna30", 25),
          ("cna33", 23),
          ("cna61", 39),
          ("mna10", 21),
          ("none", 1),
          ("pna10", 22),
          ("pna21", 36),
          ("pna30", 47))
    )



class ServerFunctionType(Integer32, TextualConvention):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("atm", 2),
          ("default", 1),
          ("e1", 5),
          ("enet", 10),
          ("mgmt", 3),
          ("oc3tdm", 8),
          ("pos", 9),
          ("sps", 7),
          ("t1", 4),
          ("t3", 6))
    )



class SonusShelfIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )



class SonusSlotIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )



class SonusEventString(OctetString, TextualConvention):
    status = "current"
    displayHint = "511a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )



class SonusEventClass(Integer32, TextualConvention):
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
        *(("callproc", 2),
          ("directory", 4),
          ("netmgmt", 5),
          ("resmgmt", 3),
          ("routing", 7),
          ("signaling", 6),
          ("sysmgmt", 1),
          ("trace", 8))
    )



class SonusEventLevel(Integer32, TextualConvention):
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
        *(("critical", 1),
          ("info", 4),
          ("major", 2),
          ("minor", 3))
    )



class SonusEventFilterLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("info", 4),
          ("major", 2),
          ("minor", 3),
          ("noevents", 0))
    )



class SonusName(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )



class SonusNameReference(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )



class SonusBoolean(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )



class PointCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )



class SonusSysId(Integer32, TextualConvention):
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
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63)
        )
    )
    namedValues = NamedValues(
        *(("acm", 34),
          ("arm", 48),
          ("arma", 49),
          ("asg", 38),
          ("atmrm", 52),
          ("brm", 9),
          ("cam", 37),
          ("cassg", 55),
          ("cb", 33),
          ("cc", 13),
          ("cli", 26),
          ("dcl", 53),
          ("debug", 18),
          ("diag", 36),
          ("drm", 10),
          ("ds", 17),
          ("enm", 47),
          ("epdh", 16),
          ("evlog", 1),
          ("fm", 4),
          ("gwfe", 21),
          ("gwsg", 22),
          ("h323fe", 61),
          ("h323sg", 60),
          ("hsim", 28),
          ("icm", 14),
          ("ipdcfe", 40),
          ("ipdh", 15),
          ("isdn", 46),
          ("led", 31),
          ("lesim", 29),
          ("ltt", 41),
          ("mgcpfe", 57),
          ("mgsg", 39),
          ("ncm", 2),
          ("nfs", 45),
          ("nrm", 7),
          ("nrma", 8),
          ("nrs", 3),
          ("ntp", 35),
          ("param", 32),
          ("pfa", 56),
          ("prm", 11),
          ("psd", 54),
          ("psdh", 51),
          ("rtcp", 24),
          ("rtm", 50),
          ("sg", 20),
          ("sg-7", 23),
          ("sipfe", 63),
          ("sipsg", 62),
          ("sm", 5),
          ("sma", 6),
          ("snmp", 27),
          ("spm", 58),
          ("spma", 59),
          ("ss7fe", 30),
          ("sta", 44),
          ("stm", 43),
          ("tccs", 25),
          ("tm", 42),
          ("trm", 19),
          ("xrm", 12))
    )



class SonusServiceState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 2),
          ("outOfService", 1))
    )



class SonusAdminState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )



class SonusAdminAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dryUp", 1),
          ("force", 2))
    )



class SonusCircuitState(Integer32, TextualConvention):
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
        *(("blocked", 2),
          ("notAvailable", 5),
          ("transientBlock", 4),
          ("transientUnblock", 3),
          ("unblocked", 1))
    )



class SonusMtaSlotIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mta1", 1),
          ("mta2", 2))
    )



class SonusTimingSource(Integer32, TextualConvention):
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
        *(("extClkA", 1),
          ("extClkB", 2),
          ("holdover", 6),
          ("oscillator", 5),
          ("refClkA", 3),
          ("refClkB", 4))
    )



class SonusSoftwareVersion(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d.1d.1d.1d.2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



class SonusSystemName(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class SonusTrapType(Integer32, TextualConvention):
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
        *(("inform", 3),
          ("none", 0),
          ("trapv1", 1),
          ("trapv2", 2))
    )



class SonusAccessLevel(Integer32, TextualConvention):
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
        *(("admin", 3),
          ("readOnly", 1),
          ("readWrite", 2))
    )



class SonusPointCode(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d-"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class SonusPointCodeFormat(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d-"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class SonusSupportFlag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 2),
          ("unsupported", 1))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-TC",
    **{"HwTypeID": HwTypeID,
       "ServerTypeID": ServerTypeID,
       "AdapterTypeID": AdapterTypeID,
       "ServerFunctionType": ServerFunctionType,
       "SonusShelfIndex": SonusShelfIndex,
       "SonusSlotIndex": SonusSlotIndex,
       "SonusEventString": SonusEventString,
       "SonusEventClass": SonusEventClass,
       "SonusEventLevel": SonusEventLevel,
       "SonusEventFilterLevel": SonusEventFilterLevel,
       "SonusName": SonusName,
       "SonusNameReference": SonusNameReference,
       "SonusBoolean": SonusBoolean,
       "PointCode": PointCode,
       "SonusSysId": SonusSysId,
       "SonusServiceState": SonusServiceState,
       "SonusAdminState": SonusAdminState,
       "SonusAdminAction": SonusAdminAction,
       "SonusCircuitState": SonusCircuitState,
       "SonusMtaSlotIndex": SonusMtaSlotIndex,
       "SonusTimingSource": SonusTimingSource,
       "SonusSoftwareVersion": SonusSoftwareVersion,
       "SonusSystemName": SonusSystemName,
       "SonusTrapType": SonusTrapType,
       "SonusAccessLevel": SonusAccessLevel,
       "SonusPointCode": SonusPointCode,
       "SonusPointCodeFormat": SonusPointCodeFormat,
       "SonusSupportFlag": SonusSupportFlag,
       "sonusTextualConventions": sonusTextualConventions}
)
