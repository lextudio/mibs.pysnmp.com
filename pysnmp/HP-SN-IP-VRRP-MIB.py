# SNMP MIB module (HP-SN-IP-VRRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-SN-IP-VRRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:45 2024
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

(snVrrp,) = mibBuilder.importSymbols(
    "HP-SN-ROOT-MIB",
    "snVrrp")

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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnVrrpGlobal_ObjectIdentity = ObjectIdentity
snVrrpGlobal = _SnVrrpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 1)
)


class _SnVrrpGroupOperMode_Type(Integer32):
    """Custom type snVrrpGroupOperMode based on Integer32"""
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


_SnVrrpGroupOperMode_Type.__name__ = "Integer32"
_SnVrrpGroupOperMode_Object = MibScalar
snVrrpGroupOperMode = _SnVrrpGroupOperMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 1, 1),
    _SnVrrpGroupOperMode_Type()
)
snVrrpGroupOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpGroupOperMode.setStatus("mandatory")


class _SnVrrpIfStateChangeTrap_Type(Integer32):
    """Custom type snVrrpIfStateChangeTrap based on Integer32"""
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


_SnVrrpIfStateChangeTrap_Type.__name__ = "Integer32"
_SnVrrpIfStateChangeTrap_Object = MibScalar
snVrrpIfStateChangeTrap = _SnVrrpIfStateChangeTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 1, 2),
    _SnVrrpIfStateChangeTrap_Type()
)
snVrrpIfStateChangeTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpIfStateChangeTrap.setStatus("mandatory")
_SnVrrpIfMaxNumVridPerIntf_Type = Integer32
_SnVrrpIfMaxNumVridPerIntf_Object = MibScalar
snVrrpIfMaxNumVridPerIntf = _SnVrrpIfMaxNumVridPerIntf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 1, 3),
    _SnVrrpIfMaxNumVridPerIntf_Type()
)
snVrrpIfMaxNumVridPerIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpIfMaxNumVridPerIntf.setStatus("mandatory")
_SnVrrpIfMaxNumVridPerSystem_Type = Integer32
_SnVrrpIfMaxNumVridPerSystem_Object = MibScalar
snVrrpIfMaxNumVridPerSystem = _SnVrrpIfMaxNumVridPerSystem_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 1, 4),
    _SnVrrpIfMaxNumVridPerSystem_Type()
)
snVrrpIfMaxNumVridPerSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpIfMaxNumVridPerSystem.setStatus("mandatory")


class _SnVrrpClearVrrpStat_Type(Integer32):
    """Custom type snVrrpClearVrrpStat based on Integer32"""
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


_SnVrrpClearVrrpStat_Type.__name__ = "Integer32"
_SnVrrpClearVrrpStat_Object = MibScalar
snVrrpClearVrrpStat = _SnVrrpClearVrrpStat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 1, 5),
    _SnVrrpClearVrrpStat_Type()
)
snVrrpClearVrrpStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpClearVrrpStat.setStatus("mandatory")


class _SnVrrpGroupOperModeVrrpextended_Type(Integer32):
    """Custom type snVrrpGroupOperModeVrrpextended based on Integer32"""
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


_SnVrrpGroupOperModeVrrpextended_Type.__name__ = "Integer32"
_SnVrrpGroupOperModeVrrpextended_Object = MibScalar
snVrrpGroupOperModeVrrpextended = _SnVrrpGroupOperModeVrrpextended_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 1, 6),
    _SnVrrpGroupOperModeVrrpextended_Type()
)
snVrrpGroupOperModeVrrpextended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpGroupOperModeVrrpextended.setStatus("mandatory")
_SnVrrpIntf_ObjectIdentity = ObjectIdentity
snVrrpIntf = _SnVrrpIntf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 2)
)
_SnVrrpIfTable_Object = MibTable
snVrrpIfTable = _SnVrrpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 2, 1)
)
if mibBuilder.loadTexts:
    snVrrpIfTable.setStatus("deprecated")
_SnVrrpIfEntry_Object = MibTableRow
snVrrpIfEntry = _SnVrrpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 2, 1, 1)
)
snVrrpIfEntry.setIndexNames(
    (0, "HP-SN-IP-VRRP-MIB", "snVrrpIfPort"),
)
if mibBuilder.loadTexts:
    snVrrpIfEntry.setStatus("deprecated")
_SnVrrpIfPort_Type = Integer32
_SnVrrpIfPort_Object = MibTableColumn
snVrrpIfPort = _SnVrrpIfPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 2, 1, 1, 1),
    _SnVrrpIfPort_Type()
)
snVrrpIfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpIfPort.setStatus("deprecated")


class _SnVrrpIfAuthType_Type(Integer32):
    """Custom type snVrrpIfAuthType based on Integer32"""
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


_SnVrrpIfAuthType_Type.__name__ = "Integer32"
_SnVrrpIfAuthType_Object = MibTableColumn
snVrrpIfAuthType = _SnVrrpIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 2, 1, 1, 2),
    _SnVrrpIfAuthType_Type()
)
snVrrpIfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpIfAuthType.setStatus("deprecated")


