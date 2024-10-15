# SNMP MIB module (EXTREME-VM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-VM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:42:31 2024
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

extremeVM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39)
)
extremeVM.setRevisions(
        ("2011-04-18 00:00",
         "2010-02-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VMVPPSynchType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("global", 1),
          ("specific", 2))
    )



class CounterDirection(Integer32, TextualConvention):
    status = "current"
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
        *(("both", 3),
          ("egress-only", 2),
          ("ingress-only", 1),
          ("none", 0))
    )



# MIB Managed Objects in the order of their OIDs

_ExtremeVMGeneral_ObjectIdentity = ObjectIdentity
extremeVMGeneral = _ExtremeVMGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 1)
)
_ExtremeVMFTPServerTable_Object = MibTable
extremeVMFTPServerTable = _ExtremeVMFTPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 1)
)
if mibBuilder.loadTexts:
    extremeVMFTPServerTable.setStatus("current")
_ExtremeVMFTPServerEntry_Object = MibTableRow
extremeVMFTPServerEntry = _ExtremeVMFTPServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 1, 1)
)
extremeVMFTPServerEntry.setIndexNames(
    (0, "EXTREME-VM-MIB", "extremeVMFTPServerType"),
)
if mibBuilder.loadTexts:
    extremeVMFTPServerEntry.setStatus("current")


class _ExtremeVMFTPServerType_Type(Integer32):
    """Custom type extremeVMFTPServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("primary", 1))
    )


_ExtremeVMFTPServerType_Type.__name__ = "Integer32"
_ExtremeVMFTPServerType_Object = MibTableColumn
extremeVMFTPServerType = _ExtremeVMFTPServerType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 1, 1, 1),
    _ExtremeVMFTPServerType_Type()
)
extremeVMFTPServerType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeVMFTPServerType.setStatus("current")
_ExtremeVMFTPAddrType_Type = InetAddressType
_ExtremeVMFTPAddrType_Object = MibTableColumn
extremeVMFTPAddrType = _ExtremeVMFTPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 1, 1, 2),
    _ExtremeVMFTPAddrType_Type()
)
extremeVMFTPAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeVMFTPAddrType.setStatus("current")
_ExtremeVMFTPServer_Type = InetAddress
_ExtremeVMFTPServer_Object = MibTableColumn
extremeVMFTPServer = _ExtremeVMFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 1, 1, 3),
    _ExtremeVMFTPServer_Type()
)
extremeVMFTPServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVMFTPServer.setStatus("current")


class _ExtremeVMFTPSynchInterval_Type(Integer32):
    """Custom type extremeVMFTPSynchInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_ExtremeVMFTPSynchInterval_Type.__name__ = "Integer32"
_ExtremeVMFTPSynchInterval_Object = MibTableColumn
extremeVMFTPSynchInterval = _ExtremeVMFTPSynchInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 1, 1, 4),
    _ExtremeVMFTPSynchInterval_Type()
)
extremeVMFTPSynchInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVMFTPSynchInterval.setStatus("current")
if mibBuilder.loadTexts:
    extremeVMFTPSynchInterval.setUnits("seconds")
_ExtremeVMFTPRowStatus_Type = RowStatus
_ExtremeVMFTPRowStatus_Object = MibTableColumn
extremeVMFTPRowStatus = _ExtremeVMFTPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 1, 1, 5),
    _ExtremeVMFTPRowStatus_Type()
)
extremeVMFTPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVMFTPRowStatus.setStatus("current")


class _ExtremeVMFTPPathName_Type(DisplayString):
    """Custom type extremeVMFTPPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeVMFTPPathName_Type.__name__ = "DisplayString"
_ExtremeVMFTPPathName_Object = MibTableColumn
extremeVMFTPPathName = _ExtremeVMFTPPathName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 1, 1, 6),
    _ExtremeVMFTPPathName_Type()
)
extremeVMFTPPathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeVMFTPPathName.setStatus("current")


class _ExtremeVMFTPUsername_Type(DisplayString):
    """Custom type extremeVMFTPUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeVMFTPUsername_Type.__name__ = "DisplayString"
_ExtremeVMFTPUsername_Object = MibTableColumn
extremeVMFTPUsername = _ExtremeVMFTPUsername_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 1, 1, 7),
    _ExtremeVMFTPUsername_Type()
)
extremeVMFTPUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeVMFTPUsername.setStatus("current")


class _ExtremeVMFTPPassword_Type(DisplayString):
    """Custom type extremeVMFTPPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeVMFTPPassword_Type.__name__ = "DisplayString"
_ExtremeVMFTPPassword_Object = MibTableColumn
extremeVMFTPPassword = _ExtremeVMFTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 1, 1, 8),
    _ExtremeVMFTPPassword_Type()
)
extremeVMFTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeVMFTPPassword.setStatus("current")


class _ExtremeVMFTPPolicyDir_Type(DisplayString):
    """Custom type extremeVMFTPPolicyDir based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeVMFTPPolicyDir_Type.__name__ = "DisplayString"
_ExtremeVMFTPPolicyDir_Object = MibScalar
extremeVMFTPPolicyDir = _ExtremeVMFTPPolicyDir_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 2),
    _ExtremeVMFTPPolicyDir_Type()
)
extremeVMFTPPolicyDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeVMFTPPolicyDir.setStatus("deprecated")
_ExtremeVMLastSynch_Type = TimeStamp
_ExtremeVMLastSynch_Object = MibScalar
extremeVMLastSynch = _ExtremeVMLastSynch_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 3),
    _ExtremeVMLastSynch_Type()
)
extremeVMLastSynch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVMLastSynch.setStatus("current")


class _ExtremeVMLastSynchStatus_Type(Integer32):
    """Custom type extremeVMLastSynchStatus based on Integer32"""
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
        *(("accessDenied", 2),
          ("serverNotConfigured", 4),
          ("serverTimeout", 3),
          ("success", 1))
    )


