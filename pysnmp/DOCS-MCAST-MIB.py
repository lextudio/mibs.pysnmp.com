# SNMP MIB module (DOCS-MCAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-MCAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:56 2024
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

(clabProjDocsis,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjDocsis")

(DocsBpkmDataEncryptAlg,
 DocsSAId) = mibBuilder.importSymbols(
    "DOCS-IETF-BPI2-MIB",
    "DocsBpkmDataEncryptAlg",
    "DocsSAId")

(ChSetId,
 Dsid) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "ChSetId",
    "Dsid")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

docsMcastMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18)
)
docsMcastMib.setRevisions(
        ("2015-04-22 00:00",
         "2014-07-29 00:00",
         "2007-08-03 00:00",
         "2006-12-07 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DocsMcastMibObjects_ObjectIdentity = ObjectIdentity
docsMcastMibObjects = _DocsMcastMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1)
)
_DocsMcastCmtsGrpCfgTable_Object = MibTable
docsMcastCmtsGrpCfgTable = _DocsMcastCmtsGrpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 1)
)
if mibBuilder.loadTexts:
    docsMcastCmtsGrpCfgTable.setStatus("current")
_DocsMcastCmtsGrpCfgEntry_Object = MibTableRow
docsMcastCmtsGrpCfgEntry = _DocsMcastCmtsGrpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 1, 1)
)
docsMcastCmtsGrpCfgEntry.setIndexNames(
    (0, "DOCS-MCAST-MIB", "docsMcastCmtsGrpCfgId"),
)
if mibBuilder.loadTexts:
    docsMcastCmtsGrpCfgEntry.setStatus("current")


class _DocsMcastCmtsGrpCfgId_Type(Unsigned32):
    """Custom type docsMcastCmtsGrpCfgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsMcastCmtsGrpCfgId_Type.__name__ = "Unsigned32"
_DocsMcastCmtsGrpCfgId_Object = MibTableColumn
docsMcastCmtsGrpCfgId = _DocsMcastCmtsGrpCfgId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 1, 1, 1),
    _DocsMcastCmtsGrpCfgId_Type()
)
docsMcastCmtsGrpCfgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpCfgId.setStatus("current")


class _DocsMcastCmtsGrpCfgRulePriority_Type(Unsigned32):
    """Custom type docsMcastCmtsGrpCfgRulePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsMcastCmtsGrpCfgRulePriority_Type.__name__ = "Unsigned32"
_DocsMcastCmtsGrpCfgRulePriority_Object = MibTableColumn
docsMcastCmtsGrpCfgRulePriority = _DocsMcastCmtsGrpCfgRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 1, 1, 2),
    _DocsMcastCmtsGrpCfgRulePriority_Type()
)
docsMcastCmtsGrpCfgRulePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpCfgRulePriority.setStatus("current")
_DocsMcastCmtsGrpCfgPrefixAddrType_Type = InetAddressType
_DocsMcastCmtsGrpCfgPrefixAddrType_Object = MibTableColumn
docsMcastCmtsGrpCfgPrefixAddrType = _DocsMcastCmtsGrpCfgPrefixAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 1, 1, 3),
    _DocsMcastCmtsGrpCfgPrefixAddrType_Type()
)
docsMcastCmtsGrpCfgPrefixAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpCfgPrefixAddrType.setStatus("current")
_DocsMcastCmtsGrpCfgSrcPrefixAddr_Type = InetAddress
_DocsMcastCmtsGrpCfgSrcPrefixAddr_Object = MibTableColumn
docsMcastCmtsGrpCfgSrcPrefixAddr = _DocsMcastCmtsGrpCfgSrcPrefixAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 1, 1, 4),
    _DocsMcastCmtsGrpCfgSrcPrefixAddr_Type()
)
docsMcastCmtsGrpCfgSrcPrefixAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpCfgSrcPrefixAddr.setStatus("current")


class _DocsMcastCmtsGrpCfgSrcPrefixLen_Type(InetAddressPrefixLength):
    """Custom type docsMcastCmtsGrpCfgSrcPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0


_DocsMcastCmtsGrpCfgSrcPrefixLen_Object = MibTableColumn
docsMcastCmtsGrpCfgSrcPrefixLen = _DocsMcastCmtsGrpCfgSrcPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 1, 1, 5),
    _DocsMcastCmtsGrpCfgSrcPrefixLen_Type()
)
docsMcastCmtsGrpCfgSrcPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpCfgSrcPrefixLen.setStatus("current")
_DocsMcastCmtsGrpCfgGrpPrefixAddr_Type = InetAddress
_DocsMcastCmtsGrpCfgGrpPrefixAddr_Object = MibTableColumn
docsMcastCmtsGrpCfgGrpPrefixAddr = _DocsMcastCmtsGrpCfgGrpPrefixAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 1, 1, 6),
    _DocsMcastCmtsGrpCfgGrpPrefixAddr_Type()
)
docsMcastCmtsGrpCfgGrpPrefixAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpCfgGrpPrefixAddr.setStatus("current")


class _DocsMcastCmtsGrpCfgGrpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type docsMcastCmtsGrpCfgGrpPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0


_DocsMcastCmtsGrpCfgGrpPrefixLen_Object = MibTableColumn
docsMcastCmtsGrpCfgGrpPrefixLen = _DocsMcastCmtsGrpCfgGrpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 1, 1, 7),
    _DocsMcastCmtsGrpCfgGrpPrefixLen_Type()
)
docsMcastCmtsGrpCfgGrpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpCfgGrpPrefixLen.setStatus("current")


class _DocsMcastCmtsGrpCfgTosLow_Type(OctetString):
    """Custom type docsMcastCmtsGrpCfgTosLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsMcastCmtsGrpCfgTosLow_Type.__name__ = "OctetString"
_DocsMcastCmtsGrpCfgTosLow_Object = MibTableColumn
docsMcastCmtsGrpCfgTosLow = _DocsMcastCmtsGrpCfgTosLow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 1, 1, 8),
    _DocsMcastCmtsGrpCfgTosLow_Type()
)
docsMcastCmtsGrpCfgTosLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpCfgTosLow.setStatus("current")


class _DocsMcastCmtsGrpCfgTosHigh_Type(OctetString):
    """Custom type docsMcastCmtsGrpCfgTosHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsMcastCmtsGrpCfgTosHigh_Type.__name__ = "OctetString"
_DocsMcastCmtsGrpCfgTosHigh_Object = MibTableColumn
docsMcastCmtsGrpCfgTosHigh = _DocsMcastCmtsGrpCfgTosHigh_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 1, 1, 9),
    _DocsMcastCmtsGrpCfgTosHigh_Type()
)
docsMcastCmtsGrpCfgTosHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpCfgTosHigh.setStatus("current")


class _DocsMcastCmtsGrpCfgTosMask_Type(OctetString):
    """Custom type docsMcastCmtsGrpCfgTosMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsMcastCmtsGrpCfgTosMask_Type.__name__ = "OctetString"
