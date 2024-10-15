# SNMP MIB module (CTRON-WAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-WAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:55 2024
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

(ctWan,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctWan")

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



class Index(Integer32):
    """Custom type Index based on Integer32"""




class DLCI(Integer32):
    """Custom type DLCI based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtWanConnection_ObjectIdentity = ObjectIdentity
ctWanConnection = _CtWanConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1)
)
_WanNumConnections_Type = Integer32
_WanNumConnections_Object = MibScalar
wanNumConnections = _WanNumConnections_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 1),
    _WanNumConnections_Type()
)
wanNumConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanNumConnections.setStatus("mandatory")
_WanConnTable_Object = MibTable
wanConnTable = _WanConnTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wanConnTable.setStatus("mandatory")
_WanConnEntry_Object = MibTableRow
wanConnEntry = _WanConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 2, 1)
)
wanConnEntry.setIndexNames(
    (0, "CTRON-WAN-MIB", "wanConnIndex"),
)
if mibBuilder.loadTexts:
    wanConnEntry.setStatus("mandatory")
_WanConnIndex_Type = Integer32
_WanConnIndex_Object = MibTableColumn
wanConnIndex = _WanConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 2, 1, 1),
    _WanConnIndex_Type()
)
wanConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanConnIndex.setStatus("mandatory")
_WanConnNumPhysPorts_Type = Integer32
_WanConnNumPhysPorts_Object = MibTableColumn
wanConnNumPhysPorts = _WanConnNumPhysPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 2, 1, 2),
    _WanConnNumPhysPorts_Type()
)
wanConnNumPhysPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanConnNumPhysPorts.setStatus("mandatory")
_WanConnDefaultPhysPort_Type = Integer32
_WanConnDefaultPhysPort_Object = MibTableColumn
wanConnDefaultPhysPort = _WanConnDefaultPhysPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 2, 1, 3),
    _WanConnDefaultPhysPort_Type()
)
wanConnDefaultPhysPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanConnDefaultPhysPort.setStatus("mandatory")
_WanConnActivePhysPort_Type = Integer32
_WanConnActivePhysPort_Object = MibTableColumn
wanConnActivePhysPort = _WanConnActivePhysPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 2, 1, 4),
    _WanConnActivePhysPort_Type()
)
wanConnActivePhysPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanConnActivePhysPort.setStatus("mandatory")
_WanPhysPortTable_Object = MibTable
wanPhysPortTable = _WanPhysPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wanPhysPortTable.setStatus("mandatory")
_WanPhysPortEntry_Object = MibTableRow
wanPhysPortEntry = _WanPhysPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 3, 1)
)
wanPhysPortEntry.setIndexNames(
    (0, "CTRON-WAN-MIB", "wanPhysPortConnectionIndex"),
    (0, "CTRON-WAN-MIB", "wanPhysPortIndex"),
)
if mibBuilder.loadTexts:
    wanPhysPortEntry.setStatus("mandatory")
_WanPhysPortConnectionIndex_Type = Integer32
_WanPhysPortConnectionIndex_Object = MibTableColumn
wanPhysPortConnectionIndex = _WanPhysPortConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 3, 1, 1),
    _WanPhysPortConnectionIndex_Type()
)
wanPhysPortConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPhysPortConnectionIndex.setStatus("mandatory")
_WanPhysPortIndex_Type = Integer32
_WanPhysPortIndex_Object = MibTableColumn
wanPhysPortIndex = _WanPhysPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 3, 1, 2),
    _WanPhysPortIndex_Type()
)
wanPhysPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPhysPortIndex.setStatus("mandatory")


class _WanPhysPortType_Type(Integer32):
    """Custom type wanPhysPortType based on Integer32"""
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
        *(("bri", 8),
          ("dds", 5),
          ("di", 6),
          ("ds30", 9),
          ("e1", 3),
          ("hdsl", 7),
          ("none", 1),
          ("synchronous", 4),
          ("t1", 2),
          ("t1DDS", 10))
    )


_WanPhysPortType_Type.__name__ = "Integer32"
_WanPhysPortType_Object = MibTableColumn
wanPhysPortType = _WanPhysPortType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 3, 1, 3),
    _WanPhysPortType_Type()
)
wanPhysPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPhysPortType.setStatus("mandatory")
_WanPhysPortSpecificMib_Type = ObjectIdentifier
_WanPhysPortSpecificMib_Object = MibTableColumn
wanPhysPortSpecificMib = _WanPhysPortSpecificMib_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 3, 1, 4),
    _WanPhysPortSpecificMib_Type()
)
wanPhysPortSpecificMib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPhysPortSpecificMib.setStatus("mandatory")
_WanInterfaceTable_Object = MibTable
wanInterfaceTable = _WanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wanInterfaceTable.setStatus("mandatory")
_WanInterfaceEntry_Object = MibTableRow
wanInterfaceEntry = _WanInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 4, 1)
)
wanInterfaceEntry.setIndexNames(
    (0, "CTRON-WAN-MIB", "wanInterfaceConnectionIndex"),
    (0, "CTRON-WAN-MIB", "wanInterfacePhysPortIndex"),
    (0, "CTRON-WAN-MIB", "wanInterfaceEntryIndex"),
)
if mibBuilder.loadTexts:
    wanInterfaceEntry.setStatus("mandatory")
_WanInterfaceConnectionIndex_Type = Integer32
_WanInterfaceConnectionIndex_Object = MibTableColumn
wanInterfaceConnectionIndex = _WanInterfaceConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 4, 1, 1),
    _WanInterfaceConnectionIndex_Type()
)
wanInterfaceConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanInterfaceConnectionIndex.setStatus("mandatory")
_WanInterfacePhysPortIndex_Type = Integer32
_WanInterfacePhysPortIndex_Object = MibTableColumn
wanInterfacePhysPortIndex = _WanInterfacePhysPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 4, 1, 2),
    _WanInterfacePhysPortIndex_Type()
)
wanInterfacePhysPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanInterfacePhysPortIndex.setStatus("mandatory")
_WanInterfaceEntryIndex_Type = Integer32
_WanInterfaceEntryIndex_Object = MibTableColumn
wanInterfaceEntryIndex = _WanInterfaceEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 4, 1, 3),
    _WanInterfaceEntryIndex_Type()
)
wanInterfaceEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanInterfaceEntryIndex.setStatus("mandatory")
_WanInterfaceEntryIfIndex_Type = Integer32
_WanInterfaceEntryIfIndex_Object = MibTableColumn
wanInterfaceEntryIfIndex = _WanInterfaceEntryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 4, 1, 4),
    _WanInterfaceEntryIfIndex_Type()
)
wanInterfaceEntryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanInterfaceEntryIfIndex.setStatus("mandatory")
_WanInterfaceEntryProtocol_Type = Integer32
_WanInterfaceEntryProtocol_Object = MibTableColumn
wanInterfaceEntryProtocol = _WanInterfaceEntryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 4, 1, 5),
    _WanInterfaceEntryProtocol_Type()
)
wanInterfaceEntryProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanInterfaceEntryProtocol.setStatus("mandatory")


class _WanInterfaceEntryCompression_Type(Integer32):
    """Custom type wanInterfaceEntryCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WanInterfaceEntryCompression_Type.__name__ = "Integer32"
_WanInterfaceEntryCompression_Object = MibTableColumn
wanInterfaceEntryCompression = _WanInterfaceEntryCompression_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 4, 1, 6),
    _WanInterfaceEntryCompression_Type()
)
wanInterfaceEntryCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanInterfaceEntryCompression.setStatus("mandatory")
_WanInterfaceEntryMTU_Type = Integer32
_WanInterfaceEntryMTU_Object = MibTableColumn
wanInterfaceEntryMTU = _WanInterfaceEntryMTU_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 4, 1, 7),
    _WanInterfaceEntryMTU_Type()
)
wanInterfaceEntryMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanInterfaceEntryMTU.setStatus("mandatory")


class _WanInterfaceEntryLineCoding_Type(Integer32):
    """Custom type wanInterfaceEntryLineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invHDLC", 3),
          ("jBZS", 2),
          ("none", 1))
    )


_WanInterfaceEntryLineCoding_Type.__name__ = "Integer32"
_WanInterfaceEntryLineCoding_Object = MibTableColumn
wanInterfaceEntryLineCoding = _WanInterfaceEntryLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 4, 1, 8),
    _WanInterfaceEntryLineCoding_Type()
)
wanInterfaceEntryLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanInterfaceEntryLineCoding.setStatus("mandatory")


class _WanInterfaceEntryCrcLength_Type(Integer32):
    """Custom type wanInterfaceEntryCrcLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sixteen-bits", 1),
          ("thirty-two-bits", 2))
    )


_WanInterfaceEntryCrcLength_Type.__name__ = "Integer32"
_WanInterfaceEntryCrcLength_Object = MibTableColumn
wanInterfaceEntryCrcLength = _WanInterfaceEntryCrcLength_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 4, 1, 9),
    _WanInterfaceEntryCrcLength_Type()
)
wanInterfaceEntryCrcLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanInterfaceEntryCrcLength.setStatus("mandatory")


class _WanInterfaceEntryLexProtocolEnable_Type(Integer32):
    """Custom type wanInterfaceEntryLexProtocolEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WanInterfaceEntryLexProtocolEnable_Type.__name__ = "Integer32"
_WanInterfaceEntryLexProtocolEnable_Object = MibTableColumn
wanInterfaceEntryLexProtocolEnable = _WanInterfaceEntryLexProtocolEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 4, 1, 10),
    _WanInterfaceEntryLexProtocolEnable_Type()
)
wanInterfaceEntryLexProtocolEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanInterfaceEntryLexProtocolEnable.setStatus("deprecated")


class _WanInterfaceEntryLexProtocolStatus_Type(Integer32):
    """Custom type wanInterfaceEntryLexProtocolStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bound", 1),
          ("unbound", 2))
    )


_WanInterfaceEntryLexProtocolStatus_Type.__name__ = "Integer32"
_WanInterfaceEntryLexProtocolStatus_Object = MibTableColumn
wanInterfaceEntryLexProtocolStatus = _WanInterfaceEntryLexProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 4, 1, 11),
    _WanInterfaceEntryLexProtocolStatus_Type()
)
wanInterfaceEntryLexProtocolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanInterfaceEntryLexProtocolStatus.setStatus("deprecated")


class _WanInterfaceEntryCompRatio_Type(OctetString):
    """Custom type wanInterfaceEntryCompRatio based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WanInterfaceEntryCompRatio_Type.__name__ = "OctetString"
_WanInterfaceEntryCompRatio_Object = MibTableColumn
wanInterfaceEntryCompRatio = _WanInterfaceEntryCompRatio_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 4, 1, 12),
    _WanInterfaceEntryCompRatio_Type()
)
wanInterfaceEntryCompRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanInterfaceEntryCompRatio.setStatus("mandatory")


class _WanInterfaceEntryCompStatus_Type(Integer32):
    """Custom type wanInterfaceEntryCompStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WanInterfaceEntryCompStatus_Type.__name__ = "Integer32"
_WanInterfaceEntryCompStatus_Object = MibTableColumn
wanInterfaceEntryCompStatus = _WanInterfaceEntryCompStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 4, 1, 13),
    _WanInterfaceEntryCompStatus_Type()
)
wanInterfaceEntryCompStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanInterfaceEntryCompStatus.setStatus("mandatory")


class _WanInterfaceEntryBackUpIfEnable_Type(Integer32):
    """Custom type wanInterfaceEntryBackUpIfEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WanInterfaceEntryBackUpIfEnable_Type.__name__ = "Integer32"
_WanInterfaceEntryBackUpIfEnable_Object = MibTableColumn
wanInterfaceEntryBackUpIfEnable = _WanInterfaceEntryBackUpIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 1, 4, 1, 14),
    _WanInterfaceEntryBackUpIfEnable_Type()
)
wanInterfaceEntryBackUpIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanInterfaceEntryBackUpIfEnable.setStatus("mandatory")
_CtWanDs1_ObjectIdentity = ObjectIdentity
ctWanDs1 = _CtWanDs1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 2)
)
_WanDs1ExtensionsTable_Object = MibTable
wanDs1ExtensionsTable = _WanDs1ExtensionsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wanDs1ExtensionsTable.setStatus("mandatory")
_WanDs1ExtensionsEntry_Object = MibTableRow
wanDs1ExtensionsEntry = _WanDs1ExtensionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 2, 1, 1)
)
wanDs1ExtensionsEntry.setIndexNames(
    (0, "CTRON-WAN-MIB", "wanDs1ExtensionsEntryIndex"),
)
if mibBuilder.loadTexts:
    wanDs1ExtensionsEntry.setStatus("mandatory")
_WanDs1ExtensionsEntryIndex_Type = Integer32
_WanDs1ExtensionsEntryIndex_Object = MibTableColumn
wanDs1ExtensionsEntryIndex = _WanDs1ExtensionsEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 2, 1, 1, 1),
    _WanDs1ExtensionsEntryIndex_Type()
)
wanDs1ExtensionsEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDs1ExtensionsEntryIndex.setStatus("mandatory")
_WanDs1ExtensionsNumInterfaces_Type = Integer32
_WanDs1ExtensionsNumInterfaces_Object = MibTableColumn
wanDs1ExtensionsNumInterfaces = _WanDs1ExtensionsNumInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 2, 1, 1, 2),
    _WanDs1ExtensionsNumInterfaces_Type()
)
wanDs1ExtensionsNumInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDs1ExtensionsNumInterfaces.setStatus("mandatory")


class _WanDs1ExtensionsToggleFracTable_Type(Integer32):
    """Custom type wanDs1ExtensionsToggleFracTable based on Integer32"""
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
        *(("display-new", 2),
          ("display-old", 3),
          ("restore-old", 4),
          ("update-table", 1))
    )


_WanDs1ExtensionsToggleFracTable_Type.__name__ = "Integer32"
_WanDs1ExtensionsToggleFracTable_Object = MibTableColumn
wanDs1ExtensionsToggleFracTable = _WanDs1ExtensionsToggleFracTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 2, 1, 1, 3),
    _WanDs1ExtensionsToggleFracTable_Type()
)
wanDs1ExtensionsToggleFracTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDs1ExtensionsToggleFracTable.setStatus("mandatory")


class _WanDs1ExtensionsLineBuildOut_Type(Integer32):
    """Custom type wanDs1ExtensionsLineBuildOut based on Integer32"""
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
        *(("a133to266feet", 5),
          ("a266to399feet", 6),
          ("a399to533feet", 7),
          ("a533to655feet", 8),
          ("minus-15", 4),
          ("minus-7point5", 3),
          ("unknown", 1),
          ("zero", 2))
    )


_WanDs1ExtensionsLineBuildOut_Type.__name__ = "Integer32"
_WanDs1ExtensionsLineBuildOut_Object = MibTableColumn
wanDs1ExtensionsLineBuildOut = _WanDs1ExtensionsLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 2, 1, 1, 4),
    _WanDs1ExtensionsLineBuildOut_Type()
)
wanDs1ExtensionsLineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDs1ExtensionsLineBuildOut.setStatus("mandatory")


class _WanDs1ExtensionsCFADuration_Type(Integer32):
    """Custom type wanDs1ExtensionsCFADuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_WanDs1ExtensionsCFADuration_Type.__name__ = "Integer32"
_WanDs1ExtensionsCFADuration_Object = MibTableColumn
wanDs1ExtensionsCFADuration = _WanDs1ExtensionsCFADuration_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 2, 1, 1, 5),
    _WanDs1ExtensionsCFADuration_Type()
)
wanDs1ExtensionsCFADuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDs1ExtensionsCFADuration.setStatus("mandatory")


class _WanDs1ExtensionsDIEnable_Type(Integer32):
    """Custom type wanDs1ExtensionsDIEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("diDataEnabled", 3),
          ("disable", 2),
          ("enable", 1))
    )


_WanDs1ExtensionsDIEnable_Type.__name__ = "Integer32"
_WanDs1ExtensionsDIEnable_Object = MibTableColumn
wanDs1ExtensionsDIEnable = _WanDs1ExtensionsDIEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 2, 1, 1, 6),
    _WanDs1ExtensionsDIEnable_Type()
)
wanDs1ExtensionsDIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDs1ExtensionsDIEnable.setStatus("mandatory")
_WanDs1ExtensionsTotalValidIntervals_Type = Counter32
_WanDs1ExtensionsTotalValidIntervals_Object = MibTableColumn
wanDs1ExtensionsTotalValidIntervals = _WanDs1ExtensionsTotalValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 2, 1, 1, 7),
    _WanDs1ExtensionsTotalValidIntervals_Type()
)
wanDs1ExtensionsTotalValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDs1ExtensionsTotalValidIntervals.setStatus("mandatory")


class _WanDs1ExtensionsBertTestMode_Type(Integer32):
    """Custom type wanDs1ExtensionsBertTestMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internal", 2),
          ("manual", 3),
          ("none", 1))
    )


_WanDs1ExtensionsBertTestMode_Type.__name__ = "Integer32"
_WanDs1ExtensionsBertTestMode_Object = MibTableColumn
wanDs1ExtensionsBertTestMode = _WanDs1ExtensionsBertTestMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 2, 1, 1, 8),
    _WanDs1ExtensionsBertTestMode_Type()
)
wanDs1ExtensionsBertTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDs1ExtensionsBertTestMode.setStatus("mandatory")


class _WanDs1ExtensionsBertRun_Type(Integer32):
    """Custom type wanDs1ExtensionsBertRun based on Integer32"""
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


