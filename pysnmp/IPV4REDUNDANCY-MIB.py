# SNMP MIB module (IPV4REDUNDANCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPV4REDUNDANCY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:24 2024
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

(apIpv4Redundancy,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "apIpv4Redundancy")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ipv4RedundancyMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApIpv4RedundancyVRConfigTable_Object = MibTable
apIpv4RedundancyVRConfigTable = _ApIpv4RedundancyVRConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 2)
)
if mibBuilder.loadTexts:
    apIpv4RedundancyVRConfigTable.setStatus("current")
_ApIpv4RedundancyVRConfigEntry_Object = MibTableRow
apIpv4RedundancyVRConfigEntry = _ApIpv4RedundancyVRConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 2, 1)
)
apIpv4RedundancyVRConfigEntry.setIndexNames(
    (0, "IPV4REDUNDANCY-MIB", "apIpv4RedundancyVRIntAddr"),
    (0, "IPV4REDUNDANCY-MIB", "apIpv4RedundancyVRID"),
)
if mibBuilder.loadTexts:
    apIpv4RedundancyVRConfigEntry.setStatus("current")


class _ApIpv4RedundancyVRID_Type(Integer32):
    """Custom type apIpv4RedundancyVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ApIpv4RedundancyVRID_Type.__name__ = "Integer32"
_ApIpv4RedundancyVRID_Object = MibTableColumn
apIpv4RedundancyVRID = _ApIpv4RedundancyVRID_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 2, 1, 1),
    _ApIpv4RedundancyVRID_Type()
)
apIpv4RedundancyVRID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RedundancyVRID.setStatus("current")
_ApIpv4RedundancyVRIntAddr_Type = IpAddress
_ApIpv4RedundancyVRIntAddr_Object = MibTableColumn
apIpv4RedundancyVRIntAddr = _ApIpv4RedundancyVRIntAddr_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 2, 1, 2),
    _ApIpv4RedundancyVRIntAddr_Type()
)
apIpv4RedundancyVRIntAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RedundancyVRIntAddr.setStatus("current")
_ApIpv4RedundancyConfigPriority_Type = Integer32
_ApIpv4RedundancyConfigPriority_Object = MibTableColumn
apIpv4RedundancyConfigPriority = _ApIpv4RedundancyConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 2, 1, 3),
    _ApIpv4RedundancyConfigPriority_Type()
)
apIpv4RedundancyConfigPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RedundancyConfigPriority.setStatus("current")
_ApIpv4RedundancyAdPriority_Type = Integer32
_ApIpv4RedundancyAdPriority_Object = MibTableColumn
apIpv4RedundancyAdPriority = _ApIpv4RedundancyAdPriority_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 2, 1, 4),
    _ApIpv4RedundancyAdPriority_Type()
)
apIpv4RedundancyAdPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RedundancyAdPriority.setStatus("current")


class _ApIpv4RedundancyName_Type(DisplayString):
    """Custom type apIpv4RedundancyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApIpv4RedundancyName_Type.__name__ = "DisplayString"
_ApIpv4RedundancyName_Object = MibTableColumn
apIpv4RedundancyName = _ApIpv4RedundancyName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 2, 1, 5),
    _ApIpv4RedundancyName_Type()
)
apIpv4RedundancyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RedundancyName.setStatus("current")