class _SnVrrpIfAuthPassword_Type(OctetString):
    """Custom type snVrrpIfAuthPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SnVrrpIfAuthPassword_Type.__name__ = "OctetString"
_SnVrrpIfAuthPassword_Object = MibTableColumn
snVrrpIfAuthPassword = _SnVrrpIfAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 2, 1, 1, 3),
    _SnVrrpIfAuthPassword_Type()
)
snVrrpIfAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpIfAuthPassword.setStatus("deprecated")
_SnVrrpIfRxHeaderErrCnts_Type = Counter32
_SnVrrpIfRxHeaderErrCnts_Object = MibTableColumn
snVrrpIfRxHeaderErrCnts = _SnVrrpIfRxHeaderErrCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 2, 1, 1, 4),
    _SnVrrpIfRxHeaderErrCnts_Type()
)
snVrrpIfRxHeaderErrCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpIfRxHeaderErrCnts.setStatus("deprecated")
_SnVrrpIfRxAuthTypeErrCnts_Type = Counter32
_SnVrrpIfRxAuthTypeErrCnts_Object = MibTableColumn
snVrrpIfRxAuthTypeErrCnts = _SnVrrpIfRxAuthTypeErrCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 2, 1, 1, 5),
    _SnVrrpIfRxAuthTypeErrCnts_Type()
)
snVrrpIfRxAuthTypeErrCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpIfRxAuthTypeErrCnts.setStatus("deprecated")
_SnVrrpIfRxAuthPwdMismatchErrCnts_Type = Counter32
_SnVrrpIfRxAuthPwdMismatchErrCnts_Object = MibTableColumn
snVrrpIfRxAuthPwdMismatchErrCnts = _SnVrrpIfRxAuthPwdMismatchErrCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 2, 1, 1, 6),
    _SnVrrpIfRxAuthPwdMismatchErrCnts_Type()
)
snVrrpIfRxAuthPwdMismatchErrCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpIfRxAuthPwdMismatchErrCnts.setStatus("deprecated")
_SnVrrpIfRxVridErrCnts_Type = Counter32
_SnVrrpIfRxVridErrCnts_Object = MibTableColumn
snVrrpIfRxVridErrCnts = _SnVrrpIfRxVridErrCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 2, 1, 1, 7),
    _SnVrrpIfRxVridErrCnts_Type()
)
snVrrpIfRxVridErrCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpIfRxVridErrCnts.setStatus("deprecated")
_SnVrrpVirRtr_ObjectIdentity = ObjectIdentity
snVrrpVirRtr = _SnVrrpVirRtr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3)
)
_SnVrrpVirRtrTable_Object = MibTable
snVrrpVirRtrTable = _SnVrrpVirRtrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1)
)
if mibBuilder.loadTexts:
    snVrrpVirRtrTable.setStatus("deprecated")
_SnVrrpVirRtrEntry_Object = MibTableRow
snVrrpVirRtrEntry = _SnVrrpVirRtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1)
)
snVrrpVirRtrEntry.setIndexNames(
    (0, "HP-SN-IP-VRRP-MIB", "snVrrpVirRtrPort"),
    (0, "HP-SN-IP-VRRP-MIB", "snVrrpVirRtrId"),
)
if mibBuilder.loadTexts:
    snVrrpVirRtrEntry.setStatus("deprecated")
_SnVrrpVirRtrPort_Type = Integer32
_SnVrrpVirRtrPort_Object = MibTableColumn
snVrrpVirRtrPort = _SnVrrpVirRtrPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 1),
    _SnVrrpVirRtrPort_Type()
)
snVrrpVirRtrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtrPort.setStatus("deprecated")


class _SnVrrpVirRtrId_Type(Integer32):
    """Custom type snVrrpVirRtrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnVrrpVirRtrId_Type.__name__ = "Integer32"
_SnVrrpVirRtrId_Object = MibTableColumn
snVrrpVirRtrId = _SnVrrpVirRtrId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 2),
    _SnVrrpVirRtrId_Type()
)
snVrrpVirRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtrId.setStatus("deprecated")


class _SnVrrpVirRtrOwnership_Type(Integer32):
    """Custom type snVrrpVirRtrOwnership based on Integer32"""
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


_SnVrrpVirRtrOwnership_Type.__name__ = "Integer32"
_SnVrrpVirRtrOwnership_Object = MibTableColumn
snVrrpVirRtrOwnership = _SnVrrpVirRtrOwnership_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 3),
    _SnVrrpVirRtrOwnership_Type()
)
snVrrpVirRtrOwnership.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtrOwnership.setStatus("deprecated")


class _SnVrrpVirRtrCfgPriority_Type(Integer32):
    """Custom type snVrrpVirRtrCfgPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 254),
    )


_SnVrrpVirRtrCfgPriority_Type.__name__ = "Integer32"
_SnVrrpVirRtrCfgPriority_Object = MibTableColumn
snVrrpVirRtrCfgPriority = _SnVrrpVirRtrCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 4),
    _SnVrrpVirRtrCfgPriority_Type()
)
snVrrpVirRtrCfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtrCfgPriority.setStatus("deprecated")


class _SnVrrpVirRtrTrackPriority_Type(Integer32):
    """Custom type snVrrpVirRtrTrackPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_SnVrrpVirRtrTrackPriority_Type.__name__ = "Integer32"
_SnVrrpVirRtrTrackPriority_Object = MibTableColumn
snVrrpVirRtrTrackPriority = _SnVrrpVirRtrTrackPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 5),
    _SnVrrpVirRtrTrackPriority_Type()
)
snVrrpVirRtrTrackPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtrTrackPriority.setStatus("deprecated")


class _SnVrrpVirRtrCurrPriority_Type(Integer32):
    """Custom type snVrrpVirRtrCurrPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_SnVrrpVirRtrCurrPriority_Type.__name__ = "Integer32"
_SnVrrpVirRtrCurrPriority_Object = MibTableColumn
snVrrpVirRtrCurrPriority = _SnVrrpVirRtrCurrPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 6),
    _SnVrrpVirRtrCurrPriority_Type()
)
snVrrpVirRtrCurrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtrCurrPriority.setStatus("deprecated")


class _SnVrrpVirRtrHelloInt_Type(Integer32):
    """Custom type snVrrpVirRtrHelloInt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 84),
    )


_SnVrrpVirRtrHelloInt_Type.__name__ = "Integer32"
_SnVrrpVirRtrHelloInt_Object = MibTableColumn
snVrrpVirRtrHelloInt = _SnVrrpVirRtrHelloInt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 7),
    _SnVrrpVirRtrHelloInt_Type()
)
snVrrpVirRtrHelloInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtrHelloInt.setStatus("deprecated")


