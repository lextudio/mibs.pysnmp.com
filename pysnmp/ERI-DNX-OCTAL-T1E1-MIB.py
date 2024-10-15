# SNMP MIB module (ERI-DNX-OCTAL-T1E1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ERI-DNX-OCTAL-T1E1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:27 2024
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

(DataSwitch,
 DecisionType,
 FunctionSwitch,
 LinkCmdStatus,
 LinkPortAddress,
 OneByteField,
 PortStatus,
 devices,
 trapSequence) = mibBuilder.importSymbols(
    "ERI-DNX-SMC-MIB",
    "DataSwitch",
    "DecisionType",
    "FunctionSwitch",
    "LinkCmdStatus",
    "LinkPortAddress",
    "OneByteField",
    "PortStatus",
    "devices",
    "trapSequence")

(eriMibs,) = mibBuilder.importSymbols(
    "ERI-ROOT-SMI",
    "eriMibs")

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

eriDNXOctalT1E1MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 644, 3, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DnxOT1E1_ObjectIdentity = ObjectIdentity
dnxOT1E1 = _DnxOT1E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4)
)
_DnxOT1E1Enterprise_ObjectIdentity = ObjectIdentity
dnxOT1E1Enterprise = _DnxOT1E1Enterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 0)
)
if mibBuilder.loadTexts:
    dnxOT1E1Enterprise.setStatus("current")
_OteConfig_ObjectIdentity = ObjectIdentity
oteConfig = _OteConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1)
)
_OT1E1ConfigTable_Object = MibTable
oT1E1ConfigTable = _OT1E1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    oT1E1ConfigTable.setStatus("current")
_OT1E1ConfigEntry_Object = MibTableRow
oT1E1ConfigEntry = _OT1E1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1)
)
oT1E1ConfigEntry.setIndexNames(
    (0, "ERI-DNX-OCTAL-T1E1-MIB", "oT1E1CfgLinkAddr"),
)
if mibBuilder.loadTexts:
    oT1E1ConfigEntry.setStatus("current")
_OT1E1CfgLinkAddr_Type = LinkPortAddress
_OT1E1CfgLinkAddr_Object = MibTableColumn
oT1E1CfgLinkAddr = _OT1E1CfgLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 1),
    _OT1E1CfgLinkAddr_Type()
)
oT1E1CfgLinkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oT1E1CfgLinkAddr.setStatus("current")
_OT1E1CfgResource_Type = Integer32
_OT1E1CfgResource_Object = MibTableColumn
oT1E1CfgResource = _OT1E1CfgResource_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 2),
    _OT1E1CfgResource_Type()
)
oT1E1CfgResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oT1E1CfgResource.setStatus("current")


class _OT1E1CfgLinkName_Type(DisplayString):
    """Custom type oT1E1CfgLinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_OT1E1CfgLinkName_Type.__name__ = "DisplayString"
_OT1E1CfgLinkName_Object = MibTableColumn
oT1E1CfgLinkName = _OT1E1CfgLinkName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 3),
    _OT1E1CfgLinkName_Type()
)
oT1E1CfgLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oT1E1CfgLinkName.setStatus("current")
_OT1E1Status_Type = PortStatus
_OT1E1Status_Object = MibTableColumn
oT1E1Status = _OT1E1Status_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 4),
    _OT1E1Status_Type()
)
oT1E1Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oT1E1Status.setStatus("current")


class _OT1E1ClearT1E1_Type(Integer32):
    """Custom type oT1E1ClearT1E1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("framed", 1),
          ("unframed", 2))
    )


_OT1E1ClearT1E1_Type.__name__ = "Integer32"
_OT1E1ClearT1E1_Object = MibTableColumn
oT1E1ClearT1E1 = _OT1E1ClearT1E1_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 5),
    _OT1E1ClearT1E1_Type()
)
oT1E1ClearT1E1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oT1E1ClearT1E1.setStatus("current")


class _OT1E1LineType_Type(Integer32):
    """Custom type oT1E1LineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("e1", 0),
          ("e1-cas", 2),
          ("e1-cas-crc", 3),
          ("e1-crc", 1),
          ("e1-unframed", 4),
          ("t1-ami-unframed", 11),
          ("t1-b8zs-unframed", 10),
          ("t1-d4-ami-62411", 8),
          ("t1-d4-ami-clear", 12),
          ("t1-d4-b8zs", 7),
          ("t1-esf-ami-62411", 6),
          ("t1-esf-ami-clear", 13),
          ("t1-esf-b8zs", 5))
    )


_OT1E1LineType_Type.__name__ = "Integer32"
_OT1E1LineType_Object = MibTableColumn
oT1E1LineType = _OT1E1LineType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 6),
    _OT1E1LineType_Type()
)
oT1E1LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oT1E1LineType.setStatus("current")
_OT1E1NetLoop_Type = FunctionSwitch
_OT1E1NetLoop_Object = MibTableColumn
oT1E1NetLoop = _OT1E1NetLoop_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 7),
    _OT1E1NetLoop_Type()
)
oT1E1NetLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oT1E1NetLoop.setStatus("current")
_OT1E1YelAlrm_Type = DecisionType
_OT1E1YelAlrm_Object = MibTableColumn
oT1E1YelAlrm = _OT1E1YelAlrm_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 8),
    _OT1E1YelAlrm_Type()
)
oT1E1YelAlrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oT1E1YelAlrm.setStatus("current")


class _OT1E1RecoverTime_Type(Integer32):
    """Custom type oT1E1RecoverTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              10,
              15)
        )
    )
    namedValues = NamedValues(
        *(("timeout-10-secs", 10),
          ("timeout-15-secs", 15),
          ("timeout-3-secs", 3))
    )