class _ApIpv4RedundancyVRPreempt_Type(Integer32):
    """Custom type apIpv4RedundancyVRPreempt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ApIpv4RedundancyVRPreempt_Type.__name__ = "Integer32"
_ApIpv4RedundancyVRPreempt_Object = MibTableColumn
apIpv4RedundancyVRPreempt = _ApIpv4RedundancyVRPreempt_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 2, 1, 6),
    _ApIpv4RedundancyVRPreempt_Type()
)
apIpv4RedundancyVRPreempt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RedundancyVRPreempt.setStatus("current")


class _ApIpv4RedundancyVRState_Type(Integer32):
    """Custom type apIpv4RedundancyVRState based on Integer32"""
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
        *(("backup", 2),
          ("idle", 4),
          ("ifDown", 0),
          ("master", 3),
          ("noService", 1))
    )


_ApIpv4RedundancyVRState_Type.__name__ = "Integer32"
_ApIpv4RedundancyVRState_Object = MibTableColumn
apIpv4RedundancyVRState = _ApIpv4RedundancyVRState_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 2, 1, 7),
    _ApIpv4RedundancyVRState_Type()
)
apIpv4RedundancyVRState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RedundancyVRState.setStatus("current")
_ApIpv4RedundancyVRMasterIP_Type = IpAddress
_ApIpv4RedundancyVRMasterIP_Object = MibTableColumn
apIpv4RedundancyVRMasterIP = _ApIpv4RedundancyVRMasterIP_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 2, 1, 8),
    _ApIpv4RedundancyVRMasterIP_Type()
)
apIpv4RedundancyVRMasterIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RedundancyVRMasterIP.setStatus("current")


class _ApIpv4RedundancyVRLastChange_Type(DisplayString):
    """Custom type apIpv4RedundancyVRLastChange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_ApIpv4RedundancyVRLastChange_Type.__name__ = "DisplayString"
_ApIpv4RedundancyVRLastChange_Object = MibTableColumn
apIpv4RedundancyVRLastChange = _ApIpv4RedundancyVRLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 2, 1, 9),
    _ApIpv4RedundancyVRLastChange_Type()
)
apIpv4RedundancyVRLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RedundancyVRLastChange.setStatus("current")
_ApIpv4RedundancyVRStateChanges_Type = Integer32
_ApIpv4RedundancyVRStateChanges_Object = MibTableColumn
apIpv4RedundancyVRStateChanges = _ApIpv4RedundancyVRStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 2, 1, 10),
    _ApIpv4RedundancyVRStateChanges_Type()
)
apIpv4RedundancyVRStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RedundancyVRStateChanges.setStatus("current")
_ApIpv4RedundancyVRStatus_Type = RowStatus
_ApIpv4RedundancyVRStatus_Object = MibTableColumn
apIpv4RedundancyVRStatus = _ApIpv4RedundancyVRStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 2, 1, 11),
    _ApIpv4RedundancyVRStatus_Type()
)
apIpv4RedundancyVRStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RedundancyVRStatus.setStatus("current")
_ApIpv4RedundancyIntConfigTable_Object = MibTable
apIpv4RedundancyIntConfigTable = _ApIpv4RedundancyIntConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 3)
)
if mibBuilder.loadTexts:
    apIpv4RedundancyIntConfigTable.setStatus("current")
_ApIpv4RedundancyIntConfigEntry_Object = MibTableRow
apIpv4RedundancyIntConfigEntry = _ApIpv4RedundancyIntConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 3, 1)
)
apIpv4RedundancyIntConfigEntry.setIndexNames(
    (0, "IPV4REDUNDANCY-MIB", "apIpv4RedundancyIntAddress"),
    (0, "IPV4REDUNDANCY-MIB", "apIpv4RedundancyIntVipAddress"),
    (0, "IPV4REDUNDANCY-MIB", "apIpv4RedundancyIntVRID"),
)
if mibBuilder.loadTexts:
    apIpv4RedundancyIntConfigEntry.setStatus("current")
_ApIpv4RedundancyIntAddress_Type = IpAddress
_ApIpv4RedundancyIntAddress_Object = MibTableColumn
apIpv4RedundancyIntAddress = _ApIpv4RedundancyIntAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 3, 1, 1),
    _ApIpv4RedundancyIntAddress_Type()
)
apIpv4RedundancyIntAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RedundancyIntAddress.setStatus("current")
_ApIpv4RedundancyIntVipAddress_Type = IpAddress
_ApIpv4RedundancyIntVipAddress_Object = MibTableColumn
apIpv4RedundancyIntVipAddress = _ApIpv4RedundancyIntVipAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 3, 1, 2),
    _ApIpv4RedundancyIntVipAddress_Type()
)
apIpv4RedundancyIntVipAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RedundancyIntVipAddress.setStatus("current")


