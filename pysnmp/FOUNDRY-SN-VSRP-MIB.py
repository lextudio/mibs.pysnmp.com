# SNMP MIB module (FOUNDRY-SN-VSRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-SN-VSRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:12 2024
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

snVsrp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21)
)
snVsrp.setRevisions(
        ("2010-06-02 00:00",
         "2009-09-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MacAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



# MIB Managed Objects in the order of their OIDs

_SnVsrpGlobal_ObjectIdentity = ObjectIdentity
snVsrpGlobal = _SnVsrpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 1)
)


class _SnVsrpGroupOperModeVsrp_Type(Integer32):
    """Custom type snVsrpGroupOperModeVsrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnVsrpGroupOperModeVsrp_Type.__name__ = "Integer32"
_SnVsrpGroupOperModeVsrp_Object = MibScalar
snVsrpGroupOperModeVsrp = _SnVsrpGroupOperModeVsrp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 1, 1),
    _SnVsrpGroupOperModeVsrp_Type()
)
snVsrpGroupOperModeVsrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVsrpGroupOperModeVsrp.setStatus("current")


class _SnVsrpIfStateChangeTrap_Type(Integer32):
    """Custom type snVsrpIfStateChangeTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnVsrpIfStateChangeTrap_Type.__name__ = "Integer32"
_SnVsrpIfStateChangeTrap_Object = MibScalar
snVsrpIfStateChangeTrap = _SnVsrpIfStateChangeTrap_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 1, 2),
    _SnVsrpIfStateChangeTrap_Type()
)
snVsrpIfStateChangeTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVsrpIfStateChangeTrap.setStatus("current")
_SnVsrpIfMaxNumVridPerIntf_Type = Integer32
_SnVsrpIfMaxNumVridPerIntf_Object = MibScalar
snVsrpIfMaxNumVridPerIntf = _SnVsrpIfMaxNumVridPerIntf_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 1, 3),
    _SnVsrpIfMaxNumVridPerIntf_Type()
)
snVsrpIfMaxNumVridPerIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpIfMaxNumVridPerIntf.setStatus("current")
_SnVsrpIfMaxNumVridPerSystem_Type = Integer32
_SnVsrpIfMaxNumVridPerSystem_Object = MibScalar
snVsrpIfMaxNumVridPerSystem = _SnVsrpIfMaxNumVridPerSystem_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 1, 4),
    _SnVsrpIfMaxNumVridPerSystem_Type()
)
snVsrpIfMaxNumVridPerSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpIfMaxNumVridPerSystem.setStatus("current")


class _SnVsrpClearVrrpStat_Type(Integer32):
    """Custom type snVsrpClearVrrpStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("normal", 0))
    )


_SnVsrpClearVrrpStat_Type.__name__ = "Integer32"
_SnVsrpClearVrrpStat_Object = MibScalar
snVsrpClearVrrpStat = _SnVsrpClearVrrpStat_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 1, 5),
    _SnVsrpClearVrrpStat_Type()
)
snVsrpClearVrrpStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVsrpClearVrrpStat.setStatus("current")
_SnVsrpIfIntf_ObjectIdentity = ObjectIdentity
snVsrpIfIntf = _SnVsrpIfIntf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 2)
)
_SnVsrpIfTable_Object = MibTable
snVsrpIfTable = _SnVsrpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 2, 1)
)
if mibBuilder.loadTexts:
    snVsrpIfTable.setStatus("current")
_SnVsrpIfEntry_Object = MibTableRow
snVsrpIfEntry = _SnVsrpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 2, 1, 1)
)
snVsrpIfEntry.setIndexNames(
    (0, "FOUNDRY-SN-VSRP-MIB", "snVsrpIfVlanId"),
)
if mibBuilder.loadTexts:
    snVsrpIfEntry.setStatus("current")
_SnVsrpIfVlanId_Type = Integer32
_SnVsrpIfVlanId_Object = MibTableColumn
snVsrpIfVlanId = _SnVsrpIfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 2, 1, 1, 1),
    _SnVsrpIfVlanId_Type()
)
snVsrpIfVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpIfVlanId.setStatus("current")


class _SnVsrpIfAuthType_Type(Integer32):
    """Custom type snVsrpIfAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipAuthHeader", 2),
          ("noAuth", 0),
          ("simpleTextPasswd", 1))
    )