_WanDs1ExtensionsBertRun_Type.__name__ = "Integer32"
_WanDs1ExtensionsBertRun_Object = MibTableColumn
wanDs1ExtensionsBertRun = _WanDs1ExtensionsBertRun_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 2, 1, 1, 9),
    _WanDs1ExtensionsBertRun_Type()
)
wanDs1ExtensionsBertRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDs1ExtensionsBertRun.setStatus("mandatory")
_WanDs1ExtensionsBertCurrentResults_Type = Integer32
_WanDs1ExtensionsBertCurrentResults_Object = MibTableColumn
wanDs1ExtensionsBertCurrentResults = _WanDs1ExtensionsBertCurrentResults_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 2, 1, 1, 10),
    _WanDs1ExtensionsBertCurrentResults_Type()
)
wanDs1ExtensionsBertCurrentResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDs1ExtensionsBertCurrentResults.setStatus("mandatory")
_WanDs1ExtensionsBertCumulativeResults_Type = Integer32
_WanDs1ExtensionsBertCumulativeResults_Object = MibTableColumn
wanDs1ExtensionsBertCumulativeResults = _WanDs1ExtensionsBertCumulativeResults_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 2, 1, 1, 11),
    _WanDs1ExtensionsBertCumulativeResults_Type()
)
wanDs1ExtensionsBertCumulativeResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDs1ExtensionsBertCumulativeResults.setStatus("mandatory")
_WanDs1ExtensionsBertPeakResults_Type = Integer32
_WanDs1ExtensionsBertPeakResults_Object = MibTableColumn
wanDs1ExtensionsBertPeakResults = _WanDs1ExtensionsBertPeakResults_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 2, 1, 1, 12),
    _WanDs1ExtensionsBertPeakResults_Type()
)
wanDs1ExtensionsBertPeakResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDs1ExtensionsBertPeakResults.setStatus("mandatory")
_WanDs1ExtensionsBertAverageResult_Type = Integer32
_WanDs1ExtensionsBertAverageResult_Object = MibTableColumn
wanDs1ExtensionsBertAverageResult = _WanDs1ExtensionsBertAverageResult_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 2, 1, 1, 13),
    _WanDs1ExtensionsBertAverageResult_Type()
)
wanDs1ExtensionsBertAverageResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDs1ExtensionsBertAverageResult.setStatus("mandatory")


class _WanDs1ExtensionsBertTestPattern_Type(Integer32):
    """Custom type wanDs1ExtensionsBertTestPattern based on Integer32"""
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
        *(("pattern1s", 2),
          ("pattern2047", 5),
          ("pattern3in24", 6),
          ("pattern511", 4),
          ("pattern63", 3),
          ("patternOther", 1),
          ("patternQRSS", 7))
    )


_WanDs1ExtensionsBertTestPattern_Type.__name__ = "Integer32"
_WanDs1ExtensionsBertTestPattern_Object = MibTableColumn
wanDs1ExtensionsBertTestPattern = _WanDs1ExtensionsBertTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 2, 1, 1, 14),
    _WanDs1ExtensionsBertTestPattern_Type()
)
wanDs1ExtensionsBertTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDs1ExtensionsBertTestPattern.setStatus("mandatory")
_WanDs1ExtensionsBertSamplePeriod_Type = Integer32
_WanDs1ExtensionsBertSamplePeriod_Object = MibTableColumn
wanDs1ExtensionsBertSamplePeriod = _WanDs1ExtensionsBertSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 2, 1, 1, 15),
    _WanDs1ExtensionsBertSamplePeriod_Type()
)
wanDs1ExtensionsBertSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDs1ExtensionsBertSamplePeriod.setStatus("mandatory")
_WanDs1ExtensionsBertNumPeriods_Type = Counter32
_WanDs1ExtensionsBertNumPeriods_Object = MibTableColumn
wanDs1ExtensionsBertNumPeriods = _WanDs1ExtensionsBertNumPeriods_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 2, 1, 1, 16),
    _WanDs1ExtensionsBertNumPeriods_Type()
)
wanDs1ExtensionsBertNumPeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDs1ExtensionsBertNumPeriods.setStatus("mandatory")


class _WanDs1ExtensionsBertTestTraps_Type(Integer32):
    """Custom type wanDs1ExtensionsBertTestTraps based on Integer32"""
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


_WanDs1ExtensionsBertTestTraps_Type.__name__ = "Integer32"
_WanDs1ExtensionsBertTestTraps_Object = MibTableColumn
wanDs1ExtensionsBertTestTraps = _WanDs1ExtensionsBertTestTraps_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 2, 1, 1, 17),
    _WanDs1ExtensionsBertTestTraps_Type()
)
wanDs1ExtensionsBertTestTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDs1ExtensionsBertTestTraps.setStatus("mandatory")


class _WanDs1ExtensionsBertDataStatus_Type(Integer32):
    """Custom type wanDs1ExtensionsBertDataStatus based on Integer32"""
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
        *(("idle", 1),
          ("running", 4),
          ("waitingForLink", 2),
          ("waitingForLoopback", 3))
    )


_WanDs1ExtensionsBertDataStatus_Type.__name__ = "Integer32"
_WanDs1ExtensionsBertDataStatus_Object = MibTableColumn
wanDs1ExtensionsBertDataStatus = _WanDs1ExtensionsBertDataStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 2, 1, 1, 18),
    _WanDs1ExtensionsBertDataStatus_Type()
)
wanDs1ExtensionsBertDataStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDs1ExtensionsBertDataStatus.setStatus("mandatory")
_CtWanRs232_ObjectIdentity = ObjectIdentity
ctWanRs232 = _CtWanRs232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 3)
)
_WanRs232ExtensionsTable_Object = MibTable
wanRs232ExtensionsTable = _WanRs232ExtensionsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wanRs232ExtensionsTable.setStatus("mandatory")
_WanRs232ExtensionsEntry_Object = MibTableRow
wanRs232ExtensionsEntry = _WanRs232ExtensionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 3, 1, 1)
)
wanRs232ExtensionsEntry.setIndexNames(
    (0, "CTRON-WAN-MIB", "wanRs232ExtensionsEntryIndex"),
)
if mibBuilder.loadTexts:
    wanRs232ExtensionsEntry.setStatus("mandatory")
_WanRs232ExtensionsEntryIndex_Type = Integer32
_WanRs232ExtensionsEntryIndex_Object = MibTableColumn
wanRs232ExtensionsEntryIndex = _WanRs232ExtensionsEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 3, 1, 1, 1),
    _WanRs232ExtensionsEntryIndex_Type()
)
wanRs232ExtensionsEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanRs232ExtensionsEntryIndex.setStatus("mandatory")


class _WanRs232ExtensionsCTSEnable_Type(Integer32):
    """Custom type wanRs232ExtensionsCTSEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WanRs232ExtensionsCTSEnable_Type.__name__ = "Integer32"
_WanRs232ExtensionsCTSEnable_Object = MibTableColumn
wanRs232ExtensionsCTSEnable = _WanRs232ExtensionsCTSEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 3, 1, 1, 2),
    _WanRs232ExtensionsCTSEnable_Type()
)
wanRs232ExtensionsCTSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanRs232ExtensionsCTSEnable.setStatus("mandatory")


class _WanRs232ExtensionsDSREnable_Type(Integer32):
    """Custom type wanRs232ExtensionsDSREnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WanRs232ExtensionsDSREnable_Type.__name__ = "Integer32"
_WanRs232ExtensionsDSREnable_Object = MibTableColumn
wanRs232ExtensionsDSREnable = _WanRs232ExtensionsDSREnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 3, 1, 1, 3),
    _WanRs232ExtensionsDSREnable_Type()
)
wanRs232ExtensionsDSREnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanRs232ExtensionsDSREnable.setStatus("mandatory")
_CtFrDcp_ObjectIdentity = ObjectIdentity
ctFrDcp = _CtFrDcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 4)
)
_FrDcpCircuitTable_Object = MibTable
frDcpCircuitTable = _FrDcpCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 4, 1)
)
if mibBuilder.loadTexts:
    frDcpCircuitTable.setStatus("mandatory")
_FrDcpCircuitEntry_Object = MibTableRow
frDcpCircuitEntry = _FrDcpCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 4, 1, 1)
)
frDcpCircuitEntry.setIndexNames(
    (0, "CTRON-WAN-MIB", "frDcpCircuitIfIndex"),
    (0, "CTRON-WAN-MIB", "frDcpCircuitDlci"),
)
if mibBuilder.loadTexts:
    frDcpCircuitEntry.setStatus("mandatory")
_FrDcpCircuitIfIndex_Type = Index
_FrDcpCircuitIfIndex_Object = MibTableColumn
frDcpCircuitIfIndex = _FrDcpCircuitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 4, 1, 1, 1),
    _FrDcpCircuitIfIndex_Type()
)
frDcpCircuitIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDcpCircuitIfIndex.setStatus("mandatory")
_FrDcpCircuitDlci_Type = DLCI
_FrDcpCircuitDlci_Object = MibTableColumn
frDcpCircuitDlci = _FrDcpCircuitDlci_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 4, 1, 1, 2),
    _FrDcpCircuitDlci_Type()
)
frDcpCircuitDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDcpCircuitDlci.setStatus("mandatory")


class _FrDcpCircuitEnable_Type(Integer32):
    """Custom type frDcpCircuitEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_FrDcpCircuitEnable_Type.__name__ = "Integer32"
_FrDcpCircuitEnable_Object = MibTableColumn
frDcpCircuitEnable = _FrDcpCircuitEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 4, 1, 1, 3),
    _FrDcpCircuitEnable_Type()
)
frDcpCircuitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDcpCircuitEnable.setStatus("mandatory")


class _FrDcpCircuitStatus_Type(Integer32):
    """Custom type frDcpCircuitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_FrDcpCircuitStatus_Type.__name__ = "Integer32"
_FrDcpCircuitStatus_Object = MibTableColumn
frDcpCircuitStatus = _FrDcpCircuitStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 4, 1, 1, 4),
    _FrDcpCircuitStatus_Type()
)
frDcpCircuitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDcpCircuitStatus.setStatus("mandatory")


class _FrDcpCircuitRatio_Type(OctetString):
    """Custom type frDcpCircuitRatio based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_FrDcpCircuitRatio_Type.__name__ = "OctetString"
_FrDcpCircuitRatio_Object = MibTableColumn
frDcpCircuitRatio = _FrDcpCircuitRatio_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 4, 1, 1, 5),
    _FrDcpCircuitRatio_Type()
)
frDcpCircuitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDcpCircuitRatio.setStatus("mandatory")
_CtDDS_ObjectIdentity = ObjectIdentity
ctDDS = _CtDDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 5)
)
_DdsConfigTable_Object = MibTable
ddsConfigTable = _DdsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ddsConfigTable.setStatus("mandatory")
_DdsConfigEntry_Object = MibTableRow
ddsConfigEntry = _DdsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 5, 1, 1)
)
ddsConfigEntry.setIndexNames(
    (0, "CTRON-WAN-MIB", "ddsLineIndex"),
)
if mibBuilder.loadTexts:
    ddsConfigEntry.setStatus("mandatory")


class _DdsLineIndex_Type(Integer32):
    """Custom type ddsLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DdsLineIndex_Type.__name__ = "Integer32"
_DdsLineIndex_Object = MibTableColumn
ddsLineIndex = _DdsLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 5, 1, 1, 1),
    _DdsLineIndex_Type()
)
ddsLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsLineIndex.setStatus("mandatory")


class _DdsIfIndex_Type(Integer32):
    """Custom type ddsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DdsIfIndex_Type.__name__ = "Integer32"
_DdsIfIndex_Object = MibTableColumn
ddsIfIndex = _DdsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 5, 1, 1, 2),
    _DdsIfIndex_Type()
)
ddsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsIfIndex.setStatus("mandatory")


class _DdsLineMode_Type(Integer32):
    """Custom type ddsLineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ddsCc", 2),
          ("ddsPri", 1))
    )


_DdsLineMode_Type.__name__ = "Integer32"
_DdsLineMode_Object = MibTableColumn
ddsLineMode = _DdsLineMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 5, 1, 1, 3),
    _DdsLineMode_Type()
)
ddsLineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsLineMode.setStatus("mandatory")


class _DdsLineCoding_Type(Integer32):
    """Custom type ddsLineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ddsJBZS", 2),
          ("ddsNone", 1),
          ("otherLineCode", 3))
    )


_DdsLineCoding_Type.__name__ = "Integer32"
_DdsLineCoding_Object = MibTableColumn
ddsLineCoding = _DdsLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 5, 1, 1, 4),
    _DdsLineCoding_Type()
)
ddsLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsLineCoding.setStatus("mandatory")


class _DdsLoopbackConfig_Type(Integer32):
    """Custom type ddsLoopbackConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ddsLineLoop", 2),
          ("ddsNoLoop", 1))
    )


_DdsLoopbackConfig_Type.__name__ = "Integer32"
_DdsLoopbackConfig_Object = MibTableColumn
ddsLoopbackConfig = _DdsLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 5, 1, 1, 5),
    _DdsLoopbackConfig_Type()
)
ddsLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsLoopbackConfig.setStatus("mandatory")


class _DdsLineStatus_Type(Integer32):
    """Custom type ddsLineStatus based on Integer32"""
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
        *(("ddsLossOfSignal", 2),
          ("ddsNoAlarm", 1),
          ("ddsOutOfFrame", 4),
          ("ddsOutOfService", 3))
    )


_DdsLineStatus_Type.__name__ = "Integer32"
_DdsLineStatus_Object = MibTableColumn
ddsLineStatus = _DdsLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 5, 1, 1, 6),
    _DdsLineStatus_Type()
)
ddsLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsLineStatus.setStatus("mandatory")


class _DdsTxClockSource_Type(Integer32):
    """Custom type ddsTxClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ddsLocalTiming", 2),
          ("ddsLoopTiming", 1))
    )


_DdsTxClockSource_Type.__name__ = "Integer32"
_DdsTxClockSource_Object = MibTableColumn
ddsTxClockSource = _DdsTxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 5, 1, 1, 7),
    _DdsTxClockSource_Type()
)
ddsTxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsTxClockSource.setStatus("mandatory")
_DdsPortInSpeed_Type = Integer32
_DdsPortInSpeed_Object = MibTableColumn
ddsPortInSpeed = _DdsPortInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 5, 1, 1, 8),
    _DdsPortInSpeed_Type()
)
ddsPortInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsPortInSpeed.setStatus("mandatory")
_DdsPortOutSpeed_Type = Integer32
_DdsPortOutSpeed_Object = MibTableColumn
ddsPortOutSpeed = _DdsPortOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 5, 1, 1, 9),
    _DdsPortOutSpeed_Type()
)
ddsPortOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsPortOutSpeed.setStatus("mandatory")
_CtDs1Alarms_ObjectIdentity = ObjectIdentity
ctDs1Alarms = _CtDs1Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 6)
)
_Ds1AlarmsGlobalConfigGroup_ObjectIdentity = ObjectIdentity
ds1AlarmsGlobalConfigGroup = _Ds1AlarmsGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 6, 1)
)


class _Ds1AlarmGlobalAdmin_Type(Integer32):
    """Custom type ds1AlarmGlobalAdmin based on Integer32"""
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


_Ds1AlarmGlobalAdmin_Type.__name__ = "Integer32"
_Ds1AlarmGlobalAdmin_Object = MibScalar
ds1AlarmGlobalAdmin = _Ds1AlarmGlobalAdmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 6, 1, 1),
    _Ds1AlarmGlobalAdmin_Type()
)
ds1AlarmGlobalAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmGlobalAdmin.setStatus("mandatory")


class _Ds1AlarmGlobalAutoRecovery_Type(Integer32):
    """Custom type ds1AlarmGlobalAutoRecovery based on Integer32"""
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


_Ds1AlarmGlobalAutoRecovery_Type.__name__ = "Integer32"
_Ds1AlarmGlobalAutoRecovery_Object = MibScalar
ds1AlarmGlobalAutoRecovery = _Ds1AlarmGlobalAutoRecovery_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 6, 1, 2),
    _Ds1AlarmGlobalAutoRecovery_Type()
)
ds1AlarmGlobalAutoRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmGlobalAutoRecovery.setStatus("mandatory")


class _Ds1AlarmGlobalTrapEnable_Type(Integer32):
    """Custom type ds1AlarmGlobalTrapEnable based on Integer32"""
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


_Ds1AlarmGlobalTrapEnable_Type.__name__ = "Integer32"
_Ds1AlarmGlobalTrapEnable_Object = MibScalar
ds1AlarmGlobalTrapEnable = _Ds1AlarmGlobalTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 6, 1, 3),
    _Ds1AlarmGlobalTrapEnable_Type()
)
ds1AlarmGlobalTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmGlobalTrapEnable.setStatus("mandatory")


class _Ds1AlarmGlobalESCount_Type(Integer32):
    """Custom type ds1AlarmGlobalESCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_Ds1AlarmGlobalESCount_Type.__name__ = "Integer32"
_Ds1AlarmGlobalESCount_Object = MibScalar
ds1AlarmGlobalESCount = _Ds1AlarmGlobalESCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 6, 1, 4),
    _Ds1AlarmGlobalESCount_Type()
)
ds1AlarmGlobalESCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmGlobalESCount.setStatus("mandatory")


class _Ds1AlarmGlobalESInterval_Type(Integer32):
    """Custom type ds1AlarmGlobalESInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Ds1AlarmGlobalESInterval_Type.__name__ = "Integer32"
_Ds1AlarmGlobalESInterval_Object = MibScalar
ds1AlarmGlobalESInterval = _Ds1AlarmGlobalESInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 6, 1, 5),
    _Ds1AlarmGlobalESInterval_Type()
)
ds1AlarmGlobalESInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmGlobalESInterval.setStatus("mandatory")


class _Ds1AlarmGlobalBPVErrorRate_Type(Integer32):
    """Custom type ds1AlarmGlobalBPVErrorRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9),
    )


_Ds1AlarmGlobalBPVErrorRate_Type.__name__ = "Integer32"
_Ds1AlarmGlobalBPVErrorRate_Object = MibScalar
ds1AlarmGlobalBPVErrorRate = _Ds1AlarmGlobalBPVErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 6, 1, 6),
    _Ds1AlarmGlobalBPVErrorRate_Type()
)
ds1AlarmGlobalBPVErrorRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmGlobalBPVErrorRate.setStatus("mandatory")


class _Ds1AlarmGlobalBPVInterval_Type(Integer32):
    """Custom type ds1AlarmGlobalBPVInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Ds1AlarmGlobalBPVInterval_Type.__name__ = "Integer32"
_Ds1AlarmGlobalBPVInterval_Object = MibScalar
ds1AlarmGlobalBPVInterval = _Ds1AlarmGlobalBPVInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 6, 1, 7),
    _Ds1AlarmGlobalBPVInterval_Type()
)
ds1AlarmGlobalBPVInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmGlobalBPVInterval.setStatus("mandatory")


class _Ds1AlarmGlobalManualRecovery_Type(Integer32):
    """Custom type ds1AlarmGlobalManualRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("recover", 1)
    )