class _ApIpv4RedundancyIntVRID_Type(Integer32):
    """Custom type apIpv4RedundancyIntVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ApIpv4RedundancyIntVRID_Type.__name__ = "Integer32"
_ApIpv4RedundancyIntVRID_Object = MibTableColumn
apIpv4RedundancyIntVRID = _ApIpv4RedundancyIntVRID_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 3, 1, 3),
    _ApIpv4RedundancyIntVRID_Type()
)
apIpv4RedundancyIntVRID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RedundancyIntVRID.setStatus("current")


class _ApIpv4RedundancyIntState_Type(Integer32):
    """Custom type apIpv4RedundancyIntState based on Integer32"""
    defaultValue = 1

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
        *(("backup", 2),
          ("backupshared", 3),
          ("master", 4),
          ("noVirtualRouter", 1))
    )


_ApIpv4RedundancyIntState_Type.__name__ = "Integer32"
_ApIpv4RedundancyIntState_Object = MibTableColumn
apIpv4RedundancyIntState = _ApIpv4RedundancyIntState_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 3, 1, 4),
    _ApIpv4RedundancyIntState_Type()
)
apIpv4RedundancyIntState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RedundancyIntState.setStatus("current")
_ApIpv4RedundancyIntMasterIP_Type = IpAddress
_ApIpv4RedundancyIntMasterIP_Object = MibTableColumn
apIpv4RedundancyIntMasterIP = _ApIpv4RedundancyIntMasterIP_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 3, 1, 5),
    _ApIpv4RedundancyIntMasterIP_Type()
)
apIpv4RedundancyIntMasterIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RedundancyIntMasterIP.setStatus("current")


class _ApIpv4RedundancyIntLastChange_Type(DisplayString):
    """Custom type apIpv4RedundancyIntLastChange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_ApIpv4RedundancyIntLastChange_Type.__name__ = "DisplayString"
_ApIpv4RedundancyIntLastChange_Object = MibTableColumn
apIpv4RedundancyIntLastChange = _ApIpv4RedundancyIntLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 3, 1, 6),
    _ApIpv4RedundancyIntLastChange_Type()
)
apIpv4RedundancyIntLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RedundancyIntLastChange.setStatus("current")
_ApIpv4RedundancyIntStateChanges_Type = Integer32
_ApIpv4RedundancyIntStateChanges_Object = MibTableColumn
apIpv4RedundancyIntStateChanges = _ApIpv4RedundancyIntStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 3, 1, 7),
    _ApIpv4RedundancyIntStateChanges_Type()
)
apIpv4RedundancyIntStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RedundancyIntStateChanges.setStatus("current")
_ApIpv4RedundancyIntStatus_Type = RowStatus
_ApIpv4RedundancyIntStatus_Object = MibTableColumn
apIpv4RedundancyIntStatus = _ApIpv4RedundancyIntStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 3, 1, 8),
    _ApIpv4RedundancyIntStatus_Type()
)
apIpv4RedundancyIntStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RedundancyIntStatus.setStatus("current")
_ApIpv4RedundancyVIPConfigTable_Object = MibTable
apIpv4RedundancyVIPConfigTable = _ApIpv4RedundancyVIPConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 4)
)
if mibBuilder.loadTexts:
    apIpv4RedundancyVIPConfigTable.setStatus("current")
_ApIpv4RedundancyVIPConfigEntry_Object = MibTableRow
apIpv4RedundancyVIPConfigEntry = _ApIpv4RedundancyVIPConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 4, 1)
)
apIpv4RedundancyVIPConfigEntry.setIndexNames(
    (0, "IPV4REDUNDANCY-MIB", "apIpv4RedundancyVIPIntAddress"),
    (0, "IPV4REDUNDANCY-MIB", "apIpv4RedundancyVIPAddress"),
    (0, "IPV4REDUNDANCY-MIB", "apIpv4RedundancyVIPVRID"),
)
if mibBuilder.loadTexts:
    apIpv4RedundancyVIPConfigEntry.setStatus("current")