_SnVsrpIfAuthType_Type.__name__ = "Integer32"
_SnVsrpIfAuthType_Object = MibTableColumn
snVsrpIfAuthType = _SnVsrpIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 2, 1, 1, 2),
    _SnVsrpIfAuthType_Type()
)
snVsrpIfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVsrpIfAuthType.setStatus("current")


class _SnVsrpIfAuthPassword_Type(OctetString):
    """Custom type snVsrpIfAuthPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SnVsrpIfAuthPassword_Type.__name__ = "OctetString"
_SnVsrpIfAuthPassword_Object = MibTableColumn
snVsrpIfAuthPassword = _SnVsrpIfAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 2, 1, 1, 3),
    _SnVsrpIfAuthPassword_Type()
)
snVsrpIfAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVsrpIfAuthPassword.setStatus("current")
_SnVsrpVirRtr_ObjectIdentity = ObjectIdentity
snVsrpVirRtr = _SnVsrpVirRtr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3)
)
_SnVsrpVirRtrTable_Object = MibTable
snVsrpVirRtrTable = _SnVsrpVirRtrTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1)
)
if mibBuilder.loadTexts:
    snVsrpVirRtrTable.setStatus("current")
_SnVsrpVirRtrEntry_Object = MibTableRow
snVsrpVirRtrEntry = _SnVsrpVirRtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1)
)
snVsrpVirRtrEntry.setIndexNames(
    (0, "FOUNDRY-SN-VSRP-MIB", "snVsrpVirRtrVlanId"),
    (0, "FOUNDRY-SN-VSRP-MIB", "snVsrpVirRtrId"),
)
if mibBuilder.loadTexts:
    snVsrpVirRtrEntry.setStatus("current")
_SnVsrpVirRtrVlanId_Type = Integer32
_SnVsrpVirRtrVlanId_Object = MibTableColumn
snVsrpVirRtrVlanId = _SnVsrpVirRtrVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 1),
    _SnVsrpVirRtrVlanId_Type()
)
snVsrpVirRtrVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpVirRtrVlanId.setStatus("current")


class _SnVsrpVirRtrId_Type(Integer32):
    """Custom type snVsrpVirRtrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnVsrpVirRtrId_Type.__name__ = "Integer32"
_SnVsrpVirRtrId_Object = MibTableColumn
snVsrpVirRtrId = _SnVsrpVirRtrId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 2),
    _SnVsrpVirRtrId_Type()
)
snVsrpVirRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpVirRtrId.setStatus("current")


class _SnVsrpVirRtrOwnership_Type(Integer32):
    """Custom type snVsrpVirRtrOwnership based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("incomplete", 0),
          ("owner", 1))
    )


_SnVsrpVirRtrOwnership_Type.__name__ = "Integer32"
_SnVsrpVirRtrOwnership_Object = MibTableColumn
snVsrpVirRtrOwnership = _SnVsrpVirRtrOwnership_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 3),
    _SnVsrpVirRtrOwnership_Type()
)
snVsrpVirRtrOwnership.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVsrpVirRtrOwnership.setStatus("current")


class _SnVsrpVirRtrCfgPriority_Type(Integer32):
    """Custom type snVsrpVirRtrCfgPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnVsrpVirRtrCfgPriority_Type.__name__ = "Integer32"
_SnVsrpVirRtrCfgPriority_Object = MibTableColumn
snVsrpVirRtrCfgPriority = _SnVsrpVirRtrCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 4),
    _SnVsrpVirRtrCfgPriority_Type()
)
snVsrpVirRtrCfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVsrpVirRtrCfgPriority.setStatus("current")


class _SnVsrpVirRtrTrackPriority_Type(Integer32):
    """Custom type snVsrpVirRtrTrackPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_SnVsrpVirRtrTrackPriority_Type.__name__ = "Integer32"
_SnVsrpVirRtrTrackPriority_Object = MibTableColumn
snVsrpVirRtrTrackPriority = _SnVsrpVirRtrTrackPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 5),
    _SnVsrpVirRtrTrackPriority_Type()
)
snVsrpVirRtrTrackPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVsrpVirRtrTrackPriority.setStatus("current")


class _SnVsrpVirRtrCurrPriority_Type(Integer32):
    """Custom type snVsrpVirRtrCurrPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_SnVsrpVirRtrCurrPriority_Type.__name__ = "Integer32"
