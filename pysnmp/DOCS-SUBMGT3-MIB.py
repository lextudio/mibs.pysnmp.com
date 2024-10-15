# SNMP MIB module (DOCS-SUBMGT3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-SUBMGT3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:59 2024
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

(DocsL2vpnIfList,
 clabProjDocsis) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "DocsL2vpnIfList",
    "clabProjDocsis")

(docsIf3CmtsCmRegStatusEntry,
 docsIf3CmtsCmRegStatusId) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "docsIf3CmtsCmRegStatusEntry",
    "docsIf3CmtsCmRegStatusId")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(SnmpTagList,) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "SnmpTagList")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

docsSubmgt3Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10)
)
docsSubmgt3Mib.setRevisions(
        ("2015-06-03 00:00",
         "2014-04-03 00:00",
         "2011-06-23 00:00",
         "2010-06-11 00:00",
         "2009-01-21 00:00",
         "2007-05-18 00:00",
         "2006-12-07 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DocsSubmgt3MibObjects_ObjectIdentity = ObjectIdentity
docsSubmgt3MibObjects = _DocsSubmgt3MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1)
)
_DocsSubmgt3Base_ObjectIdentity = ObjectIdentity
docsSubmgt3Base = _DocsSubmgt3Base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1)
)


class _DocsSubmgt3BaseCpeMaxIpv4Def_Type(Unsigned32):
    """Custom type docsSubmgt3BaseCpeMaxIpv4Def based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_DocsSubmgt3BaseCpeMaxIpv4Def_Type.__name__ = "Unsigned32"
_DocsSubmgt3BaseCpeMaxIpv4Def_Object = MibScalar
docsSubmgt3BaseCpeMaxIpv4Def = _DocsSubmgt3BaseCpeMaxIpv4Def_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 1),
    _DocsSubmgt3BaseCpeMaxIpv4Def_Type()
)
docsSubmgt3BaseCpeMaxIpv4Def.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3BaseCpeMaxIpv4Def.setStatus("current")


class _DocsSubmgt3BaseCpeMaxIpv6AddressesDef_Type(Unsigned32):
    """Custom type docsSubmgt3BaseCpeMaxIpv6AddressesDef based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_DocsSubmgt3BaseCpeMaxIpv6AddressesDef_Type.__name__ = "Unsigned32"
_DocsSubmgt3BaseCpeMaxIpv6AddressesDef_Object = MibScalar
docsSubmgt3BaseCpeMaxIpv6AddressesDef = _DocsSubmgt3BaseCpeMaxIpv6AddressesDef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 2),
    _DocsSubmgt3BaseCpeMaxIpv6AddressesDef_Type()
)
docsSubmgt3BaseCpeMaxIpv6AddressesDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3BaseCpeMaxIpv6AddressesDef.setStatus("deprecated")


class _DocsSubmgt3BaseCpeActiveDef_Type(TruthValue):
    """Custom type docsSubmgt3BaseCpeActiveDef based on TruthValue"""


_DocsSubmgt3BaseCpeActiveDef_Object = MibScalar
docsSubmgt3BaseCpeActiveDef = _DocsSubmgt3BaseCpeActiveDef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 3),
    _DocsSubmgt3BaseCpeActiveDef_Type()
)
docsSubmgt3BaseCpeActiveDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3BaseCpeActiveDef.setStatus("current")


class _DocsSubmgt3BaseCpeLearnableDef_Type(TruthValue):
    """Custom type docsSubmgt3BaseCpeLearnableDef based on TruthValue"""


_DocsSubmgt3BaseCpeLearnableDef_Object = MibScalar
docsSubmgt3BaseCpeLearnableDef = _DocsSubmgt3BaseCpeLearnableDef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 4),
    _DocsSubmgt3BaseCpeLearnableDef_Type()
)
docsSubmgt3BaseCpeLearnableDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3BaseCpeLearnableDef.setStatus("current")


class _DocsSubmgt3BaseSubFilterDownDef_Type(Unsigned32):
    """Custom type docsSubmgt3BaseSubFilterDownDef based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubmgt3BaseSubFilterDownDef_Type.__name__ = "Unsigned32"
_DocsSubmgt3BaseSubFilterDownDef_Object = MibScalar
docsSubmgt3BaseSubFilterDownDef = _DocsSubmgt3BaseSubFilterDownDef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 5),
    _DocsSubmgt3BaseSubFilterDownDef_Type()
)
docsSubmgt3BaseSubFilterDownDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3BaseSubFilterDownDef.setStatus("current")


class _DocsSubmgt3BaseSubFilterUpDef_Type(Unsigned32):
    """Custom type docsSubmgt3BaseSubFilterUpDef based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubmgt3BaseSubFilterUpDef_Type.__name__ = "Unsigned32"
_DocsSubmgt3BaseSubFilterUpDef_Object = MibScalar
docsSubmgt3BaseSubFilterUpDef = _DocsSubmgt3BaseSubFilterUpDef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 6),
    _DocsSubmgt3BaseSubFilterUpDef_Type()
)
docsSubmgt3BaseSubFilterUpDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3BaseSubFilterUpDef.setStatus("current")


class _DocsSubmgt3BaseCmFilterDownDef_Type(Unsigned32):
    """Custom type docsSubmgt3BaseCmFilterDownDef based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubmgt3BaseCmFilterDownDef_Type.__name__ = "Unsigned32"
_DocsSubmgt3BaseCmFilterDownDef_Object = MibScalar
docsSubmgt3BaseCmFilterDownDef = _DocsSubmgt3BaseCmFilterDownDef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 7),
    _DocsSubmgt3BaseCmFilterDownDef_Type()
)
docsSubmgt3BaseCmFilterDownDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3BaseCmFilterDownDef.setStatus("current")


class _DocsSubmgt3BaseCmFilterUpDef_Type(Unsigned32):
    """Custom type docsSubmgt3BaseCmFilterUpDef based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubmgt3BaseCmFilterUpDef_Type.__name__ = "Unsigned32"
_DocsSubmgt3BaseCmFilterUpDef_Object = MibScalar
docsSubmgt3BaseCmFilterUpDef = _DocsSubmgt3BaseCmFilterUpDef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 8),
    _DocsSubmgt3BaseCmFilterUpDef_Type()
)
docsSubmgt3BaseCmFilterUpDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3BaseCmFilterUpDef.setStatus("current")


class _DocsSubmgt3BasePsFilterDownDef_Type(Unsigned32):
    """Custom type docsSubmgt3BasePsFilterDownDef based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubmgt3BasePsFilterDownDef_Type.__name__ = "Unsigned32"
_DocsSubmgt3BasePsFilterDownDef_Object = MibScalar
docsSubmgt3BasePsFilterDownDef = _DocsSubmgt3BasePsFilterDownDef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 9),
    _DocsSubmgt3BasePsFilterDownDef_Type()
)
docsSubmgt3BasePsFilterDownDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3BasePsFilterDownDef.setStatus("current")


class _DocsSubmgt3BasePsFilterUpDef_Type(Unsigned32):
    """Custom type docsSubmgt3BasePsFilterUpDef based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubmgt3BasePsFilterUpDef_Type.__name__ = "Unsigned32"
