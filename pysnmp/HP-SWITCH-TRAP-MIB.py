# SNMP MIB module (HP-SWITCH-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-SWITCH-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:05 2024
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

(advStack12,
 advStack24,
 advStack48,
 advStackU16,
 advStackU8,
 arubaJL071A,
 arubaJL072A,
 arubaJL073A,
 arubaJL074A,
 arubaJL075A,
 arubaJL076A,
 arubaJL077A,
 arubaStack2930,
 arubaStack2930M,
 arubaStack3810,
 arubaSwitchJL253A,
 arubaSwitchJL254A,
 arubaSwitchJL255A,
 arubaSwitchJL256A,
 arubaSwitchJL258A,
 arubaSwitchJL259A,
 arubaSwitchJL260A,
 arubaSwitchJL261A,
 arubaSwitchJL262A,
 arubaSwitchJL263A,
 arubaSwitchJL264A,
 arubaSwitchJL319A,
 arubaSwitchJL320A,
 arubaSwitchJL321A,
 arubaSwitchJL322A,
 arubaSwitchJL323A,
 arubaSwitchJL324A,
 arubaSwitchJL354A,
 arubaSwitchJL355A,
 arubaSwitchJL356A,
 arubaSwitchJL357A,
 arubaSwitchJL557A,
 arubaSwitchJL558A,
 arubaSwitchJL559A,
 bridge1010,
 bridgeRemote,
 eswitch,
 eswitch2,
 fiberOptic,
 hp10BaseTHub12M,
 hp10BaseTHub24M,
 hpAdvStk100Tx12TM,
 hpAdvStkEnetSH12R,
 hpAdvStkEnetSH24R,
 hpAdvStkEnetSH24T,
 hpAdvStkEnetSHStack,
 hpAdvSwitch200,
 hpAdvSwitch2000,
 hpAdvSwitch2000B,
 hpAdvSwitch800T,
 hpProCurve10T100THub12M,
 hpProCurve10T100THub24M,
 hpStack,
 hpStack2920,
 hpStackVSF5400R,
 hpSwitch1600,
 hpSwitch212M,
 hpSwitch224M,
 hpSwitch2400,
 hpSwitch2424,
 hpSwitch4000,
 hpSwitch498358_B21,
 hpSwitch516733_B21,
 hpSwitch6308,
 hpSwitch8000,
 hpSwitch9304,
 hpSwitch9308,
 hpSwitchJ4812A,
 hpSwitchJ4813A,
 hpSwitchJ4819A,
 hpSwitchJ4850A,
 hpSwitchJ4865A,
 hpSwitchJ4874A,
 hpSwitchJ4887A,
 hpSwitchJ4899A,
 hpSwitchJ4899B,
 hpSwitchJ4899C,
 hpSwitchJ4900A,
 hpSwitchJ4900B,
 hpSwitchJ4900C,
 hpSwitchJ4902A,
 hpSwitchJ4903A,
 hpSwitchJ4904A,
 hpSwitchJ4905A,
 hpSwitchJ4906A,
 hpSwitchJ8164A,
 hpSwitchJ8165A,
 hpSwitchJ8433A,
 hpSwitchJ8474A,
 hpSwitchJ8680A,
 hpSwitchJ8692A,
 hpSwitchJ8693A,
 hpSwitchJ8697A,
 hpSwitchJ8698A,
 hpSwitchJ8762A,
 hpSwitchJ8992A,
 hpSwitchJ9019A,
 hpSwitchJ9019B,
 hpSwitchJ9020A,
 hpSwitchJ9021A,
 hpSwitchJ9022A,
 hpSwitchJ9028A,
 hpSwitchJ9028B,
 hpSwitchJ9029A,
 hpSwitchJ9049A,
 hpSwitchJ9050A,
 hpSwitchJ9079A,
 hpSwitchJ9080A,
 hpSwitchJ9085A,
 hpSwitchJ9086A,
 hpSwitchJ9087A,
 hpSwitchJ9088A,
 hpSwitchJ9089A,
 hpSwitchJ9091A,
 hpSwitchJ9137A,
 hpSwitchJ9138A,
 hpSwitchJ9145A,
 hpSwitchJ9146A,
 hpSwitchJ9147A,
 hpSwitchJ9148A,
 hpSwitchJ9263A,
 hpSwitchJ9264A,
 hpSwitchJ9265A,
 hpSwitchJ9279A,
 hpSwitchJ9280A,
 hpSwitchJ9298A,
 hpSwitchJ9299A,
 hpSwitchJ9310A,
 hpSwitchJ9311A,
 hpSwitchJ9449A,
 hpSwitchJ9450A,
 hpSwitchJ9451A,
 hpSwitchJ9452A,
 hpSwitchJ9470A,
 hpSwitchJ9471A,
 hpSwitchJ9472A,
 hpSwitchJ9473A,
 hpSwitchJ9477A,
 hpSwitchJ9562A,
 hpSwitchJ9565A,
 hpSwitchJ9573,
 hpSwitchJ9574,
 hpSwitchJ9575,
 hpSwitchJ9576,
 hpSwitchJ9584,
 hpSwitchJ9585,
 hpSwitchJ9586,
 hpSwitchJ9587,
 hpSwitchJ9588,
 hpSwitchJ9623A,
 hpSwitchJ9624A,
 hpSwitchJ9625A,
 hpSwitchJ9626A,
 hpSwitchJ9627A,
 hpSwitchJ9660A,
 hpSwitchJ9726A,
 hpSwitchJ9727A,
 hpSwitchJ9728A,
 hpSwitchJ9729A,
 hpSwitchJ9772A,
 hpSwitchJ9773A,
 hpSwitchJ9774A,
 hpSwitchJ9775A,
 hpSwitchJ9776A,
 hpSwitchJ9777A,
 hpSwitchJ9778A,
 hpSwitchJ9779A,
 hpSwitchJ9780A,
 hpSwitchJ9781A,
 hpSwitchJ9782A,
 hpSwitchJ9783A,
 hpSwitchJ9800A,
 hpSwitchJ9801A,
 hpSwitchJ9802A,
 hpSwitchJ9803A,
 hpSwitchJ9833A,
 hpSwitchJ9834A,
 hpSwitchJ9850A,
 hpSwitchJ9851A,
 hpSwitchJ9853A,
 hpSwitchJ9854A,
 hpSwitchJ9855A,
 hpSwitchJ9856A,
 hpSwitchJL070A,
 icfRouter210,
 icfRouter230,
 icfRouter250,
 icfRouter255,
 icfRouter650,
 icfRouterBR,
 icfRouterER,
 icfRouterFR,
 icfRouterLR,
 icfRouterPR,
 icfRouterSR,
 icfRouterTR,
 netSwitch100,
 netSwitch200) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "advStack12",
    "advStack24",
    "advStack48",
    "advStackU16",
    "advStackU8",
    "arubaJL071A",
    "arubaJL072A",
    "arubaJL073A",
    "arubaJL074A",
    "arubaJL075A",
    "arubaJL076A",
    "arubaJL077A",
    "arubaStack2930",
    "arubaStack2930M",
    "arubaStack3810",
    "arubaSwitchJL253A",
    "arubaSwitchJL254A",
    "arubaSwitchJL255A",
    "arubaSwitchJL256A",
    "arubaSwitchJL258A",
    "arubaSwitchJL259A",
    "arubaSwitchJL260A",
    "arubaSwitchJL261A",
    "arubaSwitchJL262A",
    "arubaSwitchJL263A",
    "arubaSwitchJL264A",
    "arubaSwitchJL319A",
    "arubaSwitchJL320A",
    "arubaSwitchJL321A",
    "arubaSwitchJL322A",
    "arubaSwitchJL323A",
    "arubaSwitchJL324A",
    "arubaSwitchJL354A",
    "arubaSwitchJL355A",
    "arubaSwitchJL356A",
    "arubaSwitchJL357A",
    "arubaSwitchJL557A",
    "arubaSwitchJL558A",
    "arubaSwitchJL559A",
    "bridge1010",
    "bridgeRemote",
    "eswitch",
    "eswitch2",
    "fiberOptic",
    "hp10BaseTHub12M",
    "hp10BaseTHub24M",
    "hpAdvStk100Tx12TM",
    "hpAdvStkEnetSH12R",
    "hpAdvStkEnetSH24R",
    "hpAdvStkEnetSH24T",
    "hpAdvStkEnetSHStack",
    "hpAdvSwitch200",
    "hpAdvSwitch2000",
    "hpAdvSwitch2000B",
    "hpAdvSwitch800T",
    "hpProCurve10T100THub12M",
    "hpProCurve10T100THub24M",
    "hpStack",
    "hpStack2920",
    "hpStackVSF5400R",
    "hpSwitch1600",
    "hpSwitch212M",
    "hpSwitch224M",
    "hpSwitch2400",
    "hpSwitch2424",
    "hpSwitch4000",
    "hpSwitch498358-B21",
    "hpSwitch516733-B21",
    "hpSwitch6308",
    "hpSwitch8000",
    "hpSwitch9304",
    "hpSwitch9308",
    "hpSwitchJ4812A",
    "hpSwitchJ4813A",
    "hpSwitchJ4819A",
    "hpSwitchJ4850A",
    "hpSwitchJ4865A",
    "hpSwitchJ4874A",
    "hpSwitchJ4887A",
    "hpSwitchJ4899A",
    "hpSwitchJ4899B",
    "hpSwitchJ4899C",
    "hpSwitchJ4900A",
    "hpSwitchJ4900B",
    "hpSwitchJ4900C",
    "hpSwitchJ4902A",
    "hpSwitchJ4903A",
    "hpSwitchJ4904A",
    "hpSwitchJ4905A",
    "hpSwitchJ4906A",
    "hpSwitchJ8164A",
    "hpSwitchJ8165A",
    "hpSwitchJ8433A",
    "hpSwitchJ8474A",
    "hpSwitchJ8680A",
    "hpSwitchJ8692A",
    "hpSwitchJ8693A",
    "hpSwitchJ8697A",
    "hpSwitchJ8698A",
    "hpSwitchJ8762A",
    "hpSwitchJ8992A",
    "hpSwitchJ9019A",
    "hpSwitchJ9019B",
    "hpSwitchJ9020A",
    "hpSwitchJ9021A",
    "hpSwitchJ9022A",
    "hpSwitchJ9028A",
    "hpSwitchJ9028B",
    "hpSwitchJ9029A",
    "hpSwitchJ9049A",
    "hpSwitchJ9050A",
    "hpSwitchJ9079A",
    "hpSwitchJ9080A",
    "hpSwitchJ9085A",
    "hpSwitchJ9086A",
    "hpSwitchJ9087A",
    "hpSwitchJ9088A",
    "hpSwitchJ9089A",
    "hpSwitchJ9091A",
    "hpSwitchJ9137A",
    "hpSwitchJ9138A",
    "hpSwitchJ9145A",
    "hpSwitchJ9146A",
    "hpSwitchJ9147A",
    "hpSwitchJ9148A",
    "hpSwitchJ9263A",
    "hpSwitchJ9264A",
    "hpSwitchJ9265A",
    "hpSwitchJ9279A",
    "hpSwitchJ9280A",
    "hpSwitchJ9298A",
    "hpSwitchJ9299A",
    "hpSwitchJ9310A",
    "hpSwitchJ9311A",
    "hpSwitchJ9449A",
    "hpSwitchJ9450A",
    "hpSwitchJ9451A",
    "hpSwitchJ9452A",
    "hpSwitchJ9470A",
    "hpSwitchJ9471A",
    "hpSwitchJ9472A",
    "hpSwitchJ9473A",
    "hpSwitchJ9477A",
    "hpSwitchJ9562A",
    "hpSwitchJ9565A",
    "hpSwitchJ9573",
    "hpSwitchJ9574",
    "hpSwitchJ9575",
    "hpSwitchJ9576",
    "hpSwitchJ9584",
    "hpSwitchJ9585",
    "hpSwitchJ9586",
    "hpSwitchJ9587",
    "hpSwitchJ9588",
    "hpSwitchJ9623A",
    "hpSwitchJ9624A",
    "hpSwitchJ9625A",
    "hpSwitchJ9626A",
    "hpSwitchJ9627A",
    "hpSwitchJ9660A",
    "hpSwitchJ9726A",
    "hpSwitchJ9727A",
    "hpSwitchJ9728A",
    "hpSwitchJ9729A",
    "hpSwitchJ9772A",
    "hpSwitchJ9773A",
    "hpSwitchJ9774A",
    "hpSwitchJ9775A",
    "hpSwitchJ9776A",
    "hpSwitchJ9777A",
    "hpSwitchJ9778A",
    "hpSwitchJ9779A",
    "hpSwitchJ9780A",
    "hpSwitchJ9781A",
    "hpSwitchJ9782A",
    "hpSwitchJ9783A",
    "hpSwitchJ9800A",
    "hpSwitchJ9801A",
    "hpSwitchJ9802A",
    "hpSwitchJ9803A",
    "hpSwitchJ9833A",
    "hpSwitchJ9834A",
    "hpSwitchJ9850A",
    "hpSwitchJ9851A",
    "hpSwitchJ9853A",
    "hpSwitchJ9854A",
    "hpSwitchJ9855A",
    "hpSwitchJ9856A",
    "hpSwitchJL070A",
    "icfRouter210",
    "icfRouter230",
    "icfRouter250",
    "icfRouter255",
    "icfRouter650",
    "icfRouterBR",
    "icfRouterER",
    "icfRouterFR",
    "icfRouterLR",
    "icfRouterPR",
    "icfRouterSR",
    "icfRouterTR",
    "netSwitch100",
    "netSwitch200")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