_Ds1AlarmGlobalManualRecovery_Type.__name__ = "Integer32"
_Ds1AlarmGlobalManualRecovery_Object = MibScalar
ds1AlarmGlobalManualRecovery = _Ds1AlarmGlobalManualRecovery_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 6, 1, 8),
    _Ds1AlarmGlobalManualRecovery_Type()
)
ds1AlarmGlobalManualRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmGlobalManualRecovery.setStatus("mandatory")
_Ds1AlarmConfigTable_Object = MibTable
ds1AlarmConfigTable = _Ds1AlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 6, 2)
)
if mibBuilder.loadTexts:
    ds1AlarmConfigTable.setStatus("mandatory")
_Ds1AlarmConfigEntry_Object = MibTableRow
ds1AlarmConfigEntry = _Ds1AlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 6, 2, 1)
)
ds1AlarmConfigEntry.setIndexNames(
    (0, "CTRON-WAN-MIB", "ds1PhysNum"),
)
if mibBuilder.loadTexts:
    ds1AlarmConfigEntry.setStatus("mandatory")
_Ds1PhysNum_Type = Integer32
_Ds1PhysNum_Object = MibTableColumn
ds1PhysNum = _Ds1PhysNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 6, 2, 1, 1),
    _Ds1PhysNum_Type()
)
ds1PhysNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1PhysNum.setStatus("mandatory")


class _Ds1AlarmAdmin_Type(Integer32):
    """Custom type ds1AlarmAdmin based on Integer32"""
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


_Ds1AlarmAdmin_Type.__name__ = "Integer32"
_Ds1AlarmAdmin_Object = MibTableColumn
ds1AlarmAdmin = _Ds1AlarmAdmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 6, 2, 1, 2),
    _Ds1AlarmAdmin_Type()
)
ds1AlarmAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmAdmin.setStatus("mandatory")


class _Ds1AlarmAutoRecovery_Type(Integer32):
    """Custom type ds1AlarmAutoRecovery based on Integer32"""
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


_Ds1AlarmAutoRecovery_Type.__name__ = "Integer32"
_Ds1AlarmAutoRecovery_Object = MibTableColumn
ds1AlarmAutoRecovery = _Ds1AlarmAutoRecovery_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 6, 2, 1, 3),
    _Ds1AlarmAutoRecovery_Type()
)
ds1AlarmAutoRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmAutoRecovery.setStatus("mandatory")


class _Ds1AlarmTrapEnable_Type(Integer32):
    """Custom type ds1AlarmTrapEnable based on Integer32"""
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


_Ds1AlarmTrapEnable_Type.__name__ = "Integer32"
_Ds1AlarmTrapEnable_Object = MibTableColumn
ds1AlarmTrapEnable = _Ds1AlarmTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 6, 2, 1, 4),
    _Ds1AlarmTrapEnable_Type()
)
ds1AlarmTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmTrapEnable.setStatus("mandatory")


class _Ds1AlarmESCount_Type(Integer32):
    """Custom type ds1AlarmESCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_Ds1AlarmESCount_Type.__name__ = "Integer32"
_Ds1AlarmESCount_Object = MibTableColumn
ds1AlarmESCount = _Ds1AlarmESCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 6, 2, 1, 5),
    _Ds1AlarmESCount_Type()
)
ds1AlarmESCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmESCount.setStatus("mandatory")


class _Ds1AlarmESInterval_Type(Integer32):
    """Custom type ds1AlarmESInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Ds1AlarmESInterval_Type.__name__ = "Integer32"
_Ds1AlarmESInterval_Object = MibTableColumn
ds1AlarmESInterval = _Ds1AlarmESInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 6, 2, 1, 6),
    _Ds1AlarmESInterval_Type()
)
ds1AlarmESInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmESInterval.setStatus("mandatory")


class _Ds1AlarmBPVErrorRate_Type(Integer32):
    """Custom type ds1AlarmBPVErrorRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9),
    )


_Ds1AlarmBPVErrorRate_Type.__name__ = "Integer32"
_Ds1AlarmBPVErrorRate_Object = MibTableColumn
ds1AlarmBPVErrorRate = _Ds1AlarmBPVErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 6, 2, 1, 7),
    _Ds1AlarmBPVErrorRate_Type()
)
ds1AlarmBPVErrorRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmBPVErrorRate.setStatus("mandatory")


class _Ds1AlarmBPVInterval_Type(Integer32):
    """Custom type ds1AlarmBPVInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Ds1AlarmBPVInterval_Type.__name__ = "Integer32"
_Ds1AlarmBPVInterval_Object = MibTableColumn
ds1AlarmBPVInterval = _Ds1AlarmBPVInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 6, 2, 1, 8),
    _Ds1AlarmBPVInterval_Type()
)
ds1AlarmBPVInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmBPVInterval.setStatus("mandatory")


class _Ds1AlarmManualRecovery_Type(Integer32):
    """Custom type ds1AlarmManualRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("recover", 1)
    )


_Ds1AlarmManualRecovery_Type.__name__ = "Integer32"
_Ds1AlarmManualRecovery_Object = MibTableColumn
ds1AlarmManualRecovery = _Ds1AlarmManualRecovery_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 6, 2, 1, 9),
    _Ds1AlarmManualRecovery_Type()
)
ds1AlarmManualRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmManualRecovery.setStatus("mandatory")
_CtIPPQFilters_ObjectIdentity = ObjectIdentity
ctIPPQFilters = _CtIPPQFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 7)
)
_IpPQConfigGroup_ObjectIdentity = ObjectIdentity
ipPQConfigGroup = _IpPQConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 7, 1)
)


class _IpPQAdmin_Type(Integer32):
    """Custom type ipPQAdmin based on Integer32"""
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


_IpPQAdmin_Type.__name__ = "Integer32"
_IpPQAdmin_Object = MibScalar
ipPQAdmin = _IpPQAdmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 7, 1, 1),
    _IpPQAdmin_Type()
)
ipPQAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPQAdmin.setStatus("mandatory")
_IPPQMaxEntries_Type = Integer32
_IPPQMaxEntries_Object = MibScalar
iPPQMaxEntries = _IPPQMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 7, 1, 2),
    _IPPQMaxEntries_Type()
)
iPPQMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPPQMaxEntries.setStatus("mandatory")
_IPPQNumEntries_Type = Integer32
_IPPQNumEntries_Object = MibScalar
iPPQNumEntries = _IPPQNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 7, 1, 3),
    _IPPQNumEntries_Type()
)
iPPQNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPPQNumEntries.setStatus("mandatory")
_IPPQAddAddress_Type = IpAddress
_IPPQAddAddress_Object = MibScalar
iPPQAddAddress = _IPPQAddAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 7, 1, 4),
    _IPPQAddAddress_Type()
)
iPPQAddAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPPQAddAddress.setStatus("mandatory")
_IPPQDelAddress_Type = IpAddress
_IPPQDelAddress_Object = MibScalar
iPPQDelAddress = _IPPQDelAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 7, 1, 5),
    _IPPQDelAddress_Type()
)
iPPQDelAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPPQDelAddress.setStatus("mandatory")
_IpPQAddressTable_Object = MibTable
ipPQAddressTable = _IpPQAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 7, 2)
)
if mibBuilder.loadTexts:
    ipPQAddressTable.setStatus("mandatory")
_IpPQAddressEntry_Object = MibTableRow
ipPQAddressEntry = _IpPQAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 7, 2, 1)
)
ipPQAddressEntry.setIndexNames(
    (0, "CTRON-WAN-MIB", "ipPQAddressId"),
)
if mibBuilder.loadTexts:
    ipPQAddressEntry.setStatus("mandatory")


class _IpPQAddressId_Type(Integer32):
    """Custom type ipPQAddressId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpPQAddressId_Type.__name__ = "Integer32"
_IpPQAddressId_Object = MibTableColumn
ipPQAddressId = _IpPQAddressId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 7, 2, 1, 1),
    _IpPQAddressId_Type()
)
ipPQAddressId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPQAddressId.setStatus("mandatory")
_IpPQIPAddress_Type = IpAddress
_IpPQIPAddress_Object = MibTableColumn
ipPQIPAddress = _IpPQIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 7, 2, 1, 2),
    _IpPQIPAddress_Type()
)
ipPQIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPQIPAddress.setStatus("mandatory")
_CtWanHDSLExt_ObjectIdentity = ObjectIdentity
ctWanHDSLExt = _CtWanHDSLExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8)
)
_CtWanHDSLPerformance15mTable_Object = MibTable
ctWanHDSLPerformance15mTable = _CtWanHDSLPerformance15mTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1)
)
if mibBuilder.loadTexts:
    ctWanHDSLPerformance15mTable.setStatus("mandatory")
_CtWanHDSLPerformance15mEntry_Object = MibTableRow
ctWanHDSLPerformance15mEntry = _CtWanHDSLPerformance15mEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1)
)
ctWanHDSLPerformance15mEntry.setIndexNames(
    (0, "CTRON-WAN-MIB", "ctWanHDSLPerformance15mConnIndex"),
    (0, "CTRON-WAN-MIB", "ctWanHDSLPerformance15mSlotIndex"),
)
if mibBuilder.loadTexts:
    ctWanHDSLPerformance15mEntry.setStatus("mandatory")
_CtWanHDSLPerformance15mConnIndex_Type = Integer32
_CtWanHDSLPerformance15mConnIndex_Object = MibTableColumn
ctWanHDSLPerformance15mConnIndex = _CtWanHDSLPerformance15mConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 1),
    _CtWanHDSLPerformance15mConnIndex_Type()
)
ctWanHDSLPerformance15mConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLPerformance15mConnIndex.setStatus("mandatory")
_CtWanHDSLPerformance15mSlotIndex_Type = Integer32
_CtWanHDSLPerformance15mSlotIndex_Object = MibTableColumn
ctWanHDSLPerformance15mSlotIndex = _CtWanHDSLPerformance15mSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 2),
    _CtWanHDSLPerformance15mSlotIndex_Type()
)
ctWanHDSLPerformance15mSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLPerformance15mSlotIndex.setStatus("mandatory")
_CtWanHDSLHLULoop1UAS15m_Type = Integer32
_CtWanHDSLHLULoop1UAS15m_Object = MibTableColumn
ctWanHDSLHLULoop1UAS15m = _CtWanHDSLHLULoop1UAS15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 3),
    _CtWanHDSLHLULoop1UAS15m_Type()
)
ctWanHDSLHLULoop1UAS15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLHLULoop1UAS15m.setStatus("mandatory")
_CtWanHDSLHLULoop1ES15m_Type = Integer32
_CtWanHDSLHLULoop1ES15m_Object = MibTableColumn
ctWanHDSLHLULoop1ES15m = _CtWanHDSLHLULoop1ES15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 4),
    _CtWanHDSLHLULoop1ES15m_Type()
)
ctWanHDSLHLULoop1ES15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLHLULoop1ES15m.setStatus("mandatory")
_CtWanHDSLHLULoop2UAS15m_Type = Integer32
_CtWanHDSLHLULoop2UAS15m_Object = MibTableColumn
ctWanHDSLHLULoop2UAS15m = _CtWanHDSLHLULoop2UAS15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 5),
    _CtWanHDSLHLULoop2UAS15m_Type()
)
ctWanHDSLHLULoop2UAS15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLHLULoop2UAS15m.setStatus("mandatory")
_CtWanHDSLHLULoop2ES15m_Type = Integer32
_CtWanHDSLHLULoop2ES15m_Object = MibTableColumn
ctWanHDSLHLULoop2ES15m = _CtWanHDSLHLULoop2ES15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 6),
    _CtWanHDSLHLULoop2ES15m_Type()
)
ctWanHDSLHLULoop2ES15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLHLULoop2ES15m.setStatus("mandatory")
_CtWanHDSLHRULoop1UAS15m_Type = Integer32
_CtWanHDSLHRULoop1UAS15m_Object = MibTableColumn
ctWanHDSLHRULoop1UAS15m = _CtWanHDSLHRULoop1UAS15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 7),
    _CtWanHDSLHRULoop1UAS15m_Type()
)
ctWanHDSLHRULoop1UAS15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLHRULoop1UAS15m.setStatus("mandatory")
_CtWanHDSLHRULoop1ES15m_Type = Integer32
_CtWanHDSLHRULoop1ES15m_Object = MibTableColumn
ctWanHDSLHRULoop1ES15m = _CtWanHDSLHRULoop1ES15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 8),
    _CtWanHDSLHRULoop1ES15m_Type()
)
ctWanHDSLHRULoop1ES15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLHRULoop1ES15m.setStatus("mandatory")
_CtWanHDSLHRULoop2UAS15m_Type = Integer32
_CtWanHDSLHRULoop2UAS15m_Object = MibTableColumn
ctWanHDSLHRULoop2UAS15m = _CtWanHDSLHRULoop2UAS15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 9),
    _CtWanHDSLHRULoop2UAS15m_Type()
)
ctWanHDSLHRULoop2UAS15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLHRULoop2UAS15m.setStatus("mandatory")
_CtWanHDSLHRULoop2ES15m_Type = Integer32
_CtWanHDSLHRULoop2ES15m_Object = MibTableColumn
ctWanHDSLHRULoop2ES15m = _CtWanHDSLHRULoop2ES15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 10),
    _CtWanHDSLHRULoop2ES15m_Type()
)
ctWanHDSLHRULoop2ES15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLHRULoop2ES15m.setStatus("mandatory")
_CtWanHDSLDb1NetworkLoop1UAS15m_Type = Integer32
_CtWanHDSLDb1NetworkLoop1UAS15m_Object = MibTableColumn
ctWanHDSLDb1NetworkLoop1UAS15m = _CtWanHDSLDb1NetworkLoop1UAS15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 11),
    _CtWanHDSLDb1NetworkLoop1UAS15m_Type()
)
ctWanHDSLDb1NetworkLoop1UAS15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb1NetworkLoop1UAS15m.setStatus("mandatory")
_CtWanHDSLDb1NetworkLoop1ES15m_Type = Integer32
_CtWanHDSLDb1NetworkLoop1ES15m_Object = MibTableColumn
ctWanHDSLDb1NetworkLoop1ES15m = _CtWanHDSLDb1NetworkLoop1ES15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 12),
    _CtWanHDSLDb1NetworkLoop1ES15m_Type()
)
ctWanHDSLDb1NetworkLoop1ES15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb1NetworkLoop1ES15m.setStatus("mandatory")
_CtWanHDSLDb1NetworkLoop2UAS15m_Type = Integer32
_CtWanHDSLDb1NetworkLoop2UAS15m_Object = MibTableColumn
ctWanHDSLDb1NetworkLoop2UAS15m = _CtWanHDSLDb1NetworkLoop2UAS15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 13),
    _CtWanHDSLDb1NetworkLoop2UAS15m_Type()
)
ctWanHDSLDb1NetworkLoop2UAS15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb1NetworkLoop2UAS15m.setStatus("mandatory")
_CtWanHDSLDb1NetworkLoop2ES15m_Type = Integer32
_CtWanHDSLDb1NetworkLoop2ES15m_Object = MibTableColumn
ctWanHDSLDb1NetworkLoop2ES15m = _CtWanHDSLDb1NetworkLoop2ES15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 14),
    _CtWanHDSLDb1NetworkLoop2ES15m_Type()
)
ctWanHDSLDb1NetworkLoop2ES15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb1NetworkLoop2ES15m.setStatus("mandatory")
_CtWanHDSLDb1CustomerLoop1UAS15m_Type = Integer32
_CtWanHDSLDb1CustomerLoop1UAS15m_Object = MibTableColumn
ctWanHDSLDb1CustomerLoop1UAS15m = _CtWanHDSLDb1CustomerLoop1UAS15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 15),
    _CtWanHDSLDb1CustomerLoop1UAS15m_Type()
)
ctWanHDSLDb1CustomerLoop1UAS15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb1CustomerLoop1UAS15m.setStatus("mandatory")
_CtWanHDSLDb1CustomerLoop1ES15m_Type = Integer32
_CtWanHDSLDb1CustomerLoop1ES15m_Object = MibTableColumn
ctWanHDSLDb1CustomerLoop1ES15m = _CtWanHDSLDb1CustomerLoop1ES15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 16),
    _CtWanHDSLDb1CustomerLoop1ES15m_Type()
)
ctWanHDSLDb1CustomerLoop1ES15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb1CustomerLoop1ES15m.setStatus("mandatory")
_CtWanHDSLDb1CustomerLoop2UAS15m_Type = Integer32
_CtWanHDSLDb1CustomerLoop2UAS15m_Object = MibTableColumn
ctWanHDSLDb1CustomerLoop2UAS15m = _CtWanHDSLDb1CustomerLoop2UAS15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 17),
    _CtWanHDSLDb1CustomerLoop2UAS15m_Type()
)
ctWanHDSLDb1CustomerLoop2UAS15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb1CustomerLoop2UAS15m.setStatus("mandatory")
_CtWanHDSLDb1CustomerLoop2ES15m_Type = Integer32
_CtWanHDSLDb1CustomerLoop2ES15m_Object = MibTableColumn
ctWanHDSLDb1CustomerLoop2ES15m = _CtWanHDSLDb1CustomerLoop2ES15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 18),
    _CtWanHDSLDb1CustomerLoop2ES15m_Type()
)
ctWanHDSLDb1CustomerLoop2ES15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb1CustomerLoop2ES15m.setStatus("mandatory")
_CtWanHDSLDb2NetworkLoop1UAS15m_Type = Integer32
_CtWanHDSLDb2NetworkLoop1UAS15m_Object = MibTableColumn
ctWanHDSLDb2NetworkLoop1UAS15m = _CtWanHDSLDb2NetworkLoop1UAS15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 19),
    _CtWanHDSLDb2NetworkLoop1UAS15m_Type()
)
ctWanHDSLDb2NetworkLoop1UAS15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb2NetworkLoop1UAS15m.setStatus("mandatory")
_CtWanHDSLDb2NetworkLoop1ES15m_Type = Integer32
_CtWanHDSLDb2NetworkLoop1ES15m_Object = MibTableColumn
ctWanHDSLDb2NetworkLoop1ES15m = _CtWanHDSLDb2NetworkLoop1ES15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 20),
    _CtWanHDSLDb2NetworkLoop1ES15m_Type()
)
ctWanHDSLDb2NetworkLoop1ES15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb2NetworkLoop1ES15m.setStatus("mandatory")
_CtWanHDSLDb2NetworkLoop2UAS15m_Type = Integer32
_CtWanHDSLDb2NetworkLoop2UAS15m_Object = MibTableColumn
ctWanHDSLDb2NetworkLoop2UAS15m = _CtWanHDSLDb2NetworkLoop2UAS15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 21),
    _CtWanHDSLDb2NetworkLoop2UAS15m_Type()
)
ctWanHDSLDb2NetworkLoop2UAS15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb2NetworkLoop2UAS15m.setStatus("mandatory")
_CtWanHDSLDb2NetworkLoop2ES15m_Type = Integer32
_CtWanHDSLDb2NetworkLoop2ES15m_Object = MibTableColumn
ctWanHDSLDb2NetworkLoop2ES15m = _CtWanHDSLDb2NetworkLoop2ES15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 22),
    _CtWanHDSLDb2NetworkLoop2ES15m_Type()
)
ctWanHDSLDb2NetworkLoop2ES15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb2NetworkLoop2ES15m.setStatus("mandatory")
_CtWanHDSLDb2CustomerLoop1UAS15m_Type = Integer32
_CtWanHDSLDb2CustomerLoop1UAS15m_Object = MibTableColumn
ctWanHDSLDb2CustomerLoop1UAS15m = _CtWanHDSLDb2CustomerLoop1UAS15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 23),
    _CtWanHDSLDb2CustomerLoop1UAS15m_Type()
)
ctWanHDSLDb2CustomerLoop1UAS15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb2CustomerLoop1UAS15m.setStatus("mandatory")
_CtWanHDSLDb2CustomerLoop1ES15m_Type = Integer32
_CtWanHDSLDb2CustomerLoop1ES15m_Object = MibTableColumn
ctWanHDSLDb2CustomerLoop1ES15m = _CtWanHDSLDb2CustomerLoop1ES15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 24),
    _CtWanHDSLDb2CustomerLoop1ES15m_Type()
)
ctWanHDSLDb2CustomerLoop1ES15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb2CustomerLoop1ES15m.setStatus("mandatory")
_CtWanHDSLDb2CustomerLoop2UAS15m_Type = Integer32
_CtWanHDSLDb2CustomerLoop2UAS15m_Object = MibTableColumn
ctWanHDSLDb2CustomerLoop2UAS15m = _CtWanHDSLDb2CustomerLoop2UAS15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 25),
    _CtWanHDSLDb2CustomerLoop2UAS15m_Type()
)
ctWanHDSLDb2CustomerLoop2UAS15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb2CustomerLoop2UAS15m.setStatus("mandatory")
_CtWanHDSLDb2CustomerLoop2ES15m_Type = Integer32
_CtWanHDSLDb2CustomerLoop2ES15m_Object = MibTableColumn
ctWanHDSLDb2CustomerLoop2ES15m = _CtWanHDSLDb2CustomerLoop2ES15m_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 1, 1, 26),
    _CtWanHDSLDb2CustomerLoop2ES15m_Type()
)
ctWanHDSLDb2CustomerLoop2ES15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb2CustomerLoop2ES15m.setStatus("mandatory")
_CtWanHDSLPerformance24hTable_Object = MibTable
ctWanHDSLPerformance24hTable = _CtWanHDSLPerformance24hTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2)
)
if mibBuilder.loadTexts:
    ctWanHDSLPerformance24hTable.setStatus("mandatory")