class _SnVrrpVirRtrDeadInt_Type(Integer32):
    """Custom type snVrrpVirRtrDeadInt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 84),
    )


_SnVrrpVirRtrDeadInt_Type.__name__ = "Integer32"
_SnVrrpVirRtrDeadInt_Object = MibTableColumn
snVrrpVirRtrDeadInt = _SnVrrpVirRtrDeadInt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 8),
    _SnVrrpVirRtrDeadInt_Type()
)
snVrrpVirRtrDeadInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtrDeadInt.setStatus("deprecated")


class _SnVrrpVirRtrPreemptMode_Type(Integer32):
    """Custom type snVrrpVirRtrPreemptMode based on Integer32"""
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


_SnVrrpVirRtrPreemptMode_Type.__name__ = "Integer32"
_SnVrrpVirRtrPreemptMode_Object = MibTableColumn
snVrrpVirRtrPreemptMode = _SnVrrpVirRtrPreemptMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 9),
    _SnVrrpVirRtrPreemptMode_Type()
)
snVrrpVirRtrPreemptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtrPreemptMode.setStatus("deprecated")


class _SnVrrpVirRtrState_Type(Integer32):
    """Custom type snVrrpVirRtrState based on Integer32"""
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


_SnVrrpVirRtrState_Type.__name__ = "Integer32"
_SnVrrpVirRtrState_Object = MibTableColumn
snVrrpVirRtrState = _SnVrrpVirRtrState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 10),
    _SnVrrpVirRtrState_Type()
)
snVrrpVirRtrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtrState.setStatus("deprecated")


class _SnVrrpVirRtrActivate_Type(Integer32):
    """Custom type snVrrpVirRtrActivate based on Integer32"""
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


_SnVrrpVirRtrActivate_Type.__name__ = "Integer32"
_SnVrrpVirRtrActivate_Object = MibTableColumn
snVrrpVirRtrActivate = _SnVrrpVirRtrActivate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 11),
    _SnVrrpVirRtrActivate_Type()
)
snVrrpVirRtrActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtrActivate.setStatus("deprecated")


class _SnVrrpVirRtrIpAddrMask_Type(OctetString):
    """Custom type snVrrpVirRtrIpAddrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SnVrrpVirRtrIpAddrMask_Type.__name__ = "OctetString"
_SnVrrpVirRtrIpAddrMask_Object = MibTableColumn
snVrrpVirRtrIpAddrMask = _SnVrrpVirRtrIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 12),
    _SnVrrpVirRtrIpAddrMask_Type()
)
snVrrpVirRtrIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtrIpAddrMask.setStatus("deprecated")


class _SnVrrpVirRtrTrackPortMask_Type(OctetString):
    """Custom type snVrrpVirRtrTrackPortMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 32),
    )


_SnVrrpVirRtrTrackPortMask_Type.__name__ = "OctetString"
_SnVrrpVirRtrTrackPortMask_Object = MibTableColumn
snVrrpVirRtrTrackPortMask = _SnVrrpVirRtrTrackPortMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 13),
    _SnVrrpVirRtrTrackPortMask_Type()
)
snVrrpVirRtrTrackPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtrTrackPortMask.setStatus("deprecated")


class _SnVrrpVirRtrTrackVifMask_Type(OctetString):
    """Custom type snVrrpVirRtrTrackVifMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 512),
    )


_SnVrrpVirRtrTrackVifMask_Type.__name__ = "OctetString"
_SnVrrpVirRtrTrackVifMask_Object = MibTableColumn
snVrrpVirRtrTrackVifMask = _SnVrrpVirRtrTrackVifMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 14),
    _SnVrrpVirRtrTrackVifMask_Type()
)
snVrrpVirRtrTrackVifMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtrTrackVifMask.setStatus("deprecated")


class _SnVrrpVirRtrRowStatus_Type(Integer32):
    """Custom type snVrrpVirRtrRowStatus based on Integer32"""
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


