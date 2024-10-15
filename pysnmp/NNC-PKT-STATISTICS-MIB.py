# SNMP MIB module (NNC-PKT-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNC-PKT-STATISTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:14 2024
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

(atmVclVci,
 atmVclVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclVci",
    "atmVclVpi")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(NncExtAbsIntvlNumberType,
 NncExtIntvlStateType,
 NncExtRelIntvlNumberType) = mibBuilder.importSymbols(
    "NNC-INTERVAL-STATISTICS-TC-MIB",
    "NncExtAbsIntvlNumberType",
    "NncExtIntvlStateType",
    "NncExtRelIntvlNumberType")

(NncExtCounter64,
 nncExtensions) = mibBuilder.importSymbols(
    "NNCGNI0001-SMI",
    "NncExtCounter64",
    "nncExtensions")

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


# MODULE-IDENTITY

nncExtPktStatistics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 50)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NncPktVclCoSType(Integer32, TextualConvention):
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
        *(("controlAndRouting", 1),
          ("premium", 3),
          ("standard", 2))
    )



# MIB Managed Objects in the order of their OIDs

_NncPktStatisticsObjects_ObjectIdentity = ObjectIdentity
nncPktStatisticsObjects = _NncPktStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1)
)
_NncPktVcl15MinCurTable_Object = MibTable
nncPktVcl15MinCurTable = _NncPktVcl15MinCurTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 1)
)
if mibBuilder.loadTexts:
    nncPktVcl15MinCurTable.setStatus("current")
_NncPktVcl15MinCurEntry_Object = MibTableRow
nncPktVcl15MinCurEntry = _NncPktVcl15MinCurEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 1, 1)
)
nncPktVcl15MinCurEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinCurCoS"),
)
if mibBuilder.loadTexts:
    nncPktVcl15MinCurEntry.setStatus("current")
