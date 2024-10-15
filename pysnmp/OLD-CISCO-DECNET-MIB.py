# SNMP MIB module (OLD-CISCO-DECNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OLD-CISCO-DECNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:59 2024
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

(temporary,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "temporary")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tmpdecnet_ObjectIdentity = ObjectIdentity
tmpdecnet = _Tmpdecnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 3, 1)
)
_DnForward_Type = Integer32
_DnForward_Object = MibScalar
dnForward = _DnForward_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 1),
    _DnForward_Type()
)
dnForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnForward.setStatus("mandatory")
_DnReceived_Type = Integer32
_DnReceived_Object = MibScalar
dnReceived = _DnReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 2),
    _DnReceived_Type()
)
dnReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnReceived.setStatus("mandatory")
_DnFormaterr_Type = Integer32
_DnFormaterr_Object = MibScalar
dnFormaterr = _DnFormaterr_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 3),
    _DnFormaterr_Type()
)
dnFormaterr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnFormaterr.setStatus("mandatory")
_DnNotgateway_Type = Integer32
_DnNotgateway_Object = MibScalar
dnNotgateway = _DnNotgateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 4),
    _DnNotgateway_Type()
)
dnNotgateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnNotgateway.setStatus("mandatory")
_DnNotimp_Type = Integer32
_DnNotimp_Object = MibScalar
dnNotimp = _DnNotimp_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 5),
    _DnNotimp_Type()
)
dnNotimp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnNotimp.setStatus("mandatory")
_DnHellos_Type = Integer32
_DnHellos_Object = MibScalar
dnHellos = _DnHellos_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 6),
    _DnHellos_Type()
)
dnHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnHellos.setStatus("mandatory")
_DnBadhello_Type = Integer32
_DnBadhello_Object = MibScalar
dnBadhello = _DnBadhello_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 7),
    _DnBadhello_Type()
)
dnBadhello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnBadhello.setStatus("mandatory")
_DnNotlong_Type = Integer32
_DnNotlong_Object = MibScalar
dnNotlong = _DnNotlong_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 8),
    _DnNotlong_Type()
)
dnNotlong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnNotlong.setStatus("mandatory")
_DnDatas_Type = Integer32
_DnDatas_Object = MibScalar
dnDatas = _DnDatas_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 9),
    _DnDatas_Type()
)
dnDatas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnDatas.setStatus("mandatory")
_DnBigaddr_Type = Integer32
_DnBigaddr_Object = MibScalar
dnBigaddr = _DnBigaddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 10),
    _DnBigaddr_Type()
)
dnBigaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnBigaddr.setStatus("mandatory")
_DnNoroute_Type = Integer32
_DnNoroute_Object = MibScalar
dnNoroute = _DnNoroute_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 11),
    _DnNoroute_Type()
)
dnNoroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnNoroute.setStatus("mandatory")
_DnNoencap_Type = Integer32
_DnNoencap_Object = MibScalar
dnNoencap = _DnNoencap_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 12),
    _DnNoencap_Type()
)
dnNoencap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnNoencap.setStatus("mandatory")
_DnLevel1s_Type = Integer32
_DnLevel1s_Object = MibScalar
dnLevel1s = _DnLevel1s_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 13),
    _DnLevel1s_Type()
)
dnLevel1s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnLevel1s.setStatus("mandatory")
_DnBadlevel1_Type = Integer32
_DnBadlevel1_Object = MibScalar
dnBadlevel1 = _DnBadlevel1_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 14),
    _DnBadlevel1_Type()
)
dnBadlevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnBadlevel1.setStatus("mandatory")
_DnToomanyhops_Type = Integer32
_DnToomanyhops_Object = MibScalar
dnToomanyhops = _DnToomanyhops_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 15),
    _DnToomanyhops_Type()
)
dnToomanyhops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnToomanyhops.setStatus("mandatory")
_DnHellosent_Type = Integer32
_DnHellosent_Object = MibScalar
dnHellosent = _DnHellosent_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 16),
    _DnHellosent_Type()
)
dnHellosent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnHellosent.setStatus("mandatory")
_DnLevel1sent_Type = Integer32
_DnLevel1sent_Object = MibScalar
dnLevel1sent = _DnLevel1sent_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 17),
    _DnLevel1sent_Type()
)
dnLevel1sent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnLevel1sent.setStatus("mandatory")
_DnNomemory_Type = Integer32
_DnNomemory_Object = MibScalar
dnNomemory = _DnNomemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 18),
    _DnNomemory_Type()
)
dnNomemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnNomemory.setStatus("mandatory")
_DnOtherhello_Type = Integer32
_DnOtherhello_Object = MibScalar
dnOtherhello = _DnOtherhello_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 19),
    _DnOtherhello_Type()
)
dnOtherhello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnOtherhello.setStatus("mandatory")
_DnOtherlevel1_Type = Integer32
_DnOtherlevel1_Object = MibScalar
dnOtherlevel1 = _DnOtherlevel1_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 20),
    _DnOtherlevel1_Type()
)
dnOtherlevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnOtherlevel1.setStatus("mandatory")
_DnLevel2s_Type = Integer32
_DnLevel2s_Object = MibScalar
dnLevel2s = _DnLevel2s_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 21),
    _DnLevel2s_Type()
)
dnLevel2s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnLevel2s.setStatus("mandatory")
_DnLevel2sent_Type = Integer32
_DnLevel2sent_Object = MibScalar
dnLevel2sent = _DnLevel2sent_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 22),
    _DnLevel2sent_Type()
)
dnLevel2sent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnLevel2sent.setStatus("mandatory")
_DnNovector_Type = Integer32
_DnNovector_Object = MibScalar
dnNovector = _DnNovector_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 23),
    _DnNovector_Type()
)
dnNovector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnNovector.setStatus("mandatory")
_DnOtherlevel2_Type = Integer32
_DnOtherlevel2_Object = MibScalar
dnOtherlevel2 = _DnOtherlevel2_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 24),
    _DnOtherlevel2_Type()
)
dnOtherlevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnOtherlevel2.setStatus("mandatory")
_DnNoaccess_Type = Integer32
_DnNoaccess_Object = MibScalar
dnNoaccess = _DnNoaccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 25),
    _DnNoaccess_Type()
)
dnNoaccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnNoaccess.setStatus("mandatory")
_DnAreaTable_Object = MibTable
dnAreaTable = _DnAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 26)
)
if mibBuilder.loadTexts:
    dnAreaTable.setStatus("mandatory")