_SnVrrpVirRtrRowStatus_Type.__name__ = "Integer32"
_SnVrrpVirRtrRowStatus_Object = MibTableColumn
snVrrpVirRtrRowStatus = _SnVrrpVirRtrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 15),
    _SnVrrpVirRtrRowStatus_Type()
)
snVrrpVirRtrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtrRowStatus.setStatus("deprecated")
_SnVrrpVirRtrRxArpPktDropCnts_Type = Counter32
_SnVrrpVirRtrRxArpPktDropCnts_Object = MibTableColumn
snVrrpVirRtrRxArpPktDropCnts = _SnVrrpVirRtrRxArpPktDropCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 16),
    _SnVrrpVirRtrRxArpPktDropCnts_Type()
)
snVrrpVirRtrRxArpPktDropCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtrRxArpPktDropCnts.setStatus("deprecated")
_SnVrrpVirRtrRxIpPktDropCnts_Type = Counter32
_SnVrrpVirRtrRxIpPktDropCnts_Object = MibTableColumn
snVrrpVirRtrRxIpPktDropCnts = _SnVrrpVirRtrRxIpPktDropCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 17),
    _SnVrrpVirRtrRxIpPktDropCnts_Type()
)
snVrrpVirRtrRxIpPktDropCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtrRxIpPktDropCnts.setStatus("deprecated")
_SnVrrpVirRtrRxPortMismatchCnts_Type = Counter32
_SnVrrpVirRtrRxPortMismatchCnts_Object = MibTableColumn
snVrrpVirRtrRxPortMismatchCnts = _SnVrrpVirRtrRxPortMismatchCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 18),
    _SnVrrpVirRtrRxPortMismatchCnts_Type()
)
snVrrpVirRtrRxPortMismatchCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtrRxPortMismatchCnts.setStatus("deprecated")
_SnVrrpVirRtrRxNumOfIpMismatchCnts_Type = Counter32
_SnVrrpVirRtrRxNumOfIpMismatchCnts_Object = MibTableColumn
snVrrpVirRtrRxNumOfIpMismatchCnts = _SnVrrpVirRtrRxNumOfIpMismatchCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 19),
    _SnVrrpVirRtrRxNumOfIpMismatchCnts_Type()
)
snVrrpVirRtrRxNumOfIpMismatchCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtrRxNumOfIpMismatchCnts.setStatus("deprecated")
_SnVrrpVirRtrRxIpMismatchCnts_Type = Counter32
_SnVrrpVirRtrRxIpMismatchCnts_Object = MibTableColumn
snVrrpVirRtrRxIpMismatchCnts = _SnVrrpVirRtrRxIpMismatchCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 20),
    _SnVrrpVirRtrRxIpMismatchCnts_Type()
)
snVrrpVirRtrRxIpMismatchCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtrRxIpMismatchCnts.setStatus("deprecated")
_SnVrrpVirRtrRxHelloIntMismatchCnts_Type = Counter32
_SnVrrpVirRtrRxHelloIntMismatchCnts_Object = MibTableColumn
snVrrpVirRtrRxHelloIntMismatchCnts = _SnVrrpVirRtrRxHelloIntMismatchCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 21),
    _SnVrrpVirRtrRxHelloIntMismatchCnts_Type()
)
snVrrpVirRtrRxHelloIntMismatchCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtrRxHelloIntMismatchCnts.setStatus("deprecated")
_SnVrrpVirRtrRxPriorityZeroFromMasterCnts_Type = Counter32
_SnVrrpVirRtrRxPriorityZeroFromMasterCnts_Object = MibTableColumn
snVrrpVirRtrRxPriorityZeroFromMasterCnts = _SnVrrpVirRtrRxPriorityZeroFromMasterCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 22),
    _SnVrrpVirRtrRxPriorityZeroFromMasterCnts_Type()
)
snVrrpVirRtrRxPriorityZeroFromMasterCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtrRxPriorityZeroFromMasterCnts.setStatus("deprecated")
_SnVrrpVirRtrRxHigherPriorityCnts_Type = Counter32
_SnVrrpVirRtrRxHigherPriorityCnts_Object = MibTableColumn
snVrrpVirRtrRxHigherPriorityCnts = _SnVrrpVirRtrRxHigherPriorityCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 23),
    _SnVrrpVirRtrRxHigherPriorityCnts_Type()
)
snVrrpVirRtrRxHigherPriorityCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtrRxHigherPriorityCnts.setStatus("deprecated")
_SnVrrpVirRtrTransToMasterStateCnts_Type = Counter32
_SnVrrpVirRtrTransToMasterStateCnts_Object = MibTableColumn
snVrrpVirRtrTransToMasterStateCnts = _SnVrrpVirRtrTransToMasterStateCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 24),
    _SnVrrpVirRtrTransToMasterStateCnts_Type()
)
snVrrpVirRtrTransToMasterStateCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtrTransToMasterStateCnts.setStatus("deprecated")
_SnVrrpVirRtrTransToBackupStateCnts_Type = Counter32
_SnVrrpVirRtrTransToBackupStateCnts_Object = MibTableColumn
snVrrpVirRtrTransToBackupStateCnts = _SnVrrpVirRtrTransToBackupStateCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 25),
    _SnVrrpVirRtrTransToBackupStateCnts_Type()
)
snVrrpVirRtrTransToBackupStateCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtrTransToBackupStateCnts.setStatus("deprecated")
_SnVrrpVirRtrCurrDeadInt_Type = Integer32
_SnVrrpVirRtrCurrDeadInt_Object = MibTableColumn
snVrrpVirRtrCurrDeadInt = _SnVrrpVirRtrCurrDeadInt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 26),
    _SnVrrpVirRtrCurrDeadInt_Type()
)
snVrrpVirRtrCurrDeadInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtrCurrDeadInt.setStatus("deprecated")
_SnVrrpVirRtrTrackPortList_Type = OctetString
_SnVrrpVirRtrTrackPortList_Object = MibTableColumn
snVrrpVirRtrTrackPortList = _SnVrrpVirRtrTrackPortList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 27),
    _SnVrrpVirRtrTrackPortList_Type()
)
snVrrpVirRtrTrackPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtrTrackPortList.setStatus("deprecated")
_SnVrrpVirRtrTrackVifPortList_Type = OctetString
_SnVrrpVirRtrTrackVifPortList_Object = MibTableColumn
snVrrpVirRtrTrackVifPortList = _SnVrrpVirRtrTrackVifPortList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 28),
    _SnVrrpVirRtrTrackVifPortList_Type()
)
snVrrpVirRtrTrackVifPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtrTrackVifPortList.setStatus("deprecated")
_SnVrrpIntf2_ObjectIdentity = ObjectIdentity
snVrrpIntf2 = _SnVrrpIntf2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 4)
)
_SnVrrpIf2Table_Object = MibTable
snVrrpIf2Table = _SnVrrpIf2Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 4, 1)
)
if mibBuilder.loadTexts:
    snVrrpIf2Table.setStatus("mandatory")
_SnVrrpIf2Entry_Object = MibTableRow
snVrrpIf2Entry = _SnVrrpIf2Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 4, 1, 1)
)
snVrrpIf2Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    snVrrpIf2Entry.setStatus("mandatory")


class _SnVrrpIf2AuthType_Type(Integer32):
    """Custom type snVrrpIf2AuthType based on Integer32"""
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


_SnVrrpIf2AuthType_Type.__name__ = "Integer32"
_SnVrrpIf2AuthType_Object = MibTableColumn
snVrrpIf2AuthType = _SnVrrpIf2AuthType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 4, 1, 1, 1),
    _SnVrrpIf2AuthType_Type()
)
snVrrpIf2AuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpIf2AuthType.setStatus("mandatory")


class _SnVrrpIf2AuthPassword_Type(OctetString):
    """Custom type snVrrpIf2AuthPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SnVrrpIf2AuthPassword_Type.__name__ = "OctetString"
_SnVrrpIf2AuthPassword_Object = MibTableColumn
snVrrpIf2AuthPassword = _SnVrrpIf2AuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 4, 1, 1, 2),
    _SnVrrpIf2AuthPassword_Type()
)
snVrrpIf2AuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpIf2AuthPassword.setStatus("mandatory")
_SnVrrpIf2RxHeaderErrCnts_Type = Counter32
_SnVrrpIf2RxHeaderErrCnts_Object = MibTableColumn
snVrrpIf2RxHeaderErrCnts = _SnVrrpIf2RxHeaderErrCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 4, 1, 1, 3),
    _SnVrrpIf2RxHeaderErrCnts_Type()
)
snVrrpIf2RxHeaderErrCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpIf2RxHeaderErrCnts.setStatus("mandatory")
_SnVrrpIf2RxAuthTypeErrCnts_Type = Counter32
_SnVrrpIf2RxAuthTypeErrCnts_Object = MibTableColumn
snVrrpIf2RxAuthTypeErrCnts = _SnVrrpIf2RxAuthTypeErrCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 4, 1, 1, 4),
    _SnVrrpIf2RxAuthTypeErrCnts_Type()
)
snVrrpIf2RxAuthTypeErrCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpIf2RxAuthTypeErrCnts.setStatus("mandatory")
_SnVrrpIf2RxAuthPwdMismatchErrCnts_Type = Counter32
_SnVrrpIf2RxAuthPwdMismatchErrCnts_Object = MibTableColumn
snVrrpIf2RxAuthPwdMismatchErrCnts = _SnVrrpIf2RxAuthPwdMismatchErrCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 4, 1, 1, 5),
    _SnVrrpIf2RxAuthPwdMismatchErrCnts_Type()
)
snVrrpIf2RxAuthPwdMismatchErrCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpIf2RxAuthPwdMismatchErrCnts.setStatus("mandatory")
_SnVrrpIf2RxVridErrCnts_Type = Counter32
_SnVrrpIf2RxVridErrCnts_Object = MibTableColumn
snVrrpIf2RxVridErrCnts = _SnVrrpIf2RxVridErrCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 4, 1, 1, 6),
    _SnVrrpIf2RxVridErrCnts_Type()
)
snVrrpIf2RxVridErrCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpIf2RxVridErrCnts.setStatus("mandatory")
_SnVrrpVirRtr2_ObjectIdentity = ObjectIdentity
snVrrpVirRtr2 = _SnVrrpVirRtr2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5)
)
_SnVrrpVirRtr2Table_Object = MibTable
snVrrpVirRtr2Table = _SnVrrpVirRtr2Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1)
)
if mibBuilder.loadTexts:
    snVrrpVirRtr2Table.setStatus("mandatory")
_SnVrrpVirRtr2Entry_Object = MibTableRow
snVrrpVirRtr2Entry = _SnVrrpVirRtr2Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1)
)
snVrrpVirRtr2Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HP-SN-IP-VRRP-MIB", "snVrrpVirRtr2Id"),
)
if mibBuilder.loadTexts:
    snVrrpVirRtr2Entry.setStatus("mandatory")


class _SnVrrpVirRtr2Id_Type(Integer32):
    """Custom type snVrrpVirRtr2Id based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnVrrpVirRtr2Id_Type.__name__ = "Integer32"