_DocsMcastCmtsGrpCfgTosMask_Object = MibTableColumn
docsMcastCmtsGrpCfgTosMask = _DocsMcastCmtsGrpCfgTosMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 1, 1, 10),
    _DocsMcastCmtsGrpCfgTosMask_Type()
)
docsMcastCmtsGrpCfgTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpCfgTosMask.setStatus("current")


class _DocsMcastCmtsGrpCfgQosConfigId_Type(Unsigned32):
    """Custom type docsMcastCmtsGrpCfgQosConfigId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsMcastCmtsGrpCfgQosConfigId_Type.__name__ = "Unsigned32"
_DocsMcastCmtsGrpCfgQosConfigId_Object = MibTableColumn
docsMcastCmtsGrpCfgQosConfigId = _DocsMcastCmtsGrpCfgQosConfigId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 1, 1, 11),
    _DocsMcastCmtsGrpCfgQosConfigId_Type()
)
docsMcastCmtsGrpCfgQosConfigId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpCfgQosConfigId.setStatus("current")


class _DocsMcastCmtsGrpCfgEncryptConfigId_Type(Unsigned32):
    """Custom type docsMcastCmtsGrpCfgEncryptConfigId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsMcastCmtsGrpCfgEncryptConfigId_Type.__name__ = "Unsigned32"
_DocsMcastCmtsGrpCfgEncryptConfigId_Object = MibTableColumn
docsMcastCmtsGrpCfgEncryptConfigId = _DocsMcastCmtsGrpCfgEncryptConfigId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 1, 1, 12),
    _DocsMcastCmtsGrpCfgEncryptConfigId_Type()
)
docsMcastCmtsGrpCfgEncryptConfigId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpCfgEncryptConfigId.setStatus("current")


class _DocsMcastCmtsGrpCfgPhsConfigId_Type(Unsigned32):
    """Custom type docsMcastCmtsGrpCfgPhsConfigId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsMcastCmtsGrpCfgPhsConfigId_Type.__name__ = "Unsigned32"
_DocsMcastCmtsGrpCfgPhsConfigId_Object = MibTableColumn
docsMcastCmtsGrpCfgPhsConfigId = _DocsMcastCmtsGrpCfgPhsConfigId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 1, 1, 13),
    _DocsMcastCmtsGrpCfgPhsConfigId_Type()
)
docsMcastCmtsGrpCfgPhsConfigId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpCfgPhsConfigId.setStatus("current")
_DocsMcastCmtsGrpCfgRowStatus_Type = RowStatus
_DocsMcastCmtsGrpCfgRowStatus_Object = MibTableColumn
docsMcastCmtsGrpCfgRowStatus = _DocsMcastCmtsGrpCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 1, 1, 14),
    _DocsMcastCmtsGrpCfgRowStatus_Type()
)
docsMcastCmtsGrpCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpCfgRowStatus.setStatus("current")
_DocsMcastCmtsGrpEncryptCfgTable_Object = MibTable
docsMcastCmtsGrpEncryptCfgTable = _DocsMcastCmtsGrpEncryptCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 2)
)
if mibBuilder.loadTexts:
    docsMcastCmtsGrpEncryptCfgTable.setStatus("current")
_DocsMcastCmtsGrpEncryptCfgEntry_Object = MibTableRow
docsMcastCmtsGrpEncryptCfgEntry = _DocsMcastCmtsGrpEncryptCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 2, 1)
)
docsMcastCmtsGrpEncryptCfgEntry.setIndexNames(
    (0, "DOCS-MCAST-MIB", "docsMcastCmtsGrpEncryptCfgId"),
)
if mibBuilder.loadTexts:
    docsMcastCmtsGrpEncryptCfgEntry.setStatus("current")


class _DocsMcastCmtsGrpEncryptCfgId_Type(Unsigned32):
    """Custom type docsMcastCmtsGrpEncryptCfgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsMcastCmtsGrpEncryptCfgId_Type.__name__ = "Unsigned32"
_DocsMcastCmtsGrpEncryptCfgId_Object = MibTableColumn
docsMcastCmtsGrpEncryptCfgId = _DocsMcastCmtsGrpEncryptCfgId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 2, 1, 1),
    _DocsMcastCmtsGrpEncryptCfgId_Type()
)
docsMcastCmtsGrpEncryptCfgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpEncryptCfgId.setStatus("current")


class _DocsMcastCmtsGrpEncryptCfgCtrl_Type(Integer32):
    """Custom type docsMcastCmtsGrpEncryptCfgCtrl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cmts", 1),
          ("mgmt", 2))
    )


_DocsMcastCmtsGrpEncryptCfgCtrl_Type.__name__ = "Integer32"
_DocsMcastCmtsGrpEncryptCfgCtrl_Object = MibTableColumn
docsMcastCmtsGrpEncryptCfgCtrl = _DocsMcastCmtsGrpEncryptCfgCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 2, 1, 2),
    _DocsMcastCmtsGrpEncryptCfgCtrl_Type()
)
docsMcastCmtsGrpEncryptCfgCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpEncryptCfgCtrl.setStatus("current")


class _DocsMcastCmtsGrpEncryptCfgAlg_Type(DocsBpkmDataEncryptAlg):
    """Custom type docsMcastCmtsGrpEncryptCfgAlg based on DocsBpkmDataEncryptAlg"""


_DocsMcastCmtsGrpEncryptCfgAlg_Object = MibTableColumn
docsMcastCmtsGrpEncryptCfgAlg = _DocsMcastCmtsGrpEncryptCfgAlg_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 2, 1, 3),
    _DocsMcastCmtsGrpEncryptCfgAlg_Type()
)
docsMcastCmtsGrpEncryptCfgAlg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpEncryptCfgAlg.setStatus("current")
_DocsMcastCmtsGrpEncryptCfgRowStatus_Type = RowStatus
_DocsMcastCmtsGrpEncryptCfgRowStatus_Object = MibTableColumn
docsMcastCmtsGrpEncryptCfgRowStatus = _DocsMcastCmtsGrpEncryptCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 2, 1, 4),
    _DocsMcastCmtsGrpEncryptCfgRowStatus_Type()
)
docsMcastCmtsGrpEncryptCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpEncryptCfgRowStatus.setStatus("current")
_DocsMcastCmtsGrpPhsCfgTable_Object = MibTable
docsMcastCmtsGrpPhsCfgTable = _DocsMcastCmtsGrpPhsCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 3)
)
if mibBuilder.loadTexts:
    docsMcastCmtsGrpPhsCfgTable.setStatus("current")
_DocsMcastCmtsGrpPhsCfgEntry_Object = MibTableRow
docsMcastCmtsGrpPhsCfgEntry = _DocsMcastCmtsGrpPhsCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 3, 1)
)
docsMcastCmtsGrpPhsCfgEntry.setIndexNames(
    (0, "DOCS-MCAST-MIB", "docsMcastCmtsGrpPhsCfgId"),
)
if mibBuilder.loadTexts:
    docsMcastCmtsGrpPhsCfgEntry.setStatus("current")


class _DocsMcastCmtsGrpPhsCfgId_Type(Unsigned32):
    """Custom type docsMcastCmtsGrpPhsCfgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsMcastCmtsGrpPhsCfgId_Type.__name__ = "Unsigned32"
