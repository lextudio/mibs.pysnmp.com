# SNMP MIB module (Wellfleet-SYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-SYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:12 2024
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

(wfSystem,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfSystem")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfSys_ObjectIdentity = ObjectIdentity
wfSys = _WfSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1)
)
_WfSysDescr_Type = DisplayString
_WfSysDescr_Object = MibScalar
wfSysDescr = _WfSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 1),
    _WfSysDescr_Type()
)
wfSysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSysDescr.setStatus("mandatory")
_WfSysObjectID_Type = ObjectIdentifier
_WfSysObjectID_Object = MibScalar
wfSysObjectID = _WfSysObjectID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 2),
    _WfSysObjectID_Type()
)
wfSysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSysObjectID.setStatus("mandatory")
_WfSysUpTime_Type = TimeTicks
_WfSysUpTime_Object = MibScalar
wfSysUpTime = _WfSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 3),
    _WfSysUpTime_Type()
)
wfSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSysUpTime.setStatus("mandatory")
_WfSysContact_Type = DisplayString
_WfSysContact_Object = MibScalar
wfSysContact = _WfSysContact_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 4),
    _WfSysContact_Type()
)
wfSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSysContact.setStatus("mandatory")
_WfSysName_Type = DisplayString
_WfSysName_Object = MibScalar
wfSysName = _WfSysName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 5),
    _WfSysName_Type()
)
wfSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSysName.setStatus("mandatory")
_WfSysLocation_Type = DisplayString
_WfSysLocation_Object = MibScalar
wfSysLocation = _WfSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 6),
    _WfSysLocation_Type()
)
wfSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSysLocation.setStatus("mandatory")


class _WfSysServices_Type(Integer32):
    """Custom type wfSysServices based on Integer32"""
    defaultValue = 78


_WfSysServices_Object = MibScalar
wfSysServices = _WfSysServices_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 7),
    _WfSysServices_Type()
)
wfSysServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSysServices.setStatus("mandatory")
_WfSysGmtOffset_Type = Integer32
_WfSysGmtOffset_Object = MibScalar
wfSysGmtOffset = _WfSysGmtOffset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 8),
    _WfSysGmtOffset_Type()
)
wfSysGmtOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSysGmtOffset.setStatus("mandatory")
_WfSysMibVersion_Type = DisplayString
_WfSysMibVersion_Object = MibScalar
wfSysMibVersion = _WfSysMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 9),
    _WfSysMibVersion_Type()
)
wfSysMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSysMibVersion.setStatus("mandatory")
_WfSysMibRevision_Type = Integer32
_WfSysMibRevision_Object = MibScalar
wfSysMibRevision = _WfSysMibRevision_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 10),
    _WfSysMibRevision_Type()
)
wfSysMibRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSysMibRevision.setStatus("mandatory")


class _WfSysAgentType_Type(Integer32):
    """Custom type wfSysAgentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              29,
              30)
        )
    )
    namedValues = NamedValues(
        *(("anhubagenttype", 30),
          ("anrptragenttype", 29),
          ("other", 1))
    )


_WfSysAgentType_Type.__name__ = "Integer32"
_WfSysAgentType_Object = MibScalar
wfSysAgentType = _WfSysAgentType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 11),
    _WfSysAgentType_Type()
)
wfSysAgentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSysAgentType.setStatus("mandatory")


class _WfSysMibCounterEnable_Type(Integer32):
    """Custom type wfSysMibCounterEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfSysMibCounterEnable_Type.__name__ = "Integer32"
_WfSysMibCounterEnable_Object = MibScalar
wfSysMibCounterEnable = _WfSysMibCounterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 12),
    _WfSysMibCounterEnable_Type()
)
wfSysMibCounterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSysMibCounterEnable.setStatus("mandatory")
_WfSysMaxUpTime_Type = TimeTicks
_WfSysMaxUpTime_Object = MibScalar
wfSysMaxUpTime = _WfSysMaxUpTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 13),
    _WfSysMaxUpTime_Type()
)
wfSysMaxUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSysMaxUpTime.setStatus("mandatory")


class _WfSysBccHelpFileName_Type(DisplayString):
    """Custom type wfSysBccHelpFileName based on DisplayString"""
    defaultValue = OctetString("bcc.help")


_WfSysBccHelpFileName_Object = MibScalar
wfSysBccHelpFileName = _WfSysBccHelpFileName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 14),
    _WfSysBccHelpFileName_Type()
)
wfSysBccHelpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSysBccHelpFileName.setStatus("mandatory")


class _WfSysConsoleSlotMask_Type(Gauge32):
    """Custom type wfSysConsoleSlotMask based on Gauge32"""
    defaultValue = 4294705152


_WfSysConsoleSlotMask_Object = MibScalar
wfSysConsoleSlotMask = _WfSysConsoleSlotMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 15),
    _WfSysConsoleSlotMask_Type()
)
wfSysConsoleSlotMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSysConsoleSlotMask.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-SYS-MIB",
    **{"wfSys": wfSys,
       "wfSysDescr": wfSysDescr,
       "wfSysObjectID": wfSysObjectID,
       "wfSysUpTime": wfSysUpTime,
       "wfSysContact": wfSysContact,
       "wfSysName": wfSysName,
       "wfSysLocation": wfSysLocation,
       "wfSysServices": wfSysServices,
       "wfSysGmtOffset": wfSysGmtOffset,
       "wfSysMibVersion": wfSysMibVersion,
       "wfSysMibRevision": wfSysMibRevision,
       "wfSysAgentType": wfSysAgentType,
       "wfSysMibCounterEnable": wfSysMibCounterEnable,
       "wfSysMaxUpTime": wfSysMaxUpTime,
       "wfSysBccHelpFileName": wfSysBccHelpFileName,
       "wfSysConsoleSlotMask": wfSysConsoleSlotMask}
)