_SnVrrpVirRtr2Id_Object = MibTableColumn
snVrrpVirRtr2Id = _SnVrrpVirRtr2Id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 1),
    _SnVrrpVirRtr2Id_Type()
)
snVrrpVirRtr2Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtr2Id.setStatus("mandatory")


class _SnVrrpVirRtr2Ownership_Type(Integer32):
    """Custom type snVrrpVirRtr2Ownership based on Integer32"""
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


_SnVrrpVirRtr2Ownership_Type.__name__ = "Integer32"
_SnVrrpVirRtr2Ownership_Object = MibTableColumn
snVrrpVirRtr2Ownership = _SnVrrpVirRtr2Ownership_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 2),
    _SnVrrpVirRtr2Ownership_Type()
)
snVrrpVirRtr2Ownership.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtr2Ownership.setStatus("mandatory")


class _SnVrrpVirRtr2CfgPriority_Type(Integer32):
    """Custom type snVrrpVirRtr2CfgPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnVrrpVirRtr2CfgPriority_Type.__name__ = "Integer32"
_SnVrrpVirRtr2CfgPriority_Object = MibTableColumn
snVrrpVirRtr2CfgPriority = _SnVrrpVirRtr2CfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 3),
    _SnVrrpVirRtr2CfgPriority_Type()
)
snVrrpVirRtr2CfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtr2CfgPriority.setStatus("mandatory")


class _SnVrrpVirRtr2TrackPriority_Type(Integer32):
    """Custom type snVrrpVirRtr2TrackPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_SnVrrpVirRtr2TrackPriority_Type.__name__ = "Integer32"
_SnVrrpVirRtr2TrackPriority_Object = MibTableColumn
snVrrpVirRtr2TrackPriority = _SnVrrpVirRtr2TrackPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 4),
    _SnVrrpVirRtr2TrackPriority_Type()
)
snVrrpVirRtr2TrackPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtr2TrackPriority.setStatus("mandatory")


class _SnVrrpVirRtr2CurrPriority_Type(Integer32):
    """Custom type snVrrpVirRtr2CurrPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_SnVrrpVirRtr2CurrPriority_Type.__name__ = "Integer32"
_SnVrrpVirRtr2CurrPriority_Object = MibTableColumn
snVrrpVirRtr2CurrPriority = _SnVrrpVirRtr2CurrPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 5),
    _SnVrrpVirRtr2CurrPriority_Type()
)
snVrrpVirRtr2CurrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtr2CurrPriority.setStatus("mandatory")


class _SnVrrpVirRtr2HelloInt_Type(Integer32):
    """Custom type snVrrpVirRtr2HelloInt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 84),
    )


_SnVrrpVirRtr2HelloInt_Type.__name__ = "Integer32"
_SnVrrpVirRtr2HelloInt_Object = MibTableColumn
snVrrpVirRtr2HelloInt = _SnVrrpVirRtr2HelloInt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 6),
    _SnVrrpVirRtr2HelloInt_Type()
)
snVrrpVirRtr2HelloInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtr2HelloInt.setStatus("mandatory")


class _SnVrrpVirRtr2DeadInt_Type(Integer32):
    """Custom type snVrrpVirRtr2DeadInt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_SnVrrpVirRtr2DeadInt_Type.__name__ = "Integer32"
_SnVrrpVirRtr2DeadInt_Object = MibTableColumn
snVrrpVirRtr2DeadInt = _SnVrrpVirRtr2DeadInt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 7),
    _SnVrrpVirRtr2DeadInt_Type()
)
snVrrpVirRtr2DeadInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtr2DeadInt.setStatus("mandatory")


class _SnVrrpVirRtr2PreemptMode_Type(Integer32):
    """Custom type snVrrpVirRtr2PreemptMode based on Integer32"""
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


_SnVrrpVirRtr2PreemptMode_Type.__name__ = "Integer32"
_SnVrrpVirRtr2PreemptMode_Object = MibTableColumn
snVrrpVirRtr2PreemptMode = _SnVrrpVirRtr2PreemptMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 8),
    _SnVrrpVirRtr2PreemptMode_Type()
)
snVrrpVirRtr2PreemptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtr2PreemptMode.setStatus("mandatory")


class _SnVrrpVirRtr2State_Type(Integer32):
    """Custom type snVrrpVirRtr2State based on Integer32"""
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


_SnVrrpVirRtr2State_Type.__name__ = "Integer32"
_SnVrrpVirRtr2State_Object = MibTableColumn
snVrrpVirRtr2State = _SnVrrpVirRtr2State_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 9),
    _SnVrrpVirRtr2State_Type()
)
snVrrpVirRtr2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtr2State.setStatus("mandatory")


class _SnVrrpVirRtr2IpAddrMask_Type(OctetString):
    """Custom type snVrrpVirRtr2IpAddrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SnVrrpVirRtr2IpAddrMask_Type.__name__ = "OctetString"