_DnAreaTableEntry_Object = MibTableRow
dnAreaTableEntry = _DnAreaTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 26, 1)
)
dnAreaTableEntry.setIndexNames(
    (0, "OLD-CISCO-DECNET-MIB", "dnArea"),
)
if mibBuilder.loadTexts:
    dnAreaTableEntry.setStatus("mandatory")
_DnArea_Type = Integer32
_DnArea_Object = MibTableColumn
dnArea = _DnArea_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 26, 1, 1),
    _DnArea_Type()
)
dnArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnArea.setStatus("mandatory")
_DnACost_Type = Integer32
_DnACost_Object = MibTableColumn
dnACost = _DnACost_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 26, 1, 2),
    _DnACost_Type()
)
dnACost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnACost.setStatus("mandatory")
_DnAHop_Type = Integer32
_DnAHop_Object = MibTableColumn
dnAHop = _DnAHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 26, 1, 3),
    _DnAHop_Type()
)
dnAHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnAHop.setStatus("mandatory")
_DnAIfIndex_Type = Integer32
_DnAIfIndex_Object = MibTableColumn
dnAIfIndex = _DnAIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 26, 1, 4),
    _DnAIfIndex_Type()
)
dnAIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnAIfIndex.setStatus("mandatory")
_DnANextHop_Type = OctetString
_DnANextHop_Object = MibTableColumn
dnANextHop = _DnANextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 26, 1, 5),
    _DnANextHop_Type()
)
dnANextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnANextHop.setStatus("mandatory")
_DnAAge_Type = Integer32
_DnAAge_Object = MibTableColumn
dnAAge = _DnAAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 26, 1, 6),
    _DnAAge_Type()
)
dnAAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnAAge.setStatus("mandatory")
_DnAPrio_Type = Integer32
_DnAPrio_Object = MibTableColumn
dnAPrio = _DnAPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 26, 1, 7),
    _DnAPrio_Type()
)
dnAPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnAPrio.setStatus("mandatory")
_DnHostTable_Object = MibTable
dnHostTable = _DnHostTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 27)
)
if mibBuilder.loadTexts:
    dnHostTable.setStatus("mandatory")
_DnHostTableEntry_Object = MibTableRow
dnHostTableEntry = _DnHostTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 27, 1)
)
dnHostTableEntry.setIndexNames(
    (0, "OLD-CISCO-DECNET-MIB", "dnHIdx1"),
    (0, "OLD-CISCO-DECNET-MIB", "dnHIdx2"),
)
if mibBuilder.loadTexts:
    dnHostTableEntry.setStatus("mandatory")