bridge1010trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 1, 0, 2)
)
if mibBuilder.loadTexts:
    bridge1010trap.setStatus(
        ""
    )

bridgeRemotetrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 2, 0, 2)
)
if mibBuilder.loadTexts:
    bridgeRemotetrap.setStatus(
        ""
    )

eswitchtrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 3, 0, 2)
)
if mibBuilder.loadTexts:
    eswitchtrap.setStatus(
        ""
    )

eswitch2trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 8, 0, 2)
)
if mibBuilder.loadTexts:
    eswitch2trap.setStatus(
        ""
    )

netSwitch100trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 9, 0, 2)
)
if mibBuilder.loadTexts:
    netSwitch100trap.setStatus(
        ""
    )

netSwitch200trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 10, 0, 2)
)
if mibBuilder.loadTexts:
    netSwitch200trap.setStatus(
        ""
    )

icfRouterERtrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 1, 0, 2)
)
if mibBuilder.loadTexts:
    icfRouterERtrap.setStatus(
        ""
    )

icfRouterTRtrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 2, 0, 2)
)
if mibBuilder.loadTexts:
    icfRouterTRtrap.setStatus(
        ""
    )

icfRouterSRtrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 3, 0, 2)
)
if mibBuilder.loadTexts:
    icfRouterSRtrap.setStatus(
        ""
    )

icfRouterFRtrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 4, 0, 2)
)
if mibBuilder.loadTexts:
    icfRouterFRtrap.setStatus(
        ""
    )

icfRouterLRtrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 5, 0, 2)
)
if mibBuilder.loadTexts:
    icfRouterLRtrap.setStatus(
        ""
    )

icfRouterBRtrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 6, 0, 2)
)
if mibBuilder.loadTexts:
    icfRouterBRtrap.setStatus(
        ""
    )

icfRouterPRtrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 7, 0, 2)
)
if mibBuilder.loadTexts:
    icfRouterPRtrap.setStatus(
        ""
    )

icfRouter650trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 8, 0, 2)
)
if mibBuilder.loadTexts:
    icfRouter650trap.setStatus(
        ""
    )

icfRouter230trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 9, 0, 2)
)
if mibBuilder.loadTexts:
    icfRouter230trap.setStatus(
        ""
    )

icfRouter250trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 10, 0, 2)
)
if mibBuilder.loadTexts:
    icfRouter250trap.setStatus(
        ""
    )

icfRouter255trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 11, 0, 2)
)
if mibBuilder.loadTexts:
    icfRouter255trap.setStatus(
        ""
    )

icfRouter210trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 12, 0, 2)
)
if mibBuilder.loadTexts:
    icfRouter210trap.setStatus(
        ""
    )

fiberOptictrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 3, 0, 2)
)
if mibBuilder.loadTexts:
    fiberOptictrap.setStatus(
        ""
    )

advStack12trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 7, 0, 2)
)
if mibBuilder.loadTexts:
    advStack12trap.setStatus(
        ""
    )

advStack24trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 8, 0, 2)
)
if mibBuilder.loadTexts:
    advStack24trap.setStatus(
        ""
    )

advStack48trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 9, 0, 2)
)
if mibBuilder.loadTexts:
    advStack48trap.setStatus(
        ""
    )

advStackU8trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 11, 0, 2)
)
if mibBuilder.loadTexts:
    advStackU8trap.setStatus(
        ""
    )

advStackU16trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 12, 0, 2)
)
if mibBuilder.loadTexts:
    advStackU16trap.setStatus(
        ""
    )

hpAdvStkEnetSH12Rtrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 15, 0, 2)
)
if mibBuilder.loadTexts:
    hpAdvStkEnetSH12Rtrap.setStatus(
        ""
    )

hpAdvStkEnetSH24Rtrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 16, 0, 2)
)
if mibBuilder.loadTexts:
    hpAdvStkEnetSH24Rtrap.setStatus(
        ""
    )

hpAdvStkEnetSH24Ttrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 17, 0, 2)
)
if mibBuilder.loadTexts:
    hpAdvStkEnetSH24Ttrap.setStatus(
        ""
    )

hpAdvStk100Tx12TMtrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 18, 0, 2)
)
if mibBuilder.loadTexts:
    hpAdvStk100Tx12TMtrap.setStatus(
        ""
    )

hp10BaseTHub12Mtrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 20, 0, 2)
)
if mibBuilder.loadTexts:
    hp10BaseTHub12Mtrap.setStatus(
        ""
    )

hp10BaseTHub24Mtrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 21, 0, 2)
)
if mibBuilder.loadTexts:
    hp10BaseTHub24Mtrap.setStatus(
        ""
    )

hpProCurve10T100THub12Mtrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 22, 0, 2)
)
if mibBuilder.loadTexts:
    hpProCurve10T100THub12Mtrap.setStatus(
        ""
    )

hpProCurve10T100THub24Mtrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 23, 0, 2)
)
if mibBuilder.loadTexts:
    hpProCurve10T100THub24Mtrap.setStatus(
        ""
    )

hpAdvStkEnetSHStacktrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 5, 1, 0, 2)
)
if mibBuilder.loadTexts:
    hpAdvStkEnetSHStacktrap.setStatus(
        ""
    )

hpStacktrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 5, 2, 0, 2)
)
if mibBuilder.loadTexts:
    hpStacktrap.setStatus(
        ""
    )

hpStack2920trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 5, 3, 0, 2)
)
if mibBuilder.loadTexts:
    hpStack2920trap.setStatus(
        ""
    )

arubaStack3810trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 5, 4, 0, 2)
)
if mibBuilder.loadTexts:
    arubaStack3810trap.setStatus(
        ""
    )

arubaStack2930trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 5, 5, 0, 2)
)
if mibBuilder.loadTexts:
    arubaStack2930trap.setStatus(
        ""
    )

hpStackVSF5400Rtrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 5, 6, 0, 2)
)
if mibBuilder.loadTexts:
    hpStackVSF5400Rtrap.setStatus(
        ""
    )

arubaStack2930Mtrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 5, 7, 0, 2)
)
if mibBuilder.loadTexts:
    arubaStack2930Mtrap.setStatus(
        ""
    )

hpAdvSwitch2000trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 1, 0, 2)
)
if mibBuilder.loadTexts:
    hpAdvSwitch2000trap.setStatus(
        ""
    )

hpAdvSwitch2000Btrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 2, 0, 2)
)
if mibBuilder.loadTexts:
    hpAdvSwitch2000Btrap.setStatus(
        ""
    )

hpAdvSwitch800Ttrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 3, 0, 2)
)
if mibBuilder.loadTexts:
    hpAdvSwitch800Ttrap.setStatus(
        ""
    )

hpAdvSwitch200trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 4, 0, 2)
)
if mibBuilder.loadTexts:
    hpAdvSwitch200trap.setStatus(
        ""
    )

hpSwitch212Mtrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 5, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitch212Mtrap.setStatus(
        ""
    )

hpSwitch224Mtrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 6, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitch224Mtrap.setStatus(
        ""
    )

hpSwitch8000trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 7, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitch8000trap.setStatus(
        ""
    )

hpSwitch1600trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 8, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitch1600trap.setStatus(
        ""
    )

hpSwitchJ4121Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 9, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ4121Atrap.setStatus(
        ""
    )

hpSwitch2400trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 10, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitch2400trap.setStatus(
        ""
    )

hpSwitch2424trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 11, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitch2424trap.setStatus(
        ""
    )

hpSwitchJ9308trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 13, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9308trap.setStatus(
        ""
    )

hpSwitchJ9304trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 14, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9304trap.setStatus(
        ""
    )

hpSwitch6308trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 15, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitch6308trap.setStatus(
        ""
    )

hpSwitchJ4819Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ4819Atrap.setStatus(
        ""
    )

hpSwitchJ4812Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 18, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ4812Atrap.setStatus(
        ""
    )

hpSwitchJ4813Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 19, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ4813Atrap.setStatus(
        ""
    )

hpSwitchJ4850Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 20, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ4850Atrap.setStatus(
        ""
    )

hpSwitchJ4865Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 23, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ4865Atrap.setStatus(
        ""
    )

hpSwitchJ4887Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 27, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ4887Atrap.setStatus(
        ""
    )

hpSwitchJ4874Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 28, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ4874Atrap.setStatus(
        ""
    )

hpSwitchJ4899Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 29, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ4899Atrap.setStatus(
        ""
    )

hpSwitchJ4902Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 30, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ4902Atrap.setStatus(
        ""
    )

hpSwitchJ4903Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 31, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ4903Atrap.setStatus(
        ""
    )

hpSwitchJ4904Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 32, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ4904Atrap.setStatus(
        ""
    )

hpSwitchJ4900Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 34, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ4900Atrap.setStatus(
        ""
    )

hpSwitchJ8165Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 35, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ8165Atrap.setStatus(
        ""
    )

hpSwitchJ8164Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 36, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ8164Atrap.setStatus(
        ""
    )

hpSwitchJ4905Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 42, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ4905Atrap.setStatus(
        ""
    )

hpSwitchJ4906Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 43, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ4906Atrap.setStatus(
        ""
    )

hpSwitchJ4899Btrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 44, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ4899Btrap.setStatus(
        ""
    )

hpSwitchJ4900Btrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 45, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ4900Btrap.setStatus(
        ""
    )

hpSwitchJ8433Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 48, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ8433Atrap.setStatus(
        ""
    )

hpSwitchJ8474Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 49, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ8474Atrap.setStatus(
        ""
    )

hpSwitchJ8697Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ8697Atrap.setStatus(
        ""
    )

hpSwitchJ8698Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 51, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ8698Atrap.setStatus(
        ""
    )

hpSwitchJ8680Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 54, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ8680Atrap.setStatus(
        ""
    )

hpSwitchJ8762Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 55, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ8762Atrap.setStatus(
        ""
    )

hpSwitchJ8692Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 58, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ8692Atrap.setStatus(
        ""
    )

hpSwitchJ8693Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 59, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ8693Atrap.setStatus(
        ""
    )

hpSwitchJ8992Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 60, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ8992Atrap.setStatus(
        ""
    )

hpSwitchJ9019Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 61, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9019Atrap.setStatus(
        ""
    )

hpSwitchJ9020Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 62, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9020Atrap.setStatus(
        ""
    )

hpSwitchJ9021Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 63, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9021Atrap.setStatus(
        ""
    )

hpSwitchJ9022Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 64, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9022Atrap.setStatus(
        ""
    )

hpSwitchJ9028Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 65, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9028Atrap.setStatus(
        ""
    )

hpSwitchJ9029Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 66, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9029Atrap.setStatus(
        ""
    )

hpSwitchJ9050Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 68, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9050Atrap.setStatus(
        ""
    )

hpSwitchJ9049Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 69, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9049Atrap.setStatus(
        ""
    )

hpSwitchJ9091Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 72, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9091Atrap.setStatus(
        ""
    )

hpSwitchJ9079Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 74, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9079Atrap.setStatus(
        ""
    )

hpSwitchJ9080Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 75, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9080Atrap.setStatus(
        ""
    )

hpSwitchJ9085Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 76, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9085Atrap.setStatus(
        ""
    )

hpSwitchJ9088Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 77, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9088Atrap.setStatus(
        ""
    )

hpSwitchJ9087Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 78, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9087Atrap.setStatus(
        ""
    )

hpSwitchJ9089Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 79, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9089Atrap.setStatus(
        ""
    )

hpSwitchJ9086Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 80, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9086Atrap.setStatus(
        ""
    )

hpSwitchJ9028Btrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 81, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9028Btrap.setStatus(
        ""
    )