_DocsSubmgt3BasePsFilterUpDef_Object = MibScalar
docsSubmgt3BasePsFilterUpDef = _DocsSubmgt3BasePsFilterUpDef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 10),
    _DocsSubmgt3BasePsFilterUpDef_Type()
)
docsSubmgt3BasePsFilterUpDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3BasePsFilterUpDef.setStatus("current")


class _DocsSubmgt3BaseMtaFilterDownDef_Type(Unsigned32):
    """Custom type docsSubmgt3BaseMtaFilterDownDef based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubmgt3BaseMtaFilterDownDef_Type.__name__ = "Unsigned32"
_DocsSubmgt3BaseMtaFilterDownDef_Object = MibScalar
docsSubmgt3BaseMtaFilterDownDef = _DocsSubmgt3BaseMtaFilterDownDef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 11),
    _DocsSubmgt3BaseMtaFilterDownDef_Type()
)
docsSubmgt3BaseMtaFilterDownDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3BaseMtaFilterDownDef.setStatus("current")


class _DocsSubmgt3BaseMtaFilterUpDef_Type(Unsigned32):
    """Custom type docsSubmgt3BaseMtaFilterUpDef based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubmgt3BaseMtaFilterUpDef_Type.__name__ = "Unsigned32"
_DocsSubmgt3BaseMtaFilterUpDef_Object = MibScalar
docsSubmgt3BaseMtaFilterUpDef = _DocsSubmgt3BaseMtaFilterUpDef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 12),
    _DocsSubmgt3BaseMtaFilterUpDef_Type()
)
docsSubmgt3BaseMtaFilterUpDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3BaseMtaFilterUpDef.setStatus("current")


class _DocsSubmgt3BaseStbFilterDownDef_Type(Unsigned32):
    """Custom type docsSubmgt3BaseStbFilterDownDef based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubmgt3BaseStbFilterDownDef_Type.__name__ = "Unsigned32"
_DocsSubmgt3BaseStbFilterDownDef_Object = MibScalar
docsSubmgt3BaseStbFilterDownDef = _DocsSubmgt3BaseStbFilterDownDef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 13),
    _DocsSubmgt3BaseStbFilterDownDef_Type()
)
docsSubmgt3BaseStbFilterDownDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3BaseStbFilterDownDef.setStatus("current")


class _DocsSubmgt3BaseStbFilterUpDef_Type(Unsigned32):
    """Custom type docsSubmgt3BaseStbFilterUpDef based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubmgt3BaseStbFilterUpDef_Type.__name__ = "Unsigned32"
_DocsSubmgt3BaseStbFilterUpDef_Object = MibScalar
docsSubmgt3BaseStbFilterUpDef = _DocsSubmgt3BaseStbFilterUpDef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 14),
    _DocsSubmgt3BaseStbFilterUpDef_Type()
)
docsSubmgt3BaseStbFilterUpDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3BaseStbFilterUpDef.setStatus("current")


class _DocsSubmgt3BaseCpeMaxIpv6PrefixesDef_Type(Unsigned32):
    """Custom type docsSubmgt3BaseCpeMaxIpv6PrefixesDef based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_DocsSubmgt3BaseCpeMaxIpv6PrefixesDef_Type.__name__ = "Unsigned32"
_DocsSubmgt3BaseCpeMaxIpv6PrefixesDef_Object = MibScalar
docsSubmgt3BaseCpeMaxIpv6PrefixesDef = _DocsSubmgt3BaseCpeMaxIpv6PrefixesDef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 15),
    _DocsSubmgt3BaseCpeMaxIpv6PrefixesDef_Type()
)
docsSubmgt3BaseCpeMaxIpv6PrefixesDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3BaseCpeMaxIpv6PrefixesDef.setStatus("current")
_DocsSubmgt3CpeCtrlTable_Object = MibTable
docsSubmgt3CpeCtrlTable = _DocsSubmgt3CpeCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 2)
)
if mibBuilder.loadTexts:
    docsSubmgt3CpeCtrlTable.setStatus("current")
_DocsSubmgt3CpeCtrlEntry_Object = MibTableRow
docsSubmgt3CpeCtrlEntry = _DocsSubmgt3CpeCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 2, 1)
)
if mibBuilder.loadTexts:
    docsSubmgt3CpeCtrlEntry.setStatus("current")


class _DocsSubmgt3CpeCtrlMaxCpeIpv4_Type(Unsigned32):
    """Custom type docsSubmgt3CpeCtrlMaxCpeIpv4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_DocsSubmgt3CpeCtrlMaxCpeIpv4_Type.__name__ = "Unsigned32"
_DocsSubmgt3CpeCtrlMaxCpeIpv4_Object = MibTableColumn
docsSubmgt3CpeCtrlMaxCpeIpv4 = _DocsSubmgt3CpeCtrlMaxCpeIpv4_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 2, 1, 1),
    _DocsSubmgt3CpeCtrlMaxCpeIpv4_Type()
)
docsSubmgt3CpeCtrlMaxCpeIpv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3CpeCtrlMaxCpeIpv4.setStatus("current")


class _DocsSubmgt3CpeCtrlMaxCpeIpv6Addresses_Type(Unsigned32):
    """Custom type docsSubmgt3CpeCtrlMaxCpeIpv6Addresses based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_DocsSubmgt3CpeCtrlMaxCpeIpv6Addresses_Type.__name__ = "Unsigned32"
_DocsSubmgt3CpeCtrlMaxCpeIpv6Addresses_Object = MibTableColumn
docsSubmgt3CpeCtrlMaxCpeIpv6Addresses = _DocsSubmgt3CpeCtrlMaxCpeIpv6Addresses_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 2, 1, 2),
    _DocsSubmgt3CpeCtrlMaxCpeIpv6Addresses_Type()
)
docsSubmgt3CpeCtrlMaxCpeIpv6Addresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3CpeCtrlMaxCpeIpv6Addresses.setStatus("deprecated")
_DocsSubmgt3CpeCtrlActive_Type = TruthValue
_DocsSubmgt3CpeCtrlActive_Object = MibTableColumn
docsSubmgt3CpeCtrlActive = _DocsSubmgt3CpeCtrlActive_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 2, 1, 3),
    _DocsSubmgt3CpeCtrlActive_Type()
)
docsSubmgt3CpeCtrlActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3CpeCtrlActive.setStatus("current")
_DocsSubmgt3CpeCtrlLearnable_Type = TruthValue
_DocsSubmgt3CpeCtrlLearnable_Object = MibTableColumn
docsSubmgt3CpeCtrlLearnable = _DocsSubmgt3CpeCtrlLearnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 2, 1, 4),
    _DocsSubmgt3CpeCtrlLearnable_Type()
)
docsSubmgt3CpeCtrlLearnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3CpeCtrlLearnable.setStatus("current")
_DocsSubmgt3CpeCtrlReset_Type = TruthValue
_DocsSubmgt3CpeCtrlReset_Object = MibTableColumn
docsSubmgt3CpeCtrlReset = _DocsSubmgt3CpeCtrlReset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 2, 1, 5),
    _DocsSubmgt3CpeCtrlReset_Type()
)
docsSubmgt3CpeCtrlReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3CpeCtrlReset.setStatus("current")
_DocsSubmgt3CpeCtrlLastReset_Type = TimeStamp
_DocsSubmgt3CpeCtrlLastReset_Object = MibTableColumn
docsSubmgt3CpeCtrlLastReset = _DocsSubmgt3CpeCtrlLastReset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 2, 1, 6),
    _DocsSubmgt3CpeCtrlLastReset_Type()
)
docsSubmgt3CpeCtrlLastReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3CpeCtrlLastReset.setStatus("current")


class _DocsSubmgt3CpeCtrlMaxCpeIpv6Prefixes_Type(Unsigned32):
    """Custom type docsSubmgt3CpeCtrlMaxCpeIpv6Prefixes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_DocsSubmgt3CpeCtrlMaxCpeIpv6Prefixes_Type.__name__ = "Unsigned32"