_ApIpv4RedundancyVIPIntAddress_Type = IpAddress
_ApIpv4RedundancyVIPIntAddress_Object = MibTableColumn
apIpv4RedundancyVIPIntAddress = _ApIpv4RedundancyVIPIntAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 4, 1, 1),
    _ApIpv4RedundancyVIPIntAddress_Type()
)
apIpv4RedundancyVIPIntAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RedundancyVIPIntAddress.setStatus("current")
_ApIpv4RedundancyVIPAddress_Type = IpAddress
_ApIpv4RedundancyVIPAddress_Object = MibTableColumn
apIpv4RedundancyVIPAddress = _ApIpv4RedundancyVIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 4, 1, 2),
    _ApIpv4RedundancyVIPAddress_Type()
)
apIpv4RedundancyVIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RedundancyVIPAddress.setStatus("current")


class _ApIpv4RedundancyVIPVRID_Type(Integer32):
    """Custom type apIpv4RedundancyVIPVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ApIpv4RedundancyVIPVRID_Type.__name__ = "Integer32"
_ApIpv4RedundancyVIPVRID_Object = MibTableColumn
apIpv4RedundancyVIPVRID = _ApIpv4RedundancyVIPVRID_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 4, 1, 3),
    _ApIpv4RedundancyVIPVRID_Type()
)
apIpv4RedundancyVIPVRID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RedundancyVIPVRID.setStatus("current")


class _ApIpv4RedundancyVIPRange_Type(Integer32):
    """Custom type apIpv4RedundancyVIPRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApIpv4RedundancyVIPRange_Type.__name__ = "Integer32"
_ApIpv4RedundancyVIPRange_Object = MibTableColumn
apIpv4RedundancyVIPRange = _ApIpv4RedundancyVIPRange_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 4, 1, 4),
    _ApIpv4RedundancyVIPRange_Type()
)
apIpv4RedundancyVIPRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RedundancyVIPRange.setStatus("current")


class _ApIpv4RedundancyVIPSharedVIP_Type(Integer32):
    """Custom type apIpv4RedundancyVIPSharedVIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ApIpv4RedundancyVIPSharedVIP_Type.__name__ = "Integer32"
_ApIpv4RedundancyVIPSharedVIP_Object = MibTableColumn
apIpv4RedundancyVIPSharedVIP = _ApIpv4RedundancyVIPSharedVIP_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 4, 1, 5),
    _ApIpv4RedundancyVIPSharedVIP_Type()
)
apIpv4RedundancyVIPSharedVIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RedundancyVIPSharedVIP.setStatus("current")


class _ApIpv4RedundancyVIPState_Type(Integer32):
    """Custom type apIpv4RedundancyVIPState based on Integer32"""
    defaultValue = 1

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
        *(("backup", 2),
          ("backupshared", 3),
          ("master", 4),
          ("noVirtualRouter", 1))
    )


_ApIpv4RedundancyVIPState_Type.__name__ = "Integer32"
_ApIpv4RedundancyVIPState_Object = MibTableColumn
apIpv4RedundancyVIPState = _ApIpv4RedundancyVIPState_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 4, 1, 6),
    _ApIpv4RedundancyVIPState_Type()
)
apIpv4RedundancyVIPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RedundancyVIPState.setStatus("current")
_ApIpv4RedundancyVIPMasterIP_Type = IpAddress
_ApIpv4RedundancyVIPMasterIP_Object = MibTableColumn
apIpv4RedundancyVIPMasterIP = _ApIpv4RedundancyVIPMasterIP_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 4, 1, 7),
    _ApIpv4RedundancyVIPMasterIP_Type()
)
apIpv4RedundancyVIPMasterIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RedundancyVIPMasterIP.setStatus("current")


class _ApIpv4RedundancyVIPLastChange_Type(DisplayString):
    """Custom type apIpv4RedundancyVIPLastChange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_ApIpv4RedundancyVIPLastChange_Type.__name__ = "DisplayString"