_ExtremeVMLastSynchStatus_Type.__name__ = "Integer32"
_ExtremeVMLastSynchStatus_Object = MibScalar
extremeVMLastSynchStatus = _ExtremeVMLastSynchStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 4),
    _ExtremeVMLastSynchStatus_Type()
)
extremeVMLastSynchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVMLastSynchStatus.setStatus("current")


class _ExtremeVMSynchAdminState_Type(Integer32):
    """Custom type extremeVMSynchAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("synchronizeNow", 2))
    )


_ExtremeVMSynchAdminState_Type.__name__ = "Integer32"
_ExtremeVMSynchAdminState_Object = MibScalar
extremeVMSynchAdminState = _ExtremeVMSynchAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 5),
    _ExtremeVMSynchAdminState_Type()
)
extremeVMSynchAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeVMSynchAdminState.setStatus("current")


class _ExtremeVMSynchOperState_Type(Integer32):
    """Custom type extremeVMSynchOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("synchronizing", 2))
    )


_ExtremeVMSynchOperState_Type.__name__ = "Integer32"
_ExtremeVMSynchOperState_Object = MibScalar
extremeVMSynchOperState = _ExtremeVMSynchOperState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 6),
    _ExtremeVMSynchOperState_Type()
)
extremeVMSynchOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVMSynchOperState.setStatus("current")
_ExtremeVMTrackingEnabled_Type = TruthValue
_ExtremeVMTrackingEnabled_Object = MibScalar
extremeVMTrackingEnabled = _ExtremeVMTrackingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 7),
    _ExtremeVMTrackingEnabled_Type()
)
extremeVMTrackingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeVMTrackingEnabled.setStatus("current")
_ExtremeVMPortConfigTable_Object = MibTable
extremeVMPortConfigTable = _ExtremeVMPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 8)
)
if mibBuilder.loadTexts:
    extremeVMPortConfigTable.setStatus("current")
_ExtremeVMPortConfigEntry_Object = MibTableRow
extremeVMPortConfigEntry = _ExtremeVMPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 8, 1)
)
extremeVMPortConfigEntry.setIndexNames(
    (0, "EXTREME-VM-MIB", "extremeVMPortConfigIfIndex"),
)
if mibBuilder.loadTexts:
    extremeVMPortConfigEntry.setStatus("current")
_ExtremeVMPortConfigIfIndex_Type = Integer32
_ExtremeVMPortConfigIfIndex_Object = MibTableColumn
extremeVMPortConfigIfIndex = _ExtremeVMPortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 8, 1, 1),
    _ExtremeVMPortConfigIfIndex_Type()
)
extremeVMPortConfigIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeVMPortConfigIfIndex.setStatus("current")
_ExtremeVMPortConfigVMTrackingEnabled_Type = TruthValue
_ExtremeVMPortConfigVMTrackingEnabled_Object = MibTableColumn
extremeVMPortConfigVMTrackingEnabled = _ExtremeVMPortConfigVMTrackingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 8, 1, 2),
    _ExtremeVMPortConfigVMTrackingEnabled_Type()
)
extremeVMPortConfigVMTrackingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeVMPortConfigVMTrackingEnabled.setStatus("current")
_ExtremeVMPortConfigVMTrackingDynVlanEnabled_Type = TruthValue
_ExtremeVMPortConfigVMTrackingDynVlanEnabled_Object = MibTableColumn
extremeVMPortConfigVMTrackingDynVlanEnabled = _ExtremeVMPortConfigVMTrackingDynVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 8, 1, 3),
    _ExtremeVMPortConfigVMTrackingDynVlanEnabled_Type()
)
extremeVMPortConfigVMTrackingDynVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeVMPortConfigVMTrackingDynVlanEnabled.setStatus("current")
_ExtremeVMVPP_ObjectIdentity = ObjectIdentity
extremeVMVPP = _ExtremeVMVPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2)
)
_ExtremeVMVPPTable_Object = MibTable
extremeVMVPPTable = _ExtremeVMVPPTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 1)
)
if mibBuilder.loadTexts:
    extremeVMVPPTable.setStatus("current")
_ExtremeVMVPPEntry_Object = MibTableRow
extremeVMVPPEntry = _ExtremeVMVPPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 1, 1)
)
extremeVMVPPEntry.setIndexNames(
    (0, "EXTREME-VM-MIB", "extremeVMVPPType"),
    (0, "EXTREME-VM-MIB", "extremeVMVPPName"),
)
if mibBuilder.loadTexts:
    extremeVMVPPEntry.setStatus("current")


class _ExtremeVMVPPType_Type(Integer32):
    """Custom type extremeVMVPPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("network", 1))
    )


_ExtremeVMVPPType_Type.__name__ = "Integer32"
_ExtremeVMVPPType_Object = MibTableColumn
extremeVMVPPType = _ExtremeVMVPPType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 1, 1, 1),
    _ExtremeVMVPPType_Type()
)
extremeVMVPPType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeVMVPPType.setStatus("current")


class _ExtremeVMVPPName_Type(DisplayString):
    """Custom type extremeVMVPPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeVMVPPName_Type.__name__ = "DisplayString"
_ExtremeVMVPPName_Object = MibTableColumn
extremeVMVPPName = _ExtremeVMVPPName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 1, 1, 2),
    _ExtremeVMVPPName_Type()
)
extremeVMVPPName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeVMVPPName.setStatus("current")