_DocsSubmgt3CpeCtrlMaxCpeIpv6Prefixes_Object = MibTableColumn
docsSubmgt3CpeCtrlMaxCpeIpv6Prefixes = _DocsSubmgt3CpeCtrlMaxCpeIpv6Prefixes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 2, 1, 7),
    _DocsSubmgt3CpeCtrlMaxCpeIpv6Prefixes_Type()
)
docsSubmgt3CpeCtrlMaxCpeIpv6Prefixes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3CpeCtrlMaxCpeIpv6Prefixes.setStatus("current")
_DocsSubmgt3CpeIpTable_Object = MibTable
docsSubmgt3CpeIpTable = _DocsSubmgt3CpeIpTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 3)
)
if mibBuilder.loadTexts:
    docsSubmgt3CpeIpTable.setStatus("current")
_DocsSubmgt3CpeIpEntry_Object = MibTableRow
docsSubmgt3CpeIpEntry = _DocsSubmgt3CpeIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 3, 1)
)
docsSubmgt3CpeIpEntry.setIndexNames(
    (0, "DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusId"),
    (0, "DOCS-SUBMGT3-MIB", "docsSubmgt3CpeIpId"),
)
if mibBuilder.loadTexts:
    docsSubmgt3CpeIpEntry.setStatus("current")


class _DocsSubmgt3CpeIpId_Type(Unsigned32):
    """Custom type docsSubmgt3CpeIpId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_DocsSubmgt3CpeIpId_Type.__name__ = "Unsigned32"
_DocsSubmgt3CpeIpId_Object = MibTableColumn
docsSubmgt3CpeIpId = _DocsSubmgt3CpeIpId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 3, 1, 1),
    _DocsSubmgt3CpeIpId_Type()
)
docsSubmgt3CpeIpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsSubmgt3CpeIpId.setStatus("current")
_DocsSubmgt3CpeIpAddrType_Type = InetAddressType
_DocsSubmgt3CpeIpAddrType_Object = MibTableColumn
docsSubmgt3CpeIpAddrType = _DocsSubmgt3CpeIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 3, 1, 2),
    _DocsSubmgt3CpeIpAddrType_Type()
)
docsSubmgt3CpeIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsSubmgt3CpeIpAddrType.setStatus("current")
_DocsSubmgt3CpeIpAddr_Type = InetAddress
_DocsSubmgt3CpeIpAddr_Object = MibTableColumn
docsSubmgt3CpeIpAddr = _DocsSubmgt3CpeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 3, 1, 3),
    _DocsSubmgt3CpeIpAddr_Type()
)
docsSubmgt3CpeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsSubmgt3CpeIpAddr.setStatus("current")
_DocsSubmgt3CpeIpAddrPrefixLen_Type = InetAddressPrefixLength
_DocsSubmgt3CpeIpAddrPrefixLen_Object = MibTableColumn
docsSubmgt3CpeIpAddrPrefixLen = _DocsSubmgt3CpeIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 3, 1, 4),
    _DocsSubmgt3CpeIpAddrPrefixLen_Type()
)
docsSubmgt3CpeIpAddrPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsSubmgt3CpeIpAddrPrefixLen.setStatus("current")
_DocsSubmgt3CpeIpLearned_Type = TruthValue
_DocsSubmgt3CpeIpLearned_Object = MibTableColumn
docsSubmgt3CpeIpLearned = _DocsSubmgt3CpeIpLearned_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 3, 1, 5),
    _DocsSubmgt3CpeIpLearned_Type()
)
docsSubmgt3CpeIpLearned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsSubmgt3CpeIpLearned.setStatus("current")


class _DocsSubmgt3CpeIpType_Type(Integer32):
    """Custom type docsSubmgt3CpeIpType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("card", 9),
          ("cpe", 1),
          ("dva", 7),
          ("erouter", 6),
          ("mta", 3),
          ("ps", 2),
          ("sg", 8),
          ("stb", 4),
          ("tea", 5))
    )


_DocsSubmgt3CpeIpType_Type.__name__ = "Integer32"
_DocsSubmgt3CpeIpType_Object = MibTableColumn
docsSubmgt3CpeIpType = _DocsSubmgt3CpeIpType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 3, 1, 6),
    _DocsSubmgt3CpeIpType_Type()
)
docsSubmgt3CpeIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsSubmgt3CpeIpType.setStatus("current")
_DocsSubmgt3GrpTable_Object = MibTable
docsSubmgt3GrpTable = _DocsSubmgt3GrpTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4)
)
if mibBuilder.loadTexts:
    docsSubmgt3GrpTable.setStatus("current")
_DocsSubmgt3GrpEntry_Object = MibTableRow
docsSubmgt3GrpEntry = _DocsSubmgt3GrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1)
)
if mibBuilder.loadTexts:
    docsSubmgt3GrpEntry.setStatus("current")


class _DocsSubMgt3GrpUdcGroupIds_Type(SnmpTagList):
    """Custom type docsSubMgt3GrpUdcGroupIds based on SnmpTagList"""
    defaultHexValue = ""


_DocsSubMgt3GrpUdcGroupIds_Object = MibTableColumn
docsSubMgt3GrpUdcGroupIds = _DocsSubMgt3GrpUdcGroupIds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 1),
    _DocsSubMgt3GrpUdcGroupIds_Type()
)
docsSubMgt3GrpUdcGroupIds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgt3GrpUdcGroupIds.setStatus("current")


class _DocsSubMgt3GrpUdcSentInRegRsp_Type(TruthValue):
    """Custom type docsSubMgt3GrpUdcSentInRegRsp based on TruthValue"""


_DocsSubMgt3GrpUdcSentInRegRsp_Object = MibTableColumn
docsSubMgt3GrpUdcSentInRegRsp = _DocsSubMgt3GrpUdcSentInRegRsp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 2),
    _DocsSubMgt3GrpUdcSentInRegRsp_Type()
)
docsSubMgt3GrpUdcSentInRegRsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgt3GrpUdcSentInRegRsp.setStatus("current")