_NncPktVcl15MinCurCoS_Type = NncPktVclCoSType
_NncPktVcl15MinCurCoS_Object = MibTableColumn
nncPktVcl15MinCurCoS = _NncPktVcl15MinCurCoS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 1, 1, 1),
    _NncPktVcl15MinCurCoS_Type()
)
nncPktVcl15MinCurCoS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncPktVcl15MinCurCoS.setStatus("current")
_NncPktVcl15MinCurState_Type = NncExtIntvlStateType
_NncPktVcl15MinCurState_Object = MibTableColumn
nncPktVcl15MinCurState = _NncPktVcl15MinCurState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 1, 1, 2),
    _NncPktVcl15MinCurState_Type()
)
nncPktVcl15MinCurState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinCurState.setStatus("current")
_NncPktVcl15MinCurAbsoluteIntervalNumber_Type = NncExtAbsIntvlNumberType
_NncPktVcl15MinCurAbsoluteIntervalNumber_Object = MibTableColumn
nncPktVcl15MinCurAbsoluteIntervalNumber = _NncPktVcl15MinCurAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 1, 1, 3),
    _NncPktVcl15MinCurAbsoluteIntervalNumber_Type()
)
nncPktVcl15MinCurAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinCurAbsoluteIntervalNumber.setStatus("current")
_NncPktVcl15MinCurInOctets_Type = NncExtCounter64
_NncPktVcl15MinCurInOctets_Object = MibTableColumn
nncPktVcl15MinCurInOctets = _NncPktVcl15MinCurInOctets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 1, 1, 4),
    _NncPktVcl15MinCurInOctets_Type()
)
nncPktVcl15MinCurInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinCurInOctets.setStatus("current")
_NncPktVcl15MinCurInUcastPkts_Type = NncExtCounter64
_NncPktVcl15MinCurInUcastPkts_Object = MibTableColumn
nncPktVcl15MinCurInUcastPkts = _NncPktVcl15MinCurInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 1, 1, 5),
    _NncPktVcl15MinCurInUcastPkts_Type()
)
nncPktVcl15MinCurInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinCurInUcastPkts.setStatus("current")
_NncPktVcl15MinCurInMulticastPkts_Type = NncExtCounter64
_NncPktVcl15MinCurInMulticastPkts_Object = MibTableColumn
nncPktVcl15MinCurInMulticastPkts = _NncPktVcl15MinCurInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 1, 1, 6),
    _NncPktVcl15MinCurInMulticastPkts_Type()
)
nncPktVcl15MinCurInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinCurInMulticastPkts.setStatus("current")
_NncPktVcl15MinCurInBroadcastPkts_Type = NncExtCounter64
_NncPktVcl15MinCurInBroadcastPkts_Object = MibTableColumn
nncPktVcl15MinCurInBroadcastPkts = _NncPktVcl15MinCurInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 1, 1, 7),
    _NncPktVcl15MinCurInBroadcastPkts_Type()
)
nncPktVcl15MinCurInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinCurInBroadcastPkts.setStatus("current")
_NncPktVcl15MinCurInDiscards_Type = NncExtCounter64
_NncPktVcl15MinCurInDiscards_Object = MibTableColumn
nncPktVcl15MinCurInDiscards = _NncPktVcl15MinCurInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 1, 1, 8),
    _NncPktVcl15MinCurInDiscards_Type()
)
nncPktVcl15MinCurInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinCurInDiscards.setStatus("current")
_NncPktVcl15MinCurInErrors_Type = NncExtCounter64
_NncPktVcl15MinCurInErrors_Object = MibTableColumn
nncPktVcl15MinCurInErrors = _NncPktVcl15MinCurInErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 1, 1, 9),
    _NncPktVcl15MinCurInErrors_Type()
)
nncPktVcl15MinCurInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinCurInErrors.setStatus("current")
_NncPktVcl15MinCurOutOctets_Type = NncExtCounter64
_NncPktVcl15MinCurOutOctets_Object = MibTableColumn
nncPktVcl15MinCurOutOctets = _NncPktVcl15MinCurOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 1, 1, 10),
    _NncPktVcl15MinCurOutOctets_Type()
)
nncPktVcl15MinCurOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinCurOutOctets.setStatus("current")
_NncPktVcl15MinCurOutUcastPkts_Type = NncExtCounter64
_NncPktVcl15MinCurOutUcastPkts_Object = MibTableColumn
nncPktVcl15MinCurOutUcastPkts = _NncPktVcl15MinCurOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 1, 1, 11),
    _NncPktVcl15MinCurOutUcastPkts_Type()
)
nncPktVcl15MinCurOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinCurOutUcastPkts.setStatus("current")
_NncPktVcl15MinCurOutMulticastPkts_Type = NncExtCounter64
_NncPktVcl15MinCurOutMulticastPkts_Object = MibTableColumn
nncPktVcl15MinCurOutMulticastPkts = _NncPktVcl15MinCurOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 1, 1, 12),
    _NncPktVcl15MinCurOutMulticastPkts_Type()
)
nncPktVcl15MinCurOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinCurOutMulticastPkts.setStatus("current")
_NncPktVcl15MinCurOutBroadcastPkts_Type = NncExtCounter64
_NncPktVcl15MinCurOutBroadcastPkts_Object = MibTableColumn
nncPktVcl15MinCurOutBroadcastPkts = _NncPktVcl15MinCurOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 1, 1, 13),
    _NncPktVcl15MinCurOutBroadcastPkts_Type()
)
nncPktVcl15MinCurOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinCurOutBroadcastPkts.setStatus("current")
_NncPktVcl15MinCurOutDiscards_Type = NncExtCounter64
_NncPktVcl15MinCurOutDiscards_Object = MibTableColumn
nncPktVcl15MinCurOutDiscards = _NncPktVcl15MinCurOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 1, 1, 14),
    _NncPktVcl15MinCurOutDiscards_Type()
)
nncPktVcl15MinCurOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinCurOutDiscards.setStatus("current")
_NncPktVcl15MinCurOutErrors_Type = NncExtCounter64
_NncPktVcl15MinCurOutErrors_Object = MibTableColumn
nncPktVcl15MinCurOutErrors = _NncPktVcl15MinCurOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 1, 1, 15),
    _NncPktVcl15MinCurOutErrors_Type()
)
nncPktVcl15MinCurOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinCurOutErrors.setStatus("current")
_NncPktVcl15MinIntTable_Object = MibTable
nncPktVcl15MinIntTable = _NncPktVcl15MinIntTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 2)
)
if mibBuilder.loadTexts:
    nncPktVcl15MinIntTable.setStatus("current")