_CtWanHDSLPerformance24hEntry_Object = MibTableRow
ctWanHDSLPerformance24hEntry = _CtWanHDSLPerformance24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1)
)
ctWanHDSLPerformance24hEntry.setIndexNames(
    (0, "CTRON-WAN-MIB", "ctWanHDSLPerformance24hConnIndex"),
    (0, "CTRON-WAN-MIB", "ctWanHDSLPerformance24hSlotIndex"),
)
if mibBuilder.loadTexts:
    ctWanHDSLPerformance24hEntry.setStatus("mandatory")
_CtWanHDSLPerformance24hConnIndex_Type = Integer32
_CtWanHDSLPerformance24hConnIndex_Object = MibTableColumn
ctWanHDSLPerformance24hConnIndex = _CtWanHDSLPerformance24hConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 1),
    _CtWanHDSLPerformance24hConnIndex_Type()
)
ctWanHDSLPerformance24hConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLPerformance24hConnIndex.setStatus("mandatory")
_CtWanHDSLPerformance24hSlotIndex_Type = Integer32
_CtWanHDSLPerformance24hSlotIndex_Object = MibTableColumn
ctWanHDSLPerformance24hSlotIndex = _CtWanHDSLPerformance24hSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 2),
    _CtWanHDSLPerformance24hSlotIndex_Type()
)
ctWanHDSLPerformance24hSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLPerformance24hSlotIndex.setStatus("mandatory")
_CtWanHDSLHLULoop1UAS24h_Type = Integer32
_CtWanHDSLHLULoop1UAS24h_Object = MibTableColumn
ctWanHDSLHLULoop1UAS24h = _CtWanHDSLHLULoop1UAS24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 3),
    _CtWanHDSLHLULoop1UAS24h_Type()
)
ctWanHDSLHLULoop1UAS24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLHLULoop1UAS24h.setStatus("mandatory")
_CtWanHDSLHLULoop1ES24h_Type = Integer32
_CtWanHDSLHLULoop1ES24h_Object = MibTableColumn
ctWanHDSLHLULoop1ES24h = _CtWanHDSLHLULoop1ES24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 4),
    _CtWanHDSLHLULoop1ES24h_Type()
)
ctWanHDSLHLULoop1ES24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLHLULoop1ES24h.setStatus("mandatory")
_CtWanHDSLHLULoop2UAS24h_Type = Integer32
_CtWanHDSLHLULoop2UAS24h_Object = MibTableColumn
ctWanHDSLHLULoop2UAS24h = _CtWanHDSLHLULoop2UAS24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 5),
    _CtWanHDSLHLULoop2UAS24h_Type()
)
ctWanHDSLHLULoop2UAS24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLHLULoop2UAS24h.setStatus("mandatory")
_CtWanHDSLHLULoop2ES24h_Type = Integer32
_CtWanHDSLHLULoop2ES24h_Object = MibTableColumn
ctWanHDSLHLULoop2ES24h = _CtWanHDSLHLULoop2ES24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 6),
    _CtWanHDSLHLULoop2ES24h_Type()
)
ctWanHDSLHLULoop2ES24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLHLULoop2ES24h.setStatus("mandatory")
_CtWanHDSLHRULoop1UAS24h_Type = Integer32
_CtWanHDSLHRULoop1UAS24h_Object = MibTableColumn
ctWanHDSLHRULoop1UAS24h = _CtWanHDSLHRULoop1UAS24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 7),
    _CtWanHDSLHRULoop1UAS24h_Type()
)
ctWanHDSLHRULoop1UAS24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLHRULoop1UAS24h.setStatus("mandatory")
_CtWanHDSLHRULoop1ES24h_Type = Integer32
_CtWanHDSLHRULoop1ES24h_Object = MibTableColumn
ctWanHDSLHRULoop1ES24h = _CtWanHDSLHRULoop1ES24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 8),
    _CtWanHDSLHRULoop1ES24h_Type()
)
ctWanHDSLHRULoop1ES24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLHRULoop1ES24h.setStatus("mandatory")
_CtWanHDSLHRULoop2UAS24h_Type = Integer32
_CtWanHDSLHRULoop2UAS24h_Object = MibTableColumn
ctWanHDSLHRULoop2UAS24h = _CtWanHDSLHRULoop2UAS24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 9),
    _CtWanHDSLHRULoop2UAS24h_Type()
)
ctWanHDSLHRULoop2UAS24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLHRULoop2UAS24h.setStatus("mandatory")
_CtWanHDSLHRULoop2ES24h_Type = Integer32
_CtWanHDSLHRULoop2ES24h_Object = MibTableColumn
ctWanHDSLHRULoop2ES24h = _CtWanHDSLHRULoop2ES24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 10),
    _CtWanHDSLHRULoop2ES24h_Type()
)
ctWanHDSLHRULoop2ES24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLHRULoop2ES24h.setStatus("mandatory")
_CtWanHDSLDb1NetworkLoop1UAS24h_Type = Integer32
_CtWanHDSLDb1NetworkLoop1UAS24h_Object = MibTableColumn
ctWanHDSLDb1NetworkLoop1UAS24h = _CtWanHDSLDb1NetworkLoop1UAS24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 11),
    _CtWanHDSLDb1NetworkLoop1UAS24h_Type()
)
ctWanHDSLDb1NetworkLoop1UAS24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb1NetworkLoop1UAS24h.setStatus("mandatory")
_CtWanHDSLDb1NetworkLoop1ES24h_Type = Integer32
_CtWanHDSLDb1NetworkLoop1ES24h_Object = MibTableColumn
ctWanHDSLDb1NetworkLoop1ES24h = _CtWanHDSLDb1NetworkLoop1ES24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 12),
    _CtWanHDSLDb1NetworkLoop1ES24h_Type()
)
ctWanHDSLDb1NetworkLoop1ES24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb1NetworkLoop1ES24h.setStatus("mandatory")
_CtWanHDSLDb1NetworkLoop2UAS24h_Type = Integer32
_CtWanHDSLDb1NetworkLoop2UAS24h_Object = MibTableColumn
ctWanHDSLDb1NetworkLoop2UAS24h = _CtWanHDSLDb1NetworkLoop2UAS24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 13),
    _CtWanHDSLDb1NetworkLoop2UAS24h_Type()
)
ctWanHDSLDb1NetworkLoop2UAS24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb1NetworkLoop2UAS24h.setStatus("mandatory")
_CtWanHDSLDb1NetworkLoop2ES24h_Type = Integer32
_CtWanHDSLDb1NetworkLoop2ES24h_Object = MibTableColumn
ctWanHDSLDb1NetworkLoop2ES24h = _CtWanHDSLDb1NetworkLoop2ES24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 14),
    _CtWanHDSLDb1NetworkLoop2ES24h_Type()
)
ctWanHDSLDb1NetworkLoop2ES24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb1NetworkLoop2ES24h.setStatus("mandatory")
_CtWanHDSLDb1CustomerLoop1UAS24h_Type = Integer32
_CtWanHDSLDb1CustomerLoop1UAS24h_Object = MibTableColumn
ctWanHDSLDb1CustomerLoop1UAS24h = _CtWanHDSLDb1CustomerLoop1UAS24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 15),
    _CtWanHDSLDb1CustomerLoop1UAS24h_Type()
)
ctWanHDSLDb1CustomerLoop1UAS24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb1CustomerLoop1UAS24h.setStatus("mandatory")
_CtWanHDSLDb1CustomerLoop1ES24h_Type = Integer32
_CtWanHDSLDb1CustomerLoop1ES24h_Object = MibTableColumn
ctWanHDSLDb1CustomerLoop1ES24h = _CtWanHDSLDb1CustomerLoop1ES24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 16),
    _CtWanHDSLDb1CustomerLoop1ES24h_Type()
)
ctWanHDSLDb1CustomerLoop1ES24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb1CustomerLoop1ES24h.setStatus("mandatory")
_CtWanHDSLDb1CustomerLoop2UAS24h_Type = Integer32
_CtWanHDSLDb1CustomerLoop2UAS24h_Object = MibTableColumn
ctWanHDSLDb1CustomerLoop2UAS24h = _CtWanHDSLDb1CustomerLoop2UAS24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 17),
    _CtWanHDSLDb1CustomerLoop2UAS24h_Type()
)
ctWanHDSLDb1CustomerLoop2UAS24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb1CustomerLoop2UAS24h.setStatus("mandatory")
_CtWanHDSLDb1CustomerLoop2ES24h_Type = Integer32
_CtWanHDSLDb1CustomerLoop2ES24h_Object = MibTableColumn
ctWanHDSLDb1CustomerLoop2ES24h = _CtWanHDSLDb1CustomerLoop2ES24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 18),
    _CtWanHDSLDb1CustomerLoop2ES24h_Type()
)
ctWanHDSLDb1CustomerLoop2ES24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb1CustomerLoop2ES24h.setStatus("mandatory")
_CtWanHDSLDb2NetworkLoop1UAS24h_Type = Integer32
_CtWanHDSLDb2NetworkLoop1UAS24h_Object = MibTableColumn
ctWanHDSLDb2NetworkLoop1UAS24h = _CtWanHDSLDb2NetworkLoop1UAS24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 19),
    _CtWanHDSLDb2NetworkLoop1UAS24h_Type()
)
ctWanHDSLDb2NetworkLoop1UAS24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb2NetworkLoop1UAS24h.setStatus("mandatory")
_CtWanHDSLDb2NetworkLoop1ES24h_Type = Integer32
_CtWanHDSLDb2NetworkLoop1ES24h_Object = MibTableColumn
ctWanHDSLDb2NetworkLoop1ES24h = _CtWanHDSLDb2NetworkLoop1ES24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 20),
    _CtWanHDSLDb2NetworkLoop1ES24h_Type()
)
ctWanHDSLDb2NetworkLoop1ES24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb2NetworkLoop1ES24h.setStatus("mandatory")
_CtWanHDSLDb2NetworkLoop2UAS24h_Type = Integer32
_CtWanHDSLDb2NetworkLoop2UAS24h_Object = MibTableColumn
ctWanHDSLDb2NetworkLoop2UAS24h = _CtWanHDSLDb2NetworkLoop2UAS24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 21),
    _CtWanHDSLDb2NetworkLoop2UAS24h_Type()
)
ctWanHDSLDb2NetworkLoop2UAS24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb2NetworkLoop2UAS24h.setStatus("mandatory")
_CtWanHDSLDb2NetworkLoop2ES24h_Type = Integer32
_CtWanHDSLDb2NetworkLoop2ES24h_Object = MibTableColumn
ctWanHDSLDb2NetworkLoop2ES24h = _CtWanHDSLDb2NetworkLoop2ES24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 22),
    _CtWanHDSLDb2NetworkLoop2ES24h_Type()
)
ctWanHDSLDb2NetworkLoop2ES24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb2NetworkLoop2ES24h.setStatus("mandatory")
_CtWanHDSLDb2CustomerLoop1UAS24h_Type = Integer32
_CtWanHDSLDb2CustomerLoop1UAS24h_Object = MibTableColumn
ctWanHDSLDb2CustomerLoop1UAS24h = _CtWanHDSLDb2CustomerLoop1UAS24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 23),
    _CtWanHDSLDb2CustomerLoop1UAS24h_Type()
)
ctWanHDSLDb2CustomerLoop1UAS24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb2CustomerLoop1UAS24h.setStatus("mandatory")
_CtWanHDSLDb2CustomerLoop1ES24h_Type = Integer32
_CtWanHDSLDb2CustomerLoop1ES24h_Object = MibTableColumn
ctWanHDSLDb2CustomerLoop1ES24h = _CtWanHDSLDb2CustomerLoop1ES24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 24),
    _CtWanHDSLDb2CustomerLoop1ES24h_Type()
)
ctWanHDSLDb2CustomerLoop1ES24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb2CustomerLoop1ES24h.setStatus("mandatory")
_CtWanHDSLDb2CustomerLoop2UAS24h_Type = Integer32
_CtWanHDSLDb2CustomerLoop2UAS24h_Object = MibTableColumn
ctWanHDSLDb2CustomerLoop2UAS24h = _CtWanHDSLDb2CustomerLoop2UAS24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 25),
    _CtWanHDSLDb2CustomerLoop2UAS24h_Type()
)
ctWanHDSLDb2CustomerLoop2UAS24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb2CustomerLoop2UAS24h.setStatus("mandatory")
_CtWanHDSLDb2CustomerLoop2ES24h_Type = Integer32
_CtWanHDSLDb2CustomerLoop2ES24h_Object = MibTableColumn
ctWanHDSLDb2CustomerLoop2ES24h = _CtWanHDSLDb2CustomerLoop2ES24h_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 2, 1, 26),
    _CtWanHDSLDb2CustomerLoop2ES24h_Type()
)
ctWanHDSLDb2CustomerLoop2ES24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDb2CustomerLoop2ES24h.setStatus("mandatory")
_CtWanHDSLStatisticsTable_Object = MibTable
ctWanHDSLStatisticsTable = _CtWanHDSLStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3)
)
if mibBuilder.loadTexts:
    ctWanHDSLStatisticsTable.setStatus("mandatory")
_CtWanHDSLStatisticsEntry_Object = MibTableRow
ctWanHDSLStatisticsEntry = _CtWanHDSLStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1)
)
ctWanHDSLStatisticsEntry.setIndexNames(
    (0, "CTRON-WAN-MIB", "ctWanHDSLStatisticsHLUConnIndex"),
)
if mibBuilder.loadTexts:
    ctWanHDSLStatisticsEntry.setStatus("mandatory")