_DocsMcastCmtsGrpPhsCfgId_Object = MibTableColumn
docsMcastCmtsGrpPhsCfgId = _DocsMcastCmtsGrpPhsCfgId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 3, 1, 1),
    _DocsMcastCmtsGrpPhsCfgId_Type()
)
docsMcastCmtsGrpPhsCfgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpPhsCfgId.setStatus("current")


class _DocsMcastCmtsGrpPhsCfgPhsField_Type(OctetString):
    """Custom type docsMcastCmtsGrpPhsCfgPhsField based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DocsMcastCmtsGrpPhsCfgPhsField_Type.__name__ = "OctetString"
_DocsMcastCmtsGrpPhsCfgPhsField_Object = MibTableColumn
docsMcastCmtsGrpPhsCfgPhsField = _DocsMcastCmtsGrpPhsCfgPhsField_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 3, 1, 2),
    _DocsMcastCmtsGrpPhsCfgPhsField_Type()
)
docsMcastCmtsGrpPhsCfgPhsField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpPhsCfgPhsField.setStatus("current")


class _DocsMcastCmtsGrpPhsCfgPhsMask_Type(OctetString):
    """Custom type docsMcastCmtsGrpPhsCfgPhsMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DocsMcastCmtsGrpPhsCfgPhsMask_Type.__name__ = "OctetString"
_DocsMcastCmtsGrpPhsCfgPhsMask_Object = MibTableColumn
docsMcastCmtsGrpPhsCfgPhsMask = _DocsMcastCmtsGrpPhsCfgPhsMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 3, 1, 3),
    _DocsMcastCmtsGrpPhsCfgPhsMask_Type()
)
docsMcastCmtsGrpPhsCfgPhsMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpPhsCfgPhsMask.setStatus("current")


class _DocsMcastCmtsGrpPhsCfgPhsSize_Type(Unsigned32):
    """Custom type docsMcastCmtsGrpPhsCfgPhsSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsMcastCmtsGrpPhsCfgPhsSize_Type.__name__ = "Unsigned32"
_DocsMcastCmtsGrpPhsCfgPhsSize_Object = MibTableColumn
docsMcastCmtsGrpPhsCfgPhsSize = _DocsMcastCmtsGrpPhsCfgPhsSize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 3, 1, 4),
    _DocsMcastCmtsGrpPhsCfgPhsSize_Type()
)
docsMcastCmtsGrpPhsCfgPhsSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpPhsCfgPhsSize.setStatus("current")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpPhsCfgPhsSize.setUnits("Bytes")


class _DocsMcastCmtsGrpPhsCfgPhsVerify_Type(TruthValue):
    """Custom type docsMcastCmtsGrpPhsCfgPhsVerify based on TruthValue"""


_DocsMcastCmtsGrpPhsCfgPhsVerify_Object = MibTableColumn
docsMcastCmtsGrpPhsCfgPhsVerify = _DocsMcastCmtsGrpPhsCfgPhsVerify_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 3, 1, 5),
    _DocsMcastCmtsGrpPhsCfgPhsVerify_Type()
)
docsMcastCmtsGrpPhsCfgPhsVerify.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpPhsCfgPhsVerify.setStatus("current")
_DocsMcastCmtsGrpPhsCfgRowStatus_Type = RowStatus
_DocsMcastCmtsGrpPhsCfgRowStatus_Object = MibTableColumn
docsMcastCmtsGrpPhsCfgRowStatus = _DocsMcastCmtsGrpPhsCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 3, 1, 6),
    _DocsMcastCmtsGrpPhsCfgRowStatus_Type()
)
docsMcastCmtsGrpPhsCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpPhsCfgRowStatus.setStatus("current")
_DocsMcastCmtsGrpQosCfgTable_Object = MibTable
docsMcastCmtsGrpQosCfgTable = _DocsMcastCmtsGrpQosCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 4)
)
if mibBuilder.loadTexts:
    docsMcastCmtsGrpQosCfgTable.setStatus("current")
_DocsMcastCmtsGrpQosCfgEntry_Object = MibTableRow
docsMcastCmtsGrpQosCfgEntry = _DocsMcastCmtsGrpQosCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 4, 1)
)
docsMcastCmtsGrpQosCfgEntry.setIndexNames(
    (0, "DOCS-MCAST-MIB", "docsMcastCmtsGrpQosCfgId"),
)
if mibBuilder.loadTexts:
    docsMcastCmtsGrpQosCfgEntry.setStatus("current")


class _DocsMcastCmtsGrpQosCfgId_Type(Unsigned32):
    """Custom type docsMcastCmtsGrpQosCfgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsMcastCmtsGrpQosCfgId_Type.__name__ = "Unsigned32"
_DocsMcastCmtsGrpQosCfgId_Object = MibTableColumn
docsMcastCmtsGrpQosCfgId = _DocsMcastCmtsGrpQosCfgId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 4, 1, 1),
    _DocsMcastCmtsGrpQosCfgId_Type()
)
docsMcastCmtsGrpQosCfgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpQosCfgId.setStatus("current")


class _DocsMcastCmtsGrpQosCfgServiceClassName_Type(SnmpAdminString):
    """Custom type docsMcastCmtsGrpQosCfgServiceClassName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_DocsMcastCmtsGrpQosCfgServiceClassName_Type.__name__ = "SnmpAdminString"
_DocsMcastCmtsGrpQosCfgServiceClassName_Object = MibTableColumn
docsMcastCmtsGrpQosCfgServiceClassName = _DocsMcastCmtsGrpQosCfgServiceClassName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 4, 1, 2),
    _DocsMcastCmtsGrpQosCfgServiceClassName_Type()
)
docsMcastCmtsGrpQosCfgServiceClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpQosCfgServiceClassName.setStatus("current")


class _DocsMcastCmtsGrpQosCfgQosCtrl_Type(Integer32):
    """Custom type docsMcastCmtsGrpQosCfgQosCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggregateSession", 2),
          ("singleSsession", 1))
    )


_DocsMcastCmtsGrpQosCfgQosCtrl_Type.__name__ = "Integer32"
_DocsMcastCmtsGrpQosCfgQosCtrl_Object = MibTableColumn
docsMcastCmtsGrpQosCfgQosCtrl = _DocsMcastCmtsGrpQosCfgQosCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 4, 1, 3),
    _DocsMcastCmtsGrpQosCfgQosCtrl_Type()
)
docsMcastCmtsGrpQosCfgQosCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpQosCfgQosCtrl.setStatus("current")


