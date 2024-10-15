# SNMP MIB module (HP-ICF-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:57 2024
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

(hpicfAdmin,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfAdmin")

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

hpicfTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 4)
)
hpicfTextualConventions.setRevisions(
        ("2017-03-22 08:00",
         "2016-12-07 08:00",
         "2015-01-30 08:00",
         "2014-12-09 08:00",
         "2014-09-06 08:00",
         "2014-02-04 08:00",
         "2012-02-22 08:00",
         "2012-02-17 00:00",
         "2010-10-12 08:00",
         "2009-02-10 18:00",
         "2008-08-19 09:05",
         "2008-02-04 15:36",
         "2004-02-18 23:05",
         "2000-11-03 07:17")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ConfigStatus(Integer32, TextualConvention):
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
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3))
    )



class HpSwitchPortType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              15,
              37,
              54,
              55,
              62,
              69,
              70,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204)
        )
    )
    namedValues = NamedValues(
        *(("atm", 37),
          ("ethernetCsmacd", 6),
          ("fastEther", 62),
          ("fastEtherBX-D", 131),
          ("fastEtherBX-U", 132),
          ("fastEtherFX", 69),
          ("fastEtherFX-sfp", 70),
          ("fastEtherGEN", 128),
          ("fddi", 15),
          ("fiveGbE-T", 204),
          ("fortyGbE-GEN", 171),
          ("fourGbE-GEN", 170),
          ("gigabitEthernetBX-D", 133),
          ("gigabitEthernetBX-U", 134),
          ("gigabitEthernetESP", 123),
          ("gigabitEthernetGEN", 129),
          ("gigabitEthernetLH", 121),
          ("gigabitEthernetLX", 118),
          ("gigabitEthernetSX", 117),
          ("gigabitEthernetStk", 120),
          ("gigabitEthernetT", 119),
          ("gigabitEthernetT-sfp", 127),
          ("ieee80212", 55),
          ("iso88023Csmacd", 7),
          ("none", 2),
          ("other", 1),
          ("propMultiplexor", 54),
          ("qSFP-PLUS-AO1", 188),
          ("qSFP-PLUS-AO10", 193),
          ("qSFP-PLUS-AO15", 194),
          ("qSFP-PLUS-AO2", 189),
          ("qSFP-PLUS-AO20", 195),
          ("qSFP-PLUS-AO3", 190),
          ("qSFP-PLUS-AO5", 191),
          ("qSFP-PLUS-AO7", 192),
          ("qSFP-PLUS-BIDI", 203),
          ("qSFP-PLUS-DA1", 175),
          ("qSFP-PLUS-DA3", 176),
          ("qSFP-PLUS-DA5", 177),
          ("qSFP-PLUS-LR4", 174),
          ("qSFP-PLUS-SPLIT-sFP-PLUS-AO1", 196),
          ("qSFP-PLUS-SPLIT-sFP-PLUS-AO10", 201),
          ("qSFP-PLUS-SPLIT-sFP-PLUS-AO15", 202),
          ("qSFP-PLUS-SPLIT-sFP-PLUS-AO2", 197),
          ("qSFP-PLUS-SPLIT-sFP-PLUS-AO3", 198),
          ("qSFP-PLUS-SPLIT-sFP-PLUS-AO5", 199),
          ("qSFP-PLUS-SPLIT-sFP-PLUS-AO7", 200),
          ("qSFP-PLUS-SPLIT-sFP-PLUS-DA1", 178),
          ("qSFP-PLUS-SPLIT-sFP-PLUS-DA3", 179),
          ("qSFP-PLUS-SPLIT-sFP-PLUS-DA5", 180),
          ("qSFP-PLUS-SR4", 172),
          ("qSFP-PLUS-eSR4", 173),
          ("sFP-CWDM1470", 161),
          ("sFP-CWDM1490", 162),
          ("sFP-CWDM1510", 163),
          ("sFP-CWDM1530", 164),
          ("sFP-CWDM1550", 165),
          ("sFP-CWDM1570", 166),
          ("sFP-CWDM1590", 167),
          ("sFP-CWDM1610", 168),
          ("sFP-PLUS-AO1", 181),
          ("sFP-PLUS-AO10", 186),
          ("sFP-PLUS-AO15", 187),
          ("sFP-PLUS-AO2", 182),
          ("sFP-PLUS-AO3", 183),
          ("sFP-PLUS-AO5", 184),
          ("sFP-PLUS-AO7", 185),
          ("sFP-PLUS-DA1", 140),
          ("sFP-PLUS-DA10", 145),
          ("sFP-PLUS-DA15", 146),
          ("sFP-PLUS-DA2", 141),
          ("sFP-PLUS-DA20", 147),
          ("sFP-PLUS-DA3", 142),
          ("sFP-PLUS-DA5", 143),
          ("sFP-PLUS-DA7", 144),
          ("sFP-PLUS-DAC", 139),
          ("sFP-PLUS-ER", 160),
          ("sFP-PLUS-LR", 137),
          ("sFP-PLUS-LRM", 138),
          ("sFP-PLUS-SR", 136),
          ("tenGSFP-ER", 114),
          ("tenGSFP-LR", 113),
          ("tenGSFP-LRM", 115),
          ("tenGSFP-LX4", 116),
          ("tenGSFP-SR", 112),
          ("tenGbE-CX4", 122),
          ("tenGbE-ER", 125),
          ("tenGbE-GEN", 130),
          ("tenGbE-K", 158),
          ("tenGbE-LR", 126),
          ("tenGbE-LRM", 135),
          ("tenGbE-SR", 124),
          ("tenGbE-STK", 151),
          ("tenGbE-T", 148),
          ("tenGbE-TLH", 150),
          ("tenGbE-TSH", 149),
          ("tenGigabitEthernetESP", 169),
          ("unknown", 3),
          ("xFP-SFP-PLUS-DA1", 153),
          ("xFP-SFP-PLUS-DA10", 157),
          ("xFP-SFP-PLUS-DA3", 154),
          ("xFP-SFP-PLUS-DA5", 155),
          ("xFP-SFP-PLUS-DA7", 156),
          ("xFP-SFP-PLUS-DAC", 152))
    )