class _ExtremeVMVPPControl_Type(Integer32):
    """Custom type extremeVMVPPControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 2),
          ("synchronizeNow", 1))
    )


_ExtremeVMVPPControl_Type.__name__ = "Integer32"
_ExtremeVMVPPControl_Object = MibTableColumn
extremeVMVPPControl = _ExtremeVMVPPControl_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 1, 1, 3),
    _ExtremeVMVPPControl_Type()
)
extremeVMVPPControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeVMVPPControl.setStatus("current")
_ExtremeVMVPPRowStatus_Type = RowStatus
_ExtremeVMVPPRowStatus_Object = MibTableColumn
extremeVMVPPRowStatus = _ExtremeVMVPPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 1, 1, 4),
    _ExtremeVMVPPRowStatus_Type()
)
extremeVMVPPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVMVPPRowStatus.setStatus("current")
_ExtremeVMVPPCounter_Type = CounterDirection
_ExtremeVMVPPCounter_Object = MibTableColumn
extremeVMVPPCounter = _ExtremeVMVPPCounter_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 1, 1, 5),
    _ExtremeVMVPPCounter_Type()
)
extremeVMVPPCounter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVMVPPCounter.setStatus("current")


class _ExtremeVMVPPVLANTag_Type(Integer32):
    """Custom type extremeVMVPPVLANTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ExtremeVMVPPVLANTag_Type.__name__ = "Integer32"
_ExtremeVMVPPVLANTag_Object = MibTableColumn
extremeVMVPPVLANTag = _ExtremeVMVPPVLANTag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 1, 1, 6),
    _ExtremeVMVPPVLANTag_Type()
)
extremeVMVPPVLANTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVMVPPVLANTag.setStatus("current")


class _ExtremeVMVPPVLANVRName_Type(DisplayString):
    """Custom type extremeVMVPPVLANVRName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeVMVPPVLANVRName_Type.__name__ = "DisplayString"
_ExtremeVMVPPVLANVRName_Object = MibTableColumn
extremeVMVPPVLANVRName = _ExtremeVMVPPVLANVRName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 1, 1, 7),
    _ExtremeVMVPPVLANVRName_Type()
)
extremeVMVPPVLANVRName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVMVPPVLANVRName.setStatus("current")
_ExtremeVMMappingTable_Object = MibTable
extremeVMMappingTable = _ExtremeVMMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 2)
)
if mibBuilder.loadTexts:
    extremeVMMappingTable.setStatus("current")
_ExtremeVMMappingEntry_Object = MibTableRow
extremeVMMappingEntry = _ExtremeVMMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 2, 1)
)
extremeVMMappingEntry.setIndexNames(
    (0, "EXTREME-VM-MIB", "extremeVMMappingType"),
    (0, "EXTREME-VM-MIB", "extremeVMMappingMAC"),
)
if mibBuilder.loadTexts:
    extremeVMMappingEntry.setStatus("current")


class _ExtremeVMMappingType_Type(Integer32):
    """Custom type extremeVMMappingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("network", 1))
    )


_ExtremeVMMappingType_Type.__name__ = "Integer32"
_ExtremeVMMappingType_Object = MibTableColumn
extremeVMMappingType = _ExtremeVMMappingType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 2, 1, 1),
    _ExtremeVMMappingType_Type()
)
extremeVMMappingType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeVMMappingType.setStatus("current")
_ExtremeVMMappingMAC_Type = MacAddress
_ExtremeVMMappingMAC_Object = MibTableColumn
extremeVMMappingMAC = _ExtremeVMMappingMAC_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 2, 1, 2),
    _ExtremeVMMappingMAC_Type()
)
extremeVMMappingMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeVMMappingMAC.setStatus("current")
_ExtremeVMMappingIngressVPPName_Type = DisplayString
_ExtremeVMMappingIngressVPPName_Object = MibTableColumn
extremeVMMappingIngressVPPName = _ExtremeVMMappingIngressVPPName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 2, 1, 3),
    _ExtremeVMMappingIngressVPPName_Type()
)
extremeVMMappingIngressVPPName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVMMappingIngressVPPName.setStatus("deprecated")
_ExtremeVMMappingEgressVPPName_Type = DisplayString
_ExtremeVMMappingEgressVPPName_Object = MibTableColumn
extremeVMMappingEgressVPPName = _ExtremeVMMappingEgressVPPName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 2, 1, 4),
    _ExtremeVMMappingEgressVPPName_Type()
)
extremeVMMappingEgressVPPName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVMMappingEgressVPPName.setStatus("deprecated")


class _ExtremeVMMappingStatus_Type(Integer32):
    """Custom type extremeVMMappingStatus based on Integer32"""
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
        *(("vppInvalid", 3),
          ("vppMissing", 2),
          ("vppNotMapped", 4),
          ("vppValid", 1))
    )


_ExtremeVMMappingStatus_Type.__name__ = "Integer32"
_ExtremeVMMappingStatus_Object = MibTableColumn
extremeVMMappingStatus = _ExtremeVMMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 2, 1, 5),
    _ExtremeVMMappingStatus_Type()
)
extremeVMMappingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVMMappingStatus.setStatus("current")
_ExtremeVMMappingRowStatus_Type = RowStatus
_ExtremeVMMappingRowStatus_Object = MibTableColumn
extremeVMMappingRowStatus = _ExtremeVMMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 2, 1, 6),
    _ExtremeVMMappingRowStatus_Type()
)
extremeVMMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVMMappingRowStatus.setStatus("current")


class _ExtremeVMMappingVPPName_Type(DisplayString):
    """Custom type extremeVMMappingVPPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeVMMappingVPPName_Type.__name__ = "DisplayString"
_ExtremeVMMappingVPPName_Object = MibTableColumn
extremeVMMappingVPPName = _ExtremeVMMappingVPPName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 2, 1, 7),
    _ExtremeVMMappingVPPName_Type()
)
extremeVMMappingVPPName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVMMappingVPPName.setStatus("current")


class _ExtremeVMMappingVLANTag_Type(Integer32):
    """Custom type extremeVMMappingVLANTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ExtremeVMMappingVLANTag_Type.__name__ = "Integer32"
_ExtremeVMMappingVLANTag_Object = MibTableColumn
extremeVMMappingVLANTag = _ExtremeVMMappingVLANTag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 2, 1, 8),
    _ExtremeVMMappingVLANTag_Type()
)
extremeVMMappingVLANTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVMMappingVLANTag.setStatus("current")


