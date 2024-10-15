# SNMP MIB module (FOUNDRY-SN-WIRELESS-GROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-SN-WIRELESS-GROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:01 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-AGENT-MIB",
    "MacAddress")

(snSwitch,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "snSwitch")

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

snWireless = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23)
)
snWireless.setRevisions(
        ("2010-06-02 00:00",
         "2009-09-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IfIndexList(OctetString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_WgGroup_ObjectIdentity = ObjectIdentity
wgGroup = _WgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 1)
)
_WgMobilityId_Type = Integer32
_WgMobilityId_Object = MibScalar
wgMobilityId = _WgMobilityId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 1, 1),
    _WgMobilityId_Type()
)
wgMobilityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wgMobilityId.setStatus("current")
_WgVpnPTDeletePolicy_Type = Integer32
_WgVpnPTDeletePolicy_Object = MibScalar
wgVpnPTDeletePolicy = _WgVpnPTDeletePolicy_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 1, 2),
    _WgVpnPTDeletePolicy_Type()
)
wgVpnPTDeletePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wgVpnPTDeletePolicy.setStatus("current")
_WgIfTable_Object = MibTable
wgIfTable = _WgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 2)
)
if mibBuilder.loadTexts:
    wgIfTable.setStatus("current")
_WgIfEntry_Object = MibTableRow
wgIfEntry = _WgIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 2, 1)
)
wgIfEntry.setIndexNames(
    (0, "FOUNDRY-SN-WIRELESS-GROUP-MIB", "wgIfIndex"),
)
if mibBuilder.loadTexts:
    wgIfEntry.setStatus("current")
_WgIfIndex_Type = Integer32
_WgIfIndex_Object = MibTableColumn
wgIfIndex = _WgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 2, 1, 1),
    _WgIfIndex_Type()
)
wgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIfIndex.setStatus("current")


class _WgIfWirelessEnable_Type(Integer32):
    """Custom type wgIfWirelessEnable based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_WgIfWirelessEnable_Type.__name__ = "Integer32"
_WgIfWirelessEnable_Object = MibTableColumn
wgIfWirelessEnable = _WgIfWirelessEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 2, 1, 2),
    _WgIfWirelessEnable_Type()
)
wgIfWirelessEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wgIfWirelessEnable.setStatus("current")


class _WgIfPnPLearnNewAP_Type(Integer32):
    """Custom type wgIfPnPLearnNewAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_WgIfPnPLearnNewAP_Type.__name__ = "Integer32"
_WgIfPnPLearnNewAP_Object = MibTableColumn
wgIfPnPLearnNewAP = _WgIfPnPLearnNewAP_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 2, 1, 3),
    _WgIfPnPLearnNewAP_Type()
)
wgIfPnPLearnNewAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wgIfPnPLearnNewAP.setStatus("current")


class _WgIfAutoPortDisable_Type(Integer32):
    """Custom type wgIfAutoPortDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_WgIfAutoPortDisable_Type.__name__ = "Integer32"
_WgIfAutoPortDisable_Object = MibTableColumn
wgIfAutoPortDisable = _WgIfAutoPortDisable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 2, 1, 4),
    _WgIfAutoPortDisable_Type()
)
wgIfAutoPortDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wgIfAutoPortDisable.setStatus("current")
_WgIfVpnPTPolicyId_Type = Integer32
_WgIfVpnPTPolicyId_Object = MibTableColumn
wgIfVpnPTPolicyId = _WgIfVpnPTPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 2, 1, 5),
    _WgIfVpnPTPolicyId_Type()
)
wgIfVpnPTPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wgIfVpnPTPolicyId.setStatus("current")


class _WgIfFullCompRoamingEnable_Type(Integer32):
    """Custom type wgIfFullCompRoamingEnable based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_WgIfFullCompRoamingEnable_Type.__name__ = "Integer32"
_WgIfFullCompRoamingEnable_Object = MibTableColumn
wgIfFullCompRoamingEnable = _WgIfFullCompRoamingEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 2, 1, 6),
    _WgIfFullCompRoamingEnable_Type()
)
wgIfFullCompRoamingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wgIfFullCompRoamingEnable.setStatus("current")
_WgRoamingPeerTable_Object = MibTable
wgRoamingPeerTable = _WgRoamingPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 3)
)
if mibBuilder.loadTexts:
    wgRoamingPeerTable.setStatus("current")