class _DocsMcastCmtsGrpQosCfgAggSessLimit_Type(Unsigned32):
    """Custom type docsMcastCmtsGrpQosCfgAggSessLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DocsMcastCmtsGrpQosCfgAggSessLimit_Type.__name__ = "Unsigned32"
_DocsMcastCmtsGrpQosCfgAggSessLimit_Object = MibTableColumn
docsMcastCmtsGrpQosCfgAggSessLimit = _DocsMcastCmtsGrpQosCfgAggSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 4, 1, 4),
    _DocsMcastCmtsGrpQosCfgAggSessLimit_Type()
)
docsMcastCmtsGrpQosCfgAggSessLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpQosCfgAggSessLimit.setStatus("current")


class _DocsMcastCmtsGrpQosCfgAppId_Type(Unsigned32):
    """Custom type docsMcastCmtsGrpQosCfgAppId based on Unsigned32"""
    defaultValue = 0


_DocsMcastCmtsGrpQosCfgAppId_Object = MibTableColumn
docsMcastCmtsGrpQosCfgAppId = _DocsMcastCmtsGrpQosCfgAppId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 4, 1, 5),
    _DocsMcastCmtsGrpQosCfgAppId_Type()
)
docsMcastCmtsGrpQosCfgAppId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpQosCfgAppId.setStatus("current")
_DocsMcastCmtsGrpQosCfgRowStatus_Type = RowStatus
_DocsMcastCmtsGrpQosCfgRowStatus_Object = MibTableColumn
docsMcastCmtsGrpQosCfgRowStatus = _DocsMcastCmtsGrpQosCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 4, 1, 6),
    _DocsMcastCmtsGrpQosCfgRowStatus_Type()
)
docsMcastCmtsGrpQosCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastCmtsGrpQosCfgRowStatus.setStatus("current")
_DocsMcastCmtsReplSessTable_Object = MibTable
docsMcastCmtsReplSessTable = _DocsMcastCmtsReplSessTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 5)
)
if mibBuilder.loadTexts:
    docsMcastCmtsReplSessTable.setStatus("current")
_DocsMcastCmtsReplSessEntry_Object = MibTableRow
docsMcastCmtsReplSessEntry = _DocsMcastCmtsReplSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 5, 1)
)
docsMcastCmtsReplSessEntry.setIndexNames(
    (0, "DOCS-MCAST-MIB", "docsMcastCmtsReplSessPrefixAddrType"),
    (0, "DOCS-MCAST-MIB", "docsMcastCmtsReplSessGrpPrefix"),
    (0, "DOCS-MCAST-MIB", "docsMcastCmtsReplSessSrcPrefix"),
    (0, "DOCS-MCAST-MIB", "docsMcastCmtsReplSessMdIfIndex"),
    (0, "DOCS-MCAST-MIB", "docsMcastCmtsReplSessDcsId"),
    (0, "DOCS-MCAST-MIB", "docsMcastCmtsReplSessServiceFlowId"),
)
if mibBuilder.loadTexts:
    docsMcastCmtsReplSessEntry.setStatus("current")
_DocsMcastCmtsReplSessPrefixAddrType_Type = InetAddressType
_DocsMcastCmtsReplSessPrefixAddrType_Object = MibTableColumn
docsMcastCmtsReplSessPrefixAddrType = _DocsMcastCmtsReplSessPrefixAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 5, 1, 1),
    _DocsMcastCmtsReplSessPrefixAddrType_Type()
)
docsMcastCmtsReplSessPrefixAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastCmtsReplSessPrefixAddrType.setStatus("current")
_DocsMcastCmtsReplSessGrpPrefix_Type = InetAddress
_DocsMcastCmtsReplSessGrpPrefix_Object = MibTableColumn
docsMcastCmtsReplSessGrpPrefix = _DocsMcastCmtsReplSessGrpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 5, 1, 2),
    _DocsMcastCmtsReplSessGrpPrefix_Type()
)
docsMcastCmtsReplSessGrpPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastCmtsReplSessGrpPrefix.setStatus("current")
_DocsMcastCmtsReplSessSrcPrefix_Type = InetAddress
_DocsMcastCmtsReplSessSrcPrefix_Object = MibTableColumn
docsMcastCmtsReplSessSrcPrefix = _DocsMcastCmtsReplSessSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 5, 1, 3),
    _DocsMcastCmtsReplSessSrcPrefix_Type()
)
docsMcastCmtsReplSessSrcPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastCmtsReplSessSrcPrefix.setStatus("current")
_DocsMcastCmtsReplSessMdIfIndex_Type = InterfaceIndex
_DocsMcastCmtsReplSessMdIfIndex_Object = MibTableColumn
docsMcastCmtsReplSessMdIfIndex = _DocsMcastCmtsReplSessMdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 5, 1, 4),
    _DocsMcastCmtsReplSessMdIfIndex_Type()
)
docsMcastCmtsReplSessMdIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastCmtsReplSessMdIfIndex.setStatus("current")
_DocsMcastCmtsReplSessDcsId_Type = ChSetId
_DocsMcastCmtsReplSessDcsId_Object = MibTableColumn
docsMcastCmtsReplSessDcsId = _DocsMcastCmtsReplSessDcsId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 5, 1, 5),
    _DocsMcastCmtsReplSessDcsId_Type()
)
docsMcastCmtsReplSessDcsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastCmtsReplSessDcsId.setStatus("current")


class _DocsMcastCmtsReplSessServiceFlowId_Type(Unsigned32):
    """Custom type docsMcastCmtsReplSessServiceFlowId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsMcastCmtsReplSessServiceFlowId_Type.__name__ = "Unsigned32"
_DocsMcastCmtsReplSessServiceFlowId_Object = MibTableColumn
docsMcastCmtsReplSessServiceFlowId = _DocsMcastCmtsReplSessServiceFlowId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 5, 1, 6),
    _DocsMcastCmtsReplSessServiceFlowId_Type()
)
docsMcastCmtsReplSessServiceFlowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastCmtsReplSessServiceFlowId.setStatus("current")
_DocsMcastCmtsReplSessDsid_Type = Dsid
_DocsMcastCmtsReplSessDsid_Object = MibTableColumn
docsMcastCmtsReplSessDsid = _DocsMcastCmtsReplSessDsid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 5, 1, 7),
    _DocsMcastCmtsReplSessDsid_Type()
)
docsMcastCmtsReplSessDsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastCmtsReplSessDsid.setStatus("current")
_DocsMcastCmtsReplSessSaid_Type = DocsSAId
_DocsMcastCmtsReplSessSaid_Object = MibTableColumn
docsMcastCmtsReplSessSaid = _DocsMcastCmtsReplSessSaid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 5, 1, 8),
    _DocsMcastCmtsReplSessSaid_Type()
)
docsMcastCmtsReplSessSaid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastCmtsReplSessSaid.setStatus("current")
_DocsMcastDefGrpSvcClass_ObjectIdentity = ObjectIdentity
docsMcastDefGrpSvcClass = _DocsMcastDefGrpSvcClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 6)
)