_ApIpv4RedundancyVIPLastChange_Object = MibTableColumn
apIpv4RedundancyVIPLastChange = _ApIpv4RedundancyVIPLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 4, 1, 8),
    _ApIpv4RedundancyVIPLastChange_Type()
)
apIpv4RedundancyVIPLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RedundancyVIPLastChange.setStatus("current")
_ApIpv4RedundancyVIPStateChanges_Type = Integer32
_ApIpv4RedundancyVIPStateChanges_Object = MibTableColumn
apIpv4RedundancyVIPStateChanges = _ApIpv4RedundancyVIPStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 4, 1, 9),
    _ApIpv4RedundancyVIPStateChanges_Type()
)
apIpv4RedundancyVIPStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RedundancyVIPStateChanges.setStatus("current")
_ApIpv4RedundancyVIPStatus_Type = RowStatus
_ApIpv4RedundancyVIPStatus_Object = MibTableColumn
apIpv4RedundancyVIPStatus = _ApIpv4RedundancyVIPStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 4, 1, 10),
    _ApIpv4RedundancyVIPStatus_Type()
)
apIpv4RedundancyVIPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RedundancyVIPStatus.setStatus("current")
_ApIpv4RedundancyServConfigTable_Object = MibTable
apIpv4RedundancyServConfigTable = _ApIpv4RedundancyServConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 6)
)
if mibBuilder.loadTexts:
    apIpv4RedundancyServConfigTable.setStatus("current")
_ApIpv4RedundancyServConfigEntry_Object = MibTableRow
apIpv4RedundancyServConfigEntry = _ApIpv4RedundancyServConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 6, 1)
)
apIpv4RedundancyServConfigEntry.setIndexNames(
    (0, "IPV4REDUNDANCY-MIB", "apIpv4RedundancyServIntAddr"),
    (0, "IPV4REDUNDANCY-MIB", "apIpv4RedundancyServVRID"),
    (0, "IPV4REDUNDANCY-MIB", "apIpv4RedundancyServName"),
)
if mibBuilder.loadTexts:
    apIpv4RedundancyServConfigEntry.setStatus("current")
_ApIpv4RedundancyServIntAddr_Type = IpAddress
_ApIpv4RedundancyServIntAddr_Object = MibTableColumn
apIpv4RedundancyServIntAddr = _ApIpv4RedundancyServIntAddr_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 6, 1, 1),
    _ApIpv4RedundancyServIntAddr_Type()
)
apIpv4RedundancyServIntAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RedundancyServIntAddr.setStatus("current")


class _ApIpv4RedundancyServVRID_Type(Integer32):
    """Custom type apIpv4RedundancyServVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ApIpv4RedundancyServVRID_Type.__name__ = "Integer32"
_ApIpv4RedundancyServVRID_Object = MibTableColumn
apIpv4RedundancyServVRID = _ApIpv4RedundancyServVRID_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 6, 1, 2),
    _ApIpv4RedundancyServVRID_Type()
)
apIpv4RedundancyServVRID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RedundancyServVRID.setStatus("current")


class _ApIpv4RedundancyServName_Type(DisplayString):
    """Custom type apIpv4RedundancyServName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApIpv4RedundancyServName_Type.__name__ = "DisplayString"
_ApIpv4RedundancyServName_Object = MibTableColumn
apIpv4RedundancyServName = _ApIpv4RedundancyServName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 6, 1, 3),
    _ApIpv4RedundancyServName_Type()
)
apIpv4RedundancyServName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RedundancyServName.setStatus("current")


class _ApIpv4RedundancyServType_Type(Integer32):
    """Custom type apIpv4RedundancyServType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("script", 3),
          ("unknown", 0),
          ("uplink", 1))
    )


_ApIpv4RedundancyServType_Type.__name__ = "Integer32"
_ApIpv4RedundancyServType_Object = MibTableColumn
apIpv4RedundancyServType = _ApIpv4RedundancyServType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 6, 1, 4),
    _ApIpv4RedundancyServType_Type()
)
apIpv4RedundancyServType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RedundancyServType.setStatus("current")
_ApIpv4RedundancyServStatus_Type = RowStatus
_ApIpv4RedundancyServStatus_Object = MibTableColumn
apIpv4RedundancyServStatus = _ApIpv4RedundancyServStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 6, 1, 5),
    _ApIpv4RedundancyServStatus_Type()
)
apIpv4RedundancyServStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RedundancyServStatus.setStatus("current")


class _ApIpv4RedundancyEnabled_Type(Integer32):
    """Custom type apIpv4RedundancyEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ApIpv4RedundancyEnabled_Type.__name__ = "Integer32"
