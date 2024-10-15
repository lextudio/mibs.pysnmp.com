# SNMP MIB module (CADANT-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:21 2024
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

(cadant,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadant")

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

cadTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 0)
)
cadTextualConventions.setRevisions(
        ("2015-07-16 00:00",
         "2015-06-24 00:00",
         "2015-06-01 00:00",
         "2014-12-03 00:00",
         "2014-12-01 00:00",
         "2014-10-14 00:00",
         "2014-08-01 00:00",
         "2014-03-13 00:00",
         "2014-01-13 00:00",
         "2013-10-23 00:00",
         "2013-05-16 00:00",
         "2012-04-11 00:00",
         "2012-02-23 00:00",
         "2011-12-08 00:00",
         "2011-06-09 00:00",
         "2010-11-22 00:00",
         "2011-02-24 00:00",
         "2010-12-14 00:00",
         "2010-10-28 00:00",
         "2010-05-18 00:00",
         "2010-02-23 00:00",
         "2010-01-11 00:00",
         "2009-10-15 00:00",
         "2009-09-14 00:00",
         "2009-08-28 00:00",
         "2009-08-19 00:00",
         "2009-07-10 00:00",
         "2008-10-23 00:00",
         "2008-08-06 00:00",
         "2007-11-05 00:00",
         "2007-06-25 00:00",
         "2006-10-16 00:00",
         "2006-08-23 00:00",
         "2006-07-27 00:00",
         "2006-07-27 00:00",
         "2005-12-02 00:00",
         "2005-08-30 00:00",
         "2005-09-23 00:00",
         "2005-08-31 00:00",
         "2004-11-12 00:00",
         "2004-09-15 00:00",
         "2004-03-09 00:00",
         "2003-12-18 00:00",
         "2003-08-20 00:00",
         "2003-06-08 00:00",
         "2003-05-08 00:00",
         "2003-04-21 00:00",
         "2003-04-04 00:00",
         "2003-04-01 00:00",
         "2003-03-31 00:00",
         "2003-03-17 00:00",
         "2002-11-01 00:00",
         "2002-10-25 00:00",
         "2002-10-16 00:00",
         "2002-09-25 00:00",
         "2001-02-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CardId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )



class PortId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 392),
    )



class CardType(Integer32, TextualConvention):
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
              98)
        )
    )
    namedValues = NamedValues(
        *(("ccm", 6),
          ("cdm", 7),
          ("dcam", 1),
          ("fan", 4),
          ("invalid", 0),
          ("pem", 5),
          ("rsm", 3),
          ("sam", 8),
          ("ucam", 2),
          ("unknown", 98))
    )



class CardSubType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
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
              98)
        )
    )
    namedValues = NamedValues(
        *(("ccmA", 12),
          ("ccmB", 13),
          ("cdmA", 14),
          ("cdmB", 15),
          ("dcam144d", 4),
          ("dcam192d", 1),
          ("fanA", 7),
          ("fanB", 8),
          ("fanC", 9),
          ("invalid", 0),
          ("pemA", 10),
          ("pemB", 11),
          ("rsm56g", 3),
          ("sam", 16),
          ("ucam96u", 2),
          ("unknown", 98))
    )



class CerCardType(Integer32, TextualConvention):
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
              98)
        )
    )
    namedValues = NamedValues(
        *(("ccm", 3),
          ("cdm", 4),
          ("dcam", 8),
          ("fan", 1),
          ("invalid", 0),
          ("pem", 2),
          ("rsm", 6),
          ("sam", 5),
          ("ucam", 7),
          ("unknown", 98))
    )



class CerCardSubType(Integer32, TextualConvention):
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
              98)
        )
    )
    namedValues = NamedValues(
        *(("ccm", 3),
          ("cdm", 4),
          ("dcam192m8cAnnexA", 8),
          ("dcam256m8cAnnexB", 9),
          ("fan", 1),
          ("invalid", 0),
          ("pem", 2),
          ("rsm10g", 6),
          ("sam", 5),
          ("ucam96m24c", 7),
          ("unknown", 98))
    )