_CtWanHDSLStatisticsHLUConnIndex_Type = Integer32
_CtWanHDSLStatisticsHLUConnIndex_Object = MibTableColumn
ctWanHDSLStatisticsHLUConnIndex = _CtWanHDSLStatisticsHLUConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 1),
    _CtWanHDSLStatisticsHLUConnIndex_Type()
)
ctWanHDSLStatisticsHLUConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLStatisticsHLUConnIndex.setStatus("mandatory")
_CtWanHDSLSNRHLULoop1_Type = Integer32
_CtWanHDSLSNRHLULoop1_Object = MibTableColumn
ctWanHDSLSNRHLULoop1 = _CtWanHDSLSNRHLULoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 2),
    _CtWanHDSLSNRHLULoop1_Type()
)
ctWanHDSLSNRHLULoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRHLULoop1.setStatus("mandatory")
_CtWanHDSLSNRLowHLULoop1_Type = Integer32
_CtWanHDSLSNRLowHLULoop1_Object = MibTableColumn
ctWanHDSLSNRLowHLULoop1 = _CtWanHDSLSNRLowHLULoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 3),
    _CtWanHDSLSNRLowHLULoop1_Type()
)
ctWanHDSLSNRLowHLULoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRLowHLULoop1.setStatus("mandatory")
_CtWanHDSLSNRHighHLULoop1_Type = Integer32
_CtWanHDSLSNRHighHLULoop1_Object = MibTableColumn
ctWanHDSLSNRHighHLULoop1 = _CtWanHDSLSNRHighHLULoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 4),
    _CtWanHDSLSNRHighHLULoop1_Type()
)
ctWanHDSLSNRHighHLULoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRHighHLULoop1.setStatus("mandatory")
_CtWanHDSLSNRHLULoop2_Type = Integer32
_CtWanHDSLSNRHLULoop2_Object = MibTableColumn
ctWanHDSLSNRHLULoop2 = _CtWanHDSLSNRHLULoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 5),
    _CtWanHDSLSNRHLULoop2_Type()
)
ctWanHDSLSNRHLULoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRHLULoop2.setStatus("mandatory")
_CtWanHDSLSNRLowHLULoop2_Type = Integer32
_CtWanHDSLSNRLowHLULoop2_Object = MibTableColumn
ctWanHDSLSNRLowHLULoop2 = _CtWanHDSLSNRLowHLULoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 6),
    _CtWanHDSLSNRLowHLULoop2_Type()
)
ctWanHDSLSNRLowHLULoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRLowHLULoop2.setStatus("mandatory")
_CtWanHDSLSNRHighHLULoop2_Type = Integer32
_CtWanHDSLSNRHighHLULoop2_Object = MibTableColumn
ctWanHDSLSNRHighHLULoop2 = _CtWanHDSLSNRHighHLULoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 7),
    _CtWanHDSLSNRHighHLULoop2_Type()
)
ctWanHDSLSNRHighHLULoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRHighHLULoop2.setStatus("mandatory")
_CtWanHDSLPulseAttenuationHLULoop1_Type = Integer32
_CtWanHDSLPulseAttenuationHLULoop1_Object = MibTableColumn
ctWanHDSLPulseAttenuationHLULoop1 = _CtWanHDSLPulseAttenuationHLULoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 8),
    _CtWanHDSLPulseAttenuationHLULoop1_Type()
)
ctWanHDSLPulseAttenuationHLULoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLPulseAttenuationHLULoop1.setStatus("mandatory")
_CtWanHDSLPulseAttenuationHLULoop2_Type = Integer32
_CtWanHDSLPulseAttenuationHLULoop2_Object = MibTableColumn
ctWanHDSLPulseAttenuationHLULoop2 = _CtWanHDSLPulseAttenuationHLULoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 9),
    _CtWanHDSLPulseAttenuationHLULoop2_Type()
)
ctWanHDSLPulseAttenuationHLULoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLPulseAttenuationHLULoop2.setStatus("mandatory")
_CtWanHDSLBitStat1HLU_Type = Integer32
_CtWanHDSLBitStat1HLU_Object = MibTableColumn
ctWanHDSLBitStat1HLU = _CtWanHDSLBitStat1HLU_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 10),
    _CtWanHDSLBitStat1HLU_Type()
)
ctWanHDSLBitStat1HLU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLBitStat1HLU.setStatus("mandatory")
_CtWanHDSLSNRHRULoop1_Type = Integer32
_CtWanHDSLSNRHRULoop1_Object = MibTableColumn
ctWanHDSLSNRHRULoop1 = _CtWanHDSLSNRHRULoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 11),
    _CtWanHDSLSNRHRULoop1_Type()
)
ctWanHDSLSNRHRULoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRHRULoop1.setStatus("mandatory")
_CtWanHDSLSNRLowHRULoop1_Type = Integer32
_CtWanHDSLSNRLowHRULoop1_Object = MibTableColumn
ctWanHDSLSNRLowHRULoop1 = _CtWanHDSLSNRLowHRULoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 12),
    _CtWanHDSLSNRLowHRULoop1_Type()
)
ctWanHDSLSNRLowHRULoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRLowHRULoop1.setStatus("mandatory")
_CtWanHDSLSNRHighHRULoop1_Type = Integer32
_CtWanHDSLSNRHighHRULoop1_Object = MibTableColumn
ctWanHDSLSNRHighHRULoop1 = _CtWanHDSLSNRHighHRULoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 13),
    _CtWanHDSLSNRHighHRULoop1_Type()
)
ctWanHDSLSNRHighHRULoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRHighHRULoop1.setStatus("mandatory")
_CtWanHDSLSNRHRULoop2_Type = Integer32
_CtWanHDSLSNRHRULoop2_Object = MibTableColumn
ctWanHDSLSNRHRULoop2 = _CtWanHDSLSNRHRULoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 14),
    _CtWanHDSLSNRHRULoop2_Type()
)
ctWanHDSLSNRHRULoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRHRULoop2.setStatus("mandatory")
_CtWanHDSLSNRLowHRULoop2_Type = Integer32
_CtWanHDSLSNRLowHRULoop2_Object = MibTableColumn
ctWanHDSLSNRLowHRULoop2 = _CtWanHDSLSNRLowHRULoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 15),
    _CtWanHDSLSNRLowHRULoop2_Type()
)
ctWanHDSLSNRLowHRULoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRLowHRULoop2.setStatus("mandatory")
_CtWanHDSLSNRHighHRULoop2_Type = Integer32
_CtWanHDSLSNRHighHRULoop2_Object = MibTableColumn
ctWanHDSLSNRHighHRULoop2 = _CtWanHDSLSNRHighHRULoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 16),
    _CtWanHDSLSNRHighHRULoop2_Type()
)
ctWanHDSLSNRHighHRULoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRHighHRULoop2.setStatus("mandatory")
_CtWanHDSLPulseAttenuationHRULoop1_Type = Integer32
_CtWanHDSLPulseAttenuationHRULoop1_Object = MibTableColumn
ctWanHDSLPulseAttenuationHRULoop1 = _CtWanHDSLPulseAttenuationHRULoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 17),
    _CtWanHDSLPulseAttenuationHRULoop1_Type()
)
ctWanHDSLPulseAttenuationHRULoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLPulseAttenuationHRULoop1.setStatus("mandatory")
_CtWanHDSLPulseAttenuationHRULoop2_Type = Integer32
_CtWanHDSLPulseAttenuationHRULoop2_Object = MibTableColumn
ctWanHDSLPulseAttenuationHRULoop2 = _CtWanHDSLPulseAttenuationHRULoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 18),
    _CtWanHDSLPulseAttenuationHRULoop2_Type()
)
ctWanHDSLPulseAttenuationHRULoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLPulseAttenuationHRULoop2.setStatus("mandatory")
_CtWanHDSLDs1FrameHRU_Type = Integer32
_CtWanHDSLDs1FrameHRU_Object = MibTableColumn
ctWanHDSLDs1FrameHRU = _CtWanHDSLDs1FrameHRU_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 19),
    _CtWanHDSLDs1FrameHRU_Type()
)
ctWanHDSLDs1FrameHRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLDs1FrameHRU.setStatus("mandatory")
_CtWanHDSLSNRDb1NetworkLoop1_Type = Integer32
_CtWanHDSLSNRDb1NetworkLoop1_Object = MibTableColumn
ctWanHDSLSNRDb1NetworkLoop1 = _CtWanHDSLSNRDb1NetworkLoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 20),
    _CtWanHDSLSNRDb1NetworkLoop1_Type()
)
ctWanHDSLSNRDb1NetworkLoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRDb1NetworkLoop1.setStatus("mandatory")
_CtWanHDSLSNRLowDb1NetworkLoop1_Type = Integer32
_CtWanHDSLSNRLowDb1NetworkLoop1_Object = MibTableColumn
ctWanHDSLSNRLowDb1NetworkLoop1 = _CtWanHDSLSNRLowDb1NetworkLoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 21),
    _CtWanHDSLSNRLowDb1NetworkLoop1_Type()
)
ctWanHDSLSNRLowDb1NetworkLoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRLowDb1NetworkLoop1.setStatus("mandatory")
_CtWanHDSLSNRHighDb1NetworkLoop1_Type = Integer32
_CtWanHDSLSNRHighDb1NetworkLoop1_Object = MibTableColumn
ctWanHDSLSNRHighDb1NetworkLoop1 = _CtWanHDSLSNRHighDb1NetworkLoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 22),
    _CtWanHDSLSNRHighDb1NetworkLoop1_Type()
)
ctWanHDSLSNRHighDb1NetworkLoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRHighDb1NetworkLoop1.setStatus("mandatory")
_CtWanHDSLSNRDb1NetworkLoop2_Type = Integer32
_CtWanHDSLSNRDb1NetworkLoop2_Object = MibTableColumn
ctWanHDSLSNRDb1NetworkLoop2 = _CtWanHDSLSNRDb1NetworkLoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 23),
    _CtWanHDSLSNRDb1NetworkLoop2_Type()
)
ctWanHDSLSNRDb1NetworkLoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRDb1NetworkLoop2.setStatus("mandatory")
_CtWanHDSLSNRLowDb1NetworkLoop2_Type = Integer32
_CtWanHDSLSNRLowDb1NetworkLoop2_Object = MibTableColumn
ctWanHDSLSNRLowDb1NetworkLoop2 = _CtWanHDSLSNRLowDb1NetworkLoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 24),
    _CtWanHDSLSNRLowDb1NetworkLoop2_Type()
)
ctWanHDSLSNRLowDb1NetworkLoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRLowDb1NetworkLoop2.setStatus("mandatory")
_CtWanHDSLSNRHighDb1NetworkLoop2_Type = Integer32
_CtWanHDSLSNRHighDb1NetworkLoop2_Object = MibTableColumn
ctWanHDSLSNRHighDb1NetworkLoop2 = _CtWanHDSLSNRHighDb1NetworkLoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 25),
    _CtWanHDSLSNRHighDb1NetworkLoop2_Type()
)
ctWanHDSLSNRHighDb1NetworkLoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRHighDb1NetworkLoop2.setStatus("mandatory")
_CtWanHDSLSNRDb1CustomerLoop1_Type = Integer32
_CtWanHDSLSNRDb1CustomerLoop1_Object = MibTableColumn
ctWanHDSLSNRDb1CustomerLoop1 = _CtWanHDSLSNRDb1CustomerLoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 26),
    _CtWanHDSLSNRDb1CustomerLoop1_Type()
)
ctWanHDSLSNRDb1CustomerLoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRDb1CustomerLoop1.setStatus("mandatory")
_CtWanHDSLSNRLowDb1CustomerLoop1_Type = Integer32
_CtWanHDSLSNRLowDb1CustomerLoop1_Object = MibTableColumn
ctWanHDSLSNRLowDb1CustomerLoop1 = _CtWanHDSLSNRLowDb1CustomerLoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 27),
    _CtWanHDSLSNRLowDb1CustomerLoop1_Type()
)
ctWanHDSLSNRLowDb1CustomerLoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRLowDb1CustomerLoop1.setStatus("mandatory")
_CtWanHDSLSNRHighDb1CustomerLoop1_Type = Integer32
_CtWanHDSLSNRHighDb1CustomerLoop1_Object = MibTableColumn
ctWanHDSLSNRHighDb1CustomerLoop1 = _CtWanHDSLSNRHighDb1CustomerLoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 28),
    _CtWanHDSLSNRHighDb1CustomerLoop1_Type()
)
ctWanHDSLSNRHighDb1CustomerLoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRHighDb1CustomerLoop1.setStatus("mandatory")
_CtWanHDSLSNRDb1CustomerLoop2_Type = Integer32
_CtWanHDSLSNRDb1CustomerLoop2_Object = MibTableColumn
ctWanHDSLSNRDb1CustomerLoop2 = _CtWanHDSLSNRDb1CustomerLoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 29),
    _CtWanHDSLSNRDb1CustomerLoop2_Type()
)
ctWanHDSLSNRDb1CustomerLoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRDb1CustomerLoop2.setStatus("mandatory")
_CtWanHDSLSNRLowDb1CustomerLoop2_Type = Integer32
_CtWanHDSLSNRLowDb1CustomerLoop2_Object = MibTableColumn
ctWanHDSLSNRLowDb1CustomerLoop2 = _CtWanHDSLSNRLowDb1CustomerLoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 30),
    _CtWanHDSLSNRLowDb1CustomerLoop2_Type()
)
ctWanHDSLSNRLowDb1CustomerLoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRLowDb1CustomerLoop2.setStatus("mandatory")
_CtWanHDSLSNRHighDb1CustomerLoop2_Type = Integer32
_CtWanHDSLSNRHighDb1CustomerLoop2_Object = MibTableColumn
ctWanHDSLSNRHighDb1CustomerLoop2 = _CtWanHDSLSNRHighDb1CustomerLoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 31),
    _CtWanHDSLSNRHighDb1CustomerLoop2_Type()
)
ctWanHDSLSNRHighDb1CustomerLoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRHighDb1CustomerLoop2.setStatus("mandatory")
_CtWanHDSLPulseAttenuationDb1NetworkLoop1_Type = Integer32
_CtWanHDSLPulseAttenuationDb1NetworkLoop1_Object = MibTableColumn
ctWanHDSLPulseAttenuationDb1NetworkLoop1 = _CtWanHDSLPulseAttenuationDb1NetworkLoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 32),
    _CtWanHDSLPulseAttenuationDb1NetworkLoop1_Type()
)
ctWanHDSLPulseAttenuationDb1NetworkLoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLPulseAttenuationDb1NetworkLoop1.setStatus("mandatory")
_CtWanHDSLPulseAttenuationDb1NetworkLoop2_Type = Integer32
_CtWanHDSLPulseAttenuationDb1NetworkLoop2_Object = MibTableColumn
ctWanHDSLPulseAttenuationDb1NetworkLoop2 = _CtWanHDSLPulseAttenuationDb1NetworkLoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 33),
    _CtWanHDSLPulseAttenuationDb1NetworkLoop2_Type()
)
ctWanHDSLPulseAttenuationDb1NetworkLoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLPulseAttenuationDb1NetworkLoop2.setStatus("mandatory")
_CtWanHDSLPulseAttenuationDb1CustomerLoop1_Type = Integer32
_CtWanHDSLPulseAttenuationDb1CustomerLoop1_Object = MibTableColumn
ctWanHDSLPulseAttenuationDb1CustomerLoop1 = _CtWanHDSLPulseAttenuationDb1CustomerLoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 34),
    _CtWanHDSLPulseAttenuationDb1CustomerLoop1_Type()
)
ctWanHDSLPulseAttenuationDb1CustomerLoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLPulseAttenuationDb1CustomerLoop1.setStatus("mandatory")
_CtWanHDSLPulseAttenuationDb1CustomerLoop2_Type = Integer32
_CtWanHDSLPulseAttenuationDb1CustomerLoop2_Object = MibTableColumn
ctWanHDSLPulseAttenuationDb1CustomerLoop2 = _CtWanHDSLPulseAttenuationDb1CustomerLoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 35),
    _CtWanHDSLPulseAttenuationDb1CustomerLoop2_Type()
)
ctWanHDSLPulseAttenuationDb1CustomerLoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLPulseAttenuationDb1CustomerLoop2.setStatus("mandatory")
_CtWanHDSLSNRDb2NetworkLoop1_Type = Integer32
_CtWanHDSLSNRDb2NetworkLoop1_Object = MibTableColumn
ctWanHDSLSNRDb2NetworkLoop1 = _CtWanHDSLSNRDb2NetworkLoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 36),
    _CtWanHDSLSNRDb2NetworkLoop1_Type()
)
ctWanHDSLSNRDb2NetworkLoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRDb2NetworkLoop1.setStatus("mandatory")
_CtWanHDSLSNRLowDb2NetworkLoop1_Type = Integer32
_CtWanHDSLSNRLowDb2NetworkLoop1_Object = MibTableColumn
ctWanHDSLSNRLowDb2NetworkLoop1 = _CtWanHDSLSNRLowDb2NetworkLoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 37),
    _CtWanHDSLSNRLowDb2NetworkLoop1_Type()
)
ctWanHDSLSNRLowDb2NetworkLoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRLowDb2NetworkLoop1.setStatus("mandatory")
_CtWanHDSLSNRHighDb2NetworkLoop1_Type = Integer32
_CtWanHDSLSNRHighDb2NetworkLoop1_Object = MibTableColumn
ctWanHDSLSNRHighDb2NetworkLoop1 = _CtWanHDSLSNRHighDb2NetworkLoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 38),
    _CtWanHDSLSNRHighDb2NetworkLoop1_Type()
)
ctWanHDSLSNRHighDb2NetworkLoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRHighDb2NetworkLoop1.setStatus("mandatory")
_CtWanHDSLSNRDb2NetworkLoop2_Type = Integer32
_CtWanHDSLSNRDb2NetworkLoop2_Object = MibTableColumn
ctWanHDSLSNRDb2NetworkLoop2 = _CtWanHDSLSNRDb2NetworkLoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 39),
    _CtWanHDSLSNRDb2NetworkLoop2_Type()
)
ctWanHDSLSNRDb2NetworkLoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRDb2NetworkLoop2.setStatus("mandatory")
_CtWanHDSLSNRLowDb2NetworkLoop2_Type = Integer32
_CtWanHDSLSNRLowDb2NetworkLoop2_Object = MibTableColumn
ctWanHDSLSNRLowDb2NetworkLoop2 = _CtWanHDSLSNRLowDb2NetworkLoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 40),
    _CtWanHDSLSNRLowDb2NetworkLoop2_Type()
)
ctWanHDSLSNRLowDb2NetworkLoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRLowDb2NetworkLoop2.setStatus("mandatory")
_CtWanHDSLSNRHighDb2NetworkLoop2_Type = Integer32
_CtWanHDSLSNRHighDb2NetworkLoop2_Object = MibTableColumn
ctWanHDSLSNRHighDb2NetworkLoop2 = _CtWanHDSLSNRHighDb2NetworkLoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 41),
    _CtWanHDSLSNRHighDb2NetworkLoop2_Type()
)
ctWanHDSLSNRHighDb2NetworkLoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRHighDb2NetworkLoop2.setStatus("mandatory")
_CtWanHDSLSNRDb2CustomerLoop1_Type = Integer32
_CtWanHDSLSNRDb2CustomerLoop1_Object = MibTableColumn
ctWanHDSLSNRDb2CustomerLoop1 = _CtWanHDSLSNRDb2CustomerLoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 42),
    _CtWanHDSLSNRDb2CustomerLoop1_Type()
)
ctWanHDSLSNRDb2CustomerLoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRDb2CustomerLoop1.setStatus("mandatory")
_CtWanHDSLSNRLowDb2CustomerLoop1_Type = Integer32
_CtWanHDSLSNRLowDb2CustomerLoop1_Object = MibTableColumn
ctWanHDSLSNRLowDb2CustomerLoop1 = _CtWanHDSLSNRLowDb2CustomerLoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 43),
    _CtWanHDSLSNRLowDb2CustomerLoop1_Type()
)
ctWanHDSLSNRLowDb2CustomerLoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRLowDb2CustomerLoop1.setStatus("mandatory")
_CtWanHDSLSNRHighDb2CustomerLoop1_Type = Integer32
_CtWanHDSLSNRHighDb2CustomerLoop1_Object = MibTableColumn
ctWanHDSLSNRHighDb2CustomerLoop1 = _CtWanHDSLSNRHighDb2CustomerLoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 44),
    _CtWanHDSLSNRHighDb2CustomerLoop1_Type()
)
ctWanHDSLSNRHighDb2CustomerLoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRHighDb2CustomerLoop1.setStatus("mandatory")
_CtWanHDSLSNRDb2CustomerLoop2_Type = Integer32
_CtWanHDSLSNRDb2CustomerLoop2_Object = MibTableColumn
ctWanHDSLSNRDb2CustomerLoop2 = _CtWanHDSLSNRDb2CustomerLoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 45),
    _CtWanHDSLSNRDb2CustomerLoop2_Type()
)
ctWanHDSLSNRDb2CustomerLoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRDb2CustomerLoop2.setStatus("mandatory")
_CtWanHDSLSNRLowDb2CustomerLoop2_Type = Integer32
_CtWanHDSLSNRLowDb2CustomerLoop2_Object = MibTableColumn
ctWanHDSLSNRLowDb2CustomerLoop2 = _CtWanHDSLSNRLowDb2CustomerLoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 46),
    _CtWanHDSLSNRLowDb2CustomerLoop2_Type()
)
ctWanHDSLSNRLowDb2CustomerLoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRLowDb2CustomerLoop2.setStatus("mandatory")
_CtWanHDSLSNRHighDb2CustomerLoop2_Type = Integer32
_CtWanHDSLSNRHighDb2CustomerLoop2_Object = MibTableColumn
ctWanHDSLSNRHighDb2CustomerLoop2 = _CtWanHDSLSNRHighDb2CustomerLoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 47),
    _CtWanHDSLSNRHighDb2CustomerLoop2_Type()
)
ctWanHDSLSNRHighDb2CustomerLoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLSNRHighDb2CustomerLoop2.setStatus("mandatory")
_CtWanHDSLPulseAttenuationDb2NetworkLoop1_Type = Integer32
_CtWanHDSLPulseAttenuationDb2NetworkLoop1_Object = MibTableColumn
ctWanHDSLPulseAttenuationDb2NetworkLoop1 = _CtWanHDSLPulseAttenuationDb2NetworkLoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 48),
    _CtWanHDSLPulseAttenuationDb2NetworkLoop1_Type()
)
ctWanHDSLPulseAttenuationDb2NetworkLoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLPulseAttenuationDb2NetworkLoop1.setStatus("mandatory")
_CtWanHDSLPulseAttenuationDb2NetworkLoop2_Type = Integer32
_CtWanHDSLPulseAttenuationDb2NetworkLoop2_Object = MibTableColumn
ctWanHDSLPulseAttenuationDb2NetworkLoop2 = _CtWanHDSLPulseAttenuationDb2NetworkLoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 49),
    _CtWanHDSLPulseAttenuationDb2NetworkLoop2_Type()
)
ctWanHDSLPulseAttenuationDb2NetworkLoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLPulseAttenuationDb2NetworkLoop2.setStatus("mandatory")
_CtWanHDSLPulseAttenuationDb2CustomerLoop1_Type = Integer32
_CtWanHDSLPulseAttenuationDb2CustomerLoop1_Object = MibTableColumn
ctWanHDSLPulseAttenuationDb2CustomerLoop1 = _CtWanHDSLPulseAttenuationDb2CustomerLoop1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 50),
    _CtWanHDSLPulseAttenuationDb2CustomerLoop1_Type()
)
ctWanHDSLPulseAttenuationDb2CustomerLoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLPulseAttenuationDb2CustomerLoop1.setStatus("mandatory")
_CtWanHDSLPulseAttenuationDb2CustomerLoop2_Type = Integer32
_CtWanHDSLPulseAttenuationDb2CustomerLoop2_Object = MibTableColumn
ctWanHDSLPulseAttenuationDb2CustomerLoop2 = _CtWanHDSLPulseAttenuationDb2CustomerLoop2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 3, 1, 51),
    _CtWanHDSLPulseAttenuationDb2CustomerLoop2_Type()
)
ctWanHDSLPulseAttenuationDb2CustomerLoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLPulseAttenuationDb2CustomerLoop2.setStatus("mandatory")
_CtWanHDSLTestTable_Object = MibTable
ctWanHDSLTestTable = _CtWanHDSLTestTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 4)
)
if mibBuilder.loadTexts:
    ctWanHDSLTestTable.setStatus("mandatory")