_OT1E1RecoverTime_Type.__name__ = "Integer32"
_OT1E1RecoverTime_Object = MibTableColumn
oT1E1RecoverTime = _OT1E1RecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 9),
    _OT1E1RecoverTime_Type()
)
oT1E1RecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oT1E1RecoverTime.setStatus("current")


class _OT1E1IdleCode_Type(Integer32):
    """Custom type oT1E1IdleCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("busy", 0),
          ("idle", 1))
    )


_OT1E1IdleCode_Type.__name__ = "Integer32"
_OT1E1IdleCode_Object = MibTableColumn
oT1E1IdleCode = _OT1E1IdleCode_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 10),
    _OT1E1IdleCode_Type()
)
oT1E1IdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oT1E1IdleCode.setStatus("current")


class _OT1E1EsfFormat_Type(Integer32):
    """Custom type oT1E1EsfFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ansi-t1-403", 2),
          ("att-54016", 1),
          ("none", 0))
    )


_OT1E1EsfFormat_Type.__name__ = "Integer32"
_OT1E1EsfFormat_Object = MibTableColumn
oT1E1EsfFormat = _OT1E1EsfFormat_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 11),
    _OT1E1EsfFormat_Type()
)
oT1E1EsfFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oT1E1EsfFormat.setStatus("current")


class _OT1E1CfgLBO_Type(Integer32):
    """Custom type oT1E1CfgLBO based on Integer32"""
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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("e1-longHaul-0-34db", 2),
          ("e1-shortHaul-0-6db", 1),
          ("t1-longHaul-0-0db", 3),
          ("t1-longHaul-15-0db", 5),
          ("t1-longHaul-22-5db", 6),
          ("t1-longHaul-7-5db", 4),
          ("t1-shortHaul-0-133ft", 7),
          ("t1-shortHaul-133-266ft", 8),
          ("t1-shortHaul-266-399ft", 9),
          ("t1-shortHaul-399-533ft", 10),
          ("t1-shortHaul-533-655ft", 11))
    )


_OT1E1CfgLBO_Type.__name__ = "Integer32"
_OT1E1CfgLBO_Object = MibTableColumn
oT1E1CfgLBO = _OT1E1CfgLBO_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 12),
    _OT1E1CfgLBO_Type()
)
oT1E1CfgLBO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oT1E1CfgLBO.setStatus("current")
_OT1E1CfgCmdStatus_Type = LinkCmdStatus
_OT1E1CfgCmdStatus_Object = MibTableColumn
oT1E1CfgCmdStatus = _OT1E1CfgCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 13),
    _OT1E1CfgCmdStatus_Type()
)
oT1E1CfgCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oT1E1CfgCmdStatus.setStatus("current")
_OT1E1Gr303Facility_Type = DecisionType
_OT1E1Gr303Facility_Object = MibTableColumn
oT1E1Gr303Facility = _OT1E1Gr303Facility_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 14),
    _OT1E1Gr303Facility_Type()
)
oT1E1Gr303Facility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oT1E1Gr303Facility.setStatus("obsolete")
_OT1E1NationalBits_Type = OneByteField
_OT1E1NationalBits_Object = MibTableColumn
oT1E1NationalBits = _OT1E1NationalBits_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 15),
    _OT1E1NationalBits_Type()
)
oT1E1NationalBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oT1E1NationalBits.setStatus("current")
_OT1E1InterNational_Type = OneByteField
_OT1E1InterNational_Object = MibTableColumn
oT1E1InterNational = _OT1E1InterNational_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 16),
    _OT1E1InterNational_Type()
)
oT1E1InterNational.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oT1E1InterNational.setStatus("current")
_OteDiag_ObjectIdentity = ObjectIdentity
oteDiag = _OteDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 2)
)

# Managed Objects groups


# Notification objects

oT1E1ConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 0, 1)
)
oT1E1ConfigTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-OCTAL-T1E1-MIB", "oT1E1CfgLinkAddr"),
        ("ERI-DNX-OCTAL-T1E1-MIB", "oT1E1CfgCmdStatus"))
)
if mibBuilder.loadTexts:
    oT1E1ConfigTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERI-DNX-OCTAL-T1E1-MIB",
    **{"dnxOT1E1": dnxOT1E1,
       "dnxOT1E1Enterprise": dnxOT1E1Enterprise,
       "oT1E1ConfigTrap": oT1E1ConfigTrap,
       "oteConfig": oteConfig,
       "oT1E1ConfigTable": oT1E1ConfigTable,
       "oT1E1ConfigEntry": oT1E1ConfigEntry,
       "oT1E1CfgLinkAddr": oT1E1CfgLinkAddr,
       "oT1E1CfgResource": oT1E1CfgResource,
       "oT1E1CfgLinkName": oT1E1CfgLinkName,
       "oT1E1Status": oT1E1Status,
       "oT1E1ClearT1E1": oT1E1ClearT1E1,
       "oT1E1LineType": oT1E1LineType,
       "oT1E1NetLoop": oT1E1NetLoop,
       "oT1E1YelAlrm": oT1E1YelAlrm,
       "oT1E1RecoverTime": oT1E1RecoverTime,
       "oT1E1IdleCode": oT1E1IdleCode,
       "oT1E1EsfFormat": oT1E1EsfFormat,
       "oT1E1CfgLBO": oT1E1CfgLBO,
       "oT1E1CfgCmdStatus": oT1E1CfgCmdStatus,
       "oT1E1Gr303Facility": oT1E1Gr303Facility,
       "oT1E1NationalBits": oT1E1NationalBits,
       "oT1E1InterNational": oT1E1InterNational,
       "oteDiag": oteDiag,
       "eriDNXOctalT1E1MIB": eriDNXOctalT1E1MIB}
)