class _DocsMcastDefGrpSvcClassDef_Type(SnmpAdminString):
    """Custom type docsMcastDefGrpSvcClassDef based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DocsMcastDefGrpSvcClassDef_Type.__name__ = "SnmpAdminString"
_DocsMcastDefGrpSvcClassDef_Object = MibScalar
docsMcastDefGrpSvcClassDef = _DocsMcastDefGrpSvcClassDef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 6, 1),
    _DocsMcastDefGrpSvcClassDef_Type()
)
docsMcastDefGrpSvcClassDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsMcastDefGrpSvcClassDef.setStatus("current")
_DocsMcastDsidPhsTable_Object = MibTable
docsMcastDsidPhsTable = _DocsMcastDsidPhsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 7)
)
if mibBuilder.loadTexts:
    docsMcastDsidPhsTable.setStatus("current")
_DocsMcastDsidPhsEntry_Object = MibTableRow
docsMcastDsidPhsEntry = _DocsMcastDsidPhsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 7, 1)
)
docsMcastDsidPhsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-MCAST-MIB", "docsMcastDsidPhsDsid"),
)
if mibBuilder.loadTexts:
    docsMcastDsidPhsEntry.setStatus("current")
_DocsMcastDsidPhsDsid_Type = Dsid
_DocsMcastDsidPhsDsid_Object = MibTableColumn
docsMcastDsidPhsDsid = _DocsMcastDsidPhsDsid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 7, 1, 1),
    _DocsMcastDsidPhsDsid_Type()
)
docsMcastDsidPhsDsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastDsidPhsDsid.setStatus("current")


class _DocsMcastDsidPhsPhsField_Type(OctetString):
    """Custom type docsMcastDsidPhsPhsField based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DocsMcastDsidPhsPhsField_Type.__name__ = "OctetString"
_DocsMcastDsidPhsPhsField_Object = MibTableColumn
docsMcastDsidPhsPhsField = _DocsMcastDsidPhsPhsField_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 7, 1, 2),
    _DocsMcastDsidPhsPhsField_Type()
)
docsMcastDsidPhsPhsField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastDsidPhsPhsField.setStatus("current")


class _DocsMcastDsidPhsPhsMask_Type(OctetString):
    """Custom type docsMcastDsidPhsPhsMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DocsMcastDsidPhsPhsMask_Type.__name__ = "OctetString"
_DocsMcastDsidPhsPhsMask_Object = MibTableColumn
docsMcastDsidPhsPhsMask = _DocsMcastDsidPhsPhsMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 7, 1, 3),
    _DocsMcastDsidPhsPhsMask_Type()
)
docsMcastDsidPhsPhsMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastDsidPhsPhsMask.setStatus("current")


class _DocsMcastDsidPhsPhsSize_Type(Unsigned32):
    """Custom type docsMcastDsidPhsPhsSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsMcastDsidPhsPhsSize_Type.__name__ = "Unsigned32"
_DocsMcastDsidPhsPhsSize_Object = MibTableColumn
docsMcastDsidPhsPhsSize = _DocsMcastDsidPhsPhsSize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 7, 1, 4),
    _DocsMcastDsidPhsPhsSize_Type()
)
docsMcastDsidPhsPhsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastDsidPhsPhsSize.setStatus("current")
_DocsMcastDsidPhsPhsVerify_Type = TruthValue
_DocsMcastDsidPhsPhsVerify_Object = MibTableColumn
docsMcastDsidPhsPhsVerify = _DocsMcastDsidPhsPhsVerify_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 7, 1, 5),
    _DocsMcastDsidPhsPhsVerify_Type()
)
docsMcastDsidPhsPhsVerify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastDsidPhsPhsVerify.setStatus("current")
_DocsMcastStatsTable_Object = MibTable
docsMcastStatsTable = _DocsMcastStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 8)
)
if mibBuilder.loadTexts:
    docsMcastStatsTable.setStatus("current")
_DocsMcastStatsEntry_Object = MibTableRow
docsMcastStatsEntry = _DocsMcastStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 8, 1)
)
docsMcastStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-MCAST-MIB", "docsMcastStatsGrpAddrType"),
    (0, "DOCS-MCAST-MIB", "docsMcastStatsGrpAddr"),
    (0, "DOCS-MCAST-MIB", "docsMcastStatsGrpPrefixLen"),
    (0, "DOCS-MCAST-MIB", "docsMcastStatsSrcAddrType"),
    (0, "DOCS-MCAST-MIB", "docsMcastStatsSrcAddr"),
    (0, "DOCS-MCAST-MIB", "docsMcastStatsSrcPrefixLen"),
)
if mibBuilder.loadTexts:
    docsMcastStatsEntry.setStatus("current")
_DocsMcastStatsGrpAddrType_Type = InetAddressType
_DocsMcastStatsGrpAddrType_Object = MibTableColumn
docsMcastStatsGrpAddrType = _DocsMcastStatsGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 8, 1, 1),
    _DocsMcastStatsGrpAddrType_Type()
)
docsMcastStatsGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastStatsGrpAddrType.setStatus("current")
_DocsMcastStatsGrpAddr_Type = InetAddress
_DocsMcastStatsGrpAddr_Object = MibTableColumn
docsMcastStatsGrpAddr = _DocsMcastStatsGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 8, 1, 2),
    _DocsMcastStatsGrpAddr_Type()
)
docsMcastStatsGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastStatsGrpAddr.setStatus("current")
_DocsMcastStatsGrpPrefixLen_Type = InetAddressPrefixLength
_DocsMcastStatsGrpPrefixLen_Object = MibTableColumn
docsMcastStatsGrpPrefixLen = _DocsMcastStatsGrpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 8, 1, 3),
    _DocsMcastStatsGrpPrefixLen_Type()
)
docsMcastStatsGrpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastStatsGrpPrefixLen.setStatus("current")
_DocsMcastStatsSrcAddrType_Type = InetAddressType
_DocsMcastStatsSrcAddrType_Object = MibTableColumn
docsMcastStatsSrcAddrType = _DocsMcastStatsSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 8, 1, 4),
    _DocsMcastStatsSrcAddrType_Type()
)
docsMcastStatsSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastStatsSrcAddrType.setStatus("current")
_DocsMcastStatsSrcAddr_Type = InetAddress
_DocsMcastStatsSrcAddr_Object = MibTableColumn
docsMcastStatsSrcAddr = _DocsMcastStatsSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 8, 1, 5),
    _DocsMcastStatsSrcAddr_Type()
)
docsMcastStatsSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastStatsSrcAddr.setStatus("current")
_DocsMcastStatsSrcPrefixLen_Type = InetAddressPrefixLength
_DocsMcastStatsSrcPrefixLen_Object = MibTableColumn
docsMcastStatsSrcPrefixLen = _DocsMcastStatsSrcPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 8, 1, 6),
    _DocsMcastStatsSrcPrefixLen_Type()
)
docsMcastStatsSrcPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastStatsSrcPrefixLen.setStatus("current")
_DocsMcastStatsDroppedPkts_Type = Counter32
_DocsMcastStatsDroppedPkts_Object = MibTableColumn
docsMcastStatsDroppedPkts = _DocsMcastStatsDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 8, 1, 7),
    _DocsMcastStatsDroppedPkts_Type()
)
docsMcastStatsDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastStatsDroppedPkts.setStatus("current")
_DocsMcastStatsDroppedOctets_Type = Counter32
_DocsMcastStatsDroppedOctets_Object = MibTableColumn
docsMcastStatsDroppedOctets = _DocsMcastStatsDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 8, 1, 8),
    _DocsMcastStatsDroppedOctets_Type()
)
docsMcastStatsDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastStatsDroppedOctets.setStatus("current")
_DocsMcastCpeListTable_Object = MibTable
docsMcastCpeListTable = _DocsMcastCpeListTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 9)
)
if mibBuilder.loadTexts:
    docsMcastCpeListTable.setStatus("current")