class _ExtremeVMMappingVLANVRName_Type(DisplayString):
    """Custom type extremeVMMappingVLANVRName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeVMMappingVLANVRName_Type.__name__ = "DisplayString"
_ExtremeVMMappingVLANVRName_Object = MibTableColumn
extremeVMMappingVLANVRName = _ExtremeVMMappingVLANVRName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 2, 1, 9),
    _ExtremeVMMappingVLANVRName_Type()
)
extremeVMMappingVLANVRName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVMMappingVLANVRName.setStatus("current")
_ExtremeVMVPP2PolicyTable_Object = MibTable
extremeVMVPP2PolicyTable = _ExtremeVMVPP2PolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 3)
)
if mibBuilder.loadTexts:
    extremeVMVPP2PolicyTable.setStatus("deprecated")
_ExtremeVMVPP2PolicyEntry_Object = MibTableRow
extremeVMVPP2PolicyEntry = _ExtremeVMVPP2PolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 3, 1)
)
extremeVMVPP2PolicyEntry.setIndexNames(
    (0, "EXTREME-VM-MIB", "extremeVMVPP2PolicyVPPName"),
    (0, "EXTREME-VM-MIB", "extremeVMVPP2PolicyPolicyName"),
    (0, "EXTREME-VM-MIB", "extremeVMVPP2PolicyType"),
)
if mibBuilder.loadTexts:
    extremeVMVPP2PolicyEntry.setStatus("current")


class _ExtremeVMVPP2PolicyVPPName_Type(DisplayString):
    """Custom type extremeVMVPP2PolicyVPPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeVMVPP2PolicyVPPName_Type.__name__ = "DisplayString"
_ExtremeVMVPP2PolicyVPPName_Object = MibTableColumn
extremeVMVPP2PolicyVPPName = _ExtremeVMVPP2PolicyVPPName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 3, 1, 1),
    _ExtremeVMVPP2PolicyVPPName_Type()
)
extremeVMVPP2PolicyVPPName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeVMVPP2PolicyVPPName.setStatus("current")


class _ExtremeVMVPP2PolicyPolicyName_Type(DisplayString):
    """Custom type extremeVMVPP2PolicyPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeVMVPP2PolicyPolicyName_Type.__name__ = "DisplayString"
_ExtremeVMVPP2PolicyPolicyName_Object = MibTableColumn
extremeVMVPP2PolicyPolicyName = _ExtremeVMVPP2PolicyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 3, 1, 2),
    _ExtremeVMVPP2PolicyPolicyName_Type()
)
extremeVMVPP2PolicyPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeVMVPP2PolicyPolicyName.setStatus("current")


class _ExtremeVMVPP2PolicyType_Type(Integer32):
    """Custom type extremeVMVPP2PolicyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamicACL", 2),
          ("policyFile", 1))
    )


_ExtremeVMVPP2PolicyType_Type.__name__ = "Integer32"
_ExtremeVMVPP2PolicyType_Object = MibTableColumn
extremeVMVPP2PolicyType = _ExtremeVMVPP2PolicyType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 3, 1, 3),
    _ExtremeVMVPP2PolicyType_Type()
)
extremeVMVPP2PolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeVMVPP2PolicyType.setStatus("current")
_ExtremeVMVPP2PolicyOrder_Type = Integer32
_ExtremeVMVPP2PolicyOrder_Object = MibTableColumn
extremeVMVPP2PolicyOrder = _ExtremeVMVPP2PolicyOrder_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 3, 1, 4),
    _ExtremeVMVPP2PolicyOrder_Type()
)
extremeVMVPP2PolicyOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVMVPP2PolicyOrder.setStatus("current")
_ExtremeVMVPP2PolicyRowStatus_Type = RowStatus
_ExtremeVMVPP2PolicyRowStatus_Object = MibTableColumn
extremeVMVPP2PolicyRowStatus = _ExtremeVMVPP2PolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 3, 1, 5),
    _ExtremeVMVPP2PolicyRowStatus_Type()
)
extremeVMVPP2PolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVMVPP2PolicyRowStatus.setStatus("current")
_ExtremeVMVPPDetailTable_Object = MibTable
extremeVMVPPDetailTable = _ExtremeVMVPPDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 4)
)
if mibBuilder.loadTexts:
    extremeVMVPPDetailTable.setStatus("current")
_ExtremeVMVPPDetailEntry_Object = MibTableRow
extremeVMVPPDetailEntry = _ExtremeVMVPPDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 4, 1)
)
extremeVMVPPDetailEntry.setIndexNames(
    (0, "EXTREME-VM-MIB", "extremeVMVPPDetailVPPName"),
    (0, "EXTREME-VM-MIB", "extremeVMVPPDetailDirection"),
    (0, "EXTREME-VM-MIB", "extremeVMVPPDetailType"),
    (0, "EXTREME-VM-MIB", "extremeVMVPPDetailOrder"),
    (0, "EXTREME-VM-MIB", "extremeVMVPPDetailPolicyName"),
)
if mibBuilder.loadTexts:
    extremeVMVPPDetailEntry.setStatus("current")
_ExtremeVMVPPDetailVPPName_Type = DisplayString
_ExtremeVMVPPDetailVPPName_Object = MibTableColumn
extremeVMVPPDetailVPPName = _ExtremeVMVPPDetailVPPName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 4, 1, 1),
    _ExtremeVMVPPDetailVPPName_Type()
)
extremeVMVPPDetailVPPName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeVMVPPDetailVPPName.setStatus("current")