_NncPktVcl15MinIntEntry_Object = MibTableRow
nncPktVcl15MinIntEntry = _NncPktVcl15MinIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 2, 1)
)
nncPktVcl15MinIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinIntNumber"),
    (0, "NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinIntCoS"),
)
if mibBuilder.loadTexts:
    nncPktVcl15MinIntEntry.setStatus("current")
_NncPktVcl15MinIntNumber_Type = NncExtRelIntvlNumberType
_NncPktVcl15MinIntNumber_Object = MibTableColumn
nncPktVcl15MinIntNumber = _NncPktVcl15MinIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 2, 1, 1),
    _NncPktVcl15MinIntNumber_Type()
)
nncPktVcl15MinIntNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncPktVcl15MinIntNumber.setStatus("current")
_NncPktVcl15MinIntCoS_Type = NncPktVclCoSType
_NncPktVcl15MinIntCoS_Object = MibTableColumn
nncPktVcl15MinIntCoS = _NncPktVcl15MinIntCoS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 2, 1, 2),
    _NncPktVcl15MinIntCoS_Type()
)
nncPktVcl15MinIntCoS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncPktVcl15MinIntCoS.setStatus("current")
_NncPktVcl15MinIntState_Type = NncExtIntvlStateType
_NncPktVcl15MinIntState_Object = MibTableColumn
nncPktVcl15MinIntState = _NncPktVcl15MinIntState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 2, 1, 3),
    _NncPktVcl15MinIntState_Type()
)
nncPktVcl15MinIntState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinIntState.setStatus("current")
_NncPktVcl15MinIntAbsoluteIntervalNumber_Type = NncExtAbsIntvlNumberType
_NncPktVcl15MinIntAbsoluteIntervalNumber_Object = MibTableColumn
nncPktVcl15MinIntAbsoluteIntervalNumber = _NncPktVcl15MinIntAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 2, 1, 4),
    _NncPktVcl15MinIntAbsoluteIntervalNumber_Type()
)
nncPktVcl15MinIntAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinIntAbsoluteIntervalNumber.setStatus("current")
_NncPktVcl15MinIntInOctets_Type = NncExtCounter64
_NncPktVcl15MinIntInOctets_Object = MibTableColumn
nncPktVcl15MinIntInOctets = _NncPktVcl15MinIntInOctets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 2, 1, 5),
    _NncPktVcl15MinIntInOctets_Type()
)
nncPktVcl15MinIntInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinIntInOctets.setStatus("current")
_NncPktVcl15MinIntInUcastPkts_Type = NncExtCounter64
_NncPktVcl15MinIntInUcastPkts_Object = MibTableColumn
nncPktVcl15MinIntInUcastPkts = _NncPktVcl15MinIntInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 2, 1, 6),
    _NncPktVcl15MinIntInUcastPkts_Type()
)
nncPktVcl15MinIntInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinIntInUcastPkts.setStatus("current")
_NncPktVcl15MinIntInMulticastPkts_Type = NncExtCounter64
_NncPktVcl15MinIntInMulticastPkts_Object = MibTableColumn
nncPktVcl15MinIntInMulticastPkts = _NncPktVcl15MinIntInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 2, 1, 7),
    _NncPktVcl15MinIntInMulticastPkts_Type()
)
nncPktVcl15MinIntInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinIntInMulticastPkts.setStatus("current")
_NncPktVcl15MinIntInBroadcastPkts_Type = NncExtCounter64
_NncPktVcl15MinIntInBroadcastPkts_Object = MibTableColumn
nncPktVcl15MinIntInBroadcastPkts = _NncPktVcl15MinIntInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 2, 1, 8),
    _NncPktVcl15MinIntInBroadcastPkts_Type()
)
nncPktVcl15MinIntInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinIntInBroadcastPkts.setStatus("current")
_NncPktVcl15MinIntInDiscards_Type = NncExtCounter64
_NncPktVcl15MinIntInDiscards_Object = MibTableColumn
nncPktVcl15MinIntInDiscards = _NncPktVcl15MinIntInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 2, 1, 9),
    _NncPktVcl15MinIntInDiscards_Type()
)
nncPktVcl15MinIntInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinIntInDiscards.setStatus("current")
_NncPktVcl15MinIntInErrors_Type = NncExtCounter64
_NncPktVcl15MinIntInErrors_Object = MibTableColumn
nncPktVcl15MinIntInErrors = _NncPktVcl15MinIntInErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 2, 1, 10),
    _NncPktVcl15MinIntInErrors_Type()
)
nncPktVcl15MinIntInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinIntInErrors.setStatus("current")
_NncPktVcl15MinIntOutOctets_Type = NncExtCounter64
_NncPktVcl15MinIntOutOctets_Object = MibTableColumn
nncPktVcl15MinIntOutOctets = _NncPktVcl15MinIntOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 2, 1, 11),
    _NncPktVcl15MinIntOutOctets_Type()
)
nncPktVcl15MinIntOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinIntOutOctets.setStatus("current")
_NncPktVcl15MinIntOutUcastPkts_Type = NncExtCounter64
_NncPktVcl15MinIntOutUcastPkts_Object = MibTableColumn
nncPktVcl15MinIntOutUcastPkts = _NncPktVcl15MinIntOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 2, 1, 12),
    _NncPktVcl15MinIntOutUcastPkts_Type()
)
nncPktVcl15MinIntOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinIntOutUcastPkts.setStatus("current")
_NncPktVcl15MinIntOutMulticastPkts_Type = NncExtCounter64
_NncPktVcl15MinIntOutMulticastPkts_Object = MibTableColumn
nncPktVcl15MinIntOutMulticastPkts = _NncPktVcl15MinIntOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 2, 1, 13),
    _NncPktVcl15MinIntOutMulticastPkts_Type()
)
nncPktVcl15MinIntOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinIntOutMulticastPkts.setStatus("current")
_NncPktVcl15MinIntOutBroadcastPkts_Type = NncExtCounter64
_NncPktVcl15MinIntOutBroadcastPkts_Object = MibTableColumn
nncPktVcl15MinIntOutBroadcastPkts = _NncPktVcl15MinIntOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 2, 1, 14),
    _NncPktVcl15MinIntOutBroadcastPkts_Type()
)
nncPktVcl15MinIntOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinIntOutBroadcastPkts.setStatus("current")
_NncPktVcl15MinIntOutDiscards_Type = NncExtCounter64
_NncPktVcl15MinIntOutDiscards_Object = MibTableColumn
nncPktVcl15MinIntOutDiscards = _NncPktVcl15MinIntOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 2, 1, 15),
    _NncPktVcl15MinIntOutDiscards_Type()
)
nncPktVcl15MinIntOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinIntOutDiscards.setStatus("current")
_NncPktVcl15MinIntOutErrors_Type = NncExtCounter64
_NncPktVcl15MinIntOutErrors_Object = MibTableColumn
nncPktVcl15MinIntOutErrors = _NncPktVcl15MinIntOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 2, 1, 16),
    _NncPktVcl15MinIntOutErrors_Type()
)
nncPktVcl15MinIntOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVcl15MinIntOutErrors.setStatus("current")
_NncPktVclStatTable_Object = MibTable
nncPktVclStatTable = _NncPktVclStatTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 3)
)
if mibBuilder.loadTexts:
    nncPktVclStatTable.setStatus("current")