_WgRoamingPeerEntry_Object = MibTableRow
wgRoamingPeerEntry = _WgRoamingPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 3, 1)
)
wgRoamingPeerEntry.setIndexNames(
    (0, "FOUNDRY-SN-WIRELESS-GROUP-MIB", "wgRoamingPeerIpAddress"),
)
if mibBuilder.loadTexts:
    wgRoamingPeerEntry.setStatus("current")
_WgRoamingPeerIpAddress_Type = IpAddress
_WgRoamingPeerIpAddress_Object = MibTableColumn
wgRoamingPeerIpAddress = _WgRoamingPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 3, 1, 1),
    _WgRoamingPeerIpAddress_Type()
)
wgRoamingPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgRoamingPeerIpAddress.setStatus("current")


class _WgRoamingPeerConnectionStatus_Type(Integer32):
    """Custom type wgRoamingPeerConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configured", 2),
          ("established", 3),
          ("other", 1))
    )


_WgRoamingPeerConnectionStatus_Type.__name__ = "Integer32"
_WgRoamingPeerConnectionStatus_Object = MibTableColumn
wgRoamingPeerConnectionStatus = _WgRoamingPeerConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 3, 1, 2),
    _WgRoamingPeerConnectionStatus_Type()
)
wgRoamingPeerConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgRoamingPeerConnectionStatus.setStatus("current")


class _WgRoamingPeerRowStatus_Type(Integer32):
    """Custom type wgRoamingPeerRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_WgRoamingPeerRowStatus_Type.__name__ = "Integer32"
_WgRoamingPeerRowStatus_Object = MibTableColumn
wgRoamingPeerRowStatus = _WgRoamingPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 3, 1, 3),
    _WgRoamingPeerRowStatus_Type()
)
wgRoamingPeerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wgRoamingPeerRowStatus.setStatus("current")
_WgPnPTable_Object = MibTable
wgPnPTable = _WgPnPTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 4)
)
if mibBuilder.loadTexts:
    wgPnPTable.setStatus("current")
_WgPnPEntry_Object = MibTableRow
wgPnPEntry = _WgPnPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 4, 1)
)
wgPnPEntry.setIndexNames(
    (0, "FOUNDRY-SN-WIRELESS-GROUP-MIB", "wgPnPIfIndex"),
    (0, "FOUNDRY-SN-WIRELESS-GROUP-MIB", "wgPnPMacAddress"),
)
if mibBuilder.loadTexts:
    wgPnPEntry.setStatus("current")
_WgPnPIfIndex_Type = Integer32
_WgPnPIfIndex_Object = MibTableColumn
wgPnPIfIndex = _WgPnPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 4, 1, 1),
    _WgPnPIfIndex_Type()
)
wgPnPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPnPIfIndex.setStatus("current")
_WgPnPMacAddress_Type = MacAddress
_WgPnPMacAddress_Object = MibTableColumn
wgPnPMacAddress = _WgPnPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 4, 1, 2),
    _WgPnPMacAddress_Type()
)
wgPnPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPnPMacAddress.setStatus("current")
_WgPnPIpAddress_Type = IpAddress
_WgPnPIpAddress_Object = MibTableColumn
wgPnPIpAddress = _WgPnPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 4, 1, 3),
    _WgPnPIpAddress_Type()
)
wgPnPIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wgPnPIpAddress.setStatus("current")
_WgPnPIpMask_Type = IpAddress
_WgPnPIpMask_Object = MibTableColumn
wgPnPIpMask = _WgPnPIpMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 4, 1, 4),
    _WgPnPIpMask_Type()
)
wgPnPIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wgPnPIpMask.setStatus("current")
_WgPnPIpDefaultGw_Type = IpAddress
_WgPnPIpDefaultGw_Object = MibTableColumn
wgPnPIpDefaultGw = _WgPnPIpDefaultGw_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 4, 1, 5),
    _WgPnPIpDefaultGw_Type()
)
wgPnPIpDefaultGw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wgPnPIpDefaultGw.setStatus("current")


class _WgPnPStatus_Type(Integer32):
    """Custom type wgPnPStatus based on Integer32"""
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
        *(("configured", 3),
          ("discovered", 2),
          ("operational", 4),
          ("other", 1))
    )


_WgPnPStatus_Type.__name__ = "Integer32"
_WgPnPStatus_Object = MibTableColumn
wgPnPStatus = _WgPnPStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 4, 1, 6),
    _WgPnPStatus_Type()
)
wgPnPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgPnPStatus.setStatus("current")