class _ExtremeVMVPPDetailDirection_Type(Integer32):
    """Custom type extremeVMVPPDetailDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )


_ExtremeVMVPPDetailDirection_Type.__name__ = "Integer32"
_ExtremeVMVPPDetailDirection_Object = MibTableColumn
extremeVMVPPDetailDirection = _ExtremeVMVPPDetailDirection_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 4, 1, 2),
    _ExtremeVMVPPDetailDirection_Type()
)
extremeVMVPPDetailDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeVMVPPDetailDirection.setStatus("current")


class _ExtremeVMVPPDetailType_Type(Integer32):
    """Custom type extremeVMVPPDetailType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamicACL", 2),
          ("policyFile", 1))
    )


_ExtremeVMVPPDetailType_Type.__name__ = "Integer32"
_ExtremeVMVPPDetailType_Object = MibTableColumn
extremeVMVPPDetailType = _ExtremeVMVPPDetailType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 4, 1, 3),
    _ExtremeVMVPPDetailType_Type()
)
extremeVMVPPDetailType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeVMVPPDetailType.setStatus("current")
_ExtremeVMVPPDetailOrder_Type = Integer32
_ExtremeVMVPPDetailOrder_Object = MibTableColumn
extremeVMVPPDetailOrder = _ExtremeVMVPPDetailOrder_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 4, 1, 4),
    _ExtremeVMVPPDetailOrder_Type()
)
extremeVMVPPDetailOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeVMVPPDetailOrder.setStatus("current")
_ExtremeVMVPPDetailPolicyName_Type = DisplayString
_ExtremeVMVPPDetailPolicyName_Object = MibTableColumn
extremeVMVPPDetailPolicyName = _ExtremeVMVPPDetailPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 4, 1, 5),
    _ExtremeVMVPPDetailPolicyName_Type()
)
extremeVMVPPDetailPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeVMVPPDetailPolicyName.setStatus("current")
_ExtremeVMVPPDetailRowStatus_Type = RowStatus
_ExtremeVMVPPDetailRowStatus_Object = MibTableColumn
extremeVMVPPDetailRowStatus = _ExtremeVMVPPDetailRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 4, 1, 6),
    _ExtremeVMVPPDetailRowStatus_Type()
)
extremeVMVPPDetailRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVMVPPDetailRowStatus.setStatus("current")
_ExtremeVMDetected_ObjectIdentity = ObjectIdentity
extremeVMDetected = _ExtremeVMDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 3)
)
_ExtremeVMDetectedNumber_Type = Gauge32
_ExtremeVMDetectedNumber_Object = MibScalar
extremeVMDetectedNumber = _ExtremeVMDetectedNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 1),
    _ExtremeVMDetectedNumber_Type()
)
extremeVMDetectedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVMDetectedNumber.setStatus("current")
_ExtremeVMDetectedTable_Object = MibTable
extremeVMDetectedTable = _ExtremeVMDetectedTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2)
)
if mibBuilder.loadTexts:
    extremeVMDetectedTable.setStatus("current")
_ExtremeVMDetectedEntry_Object = MibTableRow
extremeVMDetectedEntry = _ExtremeVMDetectedEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1)
)
extremeVMDetectedEntry.setIndexNames(
    (0, "EXTREME-VM-MIB", "extremeVMDetectedMAC"),
)
if mibBuilder.loadTexts:
    extremeVMDetectedEntry.setStatus("current")
_ExtremeVMDetectedMAC_Type = MacAddress
_ExtremeVMDetectedMAC_Object = MibTableColumn
extremeVMDetectedMAC = _ExtremeVMDetectedMAC_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 1),
    _ExtremeVMDetectedMAC_Type()
)
extremeVMDetectedMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeVMDetectedMAC.setStatus("current")


class _ExtremeVMDetectedVMName_Type(DisplayString):
    """Custom type extremeVMDetectedVMName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeVMDetectedVMName_Type.__name__ = "DisplayString"
_ExtremeVMDetectedVMName_Object = MibTableColumn
extremeVMDetectedVMName = _ExtremeVMDetectedVMName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 2),
    _ExtremeVMDetectedVMName_Type()
)
extremeVMDetectedVMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVMDetectedVMName.setStatus("current")
_ExtremeVMDetectedIngressVPPName_Type = DisplayString
_ExtremeVMDetectedIngressVPPName_Object = MibTableColumn
extremeVMDetectedIngressVPPName = _ExtremeVMDetectedIngressVPPName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 3),
    _ExtremeVMDetectedIngressVPPName_Type()
)
extremeVMDetectedIngressVPPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVMDetectedIngressVPPName.setStatus("deprecated")
_ExtremeVMDetectedEgressVPPName_Type = DisplayString
_ExtremeVMDetectedEgressVPPName_Object = MibTableColumn
extremeVMDetectedEgressVPPName = _ExtremeVMDetectedEgressVPPName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 4),
    _ExtremeVMDetectedEgressVPPName_Type()
)
extremeVMDetectedEgressVPPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVMDetectedEgressVPPName.setStatus("deprecated")
_ExtremeVMDetectedIfIndex_Type = Integer32
_ExtremeVMDetectedIfIndex_Object = MibTableColumn
extremeVMDetectedIfIndex = _ExtremeVMDetectedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 5),
    _ExtremeVMDetectedIfIndex_Type()
)
extremeVMDetectedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVMDetectedIfIndex.setStatus("current")


class _ExtremeVMDetectedAdminStatus_Type(Integer32):
    """Custom type extremeVMDetectedAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authenticating", 1),
          ("idle", 2))
    )


_ExtremeVMDetectedAdminStatus_Type.__name__ = "Integer32"
_ExtremeVMDetectedAdminStatus_Object = MibTableColumn
extremeVMDetectedAdminStatus = _ExtremeVMDetectedAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 6),
    _ExtremeVMDetectedAdminStatus_Type()
)
extremeVMDetectedAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeVMDetectedAdminStatus.setStatus("current")