_DocsMcastCpeListEntry_Object = MibTableRow
docsMcastCpeListEntry = _DocsMcastCpeListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 9, 1)
)
docsMcastCpeListEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-MCAST-MIB", "docsMcastCpeListGrpAddrType"),
    (0, "DOCS-MCAST-MIB", "docsMcastCpeListGrpAddr"),
    (0, "DOCS-MCAST-MIB", "docsMcastCpeListGrpPrefixLen"),
    (0, "DOCS-MCAST-MIB", "docsMcastCpeListSrcAddrType"),
    (0, "DOCS-MCAST-MIB", "docsMcastCpeListSrcAddr"),
    (0, "DOCS-MCAST-MIB", "docsMcastCpeListSrcPrefixLen"),
    (0, "DOCS-MCAST-MIB", "docsMcastCpeListCmMacAddr"),
)
if mibBuilder.loadTexts:
    docsMcastCpeListEntry.setStatus("current")
_DocsMcastCpeListGrpAddrType_Type = InetAddressType
_DocsMcastCpeListGrpAddrType_Object = MibTableColumn
docsMcastCpeListGrpAddrType = _DocsMcastCpeListGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 9, 1, 1),
    _DocsMcastCpeListGrpAddrType_Type()
)
docsMcastCpeListGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastCpeListGrpAddrType.setStatus("current")
_DocsMcastCpeListGrpAddr_Type = InetAddress
_DocsMcastCpeListGrpAddr_Object = MibTableColumn
docsMcastCpeListGrpAddr = _DocsMcastCpeListGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 9, 1, 2),
    _DocsMcastCpeListGrpAddr_Type()
)
docsMcastCpeListGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastCpeListGrpAddr.setStatus("current")
_DocsMcastCpeListGrpPrefixLen_Type = InetAddressPrefixLength
_DocsMcastCpeListGrpPrefixLen_Object = MibTableColumn
docsMcastCpeListGrpPrefixLen = _DocsMcastCpeListGrpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 9, 1, 3),
    _DocsMcastCpeListGrpPrefixLen_Type()
)
docsMcastCpeListGrpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastCpeListGrpPrefixLen.setStatus("current")
_DocsMcastCpeListSrcAddrType_Type = InetAddressType
_DocsMcastCpeListSrcAddrType_Object = MibTableColumn
docsMcastCpeListSrcAddrType = _DocsMcastCpeListSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 9, 1, 4),
    _DocsMcastCpeListSrcAddrType_Type()
)
docsMcastCpeListSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastCpeListSrcAddrType.setStatus("current")
_DocsMcastCpeListSrcAddr_Type = InetAddress
_DocsMcastCpeListSrcAddr_Object = MibTableColumn
docsMcastCpeListSrcAddr = _DocsMcastCpeListSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 9, 1, 5),
    _DocsMcastCpeListSrcAddr_Type()
)
docsMcastCpeListSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastCpeListSrcAddr.setStatus("current")
_DocsMcastCpeListSrcPrefixLen_Type = InetAddressPrefixLength
_DocsMcastCpeListSrcPrefixLen_Object = MibTableColumn
docsMcastCpeListSrcPrefixLen = _DocsMcastCpeListSrcPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 9, 1, 6),
    _DocsMcastCpeListSrcPrefixLen_Type()
)
docsMcastCpeListSrcPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastCpeListSrcPrefixLen.setStatus("current")
_DocsMcastCpeListCmMacAddr_Type = MacAddress
_DocsMcastCpeListCmMacAddr_Object = MibTableColumn
docsMcastCpeListCmMacAddr = _DocsMcastCpeListCmMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 9, 1, 7),
    _DocsMcastCpeListCmMacAddr_Type()
)
docsMcastCpeListCmMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastCpeListCmMacAddr.setStatus("current")
_DocsMcastCpeListDsid_Type = Dsid
_DocsMcastCpeListDsid_Object = MibTableColumn
docsMcastCpeListDsid = _DocsMcastCpeListDsid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 9, 1, 8),
    _DocsMcastCpeListDsid_Type()
)
docsMcastCpeListDsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastCpeListDsid.setStatus("current")
_DocsMcastCpeListCpeMacAddr_Type = MacAddress
_DocsMcastCpeListCpeMacAddr_Object = MibTableColumn
docsMcastCpeListCpeMacAddr = _DocsMcastCpeListCpeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 9, 1, 9),
    _DocsMcastCpeListCpeMacAddr_Type()
)
docsMcastCpeListCpeMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastCpeListCpeMacAddr.setStatus("current")
_DocsMcastCpeListCpeIpAddrType_Type = InetAddressType
_DocsMcastCpeListCpeIpAddrType_Object = MibTableColumn
docsMcastCpeListCpeIpAddrType = _DocsMcastCpeListCpeIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 9, 1, 10),
    _DocsMcastCpeListCpeIpAddrType_Type()
)
docsMcastCpeListCpeIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastCpeListCpeIpAddrType.setStatus("current")
_DocsMcastCpeListCpeIpAddr_Type = InetAddress
_DocsMcastCpeListCpeIpAddr_Object = MibTableColumn
docsMcastCpeListCpeIpAddr = _DocsMcastCpeListCpeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 9, 1, 11),
    _DocsMcastCpeListCpeIpAddr_Type()
)
docsMcastCpeListCpeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastCpeListCpeIpAddr.setStatus("current")
_DocsMcastBandwidthTable_Object = MibTable
docsMcastBandwidthTable = _DocsMcastBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 10)
)
if mibBuilder.loadTexts:
    docsMcastBandwidthTable.setStatus("current")