_CtWanHDSLTestEntry_Object = MibTableRow
ctWanHDSLTestEntry = _CtWanHDSLTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 4, 1)
)
ctWanHDSLTestEntry.setIndexNames(
    (0, "CTRON-WAN-MIB", "ctWanHDSLTestHLUConnIndex"),
)
if mibBuilder.loadTexts:
    ctWanHDSLTestEntry.setStatus("mandatory")
_CtWanHDSLTestHLUConnIndex_Type = Integer32
_CtWanHDSLTestHLUConnIndex_Object = MibTableColumn
ctWanHDSLTestHLUConnIndex = _CtWanHDSLTestHLUConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 4, 1, 1),
    _CtWanHDSLTestHLUConnIndex_Type()
)
ctWanHDSLTestHLUConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLTestHLUConnIndex.setStatus("mandatory")
_CtWanHDSLTestMode_Type = Integer32
_CtWanHDSLTestMode_Object = MibTableColumn
ctWanHDSLTestMode = _CtWanHDSLTestMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 4, 1, 2),
    _CtWanHDSLTestMode_Type()
)
ctWanHDSLTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctWanHDSLTestMode.setStatus("mandatory")
_CtWanHDSLHLUTestResult_Type = Integer32
_CtWanHDSLHLUTestResult_Object = MibTableColumn
ctWanHDSLHLUTestResult = _CtWanHDSLHLUTestResult_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 4, 1, 3),
    _CtWanHDSLHLUTestResult_Type()
)
ctWanHDSLHLUTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLHLUTestResult.setStatus("mandatory")
_CtWanHDSLHRUTestResult_Type = Integer32
_CtWanHDSLHRUTestResult_Object = MibTableColumn
ctWanHDSLHRUTestResult = _CtWanHDSLHRUTestResult_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 4, 1, 4),
    _CtWanHDSLHRUTestResult_Type()
)
ctWanHDSLHRUTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLHRUTestResult.setStatus("mandatory")
_CtWanHDSLAlarmsTable_Object = MibTable
ctWanHDSLAlarmsTable = _CtWanHDSLAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 5)
)
if mibBuilder.loadTexts:
    ctWanHDSLAlarmsTable.setStatus("mandatory")
_CtWanHDSLAlarmsEntry_Object = MibTableRow
ctWanHDSLAlarmsEntry = _CtWanHDSLAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 5, 1)
)
ctWanHDSLAlarmsEntry.setIndexNames(
    (0, "CTRON-WAN-MIB", "ctWanHDSLAlarmsHLUConnIndex"),
)
if mibBuilder.loadTexts:
    ctWanHDSLAlarmsEntry.setStatus("mandatory")
_CtWanHDSLAlarmsHLUConnIndex_Type = Integer32
_CtWanHDSLAlarmsHLUConnIndex_Object = MibTableColumn
ctWanHDSLAlarmsHLUConnIndex = _CtWanHDSLAlarmsHLUConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 5, 1, 1),
    _CtWanHDSLAlarmsHLUConnIndex_Type()
)
ctWanHDSLAlarmsHLUConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlarmsHLUConnIndex.setStatus("mandatory")
_CtWanHDSLAlarmsBackplane_Type = Integer32
_CtWanHDSLAlarmsBackplane_Object = MibTableColumn
ctWanHDSLAlarmsBackplane = _CtWanHDSLAlarmsBackplane_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 5, 1, 2),
    _CtWanHDSLAlarmsBackplane_Type()
)
ctWanHDSLAlarmsBackplane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlarmsBackplane.setStatus("mandatory")
_CtWanHDSLAlarmsES_Type = Integer32
_CtWanHDSLAlarmsES_Object = MibTableColumn
ctWanHDSLAlarmsES = _CtWanHDSLAlarmsES_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 5, 1, 3),
    _CtWanHDSLAlarmsES_Type()
)
ctWanHDSLAlarmsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlarmsES.setStatus("mandatory")
_CtWanHDSLAlarmHistoryTable_Object = MibTable
ctWanHDSLAlarmHistoryTable = _CtWanHDSLAlarmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6)
)
if mibBuilder.loadTexts:
    ctWanHDSLAlarmHistoryTable.setStatus("mandatory")
_CtWanHDSLAlarmHistoryEntry_Object = MibTableRow
ctWanHDSLAlarmHistoryEntry = _CtWanHDSLAlarmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1)
)
ctWanHDSLAlarmHistoryEntry.setIndexNames(
    (0, "CTRON-WAN-MIB", "ctWanHDSLAlarmHistoryConnIndex"),
)
if mibBuilder.loadTexts:
    ctWanHDSLAlarmHistoryEntry.setStatus("mandatory")
_CtWanHDSLAlarmHistoryConnIndex_Type = Integer32
_CtWanHDSLAlarmHistoryConnIndex_Object = MibTableColumn
ctWanHDSLAlarmHistoryConnIndex = _CtWanHDSLAlarmHistoryConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 1),
    _CtWanHDSLAlarmHistoryConnIndex_Type()
)
ctWanHDSLAlarmHistoryConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlarmHistoryConnIndex.setStatus("mandatory")


class _CtWanHDSLAlHistLLOSFirst_Type(DisplayString):
    """Custom type ctWanHDSLAlHistLLOSFirst based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtWanHDSLAlHistLLOSFirst_Type.__name__ = "DisplayString"
_CtWanHDSLAlHistLLOSFirst_Object = MibTableColumn
ctWanHDSLAlHistLLOSFirst = _CtWanHDSLAlHistLLOSFirst_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 2),
    _CtWanHDSLAlHistLLOSFirst_Type()
)
ctWanHDSLAlHistLLOSFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistLLOSFirst.setStatus("mandatory")


class _CtWanHDSLAlHistLLOSLast_Type(DisplayString):
    """Custom type ctWanHDSLAlHistLLOSLast based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtWanHDSLAlHistLLOSLast_Type.__name__ = "DisplayString"
_CtWanHDSLAlHistLLOSLast_Object = MibTableColumn
ctWanHDSLAlHistLLOSLast = _CtWanHDSLAlHistLLOSLast_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 3),
    _CtWanHDSLAlHistLLOSLast_Type()
)
ctWanHDSLAlHistLLOSLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistLLOSLast.setStatus("mandatory")
_CtWanHDSLAlHistLLOSCurrent_Type = Integer32
_CtWanHDSLAlHistLLOSCurrent_Object = MibTableColumn
ctWanHDSLAlHistLLOSCurrent = _CtWanHDSLAlHistLLOSCurrent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 4),
    _CtWanHDSLAlHistLLOSCurrent_Type()
)
ctWanHDSLAlHistLLOSCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistLLOSCurrent.setStatus("mandatory")
_CtWanHDSLAlHistLLOSCount_Type = Integer32
_CtWanHDSLAlHistLLOSCount_Object = MibTableColumn
ctWanHDSLAlHistLLOSCount = _CtWanHDSLAlHistLLOSCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 5),
    _CtWanHDSLAlHistLLOSCount_Type()
)
ctWanHDSLAlHistLLOSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistLLOSCount.setStatus("mandatory")


class _CtWanHDSLAlHistRLOSFirst_Type(DisplayString):
    """Custom type ctWanHDSLAlHistRLOSFirst based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtWanHDSLAlHistRLOSFirst_Type.__name__ = "DisplayString"
_CtWanHDSLAlHistRLOSFirst_Object = MibTableColumn
ctWanHDSLAlHistRLOSFirst = _CtWanHDSLAlHistRLOSFirst_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 6),
    _CtWanHDSLAlHistRLOSFirst_Type()
)
ctWanHDSLAlHistRLOSFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistRLOSFirst.setStatus("mandatory")


class _CtWanHDSLAlHistRLOSLast_Type(DisplayString):
    """Custom type ctWanHDSLAlHistRLOSLast based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtWanHDSLAlHistRLOSLast_Type.__name__ = "DisplayString"
_CtWanHDSLAlHistRLOSLast_Object = MibTableColumn
ctWanHDSLAlHistRLOSLast = _CtWanHDSLAlHistRLOSLast_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 7),
    _CtWanHDSLAlHistRLOSLast_Type()
)
ctWanHDSLAlHistRLOSLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistRLOSLast.setStatus("mandatory")
_CtWanHDSLAlHistRLOSCurrent_Type = Integer32
_CtWanHDSLAlHistRLOSCurrent_Object = MibTableColumn
ctWanHDSLAlHistRLOSCurrent = _CtWanHDSLAlHistRLOSCurrent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 8),
    _CtWanHDSLAlHistRLOSCurrent_Type()
)
ctWanHDSLAlHistRLOSCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistRLOSCurrent.setStatus("mandatory")
_CtWanHDSLAlHistRLOSCount_Type = Integer32
_CtWanHDSLAlHistRLOSCount_Object = MibTableColumn
ctWanHDSLAlHistRLOSCount = _CtWanHDSLAlHistRLOSCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 9),
    _CtWanHDSLAlHistRLOSCount_Type()
)
ctWanHDSLAlHistRLOSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistRLOSCount.setStatus("mandatory")


class _CtWanHDSLAlHistLOSW1First_Type(DisplayString):
    """Custom type ctWanHDSLAlHistLOSW1First based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtWanHDSLAlHistLOSW1First_Type.__name__ = "DisplayString"
_CtWanHDSLAlHistLOSW1First_Object = MibTableColumn
ctWanHDSLAlHistLOSW1First = _CtWanHDSLAlHistLOSW1First_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 10),
    _CtWanHDSLAlHistLOSW1First_Type()
)
ctWanHDSLAlHistLOSW1First.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistLOSW1First.setStatus("mandatory")


class _CtWanHDSLAlHistLOSW1Last_Type(DisplayString):
    """Custom type ctWanHDSLAlHistLOSW1Last based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtWanHDSLAlHistLOSW1Last_Type.__name__ = "DisplayString"
_CtWanHDSLAlHistLOSW1Last_Object = MibTableColumn
ctWanHDSLAlHistLOSW1Last = _CtWanHDSLAlHistLOSW1Last_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 11),
    _CtWanHDSLAlHistLOSW1Last_Type()
)
ctWanHDSLAlHistLOSW1Last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistLOSW1Last.setStatus("mandatory")
_CtWanHDSLAlHistLOSW1Current_Type = Integer32
_CtWanHDSLAlHistLOSW1Current_Object = MibTableColumn
ctWanHDSLAlHistLOSW1Current = _CtWanHDSLAlHistLOSW1Current_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 12),
    _CtWanHDSLAlHistLOSW1Current_Type()
)
ctWanHDSLAlHistLOSW1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistLOSW1Current.setStatus("mandatory")
_CtWanHDSLAlHistLOSW1Count_Type = Integer32
_CtWanHDSLAlHistLOSW1Count_Object = MibTableColumn
ctWanHDSLAlHistLOSW1Count = _CtWanHDSLAlHistLOSW1Count_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 13),
    _CtWanHDSLAlHistLOSW1Count_Type()
)
ctWanHDSLAlHistLOSW1Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistLOSW1Count.setStatus("mandatory")


class _CtWanHDSLAlHistLOSW2First_Type(DisplayString):
    """Custom type ctWanHDSLAlHistLOSW2First based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtWanHDSLAlHistLOSW2First_Type.__name__ = "DisplayString"
_CtWanHDSLAlHistLOSW2First_Object = MibTableColumn
ctWanHDSLAlHistLOSW2First = _CtWanHDSLAlHistLOSW2First_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 14),
    _CtWanHDSLAlHistLOSW2First_Type()
)
ctWanHDSLAlHistLOSW2First.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistLOSW2First.setStatus("mandatory")


class _CtWanHDSLAlHistLOSW2Last_Type(DisplayString):
    """Custom type ctWanHDSLAlHistLOSW2Last based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtWanHDSLAlHistLOSW2Last_Type.__name__ = "DisplayString"
_CtWanHDSLAlHistLOSW2Last_Object = MibTableColumn
ctWanHDSLAlHistLOSW2Last = _CtWanHDSLAlHistLOSW2Last_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 15),
    _CtWanHDSLAlHistLOSW2Last_Type()
)
ctWanHDSLAlHistLOSW2Last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistLOSW2Last.setStatus("mandatory")
_CtWanHDSLAlHistLOSW2Current_Type = Integer32
_CtWanHDSLAlHistLOSW2Current_Object = MibTableColumn
ctWanHDSLAlHistLOSW2Current = _CtWanHDSLAlHistLOSW2Current_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 16),
    _CtWanHDSLAlHistLOSW2Current_Type()
)
ctWanHDSLAlHistLOSW2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistLOSW2Current.setStatus("mandatory")
_CtWanHDSLAlHistLOSW2Count_Type = Integer32
_CtWanHDSLAlHistLOSW2Count_Object = MibTableColumn
ctWanHDSLAlHistLOSW2Count = _CtWanHDSLAlHistLOSW2Count_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 17),
    _CtWanHDSLAlHistLOSW2Count_Type()
)
ctWanHDSLAlHistLOSW2Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistLOSW2Count.setStatus("mandatory")