_SnVrrpVirRtr2IpAddrMask_Object = MibTableColumn
snVrrpVirRtr2IpAddrMask = _SnVrrpVirRtr2IpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 10),
    _SnVrrpVirRtr2IpAddrMask_Type()
)
snVrrpVirRtr2IpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtr2IpAddrMask.setStatus("mandatory")


class _SnVrrpVirRtr2Activate_Type(Integer32):
    """Custom type snVrrpVirRtr2Activate based on Integer32"""
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


_SnVrrpVirRtr2Activate_Type.__name__ = "Integer32"
_SnVrrpVirRtr2Activate_Object = MibTableColumn
snVrrpVirRtr2Activate = _SnVrrpVirRtr2Activate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 11),
    _SnVrrpVirRtr2Activate_Type()
)
snVrrpVirRtr2Activate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtr2Activate.setStatus("mandatory")


class _SnVrrpVirRtr2BackupInt_Type(Integer32):
    """Custom type snVrrpVirRtr2BackupInt based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_SnVrrpVirRtr2BackupInt_Type.__name__ = "Integer32"
_SnVrrpVirRtr2BackupInt_Object = MibTableColumn
snVrrpVirRtr2BackupInt = _SnVrrpVirRtr2BackupInt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 12),
    _SnVrrpVirRtr2BackupInt_Type()
)
snVrrpVirRtr2BackupInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtr2BackupInt.setStatus("mandatory")


class _SnVrrpVirRtr2RowStatus_Type(Integer32):
    """Custom type snVrrpVirRtr2RowStatus based on Integer32"""
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


_SnVrrpVirRtr2RowStatus_Type.__name__ = "Integer32"
_SnVrrpVirRtr2RowStatus_Object = MibTableColumn
snVrrpVirRtr2RowStatus = _SnVrrpVirRtr2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 13),
    _SnVrrpVirRtr2RowStatus_Type()
)
snVrrpVirRtr2RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtr2RowStatus.setStatus("mandatory")
_SnVrrpVirRtr2RxArpPktDropCnts_Type = Counter32
_SnVrrpVirRtr2RxArpPktDropCnts_Object = MibTableColumn
snVrrpVirRtr2RxArpPktDropCnts = _SnVrrpVirRtr2RxArpPktDropCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 14),
    _SnVrrpVirRtr2RxArpPktDropCnts_Type()
)
snVrrpVirRtr2RxArpPktDropCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtr2RxArpPktDropCnts.setStatus("mandatory")
_SnVrrpVirRtr2RxIpPktDropCnts_Type = Counter32
_SnVrrpVirRtr2RxIpPktDropCnts_Object = MibTableColumn
snVrrpVirRtr2RxIpPktDropCnts = _SnVrrpVirRtr2RxIpPktDropCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 15),
    _SnVrrpVirRtr2RxIpPktDropCnts_Type()
)
snVrrpVirRtr2RxIpPktDropCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtr2RxIpPktDropCnts.setStatus("mandatory")
_SnVrrpVirRtr2RxPortMismatchCnts_Type = Counter32
_SnVrrpVirRtr2RxPortMismatchCnts_Object = MibTableColumn
snVrrpVirRtr2RxPortMismatchCnts = _SnVrrpVirRtr2RxPortMismatchCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 16),
    _SnVrrpVirRtr2RxPortMismatchCnts_Type()
)
snVrrpVirRtr2RxPortMismatchCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtr2RxPortMismatchCnts.setStatus("mandatory")
_SnVrrpVirRtr2RxNumOfIpMismatchCnts_Type = Counter32
_SnVrrpVirRtr2RxNumOfIpMismatchCnts_Object = MibTableColumn
snVrrpVirRtr2RxNumOfIpMismatchCnts = _SnVrrpVirRtr2RxNumOfIpMismatchCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 17),
    _SnVrrpVirRtr2RxNumOfIpMismatchCnts_Type()
)
snVrrpVirRtr2RxNumOfIpMismatchCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtr2RxNumOfIpMismatchCnts.setStatus("mandatory")
_SnVrrpVirRtr2RxIpMismatchCnts_Type = Counter32
_SnVrrpVirRtr2RxIpMismatchCnts_Object = MibTableColumn
snVrrpVirRtr2RxIpMismatchCnts = _SnVrrpVirRtr2RxIpMismatchCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 18),
    _SnVrrpVirRtr2RxIpMismatchCnts_Type()
)
snVrrpVirRtr2RxIpMismatchCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtr2RxIpMismatchCnts.setStatus("mandatory")
_SnVrrpVirRtr2RxHelloIntMismatchCnts_Type = Counter32
_SnVrrpVirRtr2RxHelloIntMismatchCnts_Object = MibTableColumn
snVrrpVirRtr2RxHelloIntMismatchCnts = _SnVrrpVirRtr2RxHelloIntMismatchCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 19),
    _SnVrrpVirRtr2RxHelloIntMismatchCnts_Type()
)
snVrrpVirRtr2RxHelloIntMismatchCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtr2RxHelloIntMismatchCnts.setStatus("mandatory")
_SnVrrpVirRtr2RxPriorityZeroFromMasterCnts_Type = Counter32
_SnVrrpVirRtr2RxPriorityZeroFromMasterCnts_Object = MibTableColumn
snVrrpVirRtr2RxPriorityZeroFromMasterCnts = _SnVrrpVirRtr2RxPriorityZeroFromMasterCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 20),
    _SnVrrpVirRtr2RxPriorityZeroFromMasterCnts_Type()
)
snVrrpVirRtr2RxPriorityZeroFromMasterCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtr2RxPriorityZeroFromMasterCnts.setStatus("mandatory")
_SnVrrpVirRtr2RxHigherPriorityCnts_Type = Counter32
_SnVrrpVirRtr2RxHigherPriorityCnts_Object = MibTableColumn
snVrrpVirRtr2RxHigherPriorityCnts = _SnVrrpVirRtr2RxHigherPriorityCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 21),
    _SnVrrpVirRtr2RxHigherPriorityCnts_Type()
)
snVrrpVirRtr2RxHigherPriorityCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtr2RxHigherPriorityCnts.setStatus("mandatory")
_SnVrrpVirRtr2TransToMasterStateCnts_Type = Counter32
_SnVrrpVirRtr2TransToMasterStateCnts_Object = MibTableColumn
snVrrpVirRtr2TransToMasterStateCnts = _SnVrrpVirRtr2TransToMasterStateCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 22),
    _SnVrrpVirRtr2TransToMasterStateCnts_Type()
)
snVrrpVirRtr2TransToMasterStateCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtr2TransToMasterStateCnts.setStatus("mandatory")
_SnVrrpVirRtr2TransToBackupStateCnts_Type = Counter32
_SnVrrpVirRtr2TransToBackupStateCnts_Object = MibTableColumn
snVrrpVirRtr2TransToBackupStateCnts = _SnVrrpVirRtr2TransToBackupStateCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 23),
    _SnVrrpVirRtr2TransToBackupStateCnts_Type()
)
snVrrpVirRtr2TransToBackupStateCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtr2TransToBackupStateCnts.setStatus("mandatory")
_SnVrrpVirRtr2CurrDeadInt_Type = Integer32
_SnVrrpVirRtr2CurrDeadInt_Object = MibTableColumn
snVrrpVirRtr2CurrDeadInt = _SnVrrpVirRtr2CurrDeadInt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 24),
    _SnVrrpVirRtr2CurrDeadInt_Type()
)
snVrrpVirRtr2CurrDeadInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtr2CurrDeadInt.setStatus("mandatory")
_SnVrrpVirRtr2TrackPortList_Type = OctetString
_SnVrrpVirRtr2TrackPortList_Object = MibTableColumn
snVrrpVirRtr2TrackPortList = _SnVrrpVirRtr2TrackPortList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 25),
    _SnVrrpVirRtr2TrackPortList_Type()
)
snVrrpVirRtr2TrackPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtr2TrackPortList.setStatus("mandatory")


class _SnVrrpVirRtr2AdvertiseBackup_Type(Integer32):
    """Custom type snVrrpVirRtr2AdvertiseBackup based on Integer32"""
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


_SnVrrpVirRtr2AdvertiseBackup_Type.__name__ = "Integer32"
_SnVrrpVirRtr2AdvertiseBackup_Object = MibTableColumn
snVrrpVirRtr2AdvertiseBackup = _SnVrrpVirRtr2AdvertiseBackup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 26),
    _SnVrrpVirRtr2AdvertiseBackup_Type()
)
snVrrpVirRtr2AdvertiseBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVrrpVirRtr2AdvertiseBackup.setStatus("mandatory")
_SnVrrpVirRtr2MasterIpAddr_Type = IpAddress
_SnVrrpVirRtr2MasterIpAddr_Object = MibTableColumn
snVrrpVirRtr2MasterIpAddr = _SnVrrpVirRtr2MasterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 27),
    _SnVrrpVirRtr2MasterIpAddr_Type()
)
snVrrpVirRtr2MasterIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtr2MasterIpAddr.setStatus("mandatory")


class _SnVrrpVirRtr2IpAddrCount_Type(Integer32):
    """Custom type snVrrpVirRtr2IpAddrCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnVrrpVirRtr2IpAddrCount_Type.__name__ = "Integer32"