class _DocsSubmgt3GrpSubFilterDs_Type(Unsigned32):
    """Custom type docsSubmgt3GrpSubFilterDs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubmgt3GrpSubFilterDs_Type.__name__ = "Unsigned32"
_DocsSubmgt3GrpSubFilterDs_Object = MibTableColumn
docsSubmgt3GrpSubFilterDs = _DocsSubmgt3GrpSubFilterDs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 3),
    _DocsSubmgt3GrpSubFilterDs_Type()
)
docsSubmgt3GrpSubFilterDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3GrpSubFilterDs.setStatus("current")


class _DocsSubmgt3GrpSubFilterUs_Type(Unsigned32):
    """Custom type docsSubmgt3GrpSubFilterUs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubmgt3GrpSubFilterUs_Type.__name__ = "Unsigned32"
_DocsSubmgt3GrpSubFilterUs_Object = MibTableColumn
docsSubmgt3GrpSubFilterUs = _DocsSubmgt3GrpSubFilterUs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 4),
    _DocsSubmgt3GrpSubFilterUs_Type()
)
docsSubmgt3GrpSubFilterUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3GrpSubFilterUs.setStatus("current")


class _DocsSubmgt3GrpCmFilterDs_Type(Unsigned32):
    """Custom type docsSubmgt3GrpCmFilterDs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubmgt3GrpCmFilterDs_Type.__name__ = "Unsigned32"
_DocsSubmgt3GrpCmFilterDs_Object = MibTableColumn
docsSubmgt3GrpCmFilterDs = _DocsSubmgt3GrpCmFilterDs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 5),
    _DocsSubmgt3GrpCmFilterDs_Type()
)
docsSubmgt3GrpCmFilterDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3GrpCmFilterDs.setStatus("current")


class _DocsSubmgt3GrpCmFilterUs_Type(Unsigned32):
    """Custom type docsSubmgt3GrpCmFilterUs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubmgt3GrpCmFilterUs_Type.__name__ = "Unsigned32"
_DocsSubmgt3GrpCmFilterUs_Object = MibTableColumn
docsSubmgt3GrpCmFilterUs = _DocsSubmgt3GrpCmFilterUs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 6),
    _DocsSubmgt3GrpCmFilterUs_Type()
)
docsSubmgt3GrpCmFilterUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3GrpCmFilterUs.setStatus("current")


class _DocsSubmgt3GrpPsFilterDs_Type(Unsigned32):
    """Custom type docsSubmgt3GrpPsFilterDs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubmgt3GrpPsFilterDs_Type.__name__ = "Unsigned32"
_DocsSubmgt3GrpPsFilterDs_Object = MibTableColumn
docsSubmgt3GrpPsFilterDs = _DocsSubmgt3GrpPsFilterDs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 7),
    _DocsSubmgt3GrpPsFilterDs_Type()
)
docsSubmgt3GrpPsFilterDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3GrpPsFilterDs.setStatus("current")


class _DocsSubmgt3GrpPsFilterUs_Type(Unsigned32):
    """Custom type docsSubmgt3GrpPsFilterUs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubmgt3GrpPsFilterUs_Type.__name__ = "Unsigned32"
_DocsSubmgt3GrpPsFilterUs_Object = MibTableColumn
docsSubmgt3GrpPsFilterUs = _DocsSubmgt3GrpPsFilterUs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 8),
    _DocsSubmgt3GrpPsFilterUs_Type()
)
docsSubmgt3GrpPsFilterUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3GrpPsFilterUs.setStatus("current")


class _DocsSubmgt3GrpMtaFilterDs_Type(Unsigned32):
    """Custom type docsSubmgt3GrpMtaFilterDs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubmgt3GrpMtaFilterDs_Type.__name__ = "Unsigned32"
_DocsSubmgt3GrpMtaFilterDs_Object = MibTableColumn
docsSubmgt3GrpMtaFilterDs = _DocsSubmgt3GrpMtaFilterDs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 9),
    _DocsSubmgt3GrpMtaFilterDs_Type()
)
docsSubmgt3GrpMtaFilterDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3GrpMtaFilterDs.setStatus("current")


class _DocsSubmgt3GrpMtaFilterUs_Type(Unsigned32):
    """Custom type docsSubmgt3GrpMtaFilterUs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubmgt3GrpMtaFilterUs_Type.__name__ = "Unsigned32"
_DocsSubmgt3GrpMtaFilterUs_Object = MibTableColumn
docsSubmgt3GrpMtaFilterUs = _DocsSubmgt3GrpMtaFilterUs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 10),
    _DocsSubmgt3GrpMtaFilterUs_Type()
)
docsSubmgt3GrpMtaFilterUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3GrpMtaFilterUs.setStatus("current")


class _DocsSubmgt3GrpStbFilterDs_Type(Unsigned32):
    """Custom type docsSubmgt3GrpStbFilterDs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubmgt3GrpStbFilterDs_Type.__name__ = "Unsigned32"
_DocsSubmgt3GrpStbFilterDs_Object = MibTableColumn
docsSubmgt3GrpStbFilterDs = _DocsSubmgt3GrpStbFilterDs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 11),
    _DocsSubmgt3GrpStbFilterDs_Type()
)
docsSubmgt3GrpStbFilterDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3GrpStbFilterDs.setStatus("current")


class _DocsSubmgt3GrpStbFilterUs_Type(Unsigned32):
    """Custom type docsSubmgt3GrpStbFilterUs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubmgt3GrpStbFilterUs_Type.__name__ = "Unsigned32"
_DocsSubmgt3GrpStbFilterUs_Object = MibTableColumn
docsSubmgt3GrpStbFilterUs = _DocsSubmgt3GrpStbFilterUs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 12),
    _DocsSubmgt3GrpStbFilterUs_Type()
)
docsSubmgt3GrpStbFilterUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubmgt3GrpStbFilterUs.setStatus("current")
_DocsSubmgt3FilterGrpTable_Object = MibTable
docsSubmgt3FilterGrpTable = _DocsSubmgt3FilterGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5)
)
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpTable.setStatus("current")
_DocsSubmgt3FilterGrpEntry_Object = MibTableRow
docsSubmgt3FilterGrpEntry = _DocsSubmgt3FilterGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1)
)
docsSubmgt3FilterGrpEntry.setIndexNames(
    (0, "DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpGrpId"),
    (0, "DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpRuleId"),
)
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpEntry.setStatus("current")


class _DocsSubmgt3FilterGrpGrpId_Type(Unsigned32):
    """Custom type docsSubmgt3FilterGrpGrpId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_DocsSubmgt3FilterGrpGrpId_Type.__name__ = "Unsigned32"
_DocsSubmgt3FilterGrpGrpId_Object = MibTableColumn
docsSubmgt3FilterGrpGrpId = _DocsSubmgt3FilterGrpGrpId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 1),
    _DocsSubmgt3FilterGrpGrpId_Type()
)
docsSubmgt3FilterGrpGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpGrpId.setStatus("current")


class _DocsSubmgt3FilterGrpRuleId_Type(Unsigned32):
    """Custom type docsSubmgt3FilterGrpRuleId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DocsSubmgt3FilterGrpRuleId_Type.__name__ = "Unsigned32"