class PortType(Integer32, TextualConvention):
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
              8,
              9,
              10,
              11,
              12,
              13,
              98)
        )
    )
    namedValues = NamedValues(
        *(("dchannelDocsis", 9),
          ("dchannelOfdm", 13),
          ("dchannelVideo", 10),
          ("dchannelVideoReplica", 12),
          ("eport10000BaseT", 6),
          ("eport1000BaseT", 5),
          ("eport100BaseT", 4),
          ("eport10BaseT", 3),
          ("invalid", 0),
          ("linkAgg", 11),
          ("macport", 8),
          ("uchannel", 2),
          ("unknown", 98),
          ("ureceiver", 1))
    )



class CerPortType(Integer32, TextualConvention):
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
              8,
              9,
              10,
              11,
              12,
              13,
              98)
        )
    )
    namedValues = NamedValues(
        *(("dchannelDocsis", 9),
          ("dchannelOfdm", 13),
          ("dchannelVideo", 10),
          ("dchannelVideoreplica", 12),
          ("eport10000BaseT", 6),
          ("eport1000BaseT", 5),
          ("eport100BaseT", 4),
          ("eport10BaseT", 3),
          ("invalid", 0),
          ("linkAgg", 11),
          ("macport", 8),
          ("uchannel", 2),
          ("unknown", 98),
          ("ureceiver", 1))
    )



class PortMode(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiate", 1),
          ("fullDuplex10000Mpbs", 8),
          ("fullDuplex1000Mpbs", 6),
          ("fullDuplex100Mpbs", 2),
          ("fullDuplex10Mpbs", 4),
          ("halfDuplex1000Mpbs", 7),
          ("halfDuplex100Mpbs", 3),
          ("halfDuplex10Mpbs", 5),
          ("invalid", 0))
    )



class PortDetectedMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              34)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex10000Mpbs", 8),
          ("fullDuplex1000Mpbs", 6),
          ("fullDuplex100Mpbs", 2),
          ("fullDuplex10Mpbs", 4),
          ("halfDuplex1000Mpbs", 7),
          ("halfDuplex100Mpbs", 3),
          ("halfDuplex10Mpbs", 5),
          ("invalid", 0),
          ("sfpFullDuplex1000BaseCWDM", 20),
          ("sfpFullDuplex1000BaseDWDM", 21),
          ("sfpFullDuplex1000BaseLH", 17),
          ("sfpFullDuplex1000BaseLX", 16),
          ("sfpFullDuplex1000BaseLXLH", 18),
          ("sfpFullDuplex1000BaseSX", 15),
          ("sfpFullDuplex1000BaseT", 9),
          ("sfpFullDuplex1000BaseZX", 19),
          ("sfpFullDuplex100BaseT", 11),
          ("sfpFullDuplex10BaseT", 13),
          ("sfpFullDuplex10GBaseER", 32),
          ("sfpFullDuplex10GBaseLR", 31),
          ("sfpFullDuplex10GBaseLRM", 30),
          ("sfpFullDuplex10GBaseSR", 29),
          ("sfpFullDuplex10GBaseZR", 33),
          ("sfpHalfDuplex1000BaseT", 10),
          ("sfpHalfDuplex100BaseT", 12),
          ("sfpHalfDuplex10BaseT", 14),
          ("unknown", 34),
          ("xfpFullDuplex10GBaseDWDM", 28),
          ("xfpFullDuplex10GBaseER", 25),
          ("xfpFullDuplex10GBaseLR", 24),
          ("xfpFullDuplex10GBaseLRM", 23),
          ("xfpFullDuplex10GBaseLX4", 27),
          ("xfpFullDuplex10GBaseSR", 22),
          ("xfpFullDuplex10GBaseZR", 26))
    )



class FlowControlMode(Integer32, TextualConvention):
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
        *(("desired", 3),
          ("invalid", 0),
          ("off", 2),
          ("on", 1),
          ("unknown", 4))
    )



class AdminState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )



class PrimaryState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("is", 1),
          ("oos", 2))
    )



class SecondaryState(Integer32, TextualConvention):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("bootdkm", 11),
          ("degrade", 6),
          ("diagnostic", 3),
          ("fault", 2),
          ("firmwarepump", 9),
          ("initializing", 7),
          ("manual", 1),
          ("normal", 5),
          ("notapplicable", 0),
          ("overload", 4),
          ("powerup", 10),
          ("swdownload", 8))
    )