class VidList(OctetString, TextualConvention):
    status = "current"
    displayHint = "512x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )



class HpInetCidrRouteState(Bits, TextualConvention):
    status = "current"


class StpPortRole(Integer32, TextualConvention):
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
        *(("alternate", 4),
          ("backup", 5),
          ("boundary", 6),
          ("designated", 3),
          ("disabled", 1),
          ("root", 2))
    )



class HpSwitchIfMauTypeListBits(Bits, TextualConvention):
    status = "current"


class HpSwitchIfMauAutoNegCapabilityBits(Bits, TextualConvention):
    status = "current"


class HpSwitchIfMauAutoNegCapAdvertisedBits(Bits, TextualConvention):
    status = "current"


class HpSwitchIfMauAutoNegCapReceivedBits(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-TC",
    **{"ConfigStatus": ConfigStatus,
       "HpSwitchPortType": HpSwitchPortType,
       "VidList": VidList,
       "HpInetCidrRouteState": HpInetCidrRouteState,
       "StpPortRole": StpPortRole,
       "HpSwitchIfMauTypeListBits": HpSwitchIfMauTypeListBits,
       "HpSwitchIfMauAutoNegCapabilityBits": HpSwitchIfMauAutoNegCapabilityBits,
       "HpSwitchIfMauAutoNegCapAdvertisedBits": HpSwitchIfMauAutoNegCapAdvertisedBits,
       "HpSwitchIfMauAutoNegCapReceivedBits": HpSwitchIfMauAutoNegCapReceivedBits,
       "hpicfTextualConventions": hpicfTextualConventions}
)