class _CtWanHDSLAlHistES1First_Type(DisplayString):
    """Custom type ctWanHDSLAlHistES1First based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtWanHDSLAlHistES1First_Type.__name__ = "DisplayString"
_CtWanHDSLAlHistES1First_Object = MibTableColumn
ctWanHDSLAlHistES1First = _CtWanHDSLAlHistES1First_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 18),
    _CtWanHDSLAlHistES1First_Type()
)
ctWanHDSLAlHistES1First.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistES1First.setStatus("mandatory")


class _CtWanHDSLAlHistES1Last_Type(DisplayString):
    """Custom type ctWanHDSLAlHistES1Last based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtWanHDSLAlHistES1Last_Type.__name__ = "DisplayString"
_CtWanHDSLAlHistES1Last_Object = MibTableColumn
ctWanHDSLAlHistES1Last = _CtWanHDSLAlHistES1Last_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 19),
    _CtWanHDSLAlHistES1Last_Type()
)
ctWanHDSLAlHistES1Last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistES1Last.setStatus("mandatory")
_CtWanHDSLAlHistES1Current_Type = Integer32
_CtWanHDSLAlHistES1Current_Object = MibTableColumn
ctWanHDSLAlHistES1Current = _CtWanHDSLAlHistES1Current_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 20),
    _CtWanHDSLAlHistES1Current_Type()
)
ctWanHDSLAlHistES1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistES1Current.setStatus("mandatory")
_CtWanHDSLAlHistES1Count_Type = Integer32
_CtWanHDSLAlHistES1Count_Object = MibTableColumn
ctWanHDSLAlHistES1Count = _CtWanHDSLAlHistES1Count_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 21),
    _CtWanHDSLAlHistES1Count_Type()
)
ctWanHDSLAlHistES1Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistES1Count.setStatus("mandatory")


class _CtWanHDSLAlHistES2First_Type(DisplayString):
    """Custom type ctWanHDSLAlHistES2First based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtWanHDSLAlHistES2First_Type.__name__ = "DisplayString"
_CtWanHDSLAlHistES2First_Object = MibTableColumn
ctWanHDSLAlHistES2First = _CtWanHDSLAlHistES2First_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 22),
    _CtWanHDSLAlHistES2First_Type()
)
ctWanHDSLAlHistES2First.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistES2First.setStatus("mandatory")


class _CtWanHDSLAlHistES2Last_Type(DisplayString):
    """Custom type ctWanHDSLAlHistES2Last based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtWanHDSLAlHistES2Last_Type.__name__ = "DisplayString"
_CtWanHDSLAlHistES2Last_Object = MibTableColumn
ctWanHDSLAlHistES2Last = _CtWanHDSLAlHistES2Last_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 23),
    _CtWanHDSLAlHistES2Last_Type()
)
ctWanHDSLAlHistES2Last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistES2Last.setStatus("mandatory")
_CtWanHDSLAlHistES2Current_Type = Integer32
_CtWanHDSLAlHistES2Current_Object = MibTableColumn
ctWanHDSLAlHistES2Current = _CtWanHDSLAlHistES2Current_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 24),
    _CtWanHDSLAlHistES2Current_Type()
)
ctWanHDSLAlHistES2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistES2Current.setStatus("mandatory")
_CtWanHDSLAlHistES2Count_Type = Integer32
_CtWanHDSLAlHistES2Count_Object = MibTableColumn
ctWanHDSLAlHistES2Count = _CtWanHDSLAlHistES2Count_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 25),
    _CtWanHDSLAlHistES2Count_Type()
)
ctWanHDSLAlHistES2Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistES2Count.setStatus("mandatory")


class _CtWanHDSLAlHistMargin1First_Type(DisplayString):
    """Custom type ctWanHDSLAlHistMargin1First based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtWanHDSLAlHistMargin1First_Type.__name__ = "DisplayString"
_CtWanHDSLAlHistMargin1First_Object = MibTableColumn
ctWanHDSLAlHistMargin1First = _CtWanHDSLAlHistMargin1First_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 26),
    _CtWanHDSLAlHistMargin1First_Type()
)
ctWanHDSLAlHistMargin1First.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistMargin1First.setStatus("mandatory")


class _CtWanHDSLAlHistMargin1Last_Type(DisplayString):
    """Custom type ctWanHDSLAlHistMargin1Last based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtWanHDSLAlHistMargin1Last_Type.__name__ = "DisplayString"
_CtWanHDSLAlHistMargin1Last_Object = MibTableColumn
ctWanHDSLAlHistMargin1Last = _CtWanHDSLAlHistMargin1Last_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 27),
    _CtWanHDSLAlHistMargin1Last_Type()
)
ctWanHDSLAlHistMargin1Last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistMargin1Last.setStatus("mandatory")
_CtWanHDSLAlHistMargin1Current_Type = Integer32
_CtWanHDSLAlHistMargin1Current_Object = MibTableColumn
ctWanHDSLAlHistMargin1Current = _CtWanHDSLAlHistMargin1Current_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 28),
    _CtWanHDSLAlHistMargin1Current_Type()
)
ctWanHDSLAlHistMargin1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistMargin1Current.setStatus("mandatory")
_CtWanHDSLAlHistMargin1Count_Type = Integer32
_CtWanHDSLAlHistMargin1Count_Object = MibTableColumn
ctWanHDSLAlHistMargin1Count = _CtWanHDSLAlHistMargin1Count_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 29),
    _CtWanHDSLAlHistMargin1Count_Type()
)
ctWanHDSLAlHistMargin1Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistMargin1Count.setStatus("mandatory")


class _CtWanHDSLAlHistMargin2First_Type(DisplayString):
    """Custom type ctWanHDSLAlHistMargin2First based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtWanHDSLAlHistMargin2First_Type.__name__ = "DisplayString"
_CtWanHDSLAlHistMargin2First_Object = MibTableColumn
ctWanHDSLAlHistMargin2First = _CtWanHDSLAlHistMargin2First_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 30),
    _CtWanHDSLAlHistMargin2First_Type()
)
ctWanHDSLAlHistMargin2First.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistMargin2First.setStatus("mandatory")


class _CtWanHDSLAlHistMargin2Last_Type(DisplayString):
    """Custom type ctWanHDSLAlHistMargin2Last based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtWanHDSLAlHistMargin2Last_Type.__name__ = "DisplayString"
_CtWanHDSLAlHistMargin2Last_Object = MibTableColumn
ctWanHDSLAlHistMargin2Last = _CtWanHDSLAlHistMargin2Last_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 31),
    _CtWanHDSLAlHistMargin2Last_Type()
)
ctWanHDSLAlHistMargin2Last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistMargin2Last.setStatus("mandatory")
_CtWanHDSLAlHistMargin2Current_Type = Integer32
_CtWanHDSLAlHistMargin2Current_Object = MibTableColumn
ctWanHDSLAlHistMargin2Current = _CtWanHDSLAlHistMargin2Current_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 32),
    _CtWanHDSLAlHistMargin2Current_Type()
)
ctWanHDSLAlHistMargin2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistMargin2Current.setStatus("mandatory")
_CtWanHDSLAlHistMargin2Count_Type = Integer32
_CtWanHDSLAlHistMargin2Count_Object = MibTableColumn
ctWanHDSLAlHistMargin2Count = _CtWanHDSLAlHistMargin2Count_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 33),
    _CtWanHDSLAlHistMargin2Count_Type()
)
ctWanHDSLAlHistMargin2Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistMargin2Count.setStatus("mandatory")