_ApIpv4RedundancyEnabled_Object = MibScalar
apIpv4RedundancyEnabled = _ApIpv4RedundancyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8, 7),
    _ApIpv4RedundancyEnabled_Type()
)
apIpv4RedundancyEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RedundancyEnabled.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPV4REDUNDANCY-MIB",
    **{"ipv4RedundancyMib": ipv4RedundancyMib,
       "apIpv4RedundancyVRConfigTable": apIpv4RedundancyVRConfigTable,
       "apIpv4RedundancyVRConfigEntry": apIpv4RedundancyVRConfigEntry,
       "apIpv4RedundancyVRID": apIpv4RedundancyVRID,
       "apIpv4RedundancyVRIntAddr": apIpv4RedundancyVRIntAddr,
       "apIpv4RedundancyConfigPriority": apIpv4RedundancyConfigPriority,
       "apIpv4RedundancyAdPriority": apIpv4RedundancyAdPriority,
       "apIpv4RedundancyName": apIpv4RedundancyName,
       "apIpv4RedundancyVRPreempt": apIpv4RedundancyVRPreempt,
       "apIpv4RedundancyVRState": apIpv4RedundancyVRState,
       "apIpv4RedundancyVRMasterIP": apIpv4RedundancyVRMasterIP,
       "apIpv4RedundancyVRLastChange": apIpv4RedundancyVRLastChange,
       "apIpv4RedundancyVRStateChanges": apIpv4RedundancyVRStateChanges,
       "apIpv4RedundancyVRStatus": apIpv4RedundancyVRStatus,
       "apIpv4RedundancyIntConfigTable": apIpv4RedundancyIntConfigTable,
       "apIpv4RedundancyIntConfigEntry": apIpv4RedundancyIntConfigEntry,
       "apIpv4RedundancyIntAddress": apIpv4RedundancyIntAddress,
       "apIpv4RedundancyIntVipAddress": apIpv4RedundancyIntVipAddress,
       "apIpv4RedundancyIntVRID": apIpv4RedundancyIntVRID,
       "apIpv4RedundancyIntState": apIpv4RedundancyIntState,
       "apIpv4RedundancyIntMasterIP": apIpv4RedundancyIntMasterIP,
       "apIpv4RedundancyIntLastChange": apIpv4RedundancyIntLastChange,
       "apIpv4RedundancyIntStateChanges": apIpv4RedundancyIntStateChanges,
       "apIpv4RedundancyIntStatus": apIpv4RedundancyIntStatus,
       "apIpv4RedundancyVIPConfigTable": apIpv4RedundancyVIPConfigTable,
       "apIpv4RedundancyVIPConfigEntry": apIpv4RedundancyVIPConfigEntry,
       "apIpv4RedundancyVIPIntAddress": apIpv4RedundancyVIPIntAddress,
       "apIpv4RedundancyVIPAddress": apIpv4RedundancyVIPAddress,
       "apIpv4RedundancyVIPVRID": apIpv4RedundancyVIPVRID,
       "apIpv4RedundancyVIPRange": apIpv4RedundancyVIPRange,
       "apIpv4RedundancyVIPSharedVIP": apIpv4RedundancyVIPSharedVIP,
       "apIpv4RedundancyVIPState": apIpv4RedundancyVIPState,
       "apIpv4RedundancyVIPMasterIP": apIpv4RedundancyVIPMasterIP,
       "apIpv4RedundancyVIPLastChange": apIpv4RedundancyVIPLastChange,
       "apIpv4RedundancyVIPStateChanges": apIpv4RedundancyVIPStateChanges,
       "apIpv4RedundancyVIPStatus": apIpv4RedundancyVIPStatus,
       "apIpv4RedundancyServConfigTable": apIpv4RedundancyServConfigTable,
       "apIpv4RedundancyServConfigEntry": apIpv4RedundancyServConfigEntry,
       "apIpv4RedundancyServIntAddr": apIpv4RedundancyServIntAddr,
       "apIpv4RedundancyServVRID": apIpv4RedundancyServVRID,
       "apIpv4RedundancyServName": apIpv4RedundancyServName,
       "apIpv4RedundancyServType": apIpv4RedundancyServType,
       "apIpv4RedundancyServStatus": apIpv4RedundancyServStatus,
       "apIpv4RedundancyEnabled": apIpv4RedundancyEnabled}
)
