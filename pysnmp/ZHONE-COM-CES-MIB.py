# SNMP MIB module (ZHONE-COM-CES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-COM-CES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:10 2024
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

(atmfCESAdminStatus,
 atmfCESAtmIndex,
 atmfCESAtmVci,
 atmfCESAtmVpi,
 atmfCESBufMaxSize,
 atmfCESCas,
 atmfCESCbrClockMode,
 atmfCESCbrIndex,
 atmfCESCbrService,
 atmfCESCdvRxT,
 atmfCESCellLossIntegrationPeriod,
 atmfCESConfEntry,
 atmfCESConfRowStatus,
 atmfCESConnType,
 atmfCESLocalAddr,
 atmfCESOperStatus,
 atmfCESPartialFill) = mibBuilder.importSymbols(
    "ATMF-CES",
    "atmfCESAdminStatus",
    "atmfCESAtmIndex",
    "atmfCESAtmVci",
    "atmfCESAtmVpi",
    "atmfCESBufMaxSize",
    "atmfCESCas",
    "atmfCESCbrClockMode",
    "atmfCESCbrIndex",
    "atmfCESCbrService",
    "atmfCESCdvRxT",
    "atmfCESCellLossIntegrationPeriod",
    "atmfCESConfEntry",
    "atmfCESConfRowStatus",
    "atmfCESConnType",
    "atmfCESLocalAddr",
    "atmfCESOperStatus",
    "atmfCESPartialFill")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(zhoneCes,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneCes",
    "zhoneModules")


# MODULE-IDENTITY

comCesExtension = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 108)
)
comCesExtension.setRevisions(
        ("2005-04-13 12:04",
         "2004-08-16 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhoneAtmfCESConfExtTable_Object = MibTable
zhoneAtmfCESConfExtTable = _ZhoneAtmfCESConfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 10, 1)
)
if mibBuilder.loadTexts:
    zhoneAtmfCESConfExtTable.setStatus("current")
_ZhoneAtmfCESConfExtEntry_Object = MibTableRow
zhoneAtmfCESConfExtEntry = _ZhoneAtmfCESConfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 10, 1, 1)
)
if mibBuilder.loadTexts:
    zhoneAtmfCESConfExtEntry.setStatus("current")


class _ZhoneAtmfCESDs0Bundle_Type(Bits):
    """Custom type zhoneAtmfCESDs0Bundle based on Bits"""
    namedValues = NamedValues(
        *(("ts0", 0),
          ("ts1", 1),
          ("ts10", 10),
          ("ts11", 11),
          ("ts12", 12),
          ("ts13", 13),
          ("ts14", 14),
          ("ts15", 15),
          ("ts16", 16),
          ("ts17", 17),
          ("ts18", 18),
          ("ts19", 19),
          ("ts2", 2),
          ("ts20", 20),
          ("ts21", 21),
          ("ts22", 22),
          ("ts23", 23),
          ("ts24", 24),
          ("ts25", 25),
          ("ts26", 26),
          ("ts27", 27),
          ("ts28", 28),
          ("ts29", 29),
          ("ts3", 3),
          ("ts30", 30),
          ("ts31", 31),
          ("ts4", 4),
          ("ts5", 5),
          ("ts6", 6),
          ("ts7", 7),
          ("ts8", 8),
          ("ts9", 9))
    )