class _WgPnPRowStatus_Type(Integer32):
    """Custom type wgPnPRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("modify", 5),
          ("other", 1),
          ("valid", 2))
    )


_WgPnPRowStatus_Type.__name__ = "Integer32"
_WgPnPRowStatus_Object = MibTableColumn
wgPnPRowStatus = _WgPnPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 4, 1, 7),
    _WgPnPRowStatus_Type()
)
wgPnPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wgPnPRowStatus.setStatus("current")
_WgVpnPTServerTable_Object = MibTable
wgVpnPTServerTable = _WgVpnPTServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 5)
)
if mibBuilder.loadTexts:
    wgVpnPTServerTable.setStatus("current")
_WgVpnPTServerEntry_Object = MibTableRow
wgVpnPTServerEntry = _WgVpnPTServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 5, 1)
)
wgVpnPTServerEntry.setIndexNames(
    (0, "FOUNDRY-SN-WIRELESS-GROUP-MIB", "wgVpnPTServerPolicyId"),
    (0, "FOUNDRY-SN-WIRELESS-GROUP-MIB", "wgVpnPTServerIpAddress"),
)
if mibBuilder.loadTexts:
    wgVpnPTServerEntry.setStatus("current")
_WgVpnPTServerPolicyId_Type = Integer32
_WgVpnPTServerPolicyId_Object = MibTableColumn
wgVpnPTServerPolicyId = _WgVpnPTServerPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 5, 1, 1),
    _WgVpnPTServerPolicyId_Type()
)
wgVpnPTServerPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgVpnPTServerPolicyId.setStatus("current")
_WgVpnPTServerIpAddress_Type = IpAddress
_WgVpnPTServerIpAddress_Object = MibTableColumn
wgVpnPTServerIpAddress = _WgVpnPTServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 5, 1, 2),
    _WgVpnPTServerIpAddress_Type()
)
wgVpnPTServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgVpnPTServerIpAddress.setStatus("current")


class _WgVpnPTServerRowStatus_Type(Integer32):
    """Custom type wgVpnPTServerRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_WgVpnPTServerRowStatus_Type.__name__ = "Integer32"
_WgVpnPTServerRowStatus_Object = MibTableColumn
wgVpnPTServerRowStatus = _WgVpnPTServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 5, 1, 3),
    _WgVpnPTServerRowStatus_Type()
)
wgVpnPTServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wgVpnPTServerRowStatus.setStatus("current")
_WgVpnPTFilterTable_Object = MibTable
wgVpnPTFilterTable = _WgVpnPTFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 6)
)
if mibBuilder.loadTexts:
    wgVpnPTFilterTable.setStatus("current")
_WgVpnPTFilterEntry_Object = MibTableRow
wgVpnPTFilterEntry = _WgVpnPTFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 6, 1)
)
wgVpnPTFilterEntry.setIndexNames(
    (0, "FOUNDRY-SN-WIRELESS-GROUP-MIB", "wgVpnPTFilterPolicyId"),
    (0, "FOUNDRY-SN-WIRELESS-GROUP-MIB", "wgVpnPTFilterProtocol"),
    (0, "FOUNDRY-SN-WIRELESS-GROUP-MIB", "wgVpnPTFilterPort"),
)
if mibBuilder.loadTexts:
    wgVpnPTFilterEntry.setStatus("current")
_WgVpnPTFilterPolicyId_Type = Integer32
_WgVpnPTFilterPolicyId_Object = MibTableColumn
wgVpnPTFilterPolicyId = _WgVpnPTFilterPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 6, 1, 1),
    _WgVpnPTFilterPolicyId_Type()
)
wgVpnPTFilterPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgVpnPTFilterPolicyId.setStatus("current")


class _WgVpnPTFilterProtocol_Type(Integer32):
    """Custom type wgVpnPTFilterProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("tcp", 3),
          ("udp", 2))
    )


_WgVpnPTFilterProtocol_Type.__name__ = "Integer32"
_WgVpnPTFilterProtocol_Object = MibTableColumn
wgVpnPTFilterProtocol = _WgVpnPTFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 6, 1, 2),
    _WgVpnPTFilterProtocol_Type()
)
wgVpnPTFilterProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgVpnPTFilterProtocol.setStatus("current")
_WgVpnPTFilterPort_Type = Integer32
_WgVpnPTFilterPort_Object = MibTableColumn
wgVpnPTFilterPort = _WgVpnPTFilterPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 6, 1, 3),
    _WgVpnPTFilterPort_Type()
)
wgVpnPTFilterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgVpnPTFilterPort.setStatus("current")


class _WgVpnPTFilterRowStatus_Type(Integer32):
    """Custom type wgVpnPTFilterRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_WgVpnPTFilterRowStatus_Type.__name__ = "Integer32"