hpSwitchJ4900Ctrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 82, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ4900Ctrap.setStatus(
        ""
    )

hpSwitchJ4899Ctrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 83, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ4899Ctrap.setStatus(
        ""
    )

hpSwitchJ9146Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 84, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9146Atrap.setStatus(
        ""
    )

hpSwitchJ9148Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 85, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9148Atrap.setStatus(
        ""
    )

hpSwitchJ9145Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 86, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9145Atrap.setStatus(
        ""
    )

hpSwitchJ9147Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 87, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9147Atrap.setStatus(
        ""
    )

hpSwitchJ9279Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 88, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9279Atrap.setStatus(
        ""
    )

hpSwitchJ9280Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 89, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9280Atrap.setStatus(
        ""
    )

hpSwitchJ9019Btrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 90, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9019Btrap.setStatus(
        ""
    )

hpSwitchJ9137Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 94, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9137Atrap.setStatus(
        ""
    )

hpSwitchJ9138Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 95, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9138Atrap.setStatus(
        ""
    )

hpSwitchJ9298Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 96, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9298Atrap.setStatus(
        ""
    )

hpSwitchJ9299Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 97, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9299Atrap.setStatus(
        ""
    )

hpSwitchJ9265Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 98, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9265Atrap.setStatus(
        ""
    )

hpSwitchJ9263Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 100, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9263Atrap.setStatus(
        ""
    )

hpSwitchJ9264Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 101, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9264Atrap.setStatus(
        ""
    )

hpSwitchJ9449Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 103, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9449Atrap.setStatus(
        ""
    )

hpSwitchJ9450Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 104, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9450Atrap.setStatus(
        ""
    )

hpSwitchJ9452Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 105, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9452Atrap.setStatus(
        ""
    )

hpSwitchJ9451Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 106, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9451Atrap.setStatus(
        ""
    )

hpSwitch516733_B21trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 107, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitch516733_B21trap.setStatus(
        ""
    )

hpSwitch498358_B21trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 108, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitch498358_B21trap.setStatus(
        ""
    )

hpSwitchJ9471Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 109, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9471Atrap.setStatus(
        ""
    )

hpSwitchJ9473Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 110, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9473Atrap.setStatus(
        ""
    )

hpSwitchJ9470Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 111, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9470Atrap.setStatus(
        ""
    )

hpSwitchJ9472Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 112, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9472Atrap.setStatus(
        ""
    )

hpSwitchJ9477Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 113, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9477Atrap.setStatus(
        ""
    )

hpSwitchJ9310Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 114, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9310Atrap.setStatus(
        ""
    )

hpSwitchJ9311Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 115, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9311Atrap.setStatus(
        ""
    )

hpSwitchJ9565Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 117, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9565Atrap.setStatus(
        ""
    )

hpSwitchJ9562Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 118, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9562Atrap.setStatus(
        ""
    )

hpSwitchJ9573Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 119, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9573Atrap.setStatus(
        ""
    )

hpSwitchJ9574Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 120, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9574Atrap.setStatus(
        ""
    )

hpSwitchJ9575Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 121, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9575Atrap.setStatus(
        ""
    )

hpSwitchJ9576Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 122, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9576Atrap.setStatus(
        ""
    )

hpSwitchJ9584Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 123, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9584Atrap.setStatus(
        ""
    )

hpSwitchJ9585Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 124, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9585Atrap.setStatus(
        ""
    )

hpSwitchJ9586Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 125, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9586Atrap.setStatus(
        ""
    )

hpSwitchJ9587Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 126, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9587Atrap.setStatus(
        ""
    )

hpSwitchJ9588Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 127, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9588Atrap.setStatus(
        ""
    )

hpSwitchJ9623Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 129, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9623Atrap.setStatus(
        ""
    )

hpSwitchJ9624Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 130, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9624Atrap.setStatus(
        ""
    )

hpSwitchJ9625Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 131, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9625Atrap.setStatus(
        ""
    )

hpSwitchJ9626Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 132, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9626Atrap.setStatus(
        ""
    )

hpSwitchJ9627Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 133, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9627Atrap.setStatus(
        ""
    )

hpSwitchJ9660Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 134, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9660Atrap.setStatus(
        ""
    )

hpSwitchJ9772Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 136, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9772Atrap.setStatus(
        ""
    )

hpSwitchJ9773Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 137, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9773Atrap.setStatus(
        ""
    )

hpSwitchJ9774Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 138, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9774Atrap.setStatus(
        ""
    )

hpSwitchJ9775Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 139, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9775Atrap.setStatus(
        ""
    )

hpSwitchJ9776Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 140, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9776Atrap.setStatus(
        ""
    )

hpSwitchJ9777Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 141, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9777Atrap.setStatus(
        ""
    )

hpSwitchJ9778Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 142, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9778Atrap.setStatus(
        ""
    )

hpSwitchJ9779Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 143, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9779Atrap.setStatus(
        ""
    )

hpSwitchJ9780Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 144, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9780Atrap.setStatus(
        ""
    )

hpSwitchJ9781Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 145, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9781Atrap.setStatus(
        ""
    )

hpSwitchJ9782Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 146, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9782Atrap.setStatus(
        ""
    )

hpSwitchJ9783Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 147, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9783Atrap.setStatus(
        ""
    )

hpSwitchJ9800Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 148, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9800Atrap.setStatus(
        ""
    )

hpSwitchJ9801Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 149, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9801Atrap.setStatus(
        ""
    )

hpSwitchJ9802Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 150, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9802Atrap.setStatus(
        ""
    )

hpSwitchJ9803Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 151, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9803Atrap.setStatus(
        ""
    )

hpSwitchJ9726Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 152, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9726Atrap.setStatus(
        ""
    )

hpSwitchJ9727Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 153, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9727Atrap.setStatus(
        ""
    )

hpSwitchJ9728Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 154, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9728Atrap.setStatus(
        ""
    )

hpSwitchJ9729Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 155, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9729Atrap.setStatus(
        ""
    )

hpSwitchJ9833Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 158, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9833Atrap.setStatus(
        ""
    )

hpSwitchJ9834Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 159, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9834Atrap.setStatus(
        ""
    )

hpSwitchJ9850Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 160, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9850Atrap.setStatus(
        ""
    )

hpSwitchJ9851Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 161, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9851Atrap.setStatus(
        ""
    )

hpSwitchJ9853Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 163, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9853Atrap.setStatus(
        ""
    )

hpSwitchJ9854Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 164, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9854Atrap.setStatus(
        ""
    )

hpSwitchJ9855Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 165, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9855Atrap.setStatus(
        ""
    )