_DocsSubmgt3FilterGrpRuleId_Object = MibTableColumn
docsSubmgt3FilterGrpRuleId = _DocsSubmgt3FilterGrpRuleId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 2),
    _DocsSubmgt3FilterGrpRuleId_Type()
)
docsSubmgt3FilterGrpRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpRuleId.setStatus("current")


class _DocsSubmgt3FilterGrpAction_Type(Integer32):
    """Custom type docsSubmgt3FilterGrpAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_DocsSubmgt3FilterGrpAction_Type.__name__ = "Integer32"
_DocsSubmgt3FilterGrpAction_Object = MibTableColumn
docsSubmgt3FilterGrpAction = _DocsSubmgt3FilterGrpAction_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 3),
    _DocsSubmgt3FilterGrpAction_Type()
)
docsSubmgt3FilterGrpAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpAction.setStatus("current")


class _DocsSubmgt3FilterGrpPriority_Type(Unsigned32):
    """Custom type docsSubmgt3FilterGrpPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsSubmgt3FilterGrpPriority_Type.__name__ = "Unsigned32"
_DocsSubmgt3FilterGrpPriority_Object = MibTableColumn
docsSubmgt3FilterGrpPriority = _DocsSubmgt3FilterGrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 4),
    _DocsSubmgt3FilterGrpPriority_Type()
)
docsSubmgt3FilterGrpPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpPriority.setStatus("current")


class _DocsSubmgt3FilterGrpIpTosLow_Type(OctetString):
    """Custom type docsSubmgt3FilterGrpIpTosLow based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsSubmgt3FilterGrpIpTosLow_Type.__name__ = "OctetString"
_DocsSubmgt3FilterGrpIpTosLow_Object = MibTableColumn
docsSubmgt3FilterGrpIpTosLow = _DocsSubmgt3FilterGrpIpTosLow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 5),
    _DocsSubmgt3FilterGrpIpTosLow_Type()
)
docsSubmgt3FilterGrpIpTosLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpIpTosLow.setStatus("current")


class _DocsSubmgt3FilterGrpIpTosHigh_Type(OctetString):
    """Custom type docsSubmgt3FilterGrpIpTosHigh based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsSubmgt3FilterGrpIpTosHigh_Type.__name__ = "OctetString"
_DocsSubmgt3FilterGrpIpTosHigh_Object = MibTableColumn
docsSubmgt3FilterGrpIpTosHigh = _DocsSubmgt3FilterGrpIpTosHigh_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 6),
    _DocsSubmgt3FilterGrpIpTosHigh_Type()
)
docsSubmgt3FilterGrpIpTosHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpIpTosHigh.setStatus("current")


class _DocsSubmgt3FilterGrpIpTosMask_Type(OctetString):
    """Custom type docsSubmgt3FilterGrpIpTosMask based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsSubmgt3FilterGrpIpTosMask_Type.__name__ = "OctetString"
_DocsSubmgt3FilterGrpIpTosMask_Object = MibTableColumn
docsSubmgt3FilterGrpIpTosMask = _DocsSubmgt3FilterGrpIpTosMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 7),
    _DocsSubmgt3FilterGrpIpTosMask_Type()
)
docsSubmgt3FilterGrpIpTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpIpTosMask.setStatus("current")


class _DocsSubmgt3FilterGrpIpProtocol_Type(Unsigned32):
    """Custom type docsSubmgt3FilterGrpIpProtocol based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 257),
    )


_DocsSubmgt3FilterGrpIpProtocol_Type.__name__ = "Unsigned32"
_DocsSubmgt3FilterGrpIpProtocol_Object = MibTableColumn
docsSubmgt3FilterGrpIpProtocol = _DocsSubmgt3FilterGrpIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 8),
    _DocsSubmgt3FilterGrpIpProtocol_Type()
)
docsSubmgt3FilterGrpIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpIpProtocol.setStatus("current")


class _DocsSubmgt3FilterGrpInetAddrType_Type(InetAddressType):
    """Custom type docsSubmgt3FilterGrpInetAddrType based on InetAddressType"""


_DocsSubmgt3FilterGrpInetAddrType_Object = MibTableColumn
docsSubmgt3FilterGrpInetAddrType = _DocsSubmgt3FilterGrpInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 9),
    _DocsSubmgt3FilterGrpInetAddrType_Type()
)
docsSubmgt3FilterGrpInetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpInetAddrType.setStatus("current")


class _DocsSubmgt3FilterGrpInetSrcAddr_Type(InetAddress):
    """Custom type docsSubmgt3FilterGrpInetSrcAddr based on InetAddress"""
    defaultHexValue = ""


_DocsSubmgt3FilterGrpInetSrcAddr_Object = MibTableColumn
docsSubmgt3FilterGrpInetSrcAddr = _DocsSubmgt3FilterGrpInetSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 10),
    _DocsSubmgt3FilterGrpInetSrcAddr_Type()
)
docsSubmgt3FilterGrpInetSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpInetSrcAddr.setStatus("current")


class _DocsSubmgt3FilterGrpInetSrcMask_Type(InetAddress):
    """Custom type docsSubmgt3FilterGrpInetSrcMask based on InetAddress"""
    defaultHexValue = ""


_DocsSubmgt3FilterGrpInetSrcMask_Object = MibTableColumn
docsSubmgt3FilterGrpInetSrcMask = _DocsSubmgt3FilterGrpInetSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 11),
    _DocsSubmgt3FilterGrpInetSrcMask_Type()
)
docsSubmgt3FilterGrpInetSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpInetSrcMask.setStatus("current")


class _DocsSubmgt3FilterGrpInetDestAddr_Type(InetAddress):
    """Custom type docsSubmgt3FilterGrpInetDestAddr based on InetAddress"""
    defaultHexValue = ""


_DocsSubmgt3FilterGrpInetDestAddr_Object = MibTableColumn
docsSubmgt3FilterGrpInetDestAddr = _DocsSubmgt3FilterGrpInetDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 12),
    _DocsSubmgt3FilterGrpInetDestAddr_Type()
)
docsSubmgt3FilterGrpInetDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpInetDestAddr.setStatus("current")


class _DocsSubmgt3FilterGrpInetDestMask_Type(InetAddress):
    """Custom type docsSubmgt3FilterGrpInetDestMask based on InetAddress"""
    defaultHexValue = ""


_DocsSubmgt3FilterGrpInetDestMask_Object = MibTableColumn
docsSubmgt3FilterGrpInetDestMask = _DocsSubmgt3FilterGrpInetDestMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 13),
    _DocsSubmgt3FilterGrpInetDestMask_Type()
)
docsSubmgt3FilterGrpInetDestMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpInetDestMask.setStatus("current")


class _DocsSubmgt3FilterGrpSrcPortStart_Type(InetPortNumber):
    """Custom type docsSubmgt3FilterGrpSrcPortStart based on InetPortNumber"""
    defaultValue = 0


_DocsSubmgt3FilterGrpSrcPortStart_Object = MibTableColumn
docsSubmgt3FilterGrpSrcPortStart = _DocsSubmgt3FilterGrpSrcPortStart_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 14),
    _DocsSubmgt3FilterGrpSrcPortStart_Type()
)
docsSubmgt3FilterGrpSrcPortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpSrcPortStart.setStatus("current")