class _ExtremeVMDetectedOperStatus_Type(Integer32):
    """Custom type extremeVMDetectedOperStatus based on Integer32"""
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
        *(("authenticatedLocally", 3),
          ("authenticatedNetwork", 2),
          ("authenticating", 1),
          ("authenticationDenied", 4),
          ("notAuthenticated", 5))
    )


_ExtremeVMDetectedOperStatus_Type.__name__ = "Integer32"
_ExtremeVMDetectedOperStatus_Object = MibTableColumn
extremeVMDetectedOperStatus = _ExtremeVMDetectedOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 7),
    _ExtremeVMDetectedOperStatus_Type()
)
extremeVMDetectedOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVMDetectedOperStatus.setStatus("current")


class _ExtremeVMDetectedResultIngress_Type(Integer32):
    """Custom type extremeVMDetectedResultIngress based on Integer32"""
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
        *(("policyApplied", 1),
          ("policyInvalid", 3),
          ("policyNotApplied", 2),
          ("policyNotFound", 4),
          ("policyNotMapped", 5))
    )


_ExtremeVMDetectedResultIngress_Type.__name__ = "Integer32"
_ExtremeVMDetectedResultIngress_Object = MibTableColumn
extremeVMDetectedResultIngress = _ExtremeVMDetectedResultIngress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 8),
    _ExtremeVMDetectedResultIngress_Type()
)
extremeVMDetectedResultIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVMDetectedResultIngress.setStatus("current")


class _ExtremeVMDetectedResultEgress_Type(Integer32):
    """Custom type extremeVMDetectedResultEgress based on Integer32"""
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
        *(("policyApplied", 1),
          ("policyInvalid", 3),
          ("policyNotApplied", 2),
          ("policyNotFound", 4),
          ("policyNotMapped", 5))
    )


_ExtremeVMDetectedResultEgress_Type.__name__ = "Integer32"
_ExtremeVMDetectedResultEgress_Object = MibTableColumn
extremeVMDetectedResultEgress = _ExtremeVMDetectedResultEgress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 9),
    _ExtremeVMDetectedResultEgress_Type()
)
extremeVMDetectedResultEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVMDetectedResultEgress.setStatus("current")


class _ExtremeVMDetectedIngErrPolicies_Type(OctetString):
    """Custom type extremeVMDetectedIngErrPolicies based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_ExtremeVMDetectedIngErrPolicies_Type.__name__ = "OctetString"
_ExtremeVMDetectedIngErrPolicies_Object = MibTableColumn
extremeVMDetectedIngErrPolicies = _ExtremeVMDetectedIngErrPolicies_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 10),
    _ExtremeVMDetectedIngErrPolicies_Type()
)
extremeVMDetectedIngErrPolicies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVMDetectedIngErrPolicies.setStatus("current")


class _ExtremeVMDetectedEgrErrPolicies_Type(OctetString):
    """Custom type extremeVMDetectedEgrErrPolicies based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_ExtremeVMDetectedEgrErrPolicies_Type.__name__ = "OctetString"
_ExtremeVMDetectedEgrErrPolicies_Object = MibTableColumn
extremeVMDetectedEgrErrPolicies = _ExtremeVMDetectedEgrErrPolicies_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 11),
    _ExtremeVMDetectedEgrErrPolicies_Type()
)
extremeVMDetectedEgrErrPolicies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVMDetectedEgrErrPolicies.setStatus("current")


class _ExtremeVMDetectedVPPName_Type(DisplayString):
    """Custom type extremeVMDetectedVPPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeVMDetectedVPPName_Type.__name__ = "DisplayString"
_ExtremeVMDetectedVPPName_Object = MibTableColumn
extremeVMDetectedVPPName = _ExtremeVMDetectedVPPName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 12),
    _ExtremeVMDetectedVPPName_Type()
)
extremeVMDetectedVPPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVMDetectedVPPName.setStatus("current")


class _ExtremeVMDetectedVPPResult_Type(Integer32):
    """Custom type extremeVMDetectedVPPResult based on Integer32"""
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
        *(("vppInvalid", 3),
          ("vppMapped", 1),
          ("vppMissing", 4),
          ("vppNotMapped", 2))
    )


_ExtremeVMDetectedVPPResult_Type.__name__ = "Integer32"
_ExtremeVMDetectedVPPResult_Object = MibTableColumn
extremeVMDetectedVPPResult = _ExtremeVMDetectedVPPResult_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 13),
    _ExtremeVMDetectedVPPResult_Type()
)
extremeVMDetectedVPPResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVMDetectedVPPResult.setStatus("current")
_ExtremeVMDetectedCounterInstallResult_Type = CounterDirection
_ExtremeVMDetectedCounterInstallResult_Object = MibTableColumn
extremeVMDetectedCounterInstallResult = _ExtremeVMDetectedCounterInstallResult_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 14),
    _ExtremeVMDetectedCounterInstallResult_Type()
)
extremeVMDetectedCounterInstallResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVMDetectedCounterInstallResult.setStatus("current")


class _ExtremeVMDetectedVMVLANTag_Type(Integer32):
    """Custom type extremeVMDetectedVMVLANTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ExtremeVMDetectedVMVLANTag_Type.__name__ = "Integer32"
_ExtremeVMDetectedVMVLANTag_Object = MibTableColumn
extremeVMDetectedVMVLANTag = _ExtremeVMDetectedVMVLANTag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 15),
    _ExtremeVMDetectedVMVLANTag_Type()
)
extremeVMDetectedVMVLANTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVMDetectedVMVLANTag.setStatus("current")