_ZhoneAtmfCESDs0Bundle_Type.__name__ = "Bits"
_ZhoneAtmfCESDs0Bundle_Object = MibTableColumn
zhoneAtmfCESDs0Bundle = _ZhoneAtmfCESDs0Bundle_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 10, 1, 1, 1),
    _ZhoneAtmfCESDs0Bundle_Type()
)
zhoneAtmfCESDs0Bundle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneAtmfCESDs0Bundle.setStatus("current")
_ZhoneAtmfCESConfExtAtmfCESSrcIpAddr_Type = IpAddress
_ZhoneAtmfCESConfExtAtmfCESSrcIpAddr_Object = MibTableColumn
zhoneAtmfCESConfExtAtmfCESSrcIpAddr = _ZhoneAtmfCESConfExtAtmfCESSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 10, 1, 1, 2),
    _ZhoneAtmfCESConfExtAtmfCESSrcIpAddr_Type()
)
zhoneAtmfCESConfExtAtmfCESSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneAtmfCESConfExtAtmfCESSrcIpAddr.setStatus("current")
_ZhoneAtmfCESConfExtAtmfCESDstIpAddr_Type = IpAddress
_ZhoneAtmfCESConfExtAtmfCESDstIpAddr_Object = MibTableColumn
zhoneAtmfCESConfExtAtmfCESDstIpAddr = _ZhoneAtmfCESConfExtAtmfCESDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 10, 1, 1, 3),
    _ZhoneAtmfCESConfExtAtmfCESDstIpAddr_Type()
)
zhoneAtmfCESConfExtAtmfCESDstIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneAtmfCESConfExtAtmfCESDstIpAddr.setStatus("current")
_ZhoneAtmfCESConfExtAtmfCESSrcPort_Type = Unsigned32
_ZhoneAtmfCESConfExtAtmfCESSrcPort_Object = MibTableColumn
zhoneAtmfCESConfExtAtmfCESSrcPort = _ZhoneAtmfCESConfExtAtmfCESSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 10, 1, 1, 4),
    _ZhoneAtmfCESConfExtAtmfCESSrcPort_Type()
)
zhoneAtmfCESConfExtAtmfCESSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneAtmfCESConfExtAtmfCESSrcPort.setStatus("current")
_ZhoneAtmfCESConfExtAtmfCESDstPort_Type = Unsigned32
_ZhoneAtmfCESConfExtAtmfCESDstPort_Object = MibTableColumn
zhoneAtmfCESConfExtAtmfCESDstPort = _ZhoneAtmfCESConfExtAtmfCESDstPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 10, 1, 1, 5),
    _ZhoneAtmfCESConfExtAtmfCESDstPort_Type()
)
zhoneAtmfCESConfExtAtmfCESDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneAtmfCESConfExtAtmfCESDstPort.setStatus("current")
atmfCESConfEntry.registerAugmentions(
    ("ZHONE-COM-CES-MIB",
     "zhoneAtmfCESConfExtEntry")
)
zhoneAtmfCESConfExtEntry.setIndexNames(*atmfCESConfEntry.getIndexNames())

# Managed Objects groups

zhoneAtmfCESGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 10, 2)
)
zhoneAtmfCESGroup.setObjects(
    ("ZHONE-COM-CES-MIB", "zhoneAtmfCESDs0Bundle")
)
if mibBuilder.loadTexts:
    zhoneAtmfCESGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-COM-CES-MIB",
    **{"zhoneAtmfCESConfExtTable": zhoneAtmfCESConfExtTable,
       "zhoneAtmfCESConfExtEntry": zhoneAtmfCESConfExtEntry,
       "zhoneAtmfCESDs0Bundle": zhoneAtmfCESDs0Bundle,
       "zhoneAtmfCESConfExtAtmfCESSrcIpAddr": zhoneAtmfCESConfExtAtmfCESSrcIpAddr,
       "zhoneAtmfCESConfExtAtmfCESDstIpAddr": zhoneAtmfCESConfExtAtmfCESDstIpAddr,
       "zhoneAtmfCESConfExtAtmfCESSrcPort": zhoneAtmfCESConfExtAtmfCESSrcPort,
       "zhoneAtmfCESConfExtAtmfCESDstPort": zhoneAtmfCESConfExtAtmfCESDstPort,
       "zhoneAtmfCESGroup": zhoneAtmfCESGroup,
       "comCesExtension": comCesExtension}
)