_NncPktVclStatEntry_Object = MibTableRow
nncPktVclStatEntry = _NncPktVclStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 3, 1)
)
nncPktVclStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "NNC-PKT-STATISTICS-MIB", "nncPktVclStatCoS"),
)
if mibBuilder.loadTexts:
    nncPktVclStatEntry.setStatus("current")
_NncPktVclStatCoS_Type = NncPktVclCoSType
_NncPktVclStatCoS_Object = MibTableColumn
nncPktVclStatCoS = _NncPktVclStatCoS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 3, 1, 1),
    _NncPktVclStatCoS_Type()
)
nncPktVclStatCoS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncPktVclStatCoS.setStatus("current")
_NncPktVclStatInOctets_Type = NncExtCounter64
_NncPktVclStatInOctets_Object = MibTableColumn
nncPktVclStatInOctets = _NncPktVclStatInOctets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 3, 1, 2),
    _NncPktVclStatInOctets_Type()
)
nncPktVclStatInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVclStatInOctets.setStatus("current")
_NncPktVclStatInUcastPkts_Type = NncExtCounter64
_NncPktVclStatInUcastPkts_Object = MibTableColumn
nncPktVclStatInUcastPkts = _NncPktVclStatInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 3, 1, 3),
    _NncPktVclStatInUcastPkts_Type()
)
nncPktVclStatInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVclStatInUcastPkts.setStatus("current")
_NncPktVclStatInMulticastPkts_Type = NncExtCounter64
_NncPktVclStatInMulticastPkts_Object = MibTableColumn
nncPktVclStatInMulticastPkts = _NncPktVclStatInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 3, 1, 4),
    _NncPktVclStatInMulticastPkts_Type()
)
nncPktVclStatInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVclStatInMulticastPkts.setStatus("current")
_NncPktVclStatInBroadcastPkts_Type = NncExtCounter64
_NncPktVclStatInBroadcastPkts_Object = MibTableColumn
nncPktVclStatInBroadcastPkts = _NncPktVclStatInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 3, 1, 5),
    _NncPktVclStatInBroadcastPkts_Type()
)
nncPktVclStatInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVclStatInBroadcastPkts.setStatus("current")
_NncPktVclStatInDiscards_Type = NncExtCounter64
_NncPktVclStatInDiscards_Object = MibTableColumn
nncPktVclStatInDiscards = _NncPktVclStatInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 3, 1, 6),
    _NncPktVclStatInDiscards_Type()
)
nncPktVclStatInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVclStatInDiscards.setStatus("current")
_NncPktVclStatInErrors_Type = NncExtCounter64
_NncPktVclStatInErrors_Object = MibTableColumn
nncPktVclStatInErrors = _NncPktVclStatInErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 3, 1, 7),
    _NncPktVclStatInErrors_Type()
)
nncPktVclStatInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVclStatInErrors.setStatus("current")
_NncPktVclStatOutOctets_Type = NncExtCounter64
_NncPktVclStatOutOctets_Object = MibTableColumn
nncPktVclStatOutOctets = _NncPktVclStatOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 3, 1, 8),
    _NncPktVclStatOutOctets_Type()
)
nncPktVclStatOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVclStatOutOctets.setStatus("current")
_NncPktVclStatOutUcastPkts_Type = NncExtCounter64
_NncPktVclStatOutUcastPkts_Object = MibTableColumn
nncPktVclStatOutUcastPkts = _NncPktVclStatOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 3, 1, 9),
    _NncPktVclStatOutUcastPkts_Type()
)
nncPktVclStatOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVclStatOutUcastPkts.setStatus("current")
_NncPktVclStatOutMulticastPkts_Type = NncExtCounter64
_NncPktVclStatOutMulticastPkts_Object = MibTableColumn
nncPktVclStatOutMulticastPkts = _NncPktVclStatOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 3, 1, 10),
    _NncPktVclStatOutMulticastPkts_Type()
)
nncPktVclStatOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVclStatOutMulticastPkts.setStatus("current")
_NncPktVclStatOutBroadcastPkts_Type = NncExtCounter64
_NncPktVclStatOutBroadcastPkts_Object = MibTableColumn
nncPktVclStatOutBroadcastPkts = _NncPktVclStatOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 3, 1, 11),
    _NncPktVclStatOutBroadcastPkts_Type()
)
nncPktVclStatOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVclStatOutBroadcastPkts.setStatus("current")
_NncPktVclStatOutDiscards_Type = NncExtCounter64
_NncPktVclStatOutDiscards_Object = MibTableColumn
nncPktVclStatOutDiscards = _NncPktVclStatOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 3, 1, 12),
    _NncPktVclStatOutDiscards_Type()
)
nncPktVclStatOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVclStatOutDiscards.setStatus("current")
_NncPktVclStatOutErrors_Type = NncExtCounter64
_NncPktVclStatOutErrors_Object = MibTableColumn
nncPktVclStatOutErrors = _NncPktVclStatOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 1, 3, 1, 13),
    _NncPktVclStatOutErrors_Type()
)
nncPktVclStatOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncPktVclStatOutErrors.setStatus("current")
_NncPktStatisticsTraps_ObjectIdentity = ObjectIdentity
nncPktStatisticsTraps = _NncPktStatisticsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 2)
)
_NncPktStatisticsGroups_ObjectIdentity = ObjectIdentity
nncPktStatisticsGroups = _NncPktStatisticsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 3)
)
_NncPktStatisticsCompliances_ObjectIdentity = ObjectIdentity
nncPktStatisticsCompliances = _NncPktStatisticsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 4)
)