class _ExtremeVMDetectedVMVLANVRName_Type(DisplayString):
    """Custom type extremeVMDetectedVMVLANVRName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeVMDetectedVMVLANVRName_Type.__name__ = "DisplayString"
_ExtremeVMDetectedVMVLANVRName_Object = MibTableColumn
extremeVMDetectedVMVLANVRName = _ExtremeVMDetectedVMVLANVRName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 16),
    _ExtremeVMDetectedVMVLANVRName_Type()
)
extremeVMDetectedVMVLANVRName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVMDetectedVMVLANVRName.setStatus("current")
_ExtremeVMNotificationObjects_ObjectIdentity = ObjectIdentity
extremeVMNotificationObjects = _ExtremeVMNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 4)
)
_ExtremeVMVPPSynchType_Type = VMVPPSynchType
_ExtremeVMVPPSynchType_Object = MibScalar
extremeVMVPPSynchType = _ExtremeVMVPPSynchType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 4, 1),
    _ExtremeVMVPPSynchType_Type()
)
extremeVMVPPSynchType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeVMVPPSynchType.setStatus("current")
_ExtremeVMNotifications_ObjectIdentity = ObjectIdentity
extremeVMNotifications = _ExtremeVMNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 5)
)
_ExtremeVMNotificationPrefix_ObjectIdentity = ObjectIdentity
extremeVMNotificationPrefix = _ExtremeVMNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 5, 0)
)

# Managed Objects groups


# Notification objects

extremeVMVPPSyncFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 5, 0, 1)
)
extremeVMVPPSyncFailed.setObjects(
      *(("EXTREME-VM-MIB", "extremeVMFTPServer"),
        ("EXTREME-VM-MIB", "extremeVMFTPAddrType"),
        ("EXTREME-VM-MIB", "extremeVMFTPServerType"),
        ("EXTREME-VM-MIB", "extremeVMLastSynchStatus"),
        ("EXTREME-VM-MIB", "extremeVMVPPName"),
        ("EXTREME-VM-MIB", "extremeVMVPPSynchType"))
)
if mibBuilder.loadTexts:
    extremeVMVPPSyncFailed.setStatus(
        "current"
    )

extremeVMVPPInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 5, 0, 2)
)
extremeVMVPPInvalid.setObjects(
      *(("EXTREME-VM-MIB", "extremeVMVPPType"),
        ("EXTREME-VM-MIB", "extremeVMVPPName"))
)
if mibBuilder.loadTexts:
    extremeVMVPPInvalid.setStatus(
        "current"
    )

extremeVMMapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 5, 0, 3)
)
extremeVMMapped.setObjects(
      *(("EXTREME-VM-MIB", "extremeVMMappingMAC"),
        ("EXTREME-VM-MIB", "extremeVMMappingIngressVPPName"),
        ("EXTREME-VM-MIB", "extremeVMMappingEgressVPPName"),
        ("EXTREME-VM-MIB", "extremeVMMappingVPPName"))
)
if mibBuilder.loadTexts:
    extremeVMMapped.setStatus(
        "current"
    )

extremeVMUnMapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 5, 0, 4)
)
extremeVMUnMapped.setObjects(
      *(("EXTREME-VM-MIB", "extremeVMMappingMAC"),
        ("EXTREME-VM-MIB", "extremeVMMappingIngressVPPName"),
        ("EXTREME-VM-MIB", "extremeVMMappingEgressVPPName"),
        ("EXTREME-VM-MIB", "extremeVMMappingVPPName"))
)
if mibBuilder.loadTexts:
    extremeVMUnMapped.setStatus(
        "current"
    )

extremeVMDetectResult = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 5, 0, 5)
)
extremeVMDetectResult.setObjects(
      *(("EXTREME-VM-MIB", "extremeVMDetectedMAC"),
        ("EXTREME-VM-MIB", "extremeVMDetectedIfIndex"),
        ("EXTREME-VM-MIB", "extremeVMDetectedIngressVPPName"),
        ("EXTREME-VM-MIB", "extremeVMDetectedEgressVPPName"),
        ("EXTREME-VM-MIB", "extremeVMDetectedResultIngress"),
        ("EXTREME-VM-MIB", "extremeVMDetectedResultEgress"),
        ("EXTREME-VM-MIB", "extremeVMDetectedOperStatus"),
        ("EXTREME-VM-MIB", "extremeVMDetectedIngErrPolicies"),
        ("EXTREME-VM-MIB", "extremeVMDetectedEgrErrPolicies"),
        ("EXTREME-VM-MIB", "extremeVMDetectedVPPResult"),
        ("EXTREME-VM-MIB", "extremeVMDetectedVPPName"),
        ("EXTREME-VM-MIB", "extremeVMDetectedCounterInstallResult"))
)
if mibBuilder.loadTexts:
    extremeVMDetectResult.setStatus(
        "current"
    )

extremeVMUnDetectResult = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39, 5, 0, 6)
)
extremeVMUnDetectResult.setObjects(
      *(("EXTREME-VM-MIB", "extremeVMDetectedMAC"),
        ("EXTREME-VM-MIB", "extremeVMDetectedIfIndex"))
)
if mibBuilder.loadTexts:
    extremeVMUnDetectResult.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-VM-MIB",
    **{"VMVPPSynchType": VMVPPSynchType,
       "CounterDirection": CounterDirection,
       "extremeVM": extremeVM,
       "extremeVMGeneral": extremeVMGeneral,
       "extremeVMFTPServerTable": extremeVMFTPServerTable,
       "extremeVMFTPServerEntry": extremeVMFTPServerEntry,
       "extremeVMFTPServerType": extremeVMFTPServerType,
       "extremeVMFTPAddrType": extremeVMFTPAddrType,
       "extremeVMFTPServer": extremeVMFTPServer,
       "extremeVMFTPSynchInterval": extremeVMFTPSynchInterval,
       "extremeVMFTPRowStatus": extremeVMFTPRowStatus,
       "extremeVMFTPPathName": extremeVMFTPPathName,
       "extremeVMFTPUsername": extremeVMFTPUsername,
       "extremeVMFTPPassword": extremeVMFTPPassword,
       "extremeVMFTPPolicyDir": extremeVMFTPPolicyDir,
       "extremeVMLastSynch": extremeVMLastSynch,
       "extremeVMLastSynchStatus": extremeVMLastSynchStatus,
       "extremeVMSynchAdminState": extremeVMSynchAdminState,
       "extremeVMSynchOperState": extremeVMSynchOperState,
       "extremeVMTrackingEnabled": extremeVMTrackingEnabled,
       "extremeVMPortConfigTable": extremeVMPortConfigTable,
       "extremeVMPortConfigEntry": extremeVMPortConfigEntry,
       "extremeVMPortConfigIfIndex": extremeVMPortConfigIfIndex,
       "extremeVMPortConfigVMTrackingEnabled": extremeVMPortConfigVMTrackingEnabled,
       "extremeVMPortConfigVMTrackingDynVlanEnabled": extremeVMPortConfigVMTrackingDynVlanEnabled,
       "extremeVMVPP": extremeVMVPP,
       "extremeVMVPPTable": extremeVMVPPTable,
       "extremeVMVPPEntry": extremeVMVPPEntry,
       "extremeVMVPPType": extremeVMVPPType,
       "extremeVMVPPName": extremeVMVPPName,
       "extremeVMVPPControl": extremeVMVPPControl,
       "extremeVMVPPRowStatus": extremeVMVPPRowStatus,
       "extremeVMVPPCounter": extremeVMVPPCounter,
       "extremeVMVPPVLANTag": extremeVMVPPVLANTag,
       "extremeVMVPPVLANVRName": extremeVMVPPVLANVRName,
       "extremeVMMappingTable": extremeVMMappingTable,
       "extremeVMMappingEntry": extremeVMMappingEntry,
       "extremeVMMappingType": extremeVMMappingType,
       "extremeVMMappingMAC": extremeVMMappingMAC,
       "extremeVMMappingIngressVPPName": extremeVMMappingIngressVPPName,
       "extremeVMMappingEgressVPPName": extremeVMMappingEgressVPPName,
       "extremeVMMappingStatus": extremeVMMappingStatus,
       "extremeVMMappingRowStatus": extremeVMMappingRowStatus,
       "extremeVMMappingVPPName": extremeVMMappingVPPName,
       "extremeVMMappingVLANTag": extremeVMMappingVLANTag,
       "extremeVMMappingVLANVRName": extremeVMMappingVLANVRName,
       "extremeVMVPP2PolicyTable": extremeVMVPP2PolicyTable,
       "extremeVMVPP2PolicyEntry": extremeVMVPP2PolicyEntry,
       "extremeVMVPP2PolicyVPPName": extremeVMVPP2PolicyVPPName,
       "extremeVMVPP2PolicyPolicyName": extremeVMVPP2PolicyPolicyName,
       "extremeVMVPP2PolicyType": extremeVMVPP2PolicyType,
       "extremeVMVPP2PolicyOrder": extremeVMVPP2PolicyOrder,
       "extremeVMVPP2PolicyRowStatus": extremeVMVPP2PolicyRowStatus,
       "extremeVMVPPDetailTable": extremeVMVPPDetailTable,
       "extremeVMVPPDetailEntry": extremeVMVPPDetailEntry,
       "extremeVMVPPDetailVPPName": extremeVMVPPDetailVPPName,
       "extremeVMVPPDetailDirection": extremeVMVPPDetailDirection,
       "extremeVMVPPDetailType": extremeVMVPPDetailType,
       "extremeVMVPPDetailOrder": extremeVMVPPDetailOrder,
       "extremeVMVPPDetailPolicyName": extremeVMVPPDetailPolicyName,
       "extremeVMVPPDetailRowStatus": extremeVMVPPDetailRowStatus,
       "extremeVMDetected": extremeVMDetected,
       "extremeVMDetectedNumber": extremeVMDetectedNumber,
       "extremeVMDetectedTable": extremeVMDetectedTable,
       "extremeVMDetectedEntry": extremeVMDetectedEntry,
       "extremeVMDetectedMAC": extremeVMDetectedMAC,
       "extremeVMDetectedVMName": extremeVMDetectedVMName,
       "extremeVMDetectedIngressVPPName": extremeVMDetectedIngressVPPName,
       "extremeVMDetectedEgressVPPName": extremeVMDetectedEgressVPPName,
       "extremeVMDetectedIfIndex": extremeVMDetectedIfIndex,
       "extremeVMDetectedAdminStatus": extremeVMDetectedAdminStatus,
       "extremeVMDetectedOperStatus": extremeVMDetectedOperStatus,
       "extremeVMDetectedResultIngress": extremeVMDetectedResultIngress,
       "extremeVMDetectedResultEgress": extremeVMDetectedResultEgress,
       "extremeVMDetectedIngErrPolicies": extremeVMDetectedIngErrPolicies,
       "extremeVMDetectedEgrErrPolicies": extremeVMDetectedEgrErrPolicies,
       "extremeVMDetectedVPPName": extremeVMDetectedVPPName,
       "extremeVMDetectedVPPResult": extremeVMDetectedVPPResult,
       "extremeVMDetectedCounterInstallResult": extremeVMDetectedCounterInstallResult,
       "extremeVMDetectedVMVLANTag": extremeVMDetectedVMVLANTag,
       "extremeVMDetectedVMVLANVRName": extremeVMDetectedVMVLANVRName,
       "extremeVMNotificationObjects": extremeVMNotificationObjects,
       "extremeVMVPPSynchType": extremeVMVPPSynchType,
       "extremeVMNotifications": extremeVMNotifications,
       "extremeVMNotificationPrefix": extremeVMNotificationPrefix,
       "extremeVMVPPSyncFailed": extremeVMVPPSyncFailed,
       "extremeVMVPPInvalid": extremeVMVPPInvalid,
       "extremeVMMapped": extremeVMMapped,
       "extremeVMUnMapped": extremeVMUnMapped,
       "extremeVMDetectResult": extremeVMDetectResult,
       "extremeVMUnDetectResult": extremeVMUnDetectResult}
)