hpSwitchJ9856Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 166, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJ9856Atrap.setStatus(
        ""
    )

hpSwitchJL070Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 173, 0, 2)
)
if mibBuilder.loadTexts:
    hpSwitchJL070Atrap.setStatus(
        ""
    )

arubaJL071Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 1, 0, 2)
)
if mibBuilder.loadTexts:
    arubaJL071Atrap.setStatus(
        ""
    )

arubaJL072Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 2, 0, 2)
)
if mibBuilder.loadTexts:
    arubaJL072Atrap.setStatus(
        ""
    )

arubaJL073Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 3, 0, 2)
)
if mibBuilder.loadTexts:
    arubaJL073Atrap.setStatus(
        ""
    )

arubaJL074Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 4, 0, 2)
)
if mibBuilder.loadTexts:
    arubaJL074Atrap.setStatus(
        ""
    )

arubaJL075Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 5, 0, 2)
)
if mibBuilder.loadTexts:
    arubaJL075Atrap.setStatus(
        ""
    )

arubaJL076Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 6, 0, 2)
)
if mibBuilder.loadTexts:
    arubaJL076Atrap.setStatus(
        ""
    )

arubaJL077Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 7, 0, 2)
)
if mibBuilder.loadTexts:
    arubaJL077Atrap.setStatus(
        ""
    )

arubaSwitchJL319Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 2, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL319Atrap.setStatus(
        ""
    )

arubaSwitchJL321Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 3, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL321Atrap.setStatus(
        ""
    )

arubaSwitchJL320Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 4, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL320Atrap.setStatus(
        ""
    )

arubaSwitchJL322Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 5, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL322Atrap.setStatus(
        ""
    )

arubaSwitchJL324Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 6, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL324Atrap.setStatus(
        ""
    )

arubaSwitchJL323Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 9, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL323Atrap.setStatus(
        ""
    )

arubaSwitchJL258Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 16, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL258Atrap.setStatus(
        ""
    )

arubaSwitchJL253Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 18, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL253Atrap.setStatus(
        ""
    )

arubaSwitchJL254Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 19, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL254Atrap.setStatus(
        ""
    )

arubaSwitchJL255Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 20, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL255Atrap.setStatus(
        ""
    )

arubaSwitchJL256Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 21, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL256Atrap.setStatus(
        ""
    )

arubaSwitchJL259Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 22, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL259Atrap.setStatus(
        ""
    )

arubaSwitchJL260Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 23, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL260Atrap.setStatus(
        ""
    )

arubaSwitchJL261Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 24, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL261Atrap.setStatus(
        ""
    )

arubaSwitchJL262Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 25, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL262Atrap.setStatus(
        ""
    )

arubaSwitchJL558Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 26, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL558Atrap.setStatus(
        ""
    )

arubaSwitchJL557Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 27, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL557Atrap.setStatus(
        ""
    )

arubaSwitchJL263Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 276, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL263Atrap.setStatus(
        ""
    )

arubaSwitchJL264Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 277, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL264Atrap.setStatus(
        ""
    )

arubaSwitchJL559Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 282, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL559Atrap.setStatus(
        ""
    )

arubaSwitchJL354Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 182, 18, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL354Atrap.setStatus(
        ""
    )

arubaSwitchJL355Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 182, 19, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL355Atrap.setStatus(
        ""
    )

arubaSwitchJL356Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 182, 20, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL356Atrap.setStatus(
        ""
    )