_SnVrrpVirRtr2IpAddrCount_Object = MibTableColumn
snVrrpVirRtr2IpAddrCount = _SnVrrpVirRtr2IpAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 28),
    _SnVrrpVirRtr2IpAddrCount_Type()
)
snVrrpVirRtr2IpAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtr2IpAddrCount.setStatus("mandatory")
_SnVrrpVirRtr2VirtualMacAddr_Type = MacAddress
_SnVrrpVirRtr2VirtualMacAddr_Object = MibTableColumn
snVrrpVirRtr2VirtualMacAddr = _SnVrrpVirRtr2VirtualMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 29),
    _SnVrrpVirRtr2VirtualMacAddr_Type()
)
snVrrpVirRtr2VirtualMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVrrpVirRtr2VirtualMacAddr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SN-IP-VRRP-MIB",
    **{"MacAddress": MacAddress,
       "snVrrpGlobal": snVrrpGlobal,
       "snVrrpGroupOperMode": snVrrpGroupOperMode,
       "snVrrpIfStateChangeTrap": snVrrpIfStateChangeTrap,
       "snVrrpIfMaxNumVridPerIntf": snVrrpIfMaxNumVridPerIntf,
       "snVrrpIfMaxNumVridPerSystem": snVrrpIfMaxNumVridPerSystem,
       "snVrrpClearVrrpStat": snVrrpClearVrrpStat,
       "snVrrpGroupOperModeVrrpextended": snVrrpGroupOperModeVrrpextended,
       "snVrrpIntf": snVrrpIntf,
       "snVrrpIfTable": snVrrpIfTable,
       "snVrrpIfEntry": snVrrpIfEntry,
       "snVrrpIfPort": snVrrpIfPort,
       "snVrrpIfAuthType": snVrrpIfAuthType,
       "snVrrpIfAuthPassword": snVrrpIfAuthPassword,
       "snVrrpIfRxHeaderErrCnts": snVrrpIfRxHeaderErrCnts,
       "snVrrpIfRxAuthTypeErrCnts": snVrrpIfRxAuthTypeErrCnts,
       "snVrrpIfRxAuthPwdMismatchErrCnts": snVrrpIfRxAuthPwdMismatchErrCnts,
       "snVrrpIfRxVridErrCnts": snVrrpIfRxVridErrCnts,
       "snVrrpVirRtr": snVrrpVirRtr,
       "snVrrpVirRtrTable": snVrrpVirRtrTable,
       "snVrrpVirRtrEntry": snVrrpVirRtrEntry,
       "snVrrpVirRtrPort": snVrrpVirRtrPort,
       "snVrrpVirRtrId": snVrrpVirRtrId,
       "snVrrpVirRtrOwnership": snVrrpVirRtrOwnership,
       "snVrrpVirRtrCfgPriority": snVrrpVirRtrCfgPriority,
       "snVrrpVirRtrTrackPriority": snVrrpVirRtrTrackPriority,
       "snVrrpVirRtrCurrPriority": snVrrpVirRtrCurrPriority,
       "snVrrpVirRtrHelloInt": snVrrpVirRtrHelloInt,
       "snVrrpVirRtrDeadInt": snVrrpVirRtrDeadInt,
       "snVrrpVirRtrPreemptMode": snVrrpVirRtrPreemptMode,
       "snVrrpVirRtrState": snVrrpVirRtrState,
       "snVrrpVirRtrActivate": snVrrpVirRtrActivate,
       "snVrrpVirRtrIpAddrMask": snVrrpVirRtrIpAddrMask,
       "snVrrpVirRtrTrackPortMask": snVrrpVirRtrTrackPortMask,
       "snVrrpVirRtrTrackVifMask": snVrrpVirRtrTrackVifMask,
       "snVrrpVirRtrRowStatus": snVrrpVirRtrRowStatus,
       "snVrrpVirRtrRxArpPktDropCnts": snVrrpVirRtrRxArpPktDropCnts,
       "snVrrpVirRtrRxIpPktDropCnts": snVrrpVirRtrRxIpPktDropCnts,
       "snVrrpVirRtrRxPortMismatchCnts": snVrrpVirRtrRxPortMismatchCnts,
       "snVrrpVirRtrRxNumOfIpMismatchCnts": snVrrpVirRtrRxNumOfIpMismatchCnts,
       "snVrrpVirRtrRxIpMismatchCnts": snVrrpVirRtrRxIpMismatchCnts,
       "snVrrpVirRtrRxHelloIntMismatchCnts": snVrrpVirRtrRxHelloIntMismatchCnts,
       "snVrrpVirRtrRxPriorityZeroFromMasterCnts": snVrrpVirRtrRxPriorityZeroFromMasterCnts,
       "snVrrpVirRtrRxHigherPriorityCnts": snVrrpVirRtrRxHigherPriorityCnts,
       "snVrrpVirRtrTransToMasterStateCnts": snVrrpVirRtrTransToMasterStateCnts,
       "snVrrpVirRtrTransToBackupStateCnts": snVrrpVirRtrTransToBackupStateCnts,
       "snVrrpVirRtrCurrDeadInt": snVrrpVirRtrCurrDeadInt,
       "snVrrpVirRtrTrackPortList": snVrrpVirRtrTrackPortList,
       "snVrrpVirRtrTrackVifPortList": snVrrpVirRtrTrackVifPortList,
       "snVrrpIntf2": snVrrpIntf2,
       "snVrrpIf2Table": snVrrpIf2Table,
       "snVrrpIf2Entry": snVrrpIf2Entry,
       "snVrrpIf2AuthType": snVrrpIf2AuthType,
       "snVrrpIf2AuthPassword": snVrrpIf2AuthPassword,
       "snVrrpIf2RxHeaderErrCnts": snVrrpIf2RxHeaderErrCnts,
       "snVrrpIf2RxAuthTypeErrCnts": snVrrpIf2RxAuthTypeErrCnts,
       "snVrrpIf2RxAuthPwdMismatchErrCnts": snVrrpIf2RxAuthPwdMismatchErrCnts,
       "snVrrpIf2RxVridErrCnts": snVrrpIf2RxVridErrCnts,
       "snVrrpVirRtr2": snVrrpVirRtr2,
       "snVrrpVirRtr2Table": snVrrpVirRtr2Table,
       "snVrrpVirRtr2Entry": snVrrpVirRtr2Entry,
       "snVrrpVirRtr2Id": snVrrpVirRtr2Id,
       "snVrrpVirRtr2Ownership": snVrrpVirRtr2Ownership,
       "snVrrpVirRtr2CfgPriority": snVrrpVirRtr2CfgPriority,
       "snVrrpVirRtr2TrackPriority": snVrrpVirRtr2TrackPriority,
       "snVrrpVirRtr2CurrPriority": snVrrpVirRtr2CurrPriority,
       "snVrrpVirRtr2HelloInt": snVrrpVirRtr2HelloInt,
       "snVrrpVirRtr2DeadInt": snVrrpVirRtr2DeadInt,
       "snVrrpVirRtr2PreemptMode": snVrrpVirRtr2PreemptMode,
       "snVrrpVirRtr2State": snVrrpVirRtr2State,
       "snVrrpVirRtr2IpAddrMask": snVrrpVirRtr2IpAddrMask,
       "snVrrpVirRtr2Activate": snVrrpVirRtr2Activate,
       "snVrrpVirRtr2BackupInt": snVrrpVirRtr2BackupInt,
       "snVrrpVirRtr2RowStatus": snVrrpVirRtr2RowStatus,
       "snVrrpVirRtr2RxArpPktDropCnts": snVrrpVirRtr2RxArpPktDropCnts,
       "snVrrpVirRtr2RxIpPktDropCnts": snVrrpVirRtr2RxIpPktDropCnts,
       "snVrrpVirRtr2RxPortMismatchCnts": snVrrpVirRtr2RxPortMismatchCnts,
       "snVrrpVirRtr2RxNumOfIpMismatchCnts": snVrrpVirRtr2RxNumOfIpMismatchCnts,
       "snVrrpVirRtr2RxIpMismatchCnts": snVrrpVirRtr2RxIpMismatchCnts,
       "snVrrpVirRtr2RxHelloIntMismatchCnts": snVrrpVirRtr2RxHelloIntMismatchCnts,
       "snVrrpVirRtr2RxPriorityZeroFromMasterCnts": snVrrpVirRtr2RxPriorityZeroFromMasterCnts,
       "snVrrpVirRtr2RxHigherPriorityCnts": snVrrpVirRtr2RxHigherPriorityCnts,
       "snVrrpVirRtr2TransToMasterStateCnts": snVrrpVirRtr2TransToMasterStateCnts,
       "snVrrpVirRtr2TransToBackupStateCnts": snVrrpVirRtr2TransToBackupStateCnts,
       "snVrrpVirRtr2CurrDeadInt": snVrrpVirRtr2CurrDeadInt,
       "snVrrpVirRtr2TrackPortList": snVrrpVirRtr2TrackPortList,
       "snVrrpVirRtr2AdvertiseBackup": snVrrpVirRtr2AdvertiseBackup,
       "snVrrpVirRtr2MasterIpAddr": snVrrpVirRtr2MasterIpAddr,
       "snVrrpVirRtr2IpAddrCount": snVrrpVirRtr2IpAddrCount,
       "snVrrpVirRtr2VirtualMacAddr": snVrrpVirRtr2VirtualMacAddr}
)