_DnHost_Type = Integer32
_DnHost_Object = MibTableColumn
dnHost = _DnHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 27, 1, 1),
    _DnHost_Type()
)
dnHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnHost.setStatus("mandatory")
_DnHCost_Type = Integer32
_DnHCost_Object = MibTableColumn
dnHCost = _DnHCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 27, 1, 2),
    _DnHCost_Type()
)
dnHCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnHCost.setStatus("mandatory")
_DnHHop_Type = Integer32
_DnHHop_Object = MibTableColumn
dnHHop = _DnHHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 27, 1, 3),
    _DnHHop_Type()
)
dnHHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnHHop.setStatus("mandatory")
_DnHIfIndex_Type = Integer32
_DnHIfIndex_Object = MibTableColumn
dnHIfIndex = _DnHIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 27, 1, 4),
    _DnHIfIndex_Type()
)
dnHIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnHIfIndex.setStatus("mandatory")
_DnHNextHop_Type = OctetString
_DnHNextHop_Object = MibTableColumn
dnHNextHop = _DnHNextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 27, 1, 5),
    _DnHNextHop_Type()
)
dnHNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnHNextHop.setStatus("mandatory")
_DnHAge_Type = Integer32
_DnHAge_Object = MibTableColumn
dnHAge = _DnHAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 27, 1, 6),
    _DnHAge_Type()
)
dnHAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnHAge.setStatus("mandatory")
_DnHPrio_Type = Integer32
_DnHPrio_Object = MibTableColumn
dnHPrio = _DnHPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 27, 1, 7),
    _DnHPrio_Type()
)
dnHPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnHPrio.setStatus("mandatory")
_DnHIdx1_Type = Integer32
_DnHIdx1_Object = MibTableColumn
dnHIdx1 = _DnHIdx1_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 27, 1, 8),
    _DnHIdx1_Type()
)
dnHIdx1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnHIdx1.setStatus("mandatory")
_DnHIdx2_Type = Integer32
_DnHIdx2_Object = MibTableColumn
dnHIdx2 = _DnHIdx2_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 27, 1, 9),
    _DnHIdx2_Type()
)
dnHIdx2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnHIdx2.setStatus("mandatory")
_DnIfTable_Object = MibTable
dnIfTable = _DnIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 28)
)
if mibBuilder.loadTexts:
    dnIfTable.setStatus("mandatory")
_DnIfTableEntry_Object = MibTableRow
dnIfTableEntry = _DnIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 28, 1)
)
dnIfTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dnIfTableEntry.setStatus("mandatory")
_DnIfCost_Type = Integer32
_DnIfCost_Object = MibTableColumn
dnIfCost = _DnIfCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 28, 1, 1),
    _DnIfCost_Type()
)
dnIfCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnIfCost.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OLD-CISCO-DECNET-MIB",
    **{"tmpdecnet": tmpdecnet,
       "dnForward": dnForward,
       "dnReceived": dnReceived,
       "dnFormaterr": dnFormaterr,
       "dnNotgateway": dnNotgateway,
       "dnNotimp": dnNotimp,
       "dnHellos": dnHellos,
       "dnBadhello": dnBadhello,
       "dnNotlong": dnNotlong,
       "dnDatas": dnDatas,
       "dnBigaddr": dnBigaddr,
       "dnNoroute": dnNoroute,
       "dnNoencap": dnNoencap,
       "dnLevel1s": dnLevel1s,
       "dnBadlevel1": dnBadlevel1,
       "dnToomanyhops": dnToomanyhops,
       "dnHellosent": dnHellosent,
       "dnLevel1sent": dnLevel1sent,
       "dnNomemory": dnNomemory,
       "dnOtherhello": dnOtherhello,
       "dnOtherlevel1": dnOtherlevel1,
       "dnLevel2s": dnLevel2s,
       "dnLevel2sent": dnLevel2sent,
       "dnNovector": dnNovector,
       "dnOtherlevel2": dnOtherlevel2,
       "dnNoaccess": dnNoaccess,
       "dnAreaTable": dnAreaTable,
       "dnAreaTableEntry": dnAreaTableEntry,
       "dnArea": dnArea,
       "dnACost": dnACost,
       "dnAHop": dnAHop,
       "dnAIfIndex": dnAIfIndex,
       "dnANextHop": dnANextHop,
       "dnAAge": dnAAge,
       "dnAPrio": dnAPrio,
       "dnHostTable": dnHostTable,
       "dnHostTableEntry": dnHostTableEntry,
       "dnHost": dnHost,
       "dnHCost": dnHCost,
       "dnHHop": dnHHop,
       "dnHIfIndex": dnHIfIndex,
       "dnHNextHop": dnHNextHop,
       "dnHAge": dnHAge,
       "dnHPrio": dnHPrio,
       "dnHIdx1": dnHIdx1,
       "dnHIdx2": dnHIdx2,
       "dnIfTable": dnIfTable,
       "dnIfTableEntry": dnIfTableEntry,
       "dnIfCost": dnIfCost}
)