arubaSwitchJL357Atrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 182, 21, 0, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL357Atrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SWITCH-TRAP-MIB",
    **{"bridge1010trap": bridge1010trap,
       "bridgeRemotetrap": bridgeRemotetrap,
       "eswitchtrap": eswitchtrap,
       "eswitch2trap": eswitch2trap,
       "netSwitch100trap": netSwitch100trap,
       "netSwitch200trap": netSwitch200trap,
       "icfRouterERtrap": icfRouterERtrap,
       "icfRouterTRtrap": icfRouterTRtrap,
       "icfRouterSRtrap": icfRouterSRtrap,
       "icfRouterFRtrap": icfRouterFRtrap,
       "icfRouterLRtrap": icfRouterLRtrap,
       "icfRouterBRtrap": icfRouterBRtrap,
       "icfRouterPRtrap": icfRouterPRtrap,
       "icfRouter650trap": icfRouter650trap,
       "icfRouter230trap": icfRouter230trap,
       "icfRouter250trap": icfRouter250trap,
       "icfRouter255trap": icfRouter255trap,
       "icfRouter210trap": icfRouter210trap,
       "fiberOptictrap": fiberOptictrap,
       "advStack12trap": advStack12trap,
       "advStack24trap": advStack24trap,
       "advStack48trap": advStack48trap,
       "advStackU8trap": advStackU8trap,
       "advStackU16trap": advStackU16trap,
       "hpAdvStkEnetSH12Rtrap": hpAdvStkEnetSH12Rtrap,
       "hpAdvStkEnetSH24Rtrap": hpAdvStkEnetSH24Rtrap,
       "hpAdvStkEnetSH24Ttrap": hpAdvStkEnetSH24Ttrap,
       "hpAdvStk100Tx12TMtrap": hpAdvStk100Tx12TMtrap,
       "hp10BaseTHub12Mtrap": hp10BaseTHub12Mtrap,
       "hp10BaseTHub24Mtrap": hp10BaseTHub24Mtrap,
       "hpProCurve10T100THub12Mtrap": hpProCurve10T100THub12Mtrap,
       "hpProCurve10T100THub24Mtrap": hpProCurve10T100THub24Mtrap,
       "hpAdvStkEnetSHStacktrap": hpAdvStkEnetSHStacktrap,
       "hpStacktrap": hpStacktrap,
       "hpStack2920trap": hpStack2920trap,
       "arubaStack3810trap": arubaStack3810trap,
       "arubaStack2930trap": arubaStack2930trap,
       "hpStackVSF5400Rtrap": hpStackVSF5400Rtrap,
       "arubaStack2930Mtrap": arubaStack2930Mtrap,
       "hpAdvSwitch2000trap": hpAdvSwitch2000trap,
       "hpAdvSwitch2000Btrap": hpAdvSwitch2000Btrap,
       "hpAdvSwitch800Ttrap": hpAdvSwitch800Ttrap,
       "hpAdvSwitch200trap": hpAdvSwitch200trap,
       "hpSwitch212Mtrap": hpSwitch212Mtrap,
       "hpSwitch224Mtrap": hpSwitch224Mtrap,
       "hpSwitch8000trap": hpSwitch8000trap,
       "hpSwitch1600trap": hpSwitch1600trap,
       "hpSwitchJ4121Atrap": hpSwitchJ4121Atrap,
       "hpSwitch2400trap": hpSwitch2400trap,
       "hpSwitch2424trap": hpSwitch2424trap,
       "hpSwitchJ9308trap": hpSwitchJ9308trap,
       "hpSwitchJ9304trap": hpSwitchJ9304trap,
       "hpSwitch6308trap": hpSwitch6308trap,
       "hpSwitchJ4819Atrap": hpSwitchJ4819Atrap,
       "hpSwitchJ4812Atrap": hpSwitchJ4812Atrap,
       "hpSwitchJ4813Atrap": hpSwitchJ4813Atrap,
       "hpSwitchJ4850Atrap": hpSwitchJ4850Atrap,
       "hpSwitchJ4865Atrap": hpSwitchJ4865Atrap,
       "hpSwitchJ4887Atrap": hpSwitchJ4887Atrap,
       "hpSwitchJ4874Atrap": hpSwitchJ4874Atrap,
       "hpSwitchJ4899Atrap": hpSwitchJ4899Atrap,
       "hpSwitchJ4902Atrap": hpSwitchJ4902Atrap,
       "hpSwitchJ4903Atrap": hpSwitchJ4903Atrap,
       "hpSwitchJ4904Atrap": hpSwitchJ4904Atrap,
       "hpSwitchJ4900Atrap": hpSwitchJ4900Atrap,
       "hpSwitchJ8165Atrap": hpSwitchJ8165Atrap,
       "hpSwitchJ8164Atrap": hpSwitchJ8164Atrap,
       "hpSwitchJ4905Atrap": hpSwitchJ4905Atrap,
       "hpSwitchJ4906Atrap": hpSwitchJ4906Atrap,
       "hpSwitchJ4899Btrap": hpSwitchJ4899Btrap,
       "hpSwitchJ4900Btrap": hpSwitchJ4900Btrap,
       "hpSwitchJ8433Atrap": hpSwitchJ8433Atrap,
       "hpSwitchJ8474Atrap": hpSwitchJ8474Atrap,
       "hpSwitchJ8697Atrap": hpSwitchJ8697Atrap,
       "hpSwitchJ8698Atrap": hpSwitchJ8698Atrap,
       "hpSwitchJ8680Atrap": hpSwitchJ8680Atrap,
       "hpSwitchJ8762Atrap": hpSwitchJ8762Atrap,
       "hpSwitchJ8692Atrap": hpSwitchJ8692Atrap,
       "hpSwitchJ8693Atrap": hpSwitchJ8693Atrap,
       "hpSwitchJ8992Atrap": hpSwitchJ8992Atrap,
       "hpSwitchJ9019Atrap": hpSwitchJ9019Atrap,
       "hpSwitchJ9020Atrap": hpSwitchJ9020Atrap,
       "hpSwitchJ9021Atrap": hpSwitchJ9021Atrap,
       "hpSwitchJ9022Atrap": hpSwitchJ9022Atrap,
       "hpSwitchJ9028Atrap": hpSwitchJ9028Atrap,
       "hpSwitchJ9029Atrap": hpSwitchJ9029Atrap,
       "hpSwitchJ9050Atrap": hpSwitchJ9050Atrap,
       "hpSwitchJ9049Atrap": hpSwitchJ9049Atrap,
       "hpSwitchJ9091Atrap": hpSwitchJ9091Atrap,
       "hpSwitchJ9079Atrap": hpSwitchJ9079Atrap,
       "hpSwitchJ9080Atrap": hpSwitchJ9080Atrap,
       "hpSwitchJ9085Atrap": hpSwitchJ9085Atrap,
       "hpSwitchJ9088Atrap": hpSwitchJ9088Atrap,
       "hpSwitchJ9087Atrap": hpSwitchJ9087Atrap,
       "hpSwitchJ9089Atrap": hpSwitchJ9089Atrap,
       "hpSwitchJ9086Atrap": hpSwitchJ9086Atrap,
       "hpSwitchJ9028Btrap": hpSwitchJ9028Btrap,
       "hpSwitchJ4900Ctrap": hpSwitchJ4900Ctrap,
       "hpSwitchJ4899Ctrap": hpSwitchJ4899Ctrap,
       "hpSwitchJ9146Atrap": hpSwitchJ9146Atrap,
       "hpSwitchJ9148Atrap": hpSwitchJ9148Atrap,
       "hpSwitchJ9145Atrap": hpSwitchJ9145Atrap,
       "hpSwitchJ9147Atrap": hpSwitchJ9147Atrap,
       "hpSwitchJ9279Atrap": hpSwitchJ9279Atrap,
       "hpSwitchJ9280Atrap": hpSwitchJ9280Atrap,
       "hpSwitchJ9019Btrap": hpSwitchJ9019Btrap,
       "hpSwitchJ9137Atrap": hpSwitchJ9137Atrap,
       "hpSwitchJ9138Atrap": hpSwitchJ9138Atrap,
       "hpSwitchJ9298Atrap": hpSwitchJ9298Atrap,
       "hpSwitchJ9299Atrap": hpSwitchJ9299Atrap,
       "hpSwitchJ9265Atrap": hpSwitchJ9265Atrap,
       "hpSwitchJ9263Atrap": hpSwitchJ9263Atrap,
       "hpSwitchJ9264Atrap": hpSwitchJ9264Atrap,
       "hpSwitchJ9449Atrap": hpSwitchJ9449Atrap,
       "hpSwitchJ9450Atrap": hpSwitchJ9450Atrap,
       "hpSwitchJ9452Atrap": hpSwitchJ9452Atrap,
       "hpSwitchJ9451Atrap": hpSwitchJ9451Atrap,
       "hpSwitch516733-B21trap": hpSwitch516733_B21trap,
       "hpSwitch498358-B21trap": hpSwitch498358_B21trap,
       "hpSwitchJ9471Atrap": hpSwitchJ9471Atrap,
       "hpSwitchJ9473Atrap": hpSwitchJ9473Atrap,
       "hpSwitchJ9470Atrap": hpSwitchJ9470Atrap,
       "hpSwitchJ9472Atrap": hpSwitchJ9472Atrap,
       "hpSwitchJ9477Atrap": hpSwitchJ9477Atrap,
       "hpSwitchJ9310Atrap": hpSwitchJ9310Atrap,
       "hpSwitchJ9311Atrap": hpSwitchJ9311Atrap,
       "hpSwitchJ9565Atrap": hpSwitchJ9565Atrap,
       "hpSwitchJ9562Atrap": hpSwitchJ9562Atrap,
       "hpSwitchJ9573Atrap": hpSwitchJ9573Atrap,
       "hpSwitchJ9574Atrap": hpSwitchJ9574Atrap,
       "hpSwitchJ9575Atrap": hpSwitchJ9575Atrap,
       "hpSwitchJ9576Atrap": hpSwitchJ9576Atrap,
       "hpSwitchJ9584Atrap": hpSwitchJ9584Atrap,
       "hpSwitchJ9585Atrap": hpSwitchJ9585Atrap,
       "hpSwitchJ9586Atrap": hpSwitchJ9586Atrap,
       "hpSwitchJ9587Atrap": hpSwitchJ9587Atrap,
       "hpSwitchJ9588Atrap": hpSwitchJ9588Atrap,
       "hpSwitchJ9623Atrap": hpSwitchJ9623Atrap,
       "hpSwitchJ9624Atrap": hpSwitchJ9624Atrap,
       "hpSwitchJ9625Atrap": hpSwitchJ9625Atrap,
       "hpSwitchJ9626Atrap": hpSwitchJ9626Atrap,
       "hpSwitchJ9627Atrap": hpSwitchJ9627Atrap,
       "hpSwitchJ9660Atrap": hpSwitchJ9660Atrap,
       "hpSwitchJ9772Atrap": hpSwitchJ9772Atrap,
       "hpSwitchJ9773Atrap": hpSwitchJ9773Atrap,
       "hpSwitchJ9774Atrap": hpSwitchJ9774Atrap,
       "hpSwitchJ9775Atrap": hpSwitchJ9775Atrap,
       "hpSwitchJ9776Atrap": hpSwitchJ9776Atrap,
       "hpSwitchJ9777Atrap": hpSwitchJ9777Atrap,
       "hpSwitchJ9778Atrap": hpSwitchJ9778Atrap,
       "hpSwitchJ9779Atrap": hpSwitchJ9779Atrap,
       "hpSwitchJ9780Atrap": hpSwitchJ9780Atrap,
       "hpSwitchJ9781Atrap": hpSwitchJ9781Atrap,
       "hpSwitchJ9782Atrap": hpSwitchJ9782Atrap,
       "hpSwitchJ9783Atrap": hpSwitchJ9783Atrap,
       "hpSwitchJ9800Atrap": hpSwitchJ9800Atrap,
       "hpSwitchJ9801Atrap": hpSwitchJ9801Atrap,
       "hpSwitchJ9802Atrap": hpSwitchJ9802Atrap,
       "hpSwitchJ9803Atrap": hpSwitchJ9803Atrap,
       "hpSwitchJ9726Atrap": hpSwitchJ9726Atrap,
       "hpSwitchJ9727Atrap": hpSwitchJ9727Atrap,
       "hpSwitchJ9728Atrap": hpSwitchJ9728Atrap,
       "hpSwitchJ9729Atrap": hpSwitchJ9729Atrap,
       "hpSwitchJ9833Atrap": hpSwitchJ9833Atrap,
       "hpSwitchJ9834Atrap": hpSwitchJ9834Atrap,
       "hpSwitchJ9850Atrap": hpSwitchJ9850Atrap,
       "hpSwitchJ9851Atrap": hpSwitchJ9851Atrap,
       "hpSwitchJ9853Atrap": hpSwitchJ9853Atrap,
       "hpSwitchJ9854Atrap": hpSwitchJ9854Atrap,
       "hpSwitchJ9855Atrap": hpSwitchJ9855Atrap,
       "hpSwitchJ9856Atrap": hpSwitchJ9856Atrap,
       "hpSwitchJL070Atrap": hpSwitchJL070Atrap,
       "arubaJL071Atrap": arubaJL071Atrap,
       "arubaJL072Atrap": arubaJL072Atrap,
       "arubaJL073Atrap": arubaJL073Atrap,
       "arubaJL074Atrap": arubaJL074Atrap,
       "arubaJL075Atrap": arubaJL075Atrap,
       "arubaJL076Atrap": arubaJL076Atrap,
       "arubaJL077Atrap": arubaJL077Atrap,
       "arubaSwitchJL319Atrap": arubaSwitchJL319Atrap,
       "arubaSwitchJL321Atrap": arubaSwitchJL321Atrap,
       "arubaSwitchJL320Atrap": arubaSwitchJL320Atrap,
       "arubaSwitchJL322Atrap": arubaSwitchJL322Atrap,
       "arubaSwitchJL324Atrap": arubaSwitchJL324Atrap,
       "arubaSwitchJL323Atrap": arubaSwitchJL323Atrap,
       "arubaSwitchJL258Atrap": arubaSwitchJL258Atrap,
       "arubaSwitchJL253Atrap": arubaSwitchJL253Atrap,
       "arubaSwitchJL254Atrap": arubaSwitchJL254Atrap,
       "arubaSwitchJL255Atrap": arubaSwitchJL255Atrap,
       "arubaSwitchJL256Atrap": arubaSwitchJL256Atrap,
       "arubaSwitchJL259Atrap": arubaSwitchJL259Atrap,
       "arubaSwitchJL260Atrap": arubaSwitchJL260Atrap,
       "arubaSwitchJL261Atrap": arubaSwitchJL261Atrap,
       "arubaSwitchJL262Atrap": arubaSwitchJL262Atrap,
       "arubaSwitchJL558Atrap": arubaSwitchJL558Atrap,
       "arubaSwitchJL557Atrap": arubaSwitchJL557Atrap,
       "arubaSwitchJL263Atrap": arubaSwitchJL263Atrap,
       "arubaSwitchJL264Atrap": arubaSwitchJL264Atrap,
       "arubaSwitchJL559Atrap": arubaSwitchJL559Atrap,
       "arubaSwitchJL354Atrap": arubaSwitchJL354Atrap,
       "arubaSwitchJL355Atrap": arubaSwitchJL355Atrap,
       "arubaSwitchJL356Atrap": arubaSwitchJL356Atrap,
       "arubaSwitchJL357Atrap": arubaSwitchJL357Atrap}
)