class _DocsSubmgt3FilterGrpSrcPortEnd_Type(InetPortNumber):
    """Custom type docsSubmgt3FilterGrpSrcPortEnd based on InetPortNumber"""
    defaultValue = 65535


_DocsSubmgt3FilterGrpSrcPortEnd_Object = MibTableColumn
docsSubmgt3FilterGrpSrcPortEnd = _DocsSubmgt3FilterGrpSrcPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 15),
    _DocsSubmgt3FilterGrpSrcPortEnd_Type()
)
docsSubmgt3FilterGrpSrcPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpSrcPortEnd.setStatus("current")


class _DocsSubmgt3FilterGrpDestPortStart_Type(InetPortNumber):
    """Custom type docsSubmgt3FilterGrpDestPortStart based on InetPortNumber"""
    defaultValue = 0


_DocsSubmgt3FilterGrpDestPortStart_Object = MibTableColumn
docsSubmgt3FilterGrpDestPortStart = _DocsSubmgt3FilterGrpDestPortStart_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 16),
    _DocsSubmgt3FilterGrpDestPortStart_Type()
)
docsSubmgt3FilterGrpDestPortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpDestPortStart.setStatus("current")


class _DocsSubmgt3FilterGrpDestPortEnd_Type(InetPortNumber):
    """Custom type docsSubmgt3FilterGrpDestPortEnd based on InetPortNumber"""
    defaultValue = 65535


_DocsSubmgt3FilterGrpDestPortEnd_Object = MibTableColumn
docsSubmgt3FilterGrpDestPortEnd = _DocsSubmgt3FilterGrpDestPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 17),
    _DocsSubmgt3FilterGrpDestPortEnd_Type()
)
docsSubmgt3FilterGrpDestPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpDestPortEnd.setStatus("current")


class _DocsSubmgt3FilterGrpDestMacAddr_Type(MacAddress):
    """Custom type docsSubmgt3FilterGrpDestMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_DocsSubmgt3FilterGrpDestMacAddr_Object = MibTableColumn
docsSubmgt3FilterGrpDestMacAddr = _DocsSubmgt3FilterGrpDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 18),
    _DocsSubmgt3FilterGrpDestMacAddr_Type()
)
docsSubmgt3FilterGrpDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpDestMacAddr.setStatus("current")


class _DocsSubmgt3FilterGrpDestMacMask_Type(MacAddress):
    """Custom type docsSubmgt3FilterGrpDestMacMask based on MacAddress"""
    defaultHexValue = "000000000000"


_DocsSubmgt3FilterGrpDestMacMask_Object = MibTableColumn
docsSubmgt3FilterGrpDestMacMask = _DocsSubmgt3FilterGrpDestMacMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 19),
    _DocsSubmgt3FilterGrpDestMacMask_Type()
)
docsSubmgt3FilterGrpDestMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpDestMacMask.setStatus("current")


class _DocsSubmgt3FilterGrpSrcMacAddr_Type(MacAddress):
    """Custom type docsSubmgt3FilterGrpSrcMacAddr based on MacAddress"""
    defaultHexValue = "FFFFFFFFFFFF"


_DocsSubmgt3FilterGrpSrcMacAddr_Object = MibTableColumn
docsSubmgt3FilterGrpSrcMacAddr = _DocsSubmgt3FilterGrpSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 20),
    _DocsSubmgt3FilterGrpSrcMacAddr_Type()
)
docsSubmgt3FilterGrpSrcMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpSrcMacAddr.setStatus("current")


class _DocsSubmgt3FilterGrpEnetProtocolType_Type(Integer32):
    """Custom type docsSubmgt3FilterGrpEnetProtocolType based on Integer32"""
    defaultValue = 0

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
        *(("all", 4),
          ("dsap", 2),
          ("ethertype", 1),
          ("mac", 3),
          ("none", 0))
    )


_DocsSubmgt3FilterGrpEnetProtocolType_Type.__name__ = "Integer32"
_DocsSubmgt3FilterGrpEnetProtocolType_Object = MibTableColumn
docsSubmgt3FilterGrpEnetProtocolType = _DocsSubmgt3FilterGrpEnetProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 21),
    _DocsSubmgt3FilterGrpEnetProtocolType_Type()
)
docsSubmgt3FilterGrpEnetProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpEnetProtocolType.setStatus("current")


class _DocsSubmgt3FilterGrpEnetProtocol_Type(Unsigned32):
    """Custom type docsSubmgt3FilterGrpEnetProtocol based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsSubmgt3FilterGrpEnetProtocol_Type.__name__ = "Unsigned32"
_DocsSubmgt3FilterGrpEnetProtocol_Object = MibTableColumn
docsSubmgt3FilterGrpEnetProtocol = _DocsSubmgt3FilterGrpEnetProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 22),
    _DocsSubmgt3FilterGrpEnetProtocol_Type()
)
docsSubmgt3FilterGrpEnetProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpEnetProtocol.setStatus("current")


class _DocsSubmgt3FilterGrpUserPriLow_Type(Unsigned32):
    """Custom type docsSubmgt3FilterGrpUserPriLow based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DocsSubmgt3FilterGrpUserPriLow_Type.__name__ = "Unsigned32"
_DocsSubmgt3FilterGrpUserPriLow_Object = MibTableColumn
docsSubmgt3FilterGrpUserPriLow = _DocsSubmgt3FilterGrpUserPriLow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 23),
    _DocsSubmgt3FilterGrpUserPriLow_Type()
)
docsSubmgt3FilterGrpUserPriLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpUserPriLow.setStatus("current")


class _DocsSubmgt3FilterGrpUserPriHigh_Type(Unsigned32):
    """Custom type docsSubmgt3FilterGrpUserPriHigh based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DocsSubmgt3FilterGrpUserPriHigh_Type.__name__ = "Unsigned32"
_DocsSubmgt3FilterGrpUserPriHigh_Object = MibTableColumn
docsSubmgt3FilterGrpUserPriHigh = _DocsSubmgt3FilterGrpUserPriHigh_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 24),
    _DocsSubmgt3FilterGrpUserPriHigh_Type()
)
docsSubmgt3FilterGrpUserPriHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpUserPriHigh.setStatus("current")


class _DocsSubmgt3FilterGrpVlanId_Type(Unsigned32):
    """Custom type docsSubmgt3FilterGrpVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_DocsSubmgt3FilterGrpVlanId_Type.__name__ = "Unsigned32"
_DocsSubmgt3FilterGrpVlanId_Object = MibTableColumn
docsSubmgt3FilterGrpVlanId = _DocsSubmgt3FilterGrpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 25),
    _DocsSubmgt3FilterGrpVlanId_Type()
)
docsSubmgt3FilterGrpVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpVlanId.setStatus("current")
_DocsSubmgt3FilterGrpClassPkts_Type = Counter64
_DocsSubmgt3FilterGrpClassPkts_Object = MibTableColumn
docsSubmgt3FilterGrpClassPkts = _DocsSubmgt3FilterGrpClassPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 26),
    _DocsSubmgt3FilterGrpClassPkts_Type()
)
docsSubmgt3FilterGrpClassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpClassPkts.setStatus("current")


class _DocsSubmgt3FilterGrpFlowLabel_Type(Unsigned32):
    """Custom type docsSubmgt3FilterGrpFlowLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_DocsSubmgt3FilterGrpFlowLabel_Type.__name__ = "Unsigned32"