_DocsMcastBandwidthEntry_Object = MibTableRow
docsMcastBandwidthEntry = _DocsMcastBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 10, 1)
)
docsMcastBandwidthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsMcastBandwidthEntry.setStatus("current")
_DocsMcastBandwidthAdmittedAggrBW_Type = CounterBasedGauge64
_DocsMcastBandwidthAdmittedAggrBW_Object = MibTableColumn
docsMcastBandwidthAdmittedAggrBW = _DocsMcastBandwidthAdmittedAggrBW_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 10, 1, 1),
    _DocsMcastBandwidthAdmittedAggrBW_Type()
)
docsMcastBandwidthAdmittedAggrBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastBandwidthAdmittedAggrBW.setStatus("current")
_DocsMcastBandwidthAdmittedAggrLowWater_Type = CounterBasedGauge64
_DocsMcastBandwidthAdmittedAggrLowWater_Object = MibTableColumn
docsMcastBandwidthAdmittedAggrLowWater = _DocsMcastBandwidthAdmittedAggrLowWater_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 10, 1, 2),
    _DocsMcastBandwidthAdmittedAggrLowWater_Type()
)
docsMcastBandwidthAdmittedAggrLowWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastBandwidthAdmittedAggrLowWater.setStatus("current")
_DocsMcastBandwidthAdmittedAggrHighWater_Type = CounterBasedGauge64
_DocsMcastBandwidthAdmittedAggrHighWater_Object = MibTableColumn
docsMcastBandwidthAdmittedAggrHighWater = _DocsMcastBandwidthAdmittedAggrHighWater_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 1, 10, 1, 3),
    _DocsMcastBandwidthAdmittedAggrHighWater_Type()
)
docsMcastBandwidthAdmittedAggrHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastBandwidthAdmittedAggrHighWater.setStatus("current")
_DocsMcastMibConformance_ObjectIdentity = ObjectIdentity
docsMcastMibConformance = _DocsMcastMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 2)
)
_DocsMcastMibCompliances_ObjectIdentity = ObjectIdentity
docsMcastMibCompliances = _DocsMcastMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 2, 1)
)
_DocsMcastMibGroups_ObjectIdentity = ObjectIdentity
docsMcastMibGroups = _DocsMcastMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 2, 2)
)

# Managed Objects groups

docsMcastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 2, 2, 1)
)
docsMcastGroup.setObjects(
      *(("DOCS-MCAST-MIB", "docsMcastCmtsReplSessDsid"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsReplSessSaid"),
        ("DOCS-MCAST-MIB", "docsMcastDefGrpSvcClassDef"),
        ("DOCS-MCAST-MIB", "docsMcastDsidPhsPhsField"),
        ("DOCS-MCAST-MIB", "docsMcastDsidPhsPhsMask"),
        ("DOCS-MCAST-MIB", "docsMcastDsidPhsPhsSize"),
        ("DOCS-MCAST-MIB", "docsMcastDsidPhsPhsVerify"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpCfgRulePriority"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpCfgPrefixAddrType"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpCfgSrcPrefixAddr"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpCfgSrcPrefixLen"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpCfgGrpPrefixAddr"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpCfgGrpPrefixLen"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpCfgTosLow"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpCfgTosHigh"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpCfgTosMask"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpCfgQosConfigId"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpCfgEncryptConfigId"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpCfgPhsConfigId"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpCfgRowStatus"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpQosCfgServiceClassName"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpQosCfgQosCtrl"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpQosCfgAggSessLimit"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpQosCfgAppId"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpQosCfgRowStatus"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpEncryptCfgCtrl"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpEncryptCfgAlg"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpEncryptCfgRowStatus"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpPhsCfgPhsField"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpPhsCfgPhsMask"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpPhsCfgPhsSize"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpPhsCfgPhsVerify"),
        ("DOCS-MCAST-MIB", "docsMcastCmtsGrpPhsCfgRowStatus"),
        ("DOCS-MCAST-MIB", "docsMcastStatsDroppedPkts"),
        ("DOCS-MCAST-MIB", "docsMcastStatsDroppedOctets"),
        ("DOCS-MCAST-MIB", "docsMcastCpeListDsid"),
        ("DOCS-MCAST-MIB", "docsMcastCpeListCpeMacAddr"),
        ("DOCS-MCAST-MIB", "docsMcastCpeListCpeIpAddrType"),
        ("DOCS-MCAST-MIB", "docsMcastCpeListCpeIpAddr"),
        ("DOCS-MCAST-MIB", "docsMcastBandwidthAdmittedAggrBW"),
        ("DOCS-MCAST-MIB", "docsMcastBandwidthAdmittedAggrLowWater"),
        ("DOCS-MCAST-MIB", "docsMcastBandwidthAdmittedAggrHighWater"))
)
if mibBuilder.loadTexts:
    docsMcastGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsMcastCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 18, 2, 1, 1)
)
if mibBuilder.loadTexts:
    docsMcastCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-MCAST-MIB",
    **{"docsMcastMib": docsMcastMib,
       "docsMcastMibObjects": docsMcastMibObjects,
       "docsMcastCmtsGrpCfgTable": docsMcastCmtsGrpCfgTable,
       "docsMcastCmtsGrpCfgEntry": docsMcastCmtsGrpCfgEntry,
       "docsMcastCmtsGrpCfgId": docsMcastCmtsGrpCfgId,
       "docsMcastCmtsGrpCfgRulePriority": docsMcastCmtsGrpCfgRulePriority,
       "docsMcastCmtsGrpCfgPrefixAddrType": docsMcastCmtsGrpCfgPrefixAddrType,
       "docsMcastCmtsGrpCfgSrcPrefixAddr": docsMcastCmtsGrpCfgSrcPrefixAddr,
       "docsMcastCmtsGrpCfgSrcPrefixLen": docsMcastCmtsGrpCfgSrcPrefixLen,
       "docsMcastCmtsGrpCfgGrpPrefixAddr": docsMcastCmtsGrpCfgGrpPrefixAddr,
       "docsMcastCmtsGrpCfgGrpPrefixLen": docsMcastCmtsGrpCfgGrpPrefixLen,
       "docsMcastCmtsGrpCfgTosLow": docsMcastCmtsGrpCfgTosLow,
       "docsMcastCmtsGrpCfgTosHigh": docsMcastCmtsGrpCfgTosHigh,
       "docsMcastCmtsGrpCfgTosMask": docsMcastCmtsGrpCfgTosMask,
       "docsMcastCmtsGrpCfgQosConfigId": docsMcastCmtsGrpCfgQosConfigId,
       "docsMcastCmtsGrpCfgEncryptConfigId": docsMcastCmtsGrpCfgEncryptConfigId,
       "docsMcastCmtsGrpCfgPhsConfigId": docsMcastCmtsGrpCfgPhsConfigId,
       "docsMcastCmtsGrpCfgRowStatus": docsMcastCmtsGrpCfgRowStatus,
       "docsMcastCmtsGrpEncryptCfgTable": docsMcastCmtsGrpEncryptCfgTable,
       "docsMcastCmtsGrpEncryptCfgEntry": docsMcastCmtsGrpEncryptCfgEntry,
       "docsMcastCmtsGrpEncryptCfgId": docsMcastCmtsGrpEncryptCfgId,
       "docsMcastCmtsGrpEncryptCfgCtrl": docsMcastCmtsGrpEncryptCfgCtrl,
       "docsMcastCmtsGrpEncryptCfgAlg": docsMcastCmtsGrpEncryptCfgAlg,
       "docsMcastCmtsGrpEncryptCfgRowStatus": docsMcastCmtsGrpEncryptCfgRowStatus,
       "docsMcastCmtsGrpPhsCfgTable": docsMcastCmtsGrpPhsCfgTable,
       "docsMcastCmtsGrpPhsCfgEntry": docsMcastCmtsGrpPhsCfgEntry,
       "docsMcastCmtsGrpPhsCfgId": docsMcastCmtsGrpPhsCfgId,
       "docsMcastCmtsGrpPhsCfgPhsField": docsMcastCmtsGrpPhsCfgPhsField,
       "docsMcastCmtsGrpPhsCfgPhsMask": docsMcastCmtsGrpPhsCfgPhsMask,
       "docsMcastCmtsGrpPhsCfgPhsSize": docsMcastCmtsGrpPhsCfgPhsSize,
       "docsMcastCmtsGrpPhsCfgPhsVerify": docsMcastCmtsGrpPhsCfgPhsVerify,
       "docsMcastCmtsGrpPhsCfgRowStatus": docsMcastCmtsGrpPhsCfgRowStatus,
       "docsMcastCmtsGrpQosCfgTable": docsMcastCmtsGrpQosCfgTable,
       "docsMcastCmtsGrpQosCfgEntry": docsMcastCmtsGrpQosCfgEntry,
       "docsMcastCmtsGrpQosCfgId": docsMcastCmtsGrpQosCfgId,
       "docsMcastCmtsGrpQosCfgServiceClassName": docsMcastCmtsGrpQosCfgServiceClassName,
       "docsMcastCmtsGrpQosCfgQosCtrl": docsMcastCmtsGrpQosCfgQosCtrl,
       "docsMcastCmtsGrpQosCfgAggSessLimit": docsMcastCmtsGrpQosCfgAggSessLimit,
       "docsMcastCmtsGrpQosCfgAppId": docsMcastCmtsGrpQosCfgAppId,
       "docsMcastCmtsGrpQosCfgRowStatus": docsMcastCmtsGrpQosCfgRowStatus,
       "docsMcastCmtsReplSessTable": docsMcastCmtsReplSessTable,
       "docsMcastCmtsReplSessEntry": docsMcastCmtsReplSessEntry,
       "docsMcastCmtsReplSessPrefixAddrType": docsMcastCmtsReplSessPrefixAddrType,
       "docsMcastCmtsReplSessGrpPrefix": docsMcastCmtsReplSessGrpPrefix,
       "docsMcastCmtsReplSessSrcPrefix": docsMcastCmtsReplSessSrcPrefix,
       "docsMcastCmtsReplSessMdIfIndex": docsMcastCmtsReplSessMdIfIndex,
       "docsMcastCmtsReplSessDcsId": docsMcastCmtsReplSessDcsId,
       "docsMcastCmtsReplSessServiceFlowId": docsMcastCmtsReplSessServiceFlowId,
       "docsMcastCmtsReplSessDsid": docsMcastCmtsReplSessDsid,
       "docsMcastCmtsReplSessSaid": docsMcastCmtsReplSessSaid,
       "docsMcastDefGrpSvcClass": docsMcastDefGrpSvcClass,
       "docsMcastDefGrpSvcClassDef": docsMcastDefGrpSvcClassDef,
       "docsMcastDsidPhsTable": docsMcastDsidPhsTable,
       "docsMcastDsidPhsEntry": docsMcastDsidPhsEntry,
       "docsMcastDsidPhsDsid": docsMcastDsidPhsDsid,
       "docsMcastDsidPhsPhsField": docsMcastDsidPhsPhsField,
       "docsMcastDsidPhsPhsMask": docsMcastDsidPhsPhsMask,
       "docsMcastDsidPhsPhsSize": docsMcastDsidPhsPhsSize,
       "docsMcastDsidPhsPhsVerify": docsMcastDsidPhsPhsVerify,
       "docsMcastStatsTable": docsMcastStatsTable,
       "docsMcastStatsEntry": docsMcastStatsEntry,
       "docsMcastStatsGrpAddrType": docsMcastStatsGrpAddrType,
       "docsMcastStatsGrpAddr": docsMcastStatsGrpAddr,
       "docsMcastStatsGrpPrefixLen": docsMcastStatsGrpPrefixLen,
       "docsMcastStatsSrcAddrType": docsMcastStatsSrcAddrType,
       "docsMcastStatsSrcAddr": docsMcastStatsSrcAddr,
       "docsMcastStatsSrcPrefixLen": docsMcastStatsSrcPrefixLen,
       "docsMcastStatsDroppedPkts": docsMcastStatsDroppedPkts,
       "docsMcastStatsDroppedOctets": docsMcastStatsDroppedOctets,
       "docsMcastCpeListTable": docsMcastCpeListTable,
       "docsMcastCpeListEntry": docsMcastCpeListEntry,
       "docsMcastCpeListGrpAddrType": docsMcastCpeListGrpAddrType,
       "docsMcastCpeListGrpAddr": docsMcastCpeListGrpAddr,
       "docsMcastCpeListGrpPrefixLen": docsMcastCpeListGrpPrefixLen,
       "docsMcastCpeListSrcAddrType": docsMcastCpeListSrcAddrType,
       "docsMcastCpeListSrcAddr": docsMcastCpeListSrcAddr,
       "docsMcastCpeListSrcPrefixLen": docsMcastCpeListSrcPrefixLen,
       "docsMcastCpeListCmMacAddr": docsMcastCpeListCmMacAddr,
       "docsMcastCpeListDsid": docsMcastCpeListDsid,
       "docsMcastCpeListCpeMacAddr": docsMcastCpeListCpeMacAddr,
       "docsMcastCpeListCpeIpAddrType": docsMcastCpeListCpeIpAddrType,
       "docsMcastCpeListCpeIpAddr": docsMcastCpeListCpeIpAddr,
       "docsMcastBandwidthTable": docsMcastBandwidthTable,
       "docsMcastBandwidthEntry": docsMcastBandwidthEntry,
       "docsMcastBandwidthAdmittedAggrBW": docsMcastBandwidthAdmittedAggrBW,
       "docsMcastBandwidthAdmittedAggrLowWater": docsMcastBandwidthAdmittedAggrLowWater,
       "docsMcastBandwidthAdmittedAggrHighWater": docsMcastBandwidthAdmittedAggrHighWater,
       "docsMcastMibConformance": docsMcastMibConformance,
       "docsMcastMibCompliances": docsMcastMibCompliances,
       "docsMcastCompliance": docsMcastCompliance,
       "docsMcastMibGroups": docsMcastMibGroups,
       "docsMcastGroup": docsMcastGroup}
)