# Managed Objects groups

nncPktVcl15MinCurGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 3, 5)
)
nncPktVcl15MinCurGroup.setObjects(
      *(("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinCurState"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinCurAbsoluteIntervalNumber"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinCurInOctets"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinCurInUcastPkts"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinCurInMulticastPkts"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinCurInBroadcastPkts"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinCurInDiscards"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinCurInErrors"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinCurOutOctets"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinCurOutUcastPkts"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinCurOutMulticastPkts"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinCurOutBroadcastPkts"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinCurOutDiscards"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinCurOutErrors"))
)
if mibBuilder.loadTexts:
    nncPktVcl15MinCurGroup.setStatus("current")

nncPktVcl15MinIntGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 3, 6)
)
nncPktVcl15MinIntGroup.setObjects(
      *(("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinIntAbsoluteIntervalNumber"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinIntInOctets"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinIntInUcastPkts"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinIntInMulticastPkts"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinIntInBroadcastPkts"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinIntInDiscards"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinIntInErrors"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinIntOutOctets"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinIntOutUcastPkts"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinIntOutMulticastPkts"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinIntOutBroadcastPkts"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinIntOutDiscards"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinIntOutErrors"))
)
if mibBuilder.loadTexts:
    nncPktVcl15MinIntGroup.setStatus("current")

nncPktVclStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 3, 7)
)
nncPktVclStatGroup.setObjects(
      *(("NNC-PKT-STATISTICS-MIB", "nncPktVclStatInOctets"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVclStatInUcastPkts"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVclStatInMulticastPkts"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVclStatInBroadcastPkts"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVclStatInDiscards"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVclStatInErrors"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVclStatOutOctets"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVclStatOutUcastPkts"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVclStatOutMulticastPkts"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVclStatOutBroadcastPkts"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVclStatOutDiscards"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVclStatOutErrors"))
)
if mibBuilder.loadTexts:
    nncPktVclStatGroup.setStatus("current")

nncVclIntervalStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 3, 8)
)
nncVclIntervalStateGroup.setObjects(
      *(("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinCurState"),
        ("NNC-PKT-STATISTICS-MIB", "nncPktVcl15MinIntState"))
)
if mibBuilder.loadTexts:
    nncVclIntervalStateGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nncPktStatisticsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 123, 3, 50, 4, 1)
)
if mibBuilder.loadTexts:
    nncPktStatisticsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNC-PKT-STATISTICS-MIB",
    **{"NncPktVclCoSType": NncPktVclCoSType,
       "nncExtPktStatistics": nncExtPktStatistics,
       "nncPktStatisticsObjects": nncPktStatisticsObjects,
       "nncPktVcl15MinCurTable": nncPktVcl15MinCurTable,
       "nncPktVcl15MinCurEntry": nncPktVcl15MinCurEntry,
       "nncPktVcl15MinCurCoS": nncPktVcl15MinCurCoS,
       "nncPktVcl15MinCurState": nncPktVcl15MinCurState,
       "nncPktVcl15MinCurAbsoluteIntervalNumber": nncPktVcl15MinCurAbsoluteIntervalNumber,
       "nncPktVcl15MinCurInOctets": nncPktVcl15MinCurInOctets,
       "nncPktVcl15MinCurInUcastPkts": nncPktVcl15MinCurInUcastPkts,
       "nncPktVcl15MinCurInMulticastPkts": nncPktVcl15MinCurInMulticastPkts,
       "nncPktVcl15MinCurInBroadcastPkts": nncPktVcl15MinCurInBroadcastPkts,
       "nncPktVcl15MinCurInDiscards": nncPktVcl15MinCurInDiscards,
       "nncPktVcl15MinCurInErrors": nncPktVcl15MinCurInErrors,
       "nncPktVcl15MinCurOutOctets": nncPktVcl15MinCurOutOctets,
       "nncPktVcl15MinCurOutUcastPkts": nncPktVcl15MinCurOutUcastPkts,
       "nncPktVcl15MinCurOutMulticastPkts": nncPktVcl15MinCurOutMulticastPkts,
       "nncPktVcl15MinCurOutBroadcastPkts": nncPktVcl15MinCurOutBroadcastPkts,
       "nncPktVcl15MinCurOutDiscards": nncPktVcl15MinCurOutDiscards,
       "nncPktVcl15MinCurOutErrors": nncPktVcl15MinCurOutErrors,
       "nncPktVcl15MinIntTable": nncPktVcl15MinIntTable,
       "nncPktVcl15MinIntEntry": nncPktVcl15MinIntEntry,
       "nncPktVcl15MinIntNumber": nncPktVcl15MinIntNumber,
       "nncPktVcl15MinIntCoS": nncPktVcl15MinIntCoS,
       "nncPktVcl15MinIntState": nncPktVcl15MinIntState,
       "nncPktVcl15MinIntAbsoluteIntervalNumber": nncPktVcl15MinIntAbsoluteIntervalNumber,
       "nncPktVcl15MinIntInOctets": nncPktVcl15MinIntInOctets,
       "nncPktVcl15MinIntInUcastPkts": nncPktVcl15MinIntInUcastPkts,
       "nncPktVcl15MinIntInMulticastPkts": nncPktVcl15MinIntInMulticastPkts,
       "nncPktVcl15MinIntInBroadcastPkts": nncPktVcl15MinIntInBroadcastPkts,
       "nncPktVcl15MinIntInDiscards": nncPktVcl15MinIntInDiscards,
       "nncPktVcl15MinIntInErrors": nncPktVcl15MinIntInErrors,
       "nncPktVcl15MinIntOutOctets": nncPktVcl15MinIntOutOctets,
       "nncPktVcl15MinIntOutUcastPkts": nncPktVcl15MinIntOutUcastPkts,
       "nncPktVcl15MinIntOutMulticastPkts": nncPktVcl15MinIntOutMulticastPkts,
       "nncPktVcl15MinIntOutBroadcastPkts": nncPktVcl15MinIntOutBroadcastPkts,
       "nncPktVcl15MinIntOutDiscards": nncPktVcl15MinIntOutDiscards,
       "nncPktVcl15MinIntOutErrors": nncPktVcl15MinIntOutErrors,
       "nncPktVclStatTable": nncPktVclStatTable,
       "nncPktVclStatEntry": nncPktVclStatEntry,
       "nncPktVclStatCoS": nncPktVclStatCoS,
       "nncPktVclStatInOctets": nncPktVclStatInOctets,
       "nncPktVclStatInUcastPkts": nncPktVclStatInUcastPkts,
       "nncPktVclStatInMulticastPkts": nncPktVclStatInMulticastPkts,
       "nncPktVclStatInBroadcastPkts": nncPktVclStatInBroadcastPkts,
       "nncPktVclStatInDiscards": nncPktVclStatInDiscards,
       "nncPktVclStatInErrors": nncPktVclStatInErrors,
       "nncPktVclStatOutOctets": nncPktVclStatOutOctets,
       "nncPktVclStatOutUcastPkts": nncPktVclStatOutUcastPkts,
       "nncPktVclStatOutMulticastPkts": nncPktVclStatOutMulticastPkts,
       "nncPktVclStatOutBroadcastPkts": nncPktVclStatOutBroadcastPkts,
       "nncPktVclStatOutDiscards": nncPktVclStatOutDiscards,
       "nncPktVclStatOutErrors": nncPktVclStatOutErrors,
       "nncPktStatisticsTraps": nncPktStatisticsTraps,
       "nncPktStatisticsGroups": nncPktStatisticsGroups,
       "nncPktVcl15MinCurGroup": nncPktVcl15MinCurGroup,
       "nncPktVcl15MinIntGroup": nncPktVcl15MinIntGroup,
       "nncPktVclStatGroup": nncPktVclStatGroup,
       "nncVclIntervalStateGroup": nncVclIntervalStateGroup,
       "nncPktStatisticsCompliances": nncPktStatisticsCompliances,
       "nncPktStatisticsCompliance": nncPktStatisticsCompliance}
)