_SnVsrpVirRtrCurrPriority_Object = MibTableColumn
snVsrpVirRtrCurrPriority = _SnVsrpVirRtrCurrPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 6),
    _SnVsrpVirRtrCurrPriority_Type()
)
snVsrpVirRtrCurrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpVirRtrCurrPriority.setStatus("current")


class _SnVsrpVirRtrHelloInt_Type(Integer32):
    """Custom type snVsrpVirRtrHelloInt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 84),
    )


_SnVsrpVirRtrHelloInt_Type.__name__ = "Integer32"
_SnVsrpVirRtrHelloInt_Object = MibTableColumn
snVsrpVirRtrHelloInt = _SnVsrpVirRtrHelloInt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 7),
    _SnVsrpVirRtrHelloInt_Type()
)
snVsrpVirRtrHelloInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVsrpVirRtrHelloInt.setStatus("current")


class _SnVsrpVirRtrDeadInt_Type(Integer32):
    """Custom type snVsrpVirRtrDeadInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_SnVsrpVirRtrDeadInt_Type.__name__ = "Integer32"
_SnVsrpVirRtrDeadInt_Object = MibTableColumn
snVsrpVirRtrDeadInt = _SnVsrpVirRtrDeadInt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 8),
    _SnVsrpVirRtrDeadInt_Type()
)
snVsrpVirRtrDeadInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVsrpVirRtrDeadInt.setStatus("current")


class _SnVsrpVirRtrPreemptMode_Type(Integer32):
    """Custom type snVsrpVirRtrPreemptMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnVsrpVirRtrPreemptMode_Type.__name__ = "Integer32"
_SnVsrpVirRtrPreemptMode_Object = MibTableColumn
snVsrpVirRtrPreemptMode = _SnVsrpVirRtrPreemptMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 9),
    _SnVsrpVirRtrPreemptMode_Type()
)
snVsrpVirRtrPreemptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVsrpVirRtrPreemptMode.setStatus("current")


class _SnVsrpVirRtrState_Type(Integer32):
    """Custom type snVsrpVirRtrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("init", 0),
          ("master", 1))
    )


_SnVsrpVirRtrState_Type.__name__ = "Integer32"
_SnVsrpVirRtrState_Object = MibTableColumn
snVsrpVirRtrState = _SnVsrpVirRtrState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 10),
    _SnVsrpVirRtrState_Type()
)
snVsrpVirRtrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpVirRtrState.setStatus("current")


class _SnVsrpVirRtrIpAddrMask_Type(OctetString):
    """Custom type snVsrpVirRtrIpAddrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SnVsrpVirRtrIpAddrMask_Type.__name__ = "OctetString"
_SnVsrpVirRtrIpAddrMask_Object = MibTableColumn
snVsrpVirRtrIpAddrMask = _SnVsrpVirRtrIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 11),
    _SnVsrpVirRtrIpAddrMask_Type()
)
snVsrpVirRtrIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVsrpVirRtrIpAddrMask.setStatus("current")


class _SnVsrpVirRtrActivate_Type(Integer32):
    """Custom type snVsrpVirRtrActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnVsrpVirRtrActivate_Type.__name__ = "Integer32"
_SnVsrpVirRtrActivate_Object = MibTableColumn
snVsrpVirRtrActivate = _SnVsrpVirRtrActivate_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 12),
    _SnVsrpVirRtrActivate_Type()
)
snVsrpVirRtrActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVsrpVirRtrActivate.setStatus("current")
_SnVsrpVirRtrTrackPortList_Type = OctetString
_SnVsrpVirRtrTrackPortList_Object = MibTableColumn
snVsrpVirRtrTrackPortList = _SnVsrpVirRtrTrackPortList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 13),
    _SnVsrpVirRtrTrackPortList_Type()
)
snVsrpVirRtrTrackPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVsrpVirRtrTrackPortList.setStatus("current")