class _CtWanHDSLAlHistCleared_Type(DisplayString):
    """Custom type ctWanHDSLAlHistCleared based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtWanHDSLAlHistCleared_Type.__name__ = "DisplayString"
_CtWanHDSLAlHistCleared_Object = MibTableColumn
ctWanHDSLAlHistCleared = _CtWanHDSLAlHistCleared_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 34),
    _CtWanHDSLAlHistCleared_Type()
)
ctWanHDSLAlHistCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistCleared.setStatus("mandatory")
_CtWanHDSLAlHistClearit_Type = Integer32
_CtWanHDSLAlHistClearit_Object = MibTableColumn
ctWanHDSLAlHistClearit = _CtWanHDSLAlHistClearit_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 6, 1, 35),
    _CtWanHDSLAlHistClearit_Type()
)
ctWanHDSLAlHistClearit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctWanHDSLAlHistClearit.setStatus("mandatory")
_CtWanHDSLLoopbacksTable_Object = MibTable
ctWanHDSLLoopbacksTable = _CtWanHDSLLoopbacksTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 7)
)
if mibBuilder.loadTexts:
    ctWanHDSLLoopbacksTable.setStatus("mandatory")
_CtWanHDSLLoopbacksEntry_Object = MibTableRow
ctWanHDSLLoopbacksEntry = _CtWanHDSLLoopbacksEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 7, 1)
)
ctWanHDSLLoopbacksEntry.setIndexNames(
    (0, "CTRON-WAN-MIB", "ctWanHDSLLoopbacksHLUConnIndex"),
)
if mibBuilder.loadTexts:
    ctWanHDSLLoopbacksEntry.setStatus("mandatory")
_CtWanHDSLLoopbacksHLUConnIndex_Type = Integer32
_CtWanHDSLLoopbacksHLUConnIndex_Object = MibTableColumn
ctWanHDSLLoopbacksHLUConnIndex = _CtWanHDSLLoopbacksHLUConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 7, 1, 1),
    _CtWanHDSLLoopbacksHLUConnIndex_Type()
)
ctWanHDSLLoopbacksHLUConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLLoopbacksHLUConnIndex.setStatus("mandatory")
_CtWanHDSLLoopbacksAdminType_Type = Integer32
_CtWanHDSLLoopbacksAdminType_Object = MibTableColumn
ctWanHDSLLoopbacksAdminType = _CtWanHDSLLoopbacksAdminType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 7, 1, 2),
    _CtWanHDSLLoopbacksAdminType_Type()
)
ctWanHDSLLoopbacksAdminType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctWanHDSLLoopbacksAdminType.setStatus("mandatory")
_CtWanHDSLLoopbacksOperType_Type = Integer32
_CtWanHDSLLoopbacksOperType_Object = MibTableColumn
ctWanHDSLLoopbacksOperType = _CtWanHDSLLoopbacksOperType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1, 8, 7, 1, 3),
    _CtWanHDSLLoopbacksOperType_Type()
)
ctWanHDSLLoopbacksOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanHDSLLoopbacksOperType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-WAN-MIB",
    **{"Index": Index,
       "DLCI": DLCI,
       "ctWanConnection": ctWanConnection,
       "wanNumConnections": wanNumConnections,
       "wanConnTable": wanConnTable,
       "wanConnEntry": wanConnEntry,
       "wanConnIndex": wanConnIndex,
       "wanConnNumPhysPorts": wanConnNumPhysPorts,
       "wanConnDefaultPhysPort": wanConnDefaultPhysPort,
       "wanConnActivePhysPort": wanConnActivePhysPort,
       "wanPhysPortTable": wanPhysPortTable,
       "wanPhysPortEntry": wanPhysPortEntry,
       "wanPhysPortConnectionIndex": wanPhysPortConnectionIndex,
       "wanPhysPortIndex": wanPhysPortIndex,
       "wanPhysPortType": wanPhysPortType,
       "wanPhysPortSpecificMib": wanPhysPortSpecificMib,
       "wanInterfaceTable": wanInterfaceTable,
       "wanInterfaceEntry": wanInterfaceEntry,
       "wanInterfaceConnectionIndex": wanInterfaceConnectionIndex,
       "wanInterfacePhysPortIndex": wanInterfacePhysPortIndex,
       "wanInterfaceEntryIndex": wanInterfaceEntryIndex,
       "wanInterfaceEntryIfIndex": wanInterfaceEntryIfIndex,
       "wanInterfaceEntryProtocol": wanInterfaceEntryProtocol,
       "wanInterfaceEntryCompression": wanInterfaceEntryCompression,
       "wanInterfaceEntryMTU": wanInterfaceEntryMTU,
       "wanInterfaceEntryLineCoding": wanInterfaceEntryLineCoding,
       "wanInterfaceEntryCrcLength": wanInterfaceEntryCrcLength,
       "wanInterfaceEntryLexProtocolEnable": wanInterfaceEntryLexProtocolEnable,
       "wanInterfaceEntryLexProtocolStatus": wanInterfaceEntryLexProtocolStatus,
       "wanInterfaceEntryCompRatio": wanInterfaceEntryCompRatio,
       "wanInterfaceEntryCompStatus": wanInterfaceEntryCompStatus,
       "wanInterfaceEntryBackUpIfEnable": wanInterfaceEntryBackUpIfEnable,
       "ctWanDs1": ctWanDs1,
       "wanDs1ExtensionsTable": wanDs1ExtensionsTable,
       "wanDs1ExtensionsEntry": wanDs1ExtensionsEntry,
       "wanDs1ExtensionsEntryIndex": wanDs1ExtensionsEntryIndex,
       "wanDs1ExtensionsNumInterfaces": wanDs1ExtensionsNumInterfaces,
       "wanDs1ExtensionsToggleFracTable": wanDs1ExtensionsToggleFracTable,
       "wanDs1ExtensionsLineBuildOut": wanDs1ExtensionsLineBuildOut,
       "wanDs1ExtensionsCFADuration": wanDs1ExtensionsCFADuration,
       "wanDs1ExtensionsDIEnable": wanDs1ExtensionsDIEnable,
       "wanDs1ExtensionsTotalValidIntervals": wanDs1ExtensionsTotalValidIntervals,
       "wanDs1ExtensionsBertTestMode": wanDs1ExtensionsBertTestMode,
       "wanDs1ExtensionsBertRun": wanDs1ExtensionsBertRun,
       "wanDs1ExtensionsBertCurrentResults": wanDs1ExtensionsBertCurrentResults,
       "wanDs1ExtensionsBertCumulativeResults": wanDs1ExtensionsBertCumulativeResults,
       "wanDs1ExtensionsBertPeakResults": wanDs1ExtensionsBertPeakResults,
       "wanDs1ExtensionsBertAverageResult": wanDs1ExtensionsBertAverageResult,
       "wanDs1ExtensionsBertTestPattern": wanDs1ExtensionsBertTestPattern,
       "wanDs1ExtensionsBertSamplePeriod": wanDs1ExtensionsBertSamplePeriod,
       "wanDs1ExtensionsBertNumPeriods": wanDs1ExtensionsBertNumPeriods,
       "wanDs1ExtensionsBertTestTraps": wanDs1ExtensionsBertTestTraps,
       "wanDs1ExtensionsBertDataStatus": wanDs1ExtensionsBertDataStatus,
       "ctWanRs232": ctWanRs232,
       "wanRs232ExtensionsTable": wanRs232ExtensionsTable,
       "wanRs232ExtensionsEntry": wanRs232ExtensionsEntry,
       "wanRs232ExtensionsEntryIndex": wanRs232ExtensionsEntryIndex,
       "wanRs232ExtensionsCTSEnable": wanRs232ExtensionsCTSEnable,
       "wanRs232ExtensionsDSREnable": wanRs232ExtensionsDSREnable,
       "ctFrDcp": ctFrDcp,
       "frDcpCircuitTable": frDcpCircuitTable,
       "frDcpCircuitEntry": frDcpCircuitEntry,
       "frDcpCircuitIfIndex": frDcpCircuitIfIndex,
       "frDcpCircuitDlci": frDcpCircuitDlci,
       "frDcpCircuitEnable": frDcpCircuitEnable,
       "frDcpCircuitStatus": frDcpCircuitStatus,
       "frDcpCircuitRatio": frDcpCircuitRatio,
       "ctDDS": ctDDS,
       "ddsConfigTable": ddsConfigTable,
       "ddsConfigEntry": ddsConfigEntry,
       "ddsLineIndex": ddsLineIndex,
       "ddsIfIndex": ddsIfIndex,
       "ddsLineMode": ddsLineMode,
       "ddsLineCoding": ddsLineCoding,
       "ddsLoopbackConfig": ddsLoopbackConfig,
       "ddsLineStatus": ddsLineStatus,
       "ddsTxClockSource": ddsTxClockSource,
       "ddsPortInSpeed": ddsPortInSpeed,
       "ddsPortOutSpeed": ddsPortOutSpeed,
       "ctDs1Alarms": ctDs1Alarms,
       "ds1AlarmsGlobalConfigGroup": ds1AlarmsGlobalConfigGroup,
       "ds1AlarmGlobalAdmin": ds1AlarmGlobalAdmin,
       "ds1AlarmGlobalAutoRecovery": ds1AlarmGlobalAutoRecovery,
       "ds1AlarmGlobalTrapEnable": ds1AlarmGlobalTrapEnable,
       "ds1AlarmGlobalESCount": ds1AlarmGlobalESCount,
       "ds1AlarmGlobalESInterval": ds1AlarmGlobalESInterval,
       "ds1AlarmGlobalBPVErrorRate": ds1AlarmGlobalBPVErrorRate,
       "ds1AlarmGlobalBPVInterval": ds1AlarmGlobalBPVInterval,
       "ds1AlarmGlobalManualRecovery": ds1AlarmGlobalManualRecovery,
       "ds1AlarmConfigTable": ds1AlarmConfigTable,
       "ds1AlarmConfigEntry": ds1AlarmConfigEntry,
       "ds1PhysNum": ds1PhysNum,
       "ds1AlarmAdmin": ds1AlarmAdmin,
       "ds1AlarmAutoRecovery": ds1AlarmAutoRecovery,
       "ds1AlarmTrapEnable": ds1AlarmTrapEnable,
       "ds1AlarmESCount": ds1AlarmESCount,
       "ds1AlarmESInterval": ds1AlarmESInterval,
       "ds1AlarmBPVErrorRate": ds1AlarmBPVErrorRate,
       "ds1AlarmBPVInterval": ds1AlarmBPVInterval,
       "ds1AlarmManualRecovery": ds1AlarmManualRecovery,
       "ctIPPQFilters": ctIPPQFilters,
       "ipPQConfigGroup": ipPQConfigGroup,
       "ipPQAdmin": ipPQAdmin,
       "iPPQMaxEntries": iPPQMaxEntries,
       "iPPQNumEntries": iPPQNumEntries,
       "iPPQAddAddress": iPPQAddAddress,
       "iPPQDelAddress": iPPQDelAddress,
       "ipPQAddressTable": ipPQAddressTable,
       "ipPQAddressEntry": ipPQAddressEntry,
       "ipPQAddressId": ipPQAddressId,
       "ipPQIPAddress": ipPQIPAddress,
       "ctWanHDSLExt": ctWanHDSLExt,
       "ctWanHDSLPerformance15mTable": ctWanHDSLPerformance15mTable,
       "ctWanHDSLPerformance15mEntry": ctWanHDSLPerformance15mEntry,
       "ctWanHDSLPerformance15mConnIndex": ctWanHDSLPerformance15mConnIndex,
       "ctWanHDSLPerformance15mSlotIndex": ctWanHDSLPerformance15mSlotIndex,
       "ctWanHDSLHLULoop1UAS15m": ctWanHDSLHLULoop1UAS15m,
       "ctWanHDSLHLULoop1ES15m": ctWanHDSLHLULoop1ES15m,
       "ctWanHDSLHLULoop2UAS15m": ctWanHDSLHLULoop2UAS15m,
       "ctWanHDSLHLULoop2ES15m": ctWanHDSLHLULoop2ES15m,
       "ctWanHDSLHRULoop1UAS15m": ctWanHDSLHRULoop1UAS15m,
       "ctWanHDSLHRULoop1ES15m": ctWanHDSLHRULoop1ES15m,
       "ctWanHDSLHRULoop2UAS15m": ctWanHDSLHRULoop2UAS15m,
       "ctWanHDSLHRULoop2ES15m": ctWanHDSLHRULoop2ES15m,
       "ctWanHDSLDb1NetworkLoop1UAS15m": ctWanHDSLDb1NetworkLoop1UAS15m,
       "ctWanHDSLDb1NetworkLoop1ES15m": ctWanHDSLDb1NetworkLoop1ES15m,
       "ctWanHDSLDb1NetworkLoop2UAS15m": ctWanHDSLDb1NetworkLoop2UAS15m,
       "ctWanHDSLDb1NetworkLoop2ES15m": ctWanHDSLDb1NetworkLoop2ES15m,
       "ctWanHDSLDb1CustomerLoop1UAS15m": ctWanHDSLDb1CustomerLoop1UAS15m,
       "ctWanHDSLDb1CustomerLoop1ES15m": ctWanHDSLDb1CustomerLoop1ES15m,
       "ctWanHDSLDb1CustomerLoop2UAS15m": ctWanHDSLDb1CustomerLoop2UAS15m,
       "ctWanHDSLDb1CustomerLoop2ES15m": ctWanHDSLDb1CustomerLoop2ES15m,
       "ctWanHDSLDb2NetworkLoop1UAS15m": ctWanHDSLDb2NetworkLoop1UAS15m,
       "ctWanHDSLDb2NetworkLoop1ES15m": ctWanHDSLDb2NetworkLoop1ES15m,
       "ctWanHDSLDb2NetworkLoop2UAS15m": ctWanHDSLDb2NetworkLoop2UAS15m,
       "ctWanHDSLDb2NetworkLoop2ES15m": ctWanHDSLDb2NetworkLoop2ES15m,
       "ctWanHDSLDb2CustomerLoop1UAS15m": ctWanHDSLDb2CustomerLoop1UAS15m,
       "ctWanHDSLDb2CustomerLoop1ES15m": ctWanHDSLDb2CustomerLoop1ES15m,
       "ctWanHDSLDb2CustomerLoop2UAS15m": ctWanHDSLDb2CustomerLoop2UAS15m,
       "ctWanHDSLDb2CustomerLoop2ES15m": ctWanHDSLDb2CustomerLoop2ES15m,
       "ctWanHDSLPerformance24hTable": ctWanHDSLPerformance24hTable,
       "ctWanHDSLPerformance24hEntry": ctWanHDSLPerformance24hEntry,
       "ctWanHDSLPerformance24hConnIndex": ctWanHDSLPerformance24hConnIndex,
       "ctWanHDSLPerformance24hSlotIndex": ctWanHDSLPerformance24hSlotIndex,
       "ctWanHDSLHLULoop1UAS24h": ctWanHDSLHLULoop1UAS24h,
       "ctWanHDSLHLULoop1ES24h": ctWanHDSLHLULoop1ES24h,
       "ctWanHDSLHLULoop2UAS24h": ctWanHDSLHLULoop2UAS24h,
       "ctWanHDSLHLULoop2ES24h": ctWanHDSLHLULoop2ES24h,
       "ctWanHDSLHRULoop1UAS24h": ctWanHDSLHRULoop1UAS24h,
       "ctWanHDSLHRULoop1ES24h": ctWanHDSLHRULoop1ES24h,
       "ctWanHDSLHRULoop2UAS24h": ctWanHDSLHRULoop2UAS24h,
       "ctWanHDSLHRULoop2ES24h": ctWanHDSLHRULoop2ES24h,
       "ctWanHDSLDb1NetworkLoop1UAS24h": ctWanHDSLDb1NetworkLoop1UAS24h,
       "ctWanHDSLDb1NetworkLoop1ES24h": ctWanHDSLDb1NetworkLoop1ES24h,
       "ctWanHDSLDb1NetworkLoop2UAS24h": ctWanHDSLDb1NetworkLoop2UAS24h,
       "ctWanHDSLDb1NetworkLoop2ES24h": ctWanHDSLDb1NetworkLoop2ES24h,
       "ctWanHDSLDb1CustomerLoop1UAS24h": ctWanHDSLDb1CustomerLoop1UAS24h,
       "ctWanHDSLDb1CustomerLoop1ES24h": ctWanHDSLDb1CustomerLoop1ES24h,
       "ctWanHDSLDb1CustomerLoop2UAS24h": ctWanHDSLDb1CustomerLoop2UAS24h,
       "ctWanHDSLDb1CustomerLoop2ES24h": ctWanHDSLDb1CustomerLoop2ES24h,
       "ctWanHDSLDb2NetworkLoop1UAS24h": ctWanHDSLDb2NetworkLoop1UAS24h,
       "ctWanHDSLDb2NetworkLoop1ES24h": ctWanHDSLDb2NetworkLoop1ES24h,
       "ctWanHDSLDb2NetworkLoop2UAS24h": ctWanHDSLDb2NetworkLoop2UAS24h,
       "ctWanHDSLDb2NetworkLoop2ES24h": ctWanHDSLDb2NetworkLoop2ES24h,
       "ctWanHDSLDb2CustomerLoop1UAS24h": ctWanHDSLDb2CustomerLoop1UAS24h,
       "ctWanHDSLDb2CustomerLoop1ES24h": ctWanHDSLDb2CustomerLoop1ES24h,
       "ctWanHDSLDb2CustomerLoop2UAS24h": ctWanHDSLDb2CustomerLoop2UAS24h,
       "ctWanHDSLDb2CustomerLoop2ES24h": ctWanHDSLDb2CustomerLoop2ES24h,
       "ctWanHDSLStatisticsTable": ctWanHDSLStatisticsTable,
       "ctWanHDSLStatisticsEntry": ctWanHDSLStatisticsEntry,
       "ctWanHDSLStatisticsHLUConnIndex": ctWanHDSLStatisticsHLUConnIndex,
       "ctWanHDSLSNRHLULoop1": ctWanHDSLSNRHLULoop1,
       "ctWanHDSLSNRLowHLULoop1": ctWanHDSLSNRLowHLULoop1,
       "ctWanHDSLSNRHighHLULoop1": ctWanHDSLSNRHighHLULoop1,
       "ctWanHDSLSNRHLULoop2": ctWanHDSLSNRHLULoop2,
       "ctWanHDSLSNRLowHLULoop2": ctWanHDSLSNRLowHLULoop2,
       "ctWanHDSLSNRHighHLULoop2": ctWanHDSLSNRHighHLULoop2,
       "ctWanHDSLPulseAttenuationHLULoop1": ctWanHDSLPulseAttenuationHLULoop1,
       "ctWanHDSLPulseAttenuationHLULoop2": ctWanHDSLPulseAttenuationHLULoop2,
       "ctWanHDSLBitStat1HLU": ctWanHDSLBitStat1HLU,
       "ctWanHDSLSNRHRULoop1": ctWanHDSLSNRHRULoop1,
       "ctWanHDSLSNRLowHRULoop1": ctWanHDSLSNRLowHRULoop1,
       "ctWanHDSLSNRHighHRULoop1": ctWanHDSLSNRHighHRULoop1,
       "ctWanHDSLSNRHRULoop2": ctWanHDSLSNRHRULoop2,
       "ctWanHDSLSNRLowHRULoop2": ctWanHDSLSNRLowHRULoop2,
       "ctWanHDSLSNRHighHRULoop2": ctWanHDSLSNRHighHRULoop2,
       "ctWanHDSLPulseAttenuationHRULoop1": ctWanHDSLPulseAttenuationHRULoop1,
       "ctWanHDSLPulseAttenuationHRULoop2": ctWanHDSLPulseAttenuationHRULoop2,
       "ctWanHDSLDs1FrameHRU": ctWanHDSLDs1FrameHRU,
       "ctWanHDSLSNRDb1NetworkLoop1": ctWanHDSLSNRDb1NetworkLoop1,
       "ctWanHDSLSNRLowDb1NetworkLoop1": ctWanHDSLSNRLowDb1NetworkLoop1,
       "ctWanHDSLSNRHighDb1NetworkLoop1": ctWanHDSLSNRHighDb1NetworkLoop1,
       "ctWanHDSLSNRDb1NetworkLoop2": ctWanHDSLSNRDb1NetworkLoop2,
       "ctWanHDSLSNRLowDb1NetworkLoop2": ctWanHDSLSNRLowDb1NetworkLoop2,
       "ctWanHDSLSNRHighDb1NetworkLoop2": ctWanHDSLSNRHighDb1NetworkLoop2,
       "ctWanHDSLSNRDb1CustomerLoop1": ctWanHDSLSNRDb1CustomerLoop1,
       "ctWanHDSLSNRLowDb1CustomerLoop1": ctWanHDSLSNRLowDb1CustomerLoop1,
       "ctWanHDSLSNRHighDb1CustomerLoop1": ctWanHDSLSNRHighDb1CustomerLoop1,
       "ctWanHDSLSNRDb1CustomerLoop2": ctWanHDSLSNRDb1CustomerLoop2,
       "ctWanHDSLSNRLowDb1CustomerLoop2": ctWanHDSLSNRLowDb1CustomerLoop2,
       "ctWanHDSLSNRHighDb1CustomerLoop2": ctWanHDSLSNRHighDb1CustomerLoop2,
       "ctWanHDSLPulseAttenuationDb1NetworkLoop1": ctWanHDSLPulseAttenuationDb1NetworkLoop1,
       "ctWanHDSLPulseAttenuationDb1NetworkLoop2": ctWanHDSLPulseAttenuationDb1NetworkLoop2,
       "ctWanHDSLPulseAttenuationDb1CustomerLoop1": ctWanHDSLPulseAttenuationDb1CustomerLoop1,
       "ctWanHDSLPulseAttenuationDb1CustomerLoop2": ctWanHDSLPulseAttenuationDb1CustomerLoop2,
       "ctWanHDSLSNRDb2NetworkLoop1": ctWanHDSLSNRDb2NetworkLoop1,
       "ctWanHDSLSNRLowDb2NetworkLoop1": ctWanHDSLSNRLowDb2NetworkLoop1,
       "ctWanHDSLSNRHighDb2NetworkLoop1": ctWanHDSLSNRHighDb2NetworkLoop1,
       "ctWanHDSLSNRDb2NetworkLoop2": ctWanHDSLSNRDb2NetworkLoop2,
       "ctWanHDSLSNRLowDb2NetworkLoop2": ctWanHDSLSNRLowDb2NetworkLoop2,
       "ctWanHDSLSNRHighDb2NetworkLoop2": ctWanHDSLSNRHighDb2NetworkLoop2,
       "ctWanHDSLSNRDb2CustomerLoop1": ctWanHDSLSNRDb2CustomerLoop1,
       "ctWanHDSLSNRLowDb2CustomerLoop1": ctWanHDSLSNRLowDb2CustomerLoop1,
       "ctWanHDSLSNRHighDb2CustomerLoop1": ctWanHDSLSNRHighDb2CustomerLoop1,
       "ctWanHDSLSNRDb2CustomerLoop2": ctWanHDSLSNRDb2CustomerLoop2,
       "ctWanHDSLSNRLowDb2CustomerLoop2": ctWanHDSLSNRLowDb2CustomerLoop2,
       "ctWanHDSLSNRHighDb2CustomerLoop2": ctWanHDSLSNRHighDb2CustomerLoop2,
       "ctWanHDSLPulseAttenuationDb2NetworkLoop1": ctWanHDSLPulseAttenuationDb2NetworkLoop1,
       "ctWanHDSLPulseAttenuationDb2NetworkLoop2": ctWanHDSLPulseAttenuationDb2NetworkLoop2,
       "ctWanHDSLPulseAttenuationDb2CustomerLoop1": ctWanHDSLPulseAttenuationDb2CustomerLoop1,
       "ctWanHDSLPulseAttenuationDb2CustomerLoop2": ctWanHDSLPulseAttenuationDb2CustomerLoop2,
       "ctWanHDSLTestTable": ctWanHDSLTestTable,
       "ctWanHDSLTestEntry": ctWanHDSLTestEntry,
       "ctWanHDSLTestHLUConnIndex": ctWanHDSLTestHLUConnIndex,
       "ctWanHDSLTestMode": ctWanHDSLTestMode,
       "ctWanHDSLHLUTestResult": ctWanHDSLHLUTestResult,
       "ctWanHDSLHRUTestResult": ctWanHDSLHRUTestResult,
       "ctWanHDSLAlarmsTable": ctWanHDSLAlarmsTable,
       "ctWanHDSLAlarmsEntry": ctWanHDSLAlarmsEntry,
       "ctWanHDSLAlarmsHLUConnIndex": ctWanHDSLAlarmsHLUConnIndex,
       "ctWanHDSLAlarmsBackplane": ctWanHDSLAlarmsBackplane,
       "ctWanHDSLAlarmsES": ctWanHDSLAlarmsES,
       "ctWanHDSLAlarmHistoryTable": ctWanHDSLAlarmHistoryTable,
       "ctWanHDSLAlarmHistoryEntry": ctWanHDSLAlarmHistoryEntry,
       "ctWanHDSLAlarmHistoryConnIndex": ctWanHDSLAlarmHistoryConnIndex,
       "ctWanHDSLAlHistLLOSFirst": ctWanHDSLAlHistLLOSFirst,
       "ctWanHDSLAlHistLLOSLast": ctWanHDSLAlHistLLOSLast,
       "ctWanHDSLAlHistLLOSCurrent": ctWanHDSLAlHistLLOSCurrent,
       "ctWanHDSLAlHistLLOSCount": ctWanHDSLAlHistLLOSCount,
       "ctWanHDSLAlHistRLOSFirst": ctWanHDSLAlHistRLOSFirst,
       "ctWanHDSLAlHistRLOSLast": ctWanHDSLAlHistRLOSLast,
       "ctWanHDSLAlHistRLOSCurrent": ctWanHDSLAlHistRLOSCurrent,
       "ctWanHDSLAlHistRLOSCount": ctWanHDSLAlHistRLOSCount,
       "ctWanHDSLAlHistLOSW1First": ctWanHDSLAlHistLOSW1First,
       "ctWanHDSLAlHistLOSW1Last": ctWanHDSLAlHistLOSW1Last,
       "ctWanHDSLAlHistLOSW1Current": ctWanHDSLAlHistLOSW1Current,
       "ctWanHDSLAlHistLOSW1Count": ctWanHDSLAlHistLOSW1Count,
       "ctWanHDSLAlHistLOSW2First": ctWanHDSLAlHistLOSW2First,
       "ctWanHDSLAlHistLOSW2Last": ctWanHDSLAlHistLOSW2Last,
       "ctWanHDSLAlHistLOSW2Current": ctWanHDSLAlHistLOSW2Current,
       "ctWanHDSLAlHistLOSW2Count": ctWanHDSLAlHistLOSW2Count,
       "ctWanHDSLAlHistES1First": ctWanHDSLAlHistES1First,
       "ctWanHDSLAlHistES1Last": ctWanHDSLAlHistES1Last,
       "ctWanHDSLAlHistES1Current": ctWanHDSLAlHistES1Current,
       "ctWanHDSLAlHistES1Count": ctWanHDSLAlHistES1Count,
       "ctWanHDSLAlHistES2First": ctWanHDSLAlHistES2First,
       "ctWanHDSLAlHistES2Last": ctWanHDSLAlHistES2Last,
       "ctWanHDSLAlHistES2Current": ctWanHDSLAlHistES2Current,
       "ctWanHDSLAlHistES2Count": ctWanHDSLAlHistES2Count,
       "ctWanHDSLAlHistMargin1First": ctWanHDSLAlHistMargin1First,
       "ctWanHDSLAlHistMargin1Last": ctWanHDSLAlHistMargin1Last,
       "ctWanHDSLAlHistMargin1Current": ctWanHDSLAlHistMargin1Current,
       "ctWanHDSLAlHistMargin1Count": ctWanHDSLAlHistMargin1Count,
       "ctWanHDSLAlHistMargin2First": ctWanHDSLAlHistMargin2First,
       "ctWanHDSLAlHistMargin2Last": ctWanHDSLAlHistMargin2Last,
       "ctWanHDSLAlHistMargin2Current": ctWanHDSLAlHistMargin2Current,
       "ctWanHDSLAlHistMargin2Count": ctWanHDSLAlHistMargin2Count,
       "ctWanHDSLAlHistCleared": ctWanHDSLAlHistCleared,
       "ctWanHDSLAlHistClearit": ctWanHDSLAlHistClearit,
       "ctWanHDSLLoopbacksTable": ctWanHDSLLoopbacksTable,
       "ctWanHDSLLoopbacksEntry": ctWanHDSLLoopbacksEntry,
       "ctWanHDSLLoopbacksHLUConnIndex": ctWanHDSLLoopbacksHLUConnIndex,
       "ctWanHDSLLoopbacksAdminType": ctWanHDSLLoopbacksAdminType,
       "ctWanHDSLLoopbacksOperType": ctWanHDSLLoopbacksOperType}
)