_DocsSubmgt3FilterGrpFlowLabel_Object = MibTableColumn
docsSubmgt3FilterGrpFlowLabel = _DocsSubmgt3FilterGrpFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 27),
    _DocsSubmgt3FilterGrpFlowLabel_Type()
)
docsSubmgt3FilterGrpFlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpFlowLabel.setStatus("current")
_DocsSubmgt3FilterGrpCmInterfaceMask_Type = DocsL2vpnIfList
_DocsSubmgt3FilterGrpCmInterfaceMask_Object = MibTableColumn
docsSubmgt3FilterGrpCmInterfaceMask = _DocsSubmgt3FilterGrpCmInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 28),
    _DocsSubmgt3FilterGrpCmInterfaceMask_Type()
)
docsSubmgt3FilterGrpCmInterfaceMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpCmInterfaceMask.setStatus("current")
_DocsSubmgt3FilterGrpRowStatus_Type = RowStatus
_DocsSubmgt3FilterGrpRowStatus_Object = MibTableColumn
docsSubmgt3FilterGrpRowStatus = _DocsSubmgt3FilterGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 29),
    _DocsSubmgt3FilterGrpRowStatus_Type()
)
docsSubmgt3FilterGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubmgt3FilterGrpRowStatus.setStatus("current")
_DocsSubmgt3MibConformance_ObjectIdentity = ObjectIdentity
docsSubmgt3MibConformance = _DocsSubmgt3MibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 2)
)
_DocsSubmgt3MibCompliances_ObjectIdentity = ObjectIdentity
docsSubmgt3MibCompliances = _DocsSubmgt3MibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 2, 1)
)
_DocsSubmgt3MibGroups_ObjectIdentity = ObjectIdentity
docsSubmgt3MibGroups = _DocsSubmgt3MibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 2, 2)
)
docsIf3CmtsCmRegStatusEntry.registerAugmentions(
    ("DOCS-SUBMGT3-MIB",
     "docsSubmgt3CpeCtrlEntry")
)
docsSubmgt3CpeCtrlEntry.setIndexNames(*docsIf3CmtsCmRegStatusEntry.getIndexNames())
docsIf3CmtsCmRegStatusEntry.registerAugmentions(
    ("DOCS-SUBMGT3-MIB",
     "docsSubmgt3GrpEntry")
)
docsSubmgt3GrpEntry.setIndexNames(*docsIf3CmtsCmRegStatusEntry.getIndexNames())

# Managed Objects groups