class _SnVsrpVirRtrAdvertiseBackup_Type(Integer32):
    """Custom type snVsrpVirRtrAdvertiseBackup based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnVsrpVirRtrAdvertiseBackup_Type.__name__ = "Integer32"
_SnVsrpVirRtrAdvertiseBackup_Object = MibTableColumn
snVsrpVirRtrAdvertiseBackup = _SnVsrpVirRtrAdvertiseBackup_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 14),
    _SnVsrpVirRtrAdvertiseBackup_Type()
)
snVsrpVirRtrAdvertiseBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVsrpVirRtrAdvertiseBackup.setStatus("current")


class _SnVsrpVirRtrHoldDownInt_Type(Integer32):
    """Custom type snVsrpVirRtrHoldDownInt based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 84),
    )


_SnVsrpVirRtrHoldDownInt_Type.__name__ = "Integer32"
_SnVsrpVirRtrHoldDownInt_Object = MibTableColumn
snVsrpVirRtrHoldDownInt = _SnVsrpVirRtrHoldDownInt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 15),
    _SnVsrpVirRtrHoldDownInt_Type()
)
snVsrpVirRtrHoldDownInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVsrpVirRtrHoldDownInt.setStatus("current")


class _SnVsrpVirRtrInitTtl_Type(Integer32):
    """Custom type snVsrpVirRtrInitTtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnVsrpVirRtrInitTtl_Type.__name__ = "Integer32"
_SnVsrpVirRtrInitTtl_Object = MibTableColumn
snVsrpVirRtrInitTtl = _SnVsrpVirRtrInitTtl_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 16),
    _SnVsrpVirRtrInitTtl_Type()
)
snVsrpVirRtrInitTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVsrpVirRtrInitTtl.setStatus("current")
_SnVsrpVirRtrIncPortList_Type = OctetString
_SnVsrpVirRtrIncPortList_Object = MibTableColumn
snVsrpVirRtrIncPortList = _SnVsrpVirRtrIncPortList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 17),
    _SnVsrpVirRtrIncPortList_Type()
)
snVsrpVirRtrIncPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVsrpVirRtrIncPortList.setStatus("current")


class _SnVsrpVirRtrSave_Type(Integer32):
    """Custom type snVsrpVirRtrSave based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnVsrpVirRtrSave_Type.__name__ = "Integer32"
_SnVsrpVirRtrSave_Object = MibTableColumn
snVsrpVirRtrSave = _SnVsrpVirRtrSave_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 18),
    _SnVsrpVirRtrSave_Type()
)
snVsrpVirRtrSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVsrpVirRtrSave.setStatus("current")