class UnknownState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("known", 0),
          ("unknown", 1))
    )



class DuplexStatus(Integer32, TextualConvention):
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
        *(("active", 1),
          ("notapplicable", 0),
          ("protected", 4),
          ("simplex", 3),
          ("standby", 2))
    )



class MacPortId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 416),
    )



class MacPortIdWithInvalid(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 416),
    )



class EqActionType(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("cardreset", 7),
          ("initialize", 1),
          ("notapplicable", 0),
          ("remove", 3),
          ("restorecond", 4),
          ("restoreuncd", 5),
          ("switch", 2),
          ("systemreset", 6))
    )



class OverloadStatus(Integer32, TextualConvention):
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
        *(("normal", 1),
          ("red", 3),
          ("yellow", 2))
    )



class OverloadThreshold(Integer32, TextualConvention):
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
        *(("high", 4),
          ("low", 0),
          ("med", 2),
          ("medhigh", 3),
          ("medlow", 1))
    )



class DiskVolumeUsageLevel(Integer32, TextualConvention):
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
        *(("critical", 4),
          ("major", 3),
          ("minor", 2),
          ("normal", 1))
    )



class CadBridgeGroupId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(33, 255),
    )



class CadBridgePortType(Integer32, TextualConvention):
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
        *(("any", 4),
          ("cm", 1),
          ("cpeauth", 2),
          ("cpeunauth", 3),
          ("none", 5))
    )



class VlanId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )



class FlowActivityState(Integer32, TextualConvention):
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
        *(("greedy", 3),
          ("needy", 1),
          ("normal", 2))
    )



class InetAddressIPv4or6(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )



class LineType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("console", 1),
          ("vty", 2))
    )



class AAAmethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("group", 5),
          ("line", 2),
          ("local", 4),
          ("none", 1))
    )



class SshService(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sftp", 2),
          ("terminal", 1))
    )



class SshAuthMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("password", 1),
          ("public-key", 2))
    )



class SshCipher(Bits, TextualConvention):
    status = "current"


class SshCipherType(Integer32, TextualConvention):
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
        *(("aes128", 6),
          ("aes192", 7),
          ("aes256", 8),
          ("arcfour", 3),
          ("blowfish", 4),
          ("cast128", 5),
          ("des", 9),
          ("other", 1),
          ("rc4", 10),
          ("threedes", 2))
    )



class SshMacAlg(Integer32, TextualConvention):
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
        *(("hmac-md5", 4),
          ("hmac-md5-96", 5),
          ("hmac-sha1", 2),
          ("hmac-sha1-96", 3),
          ("none", 1))
    )



class SshProtocol(Integer32, TextualConvention):
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
        *(("ssh1", 1),
          ("ssh1ssh2", 3),
          ("ssh2", 2))
    )



class SshKeyType(Integer32, TextualConvention):
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
        *(("dsa1024", 1),
          ("rsa2048", 2),
          ("unknown", 0))
    )



class SshKeyExchangeMethod(Bits, TextualConvention):
    status = "current"


class CadDouble(Counter64, TextualConvention):
    status = "current"
    displayHint = "d-10"


class FirmwareSource(Integer32, TextualConvention):
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
        *(("boot1", 3),
          ("boot2", 4),
          ("committed", 1),
          ("transient", 2),
          ("unknown", 5))
    )



class PicType(Integer32, TextualConvention):
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
              98)
        )
    )
    namedValues = NamedValues(
        *(("dcam", 3),
          ("dcamLeft", 1),
          ("dcamRight", 2),
          ("invalid", 0),
          ("rsm", 6),
          ("ucam", 5),
          ("ucamRight", 4),
          ("unknown", 98))
    )



class CerPicType(Integer32, TextualConvention):
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
              98)
        )
    )
    namedValues = NamedValues(
        *(("dcamHighPic8c", 2),
          ("dcamLowPic8c", 1),
          ("dcamSparePic8c", 3),
          ("invalid", 0),
          ("rsmPic", 6),
          ("ucamHighPic24c", 4),
          ("ucamSparePic24c", 5),
          ("unknown", 98))
    )