docsSubmgt3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 2, 2, 1)
)
docsSubmgt3Group.setObjects(
      *(("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseCpeMaxIpv4Def"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseCpeMaxIpv6PrefixesDef"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseCpeActiveDef"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseCpeLearnableDef"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseSubFilterDownDef"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseSubFilterUpDef"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseCmFilterDownDef"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseCmFilterUpDef"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3BasePsFilterDownDef"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3BasePsFilterUpDef"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseMtaFilterDownDef"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseMtaFilterUpDef"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseStbFilterDownDef"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseStbFilterUpDef"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeCtrlMaxCpeIpv4"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeCtrlMaxCpeIpv6Prefixes"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeCtrlActive"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeCtrlLearnable"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeCtrlReset"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeCtrlLastReset"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeIpAddrType"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeIpAddr"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeIpAddrPrefixLen"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeIpLearned"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeIpType"),
        ("DOCS-SUBMGT3-MIB", "docsSubMgt3GrpUdcGroupIds"),
        ("DOCS-SUBMGT3-MIB", "docsSubMgt3GrpUdcSentInRegRsp"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3GrpSubFilterDs"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3GrpSubFilterUs"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3GrpCmFilterDs"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3GrpCmFilterUs"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3GrpPsFilterDs"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3GrpPsFilterUs"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3GrpMtaFilterDs"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3GrpMtaFilterUs"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3GrpStbFilterDs"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3GrpStbFilterUs"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpAction"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpPriority"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpIpTosLow"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpIpTosHigh"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpIpTosMask"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpIpProtocol"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpInetAddrType"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpInetSrcAddr"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpInetSrcMask"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpInetDestAddr"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpInetDestMask"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpSrcPortStart"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpSrcPortEnd"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpDestPortStart"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpDestPortEnd"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpDestMacAddr"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpDestMacMask"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpSrcMacAddr"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpEnetProtocolType"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpEnetProtocol"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpUserPriLow"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpUserPriHigh"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpVlanId"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpClassPkts"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpFlowLabel"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpCmInterfaceMask"),
        ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpRowStatus"))
)
if mibBuilder.loadTexts:
    docsSubmgt3Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsSubmgt3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 2, 1, 1)
)
if mibBuilder.loadTexts:
    docsSubmgt3Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-SUBMGT3-MIB",
    **{"docsSubmgt3Mib": docsSubmgt3Mib,
       "docsSubmgt3MibObjects": docsSubmgt3MibObjects,
       "docsSubmgt3Base": docsSubmgt3Base,
       "docsSubmgt3BaseCpeMaxIpv4Def": docsSubmgt3BaseCpeMaxIpv4Def,
       "docsSubmgt3BaseCpeMaxIpv6AddressesDef": docsSubmgt3BaseCpeMaxIpv6AddressesDef,
       "docsSubmgt3BaseCpeActiveDef": docsSubmgt3BaseCpeActiveDef,
       "docsSubmgt3BaseCpeLearnableDef": docsSubmgt3BaseCpeLearnableDef,
       "docsSubmgt3BaseSubFilterDownDef": docsSubmgt3BaseSubFilterDownDef,
       "docsSubmgt3BaseSubFilterUpDef": docsSubmgt3BaseSubFilterUpDef,
       "docsSubmgt3BaseCmFilterDownDef": docsSubmgt3BaseCmFilterDownDef,
       "docsSubmgt3BaseCmFilterUpDef": docsSubmgt3BaseCmFilterUpDef,
       "docsSubmgt3BasePsFilterDownDef": docsSubmgt3BasePsFilterDownDef,
       "docsSubmgt3BasePsFilterUpDef": docsSubmgt3BasePsFilterUpDef,
       "docsSubmgt3BaseMtaFilterDownDef": docsSubmgt3BaseMtaFilterDownDef,
       "docsSubmgt3BaseMtaFilterUpDef": docsSubmgt3BaseMtaFilterUpDef,
       "docsSubmgt3BaseStbFilterDownDef": docsSubmgt3BaseStbFilterDownDef,
       "docsSubmgt3BaseStbFilterUpDef": docsSubmgt3BaseStbFilterUpDef,
       "docsSubmgt3BaseCpeMaxIpv6PrefixesDef": docsSubmgt3BaseCpeMaxIpv6PrefixesDef,
       "docsSubmgt3CpeCtrlTable": docsSubmgt3CpeCtrlTable,
       "docsSubmgt3CpeCtrlEntry": docsSubmgt3CpeCtrlEntry,
       "docsSubmgt3CpeCtrlMaxCpeIpv4": docsSubmgt3CpeCtrlMaxCpeIpv4,
       "docsSubmgt3CpeCtrlMaxCpeIpv6Addresses": docsSubmgt3CpeCtrlMaxCpeIpv6Addresses,
       "docsSubmgt3CpeCtrlActive": docsSubmgt3CpeCtrlActive,
       "docsSubmgt3CpeCtrlLearnable": docsSubmgt3CpeCtrlLearnable,
       "docsSubmgt3CpeCtrlReset": docsSubmgt3CpeCtrlReset,
       "docsSubmgt3CpeCtrlLastReset": docsSubmgt3CpeCtrlLastReset,
       "docsSubmgt3CpeCtrlMaxCpeIpv6Prefixes": docsSubmgt3CpeCtrlMaxCpeIpv6Prefixes,
       "docsSubmgt3CpeIpTable": docsSubmgt3CpeIpTable,
       "docsSubmgt3CpeIpEntry": docsSubmgt3CpeIpEntry,
       "docsSubmgt3CpeIpId": docsSubmgt3CpeIpId,
       "docsSubmgt3CpeIpAddrType": docsSubmgt3CpeIpAddrType,
       "docsSubmgt3CpeIpAddr": docsSubmgt3CpeIpAddr,
       "docsSubmgt3CpeIpAddrPrefixLen": docsSubmgt3CpeIpAddrPrefixLen,
       "docsSubmgt3CpeIpLearned": docsSubmgt3CpeIpLearned,
       "docsSubmgt3CpeIpType": docsSubmgt3CpeIpType,
       "docsSubmgt3GrpTable": docsSubmgt3GrpTable,
       "docsSubmgt3GrpEntry": docsSubmgt3GrpEntry,
       "docsSubMgt3GrpUdcGroupIds": docsSubMgt3GrpUdcGroupIds,
       "docsSubMgt3GrpUdcSentInRegRsp": docsSubMgt3GrpUdcSentInRegRsp,
       "docsSubmgt3GrpSubFilterDs": docsSubmgt3GrpSubFilterDs,
       "docsSubmgt3GrpSubFilterUs": docsSubmgt3GrpSubFilterUs,
       "docsSubmgt3GrpCmFilterDs": docsSubmgt3GrpCmFilterDs,
       "docsSubmgt3GrpCmFilterUs": docsSubmgt3GrpCmFilterUs,
       "docsSubmgt3GrpPsFilterDs": docsSubmgt3GrpPsFilterDs,
       "docsSubmgt3GrpPsFilterUs": docsSubmgt3GrpPsFilterUs,
       "docsSubmgt3GrpMtaFilterDs": docsSubmgt3GrpMtaFilterDs,
       "docsSubmgt3GrpMtaFilterUs": docsSubmgt3GrpMtaFilterUs,
       "docsSubmgt3GrpStbFilterDs": docsSubmgt3GrpStbFilterDs,
       "docsSubmgt3GrpStbFilterUs": docsSubmgt3GrpStbFilterUs,
       "docsSubmgt3FilterGrpTable": docsSubmgt3FilterGrpTable,
       "docsSubmgt3FilterGrpEntry": docsSubmgt3FilterGrpEntry,
       "docsSubmgt3FilterGrpGrpId": docsSubmgt3FilterGrpGrpId,
       "docsSubmgt3FilterGrpRuleId": docsSubmgt3FilterGrpRuleId,
       "docsSubmgt3FilterGrpAction": docsSubmgt3FilterGrpAction,
       "docsSubmgt3FilterGrpPriority": docsSubmgt3FilterGrpPriority,
       "docsSubmgt3FilterGrpIpTosLow": docsSubmgt3FilterGrpIpTosLow,
       "docsSubmgt3FilterGrpIpTosHigh": docsSubmgt3FilterGrpIpTosHigh,
       "docsSubmgt3FilterGrpIpTosMask": docsSubmgt3FilterGrpIpTosMask,
       "docsSubmgt3FilterGrpIpProtocol": docsSubmgt3FilterGrpIpProtocol,
       "docsSubmgt3FilterGrpInetAddrType": docsSubmgt3FilterGrpInetAddrType,
       "docsSubmgt3FilterGrpInetSrcAddr": docsSubmgt3FilterGrpInetSrcAddr,
       "docsSubmgt3FilterGrpInetSrcMask": docsSubmgt3FilterGrpInetSrcMask,
       "docsSubmgt3FilterGrpInetDestAddr": docsSubmgt3FilterGrpInetDestAddr,
       "docsSubmgt3FilterGrpInetDestMask": docsSubmgt3FilterGrpInetDestMask,
       "docsSubmgt3FilterGrpSrcPortStart": docsSubmgt3FilterGrpSrcPortStart,
       "docsSubmgt3FilterGrpSrcPortEnd": docsSubmgt3FilterGrpSrcPortEnd,
       "docsSubmgt3FilterGrpDestPortStart": docsSubmgt3FilterGrpDestPortStart,
       "docsSubmgt3FilterGrpDestPortEnd": docsSubmgt3FilterGrpDestPortEnd,
       "docsSubmgt3FilterGrpDestMacAddr": docsSubmgt3FilterGrpDestMacAddr,
       "docsSubmgt3FilterGrpDestMacMask": docsSubmgt3FilterGrpDestMacMask,
       "docsSubmgt3FilterGrpSrcMacAddr": docsSubmgt3FilterGrpSrcMacAddr,
       "docsSubmgt3FilterGrpEnetProtocolType": docsSubmgt3FilterGrpEnetProtocolType,
       "docsSubmgt3FilterGrpEnetProtocol": docsSubmgt3FilterGrpEnetProtocol,
       "docsSubmgt3FilterGrpUserPriLow": docsSubmgt3FilterGrpUserPriLow,
       "docsSubmgt3FilterGrpUserPriHigh": docsSubmgt3FilterGrpUserPriHigh,
       "docsSubmgt3FilterGrpVlanId": docsSubmgt3FilterGrpVlanId,
       "docsSubmgt3FilterGrpClassPkts": docsSubmgt3FilterGrpClassPkts,
       "docsSubmgt3FilterGrpFlowLabel": docsSubmgt3FilterGrpFlowLabel,
       "docsSubmgt3FilterGrpCmInterfaceMask": docsSubmgt3FilterGrpCmInterfaceMask,
       "docsSubmgt3FilterGrpRowStatus": docsSubmgt3FilterGrpRowStatus,
       "docsSubmgt3MibConformance": docsSubmgt3MibConformance,
       "docsSubmgt3MibCompliances": docsSubmgt3MibCompliances,
       "docsSubmgt3Compliance": docsSubmgt3Compliance,
       "docsSubmgt3MibGroups": docsSubmgt3MibGroups,
       "docsSubmgt3Group": docsSubmgt3Group}
)