class _SnVsrpVirRtrBackupInt_Type(Integer32):
    """Custom type snVsrpVirRtrBackupInt based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_SnVsrpVirRtrBackupInt_Type.__name__ = "Integer32"
_SnVsrpVirRtrBackupInt_Object = MibTableColumn
snVsrpVirRtrBackupInt = _SnVsrpVirRtrBackupInt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 19),
    _SnVsrpVirRtrBackupInt_Type()
)
snVsrpVirRtrBackupInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVsrpVirRtrBackupInt.setStatus("current")


class _SnVsrpVirRtrRowStatus_Type(Integer32):
    """Custom type snVsrpVirRtrRowStatus based on Integer32"""
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
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnVsrpVirRtrRowStatus_Type.__name__ = "Integer32"
_SnVsrpVirRtrRowStatus_Object = MibTableColumn
snVsrpVirRtrRowStatus = _SnVsrpVirRtrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 20),
    _SnVsrpVirRtrRowStatus_Type()
)
snVsrpVirRtrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVsrpVirRtrRowStatus.setStatus("current")
_SnVsrpVirRtrRxArpPktDropCnts_Type = Counter32
_SnVsrpVirRtrRxArpPktDropCnts_Object = MibTableColumn
snVsrpVirRtrRxArpPktDropCnts = _SnVsrpVirRtrRxArpPktDropCnts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 21),
    _SnVsrpVirRtrRxArpPktDropCnts_Type()
)
snVsrpVirRtrRxArpPktDropCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpVirRtrRxArpPktDropCnts.setStatus("current")
_SnVsrpVirRtrRxIpPktDropCnts_Type = Counter32
_SnVsrpVirRtrRxIpPktDropCnts_Object = MibTableColumn
snVsrpVirRtrRxIpPktDropCnts = _SnVsrpVirRtrRxIpPktDropCnts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 22),
    _SnVsrpVirRtrRxIpPktDropCnts_Type()
)
snVsrpVirRtrRxIpPktDropCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpVirRtrRxIpPktDropCnts.setStatus("current")
_SnVsrpVirRtrRxPortMismatchCnts_Type = Counter32
_SnVsrpVirRtrRxPortMismatchCnts_Object = MibTableColumn
snVsrpVirRtrRxPortMismatchCnts = _SnVsrpVirRtrRxPortMismatchCnts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 23),
    _SnVsrpVirRtrRxPortMismatchCnts_Type()
)
snVsrpVirRtrRxPortMismatchCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpVirRtrRxPortMismatchCnts.setStatus("current")
_SnVsrpVirRtrRxNumOfIpMismatchCnts_Type = Counter32
_SnVsrpVirRtrRxNumOfIpMismatchCnts_Object = MibTableColumn
snVsrpVirRtrRxNumOfIpMismatchCnts = _SnVsrpVirRtrRxNumOfIpMismatchCnts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 24),
    _SnVsrpVirRtrRxNumOfIpMismatchCnts_Type()
)
snVsrpVirRtrRxNumOfIpMismatchCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpVirRtrRxNumOfIpMismatchCnts.setStatus("current")
_SnVsrpVirRtrRxIpMismatchCnts_Type = Counter32
_SnVsrpVirRtrRxIpMismatchCnts_Object = MibTableColumn
snVsrpVirRtrRxIpMismatchCnts = _SnVsrpVirRtrRxIpMismatchCnts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 25),
    _SnVsrpVirRtrRxIpMismatchCnts_Type()
)
snVsrpVirRtrRxIpMismatchCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpVirRtrRxIpMismatchCnts.setStatus("current")
_SnVsrpVirRtrRxHelloIntMismatchCnts_Type = Counter32
_SnVsrpVirRtrRxHelloIntMismatchCnts_Object = MibTableColumn
snVsrpVirRtrRxHelloIntMismatchCnts = _SnVsrpVirRtrRxHelloIntMismatchCnts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 26),
    _SnVsrpVirRtrRxHelloIntMismatchCnts_Type()
)
snVsrpVirRtrRxHelloIntMismatchCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpVirRtrRxHelloIntMismatchCnts.setStatus("current")
_SnVsrpVirRtrRxPriorityZeroFromMasterCnts_Type = Counter32
_SnVsrpVirRtrRxPriorityZeroFromMasterCnts_Object = MibTableColumn
snVsrpVirRtrRxPriorityZeroFromMasterCnts = _SnVsrpVirRtrRxPriorityZeroFromMasterCnts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 27),
    _SnVsrpVirRtrRxPriorityZeroFromMasterCnts_Type()
)
snVsrpVirRtrRxPriorityZeroFromMasterCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpVirRtrRxPriorityZeroFromMasterCnts.setStatus("current")
_SnVsrpVirRtrRxHigherPriorityCnts_Type = Counter32
_SnVsrpVirRtrRxHigherPriorityCnts_Object = MibTableColumn
snVsrpVirRtrRxHigherPriorityCnts = _SnVsrpVirRtrRxHigherPriorityCnts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 28),
    _SnVsrpVirRtrRxHigherPriorityCnts_Type()
)
snVsrpVirRtrRxHigherPriorityCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpVirRtrRxHigherPriorityCnts.setStatus("current")
_SnVsrpVirRtrTransToMasterStateCnts_Type = Counter32
_SnVsrpVirRtrTransToMasterStateCnts_Object = MibTableColumn
snVsrpVirRtrTransToMasterStateCnts = _SnVsrpVirRtrTransToMasterStateCnts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 29),
    _SnVsrpVirRtrTransToMasterStateCnts_Type()
)
snVsrpVirRtrTransToMasterStateCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpVirRtrTransToMasterStateCnts.setStatus("current")
_SnVsrpVirRtrTransToBackupStateCnts_Type = Counter32
_SnVsrpVirRtrTransToBackupStateCnts_Object = MibTableColumn
snVsrpVirRtrTransToBackupStateCnts = _SnVsrpVirRtrTransToBackupStateCnts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 30),
    _SnVsrpVirRtrTransToBackupStateCnts_Type()
)
snVsrpVirRtrTransToBackupStateCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpVirRtrTransToBackupStateCnts.setStatus("current")
_SnVsrpVirRtrCurrDeadInt_Type = Integer32
_SnVsrpVirRtrCurrDeadInt_Object = MibTableColumn
snVsrpVirRtrCurrDeadInt = _SnVsrpVirRtrCurrDeadInt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 31),
    _SnVsrpVirRtrCurrDeadInt_Type()
)
snVsrpVirRtrCurrDeadInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpVirRtrCurrDeadInt.setStatus("current")


class _SnVsrpVirRtrCurHelloInt_Type(Integer32):
    """Custom type snVsrpVirRtrCurHelloInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 84),
    )