_WgVpnPTFilterRowStatus_Object = MibTableColumn
wgVpnPTFilterRowStatus = _WgVpnPTFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 6, 1, 4),
    _WgVpnPTFilterRowStatus_Type()
)
wgVpnPTFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wgVpnPTFilterRowStatus.setStatus("current")
_WgVpnPTPolicyTable_Object = MibTable
wgVpnPTPolicyTable = _WgVpnPTPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 7)
)
if mibBuilder.loadTexts:
    wgVpnPTPolicyTable.setStatus("current")
_WgVpnPTPolicyEntry_Object = MibTableRow
wgVpnPTPolicyEntry = _WgVpnPTPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 7, 1)
)
wgVpnPTPolicyEntry.setIndexNames(
    (0, "FOUNDRY-SN-WIRELESS-GROUP-MIB", "wgVpnPTPolicyId"),
)
if mibBuilder.loadTexts:
    wgVpnPTPolicyEntry.setStatus("current")
_WgVpnPTPolicyId_Type = Integer32
_WgVpnPTPolicyId_Object = MibTableColumn
wgVpnPTPolicyId = _WgVpnPTPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 7, 1, 1),
    _WgVpnPTPolicyId_Type()
)
wgVpnPTPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgVpnPTPolicyId.setStatus("current")
_WgVpnPTPolicyPortList_Type = IfIndexList
_WgVpnPTPolicyPortList_Object = MibTableColumn
wgVpnPTPolicyPortList = _WgVpnPTPolicyPortList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23, 7, 1, 2),
    _WgVpnPTPolicyPortList_Type()
)
wgVpnPTPolicyPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgVpnPTPolicyPortList.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-WIRELESS-GROUP-MIB",
    **{"IfIndexList": IfIndexList,
       "snWireless": snWireless,
       "wgGroup": wgGroup,
       "wgMobilityId": wgMobilityId,
       "wgVpnPTDeletePolicy": wgVpnPTDeletePolicy,
       "wgIfTable": wgIfTable,
       "wgIfEntry": wgIfEntry,
       "wgIfIndex": wgIfIndex,
       "wgIfWirelessEnable": wgIfWirelessEnable,
       "wgIfPnPLearnNewAP": wgIfPnPLearnNewAP,
       "wgIfAutoPortDisable": wgIfAutoPortDisable,
       "wgIfVpnPTPolicyId": wgIfVpnPTPolicyId,
       "wgIfFullCompRoamingEnable": wgIfFullCompRoamingEnable,
       "wgRoamingPeerTable": wgRoamingPeerTable,
       "wgRoamingPeerEntry": wgRoamingPeerEntry,
       "wgRoamingPeerIpAddress": wgRoamingPeerIpAddress,
       "wgRoamingPeerConnectionStatus": wgRoamingPeerConnectionStatus,
       "wgRoamingPeerRowStatus": wgRoamingPeerRowStatus,
       "wgPnPTable": wgPnPTable,
       "wgPnPEntry": wgPnPEntry,
       "wgPnPIfIndex": wgPnPIfIndex,
       "wgPnPMacAddress": wgPnPMacAddress,
       "wgPnPIpAddress": wgPnPIpAddress,
       "wgPnPIpMask": wgPnPIpMask,
       "wgPnPIpDefaultGw": wgPnPIpDefaultGw,
       "wgPnPStatus": wgPnPStatus,
       "wgPnPRowStatus": wgPnPRowStatus,
       "wgVpnPTServerTable": wgVpnPTServerTable,
       "wgVpnPTServerEntry": wgVpnPTServerEntry,
       "wgVpnPTServerPolicyId": wgVpnPTServerPolicyId,
       "wgVpnPTServerIpAddress": wgVpnPTServerIpAddress,
       "wgVpnPTServerRowStatus": wgVpnPTServerRowStatus,
       "wgVpnPTFilterTable": wgVpnPTFilterTable,
       "wgVpnPTFilterEntry": wgVpnPTFilterEntry,
       "wgVpnPTFilterPolicyId": wgVpnPTFilterPolicyId,
       "wgVpnPTFilterProtocol": wgVpnPTFilterProtocol,
       "wgVpnPTFilterPort": wgVpnPTFilterPort,
       "wgVpnPTFilterRowStatus": wgVpnPTFilterRowStatus,
       "wgVpnPTPolicyTable": wgVpnPTPolicyTable,
       "wgVpnPTPolicyEntry": wgVpnPTPolicyEntry,
       "wgVpnPTPolicyId": wgVpnPTPolicyId,
       "wgVpnPTPolicyPortList": wgVpnPTPolicyPortList}
)