class CadExtAclCondition(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("eq", 1),
          ("ge", 6),
          ("gt", 5),
          ("le", 4),
          ("lt", 3),
          ("na", 0),
          ("ne", 2),
          ("range", 7))
    )



class ServerType(Integer32, TextualConvention):
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
        *(("ftp", 2),
          ("other", 7),
          ("radius", 5),
          ("snmp", 3),
          ("syslog", 4),
          ("tacacs", 6),
          ("telnet", 1))
    )



class AccountingType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start-stop", 1),
          ("stop-only", 2))
    )



class CadIfDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )



class CadIpPort(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
        ValueRangeConstraint(-1, -1),
    )



class CadIpTos(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class CadIpTosMask(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(224, 224),
        ValueRangeConstraint(254, 254),
        ValueRangeConstraint(255, 255),
    )



class CadProtocolType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(-1, -1),
    )



class CadTcpFlags(Bits, TextualConvention):
    status = "current"


class CadAclType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ext-access-list", 2),
          ("ipv6-access-list", 5),
          ("none", 0),
          ("rate-limit-access-list", 3),
          ("remark", 4),
          ("std-access-list", 1))
    )



class CadAclString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class OUIAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class CadCpeDeviceTypes(Bits, TextualConvention):
    status = "current"


class AdminSrcAddrType(Integer32, TextualConvention):
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("dns", 16),
          ("ftp", 2),
          ("http", 3),
          ("ipdr", 4),
          ("legal-intercept", 5),
          ("ntp", 6),
          ("other", 1),
          ("pc-dqos", 7),
          ("pc-mm", 8),
          ("radius", 13),
          ("remote-query", 9),
          ("snmp-trap", 10),
          ("ssh", 11),
          ("syslog", 12),
          ("tacacs", 14),
          ("telnet", 15))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-TC",
    **{"CardId": CardId,
       "PortId": PortId,
       "CardType": CardType,
       "CardSubType": CardSubType,
       "CerCardType": CerCardType,
       "CerCardSubType": CerCardSubType,
       "PortType": PortType,
       "CerPortType": CerPortType,
       "PortMode": PortMode,
       "PortDetectedMode": PortDetectedMode,
       "FlowControlMode": FlowControlMode,
       "AdminState": AdminState,
       "PrimaryState": PrimaryState,
       "SecondaryState": SecondaryState,
       "UnknownState": UnknownState,
       "DuplexStatus": DuplexStatus,
       "MacPortId": MacPortId,
       "MacPortIdWithInvalid": MacPortIdWithInvalid,
       "EqActionType": EqActionType,
       "OverloadStatus": OverloadStatus,
       "OverloadThreshold": OverloadThreshold,
       "DiskVolumeUsageLevel": DiskVolumeUsageLevel,
       "CadBridgeGroupId": CadBridgeGroupId,
       "CadBridgePortType": CadBridgePortType,
       "VlanId": VlanId,
       "FlowActivityState": FlowActivityState,
       "InetAddressIPv4or6": InetAddressIPv4or6,
       "LineType": LineType,
       "AAAmethod": AAAmethod,
       "SshService": SshService,
       "SshAuthMethod": SshAuthMethod,
       "SshCipher": SshCipher,
       "SshCipherType": SshCipherType,
       "SshMacAlg": SshMacAlg,
       "SshProtocol": SshProtocol,
       "SshKeyType": SshKeyType,
       "SshKeyExchangeMethod": SshKeyExchangeMethod,
       "CadDouble": CadDouble,
       "FirmwareSource": FirmwareSource,
       "PicType": PicType,
       "CerPicType": CerPicType,
       "CadExtAclCondition": CadExtAclCondition,
       "ServerType": ServerType,
       "AccountingType": AccountingType,
       "CadIfDirection": CadIfDirection,
       "CadIpPort": CadIpPort,
       "CadIpTos": CadIpTos,
       "CadIpTosMask": CadIpTosMask,
       "CadProtocolType": CadProtocolType,
       "CadTcpFlags": CadTcpFlags,
       "CadAclType": CadAclType,
       "CadAclString": CadAclString,
       "OUIAddress": OUIAddress,
       "CadCpeDeviceTypes": CadCpeDeviceTypes,
       "AdminSrcAddrType": AdminSrcAddrType,
       "cadTextualConventions": cadTextualConventions}
)