_SnVsrpVirRtrCurHelloInt_Type.__name__ = "Integer32"
_SnVsrpVirRtrCurHelloInt_Object = MibTableColumn
snVsrpVirRtrCurHelloInt = _SnVsrpVirRtrCurHelloInt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 32),
    _SnVsrpVirRtrCurHelloInt_Type()
)
snVsrpVirRtrCurHelloInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpVirRtrCurHelloInt.setStatus("current")


class _SnVsrpVirRtrCurHoldDownInt_Type(Integer32):
    """Custom type snVsrpVirRtrCurHoldDownInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 84),
    )


_SnVsrpVirRtrCurHoldDownInt_Type.__name__ = "Integer32"
_SnVsrpVirRtrCurHoldDownInt_Object = MibTableColumn
snVsrpVirRtrCurHoldDownInt = _SnVsrpVirRtrCurHoldDownInt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 33),
    _SnVsrpVirRtrCurHoldDownInt_Type()
)
snVsrpVirRtrCurHoldDownInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpVirRtrCurHoldDownInt.setStatus("current")


class _SnVsrpVirRtrCurInitTtl_Type(Integer32):
    """Custom type snVsrpVirRtrCurInitTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnVsrpVirRtrCurInitTtl_Type.__name__ = "Integer32"
_SnVsrpVirRtrCurInitTtl_Object = MibTableColumn
snVsrpVirRtrCurInitTtl = _SnVsrpVirRtrCurInitTtl_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 34),
    _SnVsrpVirRtrCurInitTtl_Type()
)
snVsrpVirRtrCurInitTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpVirRtrCurInitTtl.setStatus("current")
_SnVsrpVirRtrHelloMacAddress_Type = MacAddress
_SnVsrpVirRtrHelloMacAddress_Object = MibTableColumn
snVsrpVirRtrHelloMacAddress = _SnVsrpVirRtrHelloMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 35),
    _SnVsrpVirRtrHelloMacAddress_Type()
)
snVsrpVirRtrHelloMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpVirRtrHelloMacAddress.setStatus("current")
_SnVsrpVirRtrMasterIpAddr_Type = IpAddress
_SnVsrpVirRtrMasterIpAddr_Object = MibTableColumn
snVsrpVirRtrMasterIpAddr = _SnVsrpVirRtrMasterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21, 3, 1, 1, 36),
    _SnVsrpVirRtrMasterIpAddr_Type()
)
snVsrpVirRtrMasterIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVsrpVirRtrMasterIpAddr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-VSRP-MIB",
    **{"MacAddress": MacAddress,
       "snVsrp": snVsrp,
       "snVsrpGlobal": snVsrpGlobal,
       "snVsrpGroupOperModeVsrp": snVsrpGroupOperModeVsrp,
       "snVsrpIfStateChangeTrap": snVsrpIfStateChangeTrap,
       "snVsrpIfMaxNumVridPerIntf": snVsrpIfMaxNumVridPerIntf,
       "snVsrpIfMaxNumVridPerSystem": snVsrpIfMaxNumVridPerSystem,
       "snVsrpClearVrrpStat": snVsrpClearVrrpStat,
       "snVsrpIfIntf": snVsrpIfIntf,
       "snVsrpIfTable": snVsrpIfTable,
       "snVsrpIfEntry": snVsrpIfEntry,
       "snVsrpIfVlanId": snVsrpIfVlanId,
       "snVsrpIfAuthType": snVsrpIfAuthType,
       "snVsrpIfAuthPassword": snVsrpIfAuthPassword,
       "snVsrpVirRtr": snVsrpVirRtr,
       "snVsrpVirRtrTable": snVsrpVirRtrTable,
       "snVsrpVirRtrEntry": snVsrpVirRtrEntry,
       "snVsrpVirRtrVlanId": snVsrpVirRtrVlanId,
       "snVsrpVirRtrId": snVsrpVirRtrId,
       "snVsrpVirRtrOwnership": snVsrpVirRtrOwnership,
       "snVsrpVirRtrCfgPriority": snVsrpVirRtrCfgPriority,
       "snVsrpVirRtrTrackPriority": snVsrpVirRtrTrackPriority,
       "snVsrpVirRtrCurrPriority": snVsrpVirRtrCurrPriority,
       "snVsrpVirRtrHelloInt": snVsrpVirRtrHelloInt,
       "snVsrpVirRtrDeadInt": snVsrpVirRtrDeadInt,
       "snVsrpVirRtrPreemptMode": snVsrpVirRtrPreemptMode,
       "snVsrpVirRtrState": snVsrpVirRtrState,
       "snVsrpVirRtrIpAddrMask": snVsrpVirRtrIpAddrMask,
       "snVsrpVirRtrActivate": snVsrpVirRtrActivate,
       "snVsrpVirRtrTrackPortList": snVsrpVirRtrTrackPortList,
       "snVsrpVirRtrAdvertiseBackup": snVsrpVirRtrAdvertiseBackup,
       "snVsrpVirRtrHoldDownInt": snVsrpVirRtrHoldDownInt,
       "snVsrpVirRtrInitTtl": snVsrpVirRtrInitTtl,
       "snVsrpVirRtrIncPortList": snVsrpVirRtrIncPortList,
       "snVsrpVirRtrSave": snVsrpVirRtrSave,
       "snVsrpVirRtrBackupInt": snVsrpVirRtrBackupInt,
       "snVsrpVirRtrRowStatus": snVsrpVirRtrRowStatus,
       "snVsrpVirRtrRxArpPktDropCnts": snVsrpVirRtrRxArpPktDropCnts,
       "snVsrpVirRtrRxIpPktDropCnts": snVsrpVirRtrRxIpPktDropCnts,
       "snVsrpVirRtrRxPortMismatchCnts": snVsrpVirRtrRxPortMismatchCnts,
       "snVsrpVirRtrRxNumOfIpMismatchCnts": snVsrpVirRtrRxNumOfIpMismatchCnts,
       "snVsrpVirRtrRxIpMismatchCnts": snVsrpVirRtrRxIpMismatchCnts,
       "snVsrpVirRtrRxHelloIntMismatchCnts": snVsrpVirRtrRxHelloIntMismatchCnts,
       "snVsrpVirRtrRxPriorityZeroFromMasterCnts": snVsrpVirRtrRxPriorityZeroFromMasterCnts,
       "snVsrpVirRtrRxHigherPriorityCnts": snVsrpVirRtrRxHigherPriorityCnts,
       "snVsrpVirRtrTransToMasterStateCnts": snVsrpVirRtrTransToMasterStateCnts,
       "snVsrpVirRtrTransToBackupStateCnts": snVsrpVirRtrTransToBackupStateCnts,
       "snVsrpVirRtrCurrDeadInt": snVsrpVirRtrCurrDeadInt,
       "snVsrpVirRtrCurHelloInt": snVsrpVirRtrCurHelloInt,
       "snVsrpVirRtrCurHoldDownInt": snVsrpVirRtrCurHoldDownInt,
       "snVsrpVirRtrCurInitTtl": snVsrpVirRtrCurInitTtl,
       "snVsrpVirRtrHelloMacAddress": snVsrpVirRtrHelloMacAddress,
       "snVsrpVirRtrMasterIpAddr": snVsrpVirRtrMasterIpAddr}
)
