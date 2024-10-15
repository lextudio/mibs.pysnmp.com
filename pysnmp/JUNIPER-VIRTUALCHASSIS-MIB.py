# SNMP MIB module (JUNIPER-VIRTUALCHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-VIRTUALCHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:26 2024
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

(jnxExVirtualChassis,) = mibBuilder.importSymbols(
    "JUNIPER-EX-SMI",
    "jnxExVirtualChassis")

(JnxChassisId,) = mibBuilder.importSymbols(
    "JUNIPER-MIB",
    "JnxChassisId")

(jnxVccpNotifications,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxVccpNotifications")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxVirtualChassisMemberMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1)
)
jnxVirtualChassisMemberMIB.setRevisions(
        ("2010-07-13 00:00",
         "2010-10-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxVirtualChassisMemberTable_Object = MibTable
jnxVirtualChassisMemberTable = _JnxVirtualChassisMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    jnxVirtualChassisMemberTable.setStatus("current")
_JnxVirtualChassisMemberEntry_Object = MibTableRow
jnxVirtualChassisMemberEntry = _JnxVirtualChassisMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 1, 1)
)
jnxVirtualChassisMemberEntry.setIndexNames(
    (0, "JUNIPER-VIRTUALCHASSIS-MIB", "jnxVirtualChassisMemberId"),
)
if mibBuilder.loadTexts:
    jnxVirtualChassisMemberEntry.setStatus("current")


class _JnxVirtualChassisMemberId_Type(Integer32):
    """Custom type jnxVirtualChassisMemberId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_JnxVirtualChassisMemberId_Type.__name__ = "Integer32"
_JnxVirtualChassisMemberId_Object = MibTableColumn
jnxVirtualChassisMemberId = _JnxVirtualChassisMemberId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 1, 1, 1),
    _JnxVirtualChassisMemberId_Type()
)
jnxVirtualChassisMemberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxVirtualChassisMemberId.setStatus("current")
_JnxVirtualChassisMemberSerialnumber_Type = DisplayString
_JnxVirtualChassisMemberSerialnumber_Object = MibTableColumn
jnxVirtualChassisMemberSerialnumber = _JnxVirtualChassisMemberSerialnumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 1, 1, 2),
    _JnxVirtualChassisMemberSerialnumber_Type()
)
jnxVirtualChassisMemberSerialnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisMemberSerialnumber.setStatus("current")


class _JnxVirtualChassisMemberRole_Type(Integer32):
    """Custom type jnxVirtualChassisMemberRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("linecard", 3),
          ("master", 1))
    )


_JnxVirtualChassisMemberRole_Type.__name__ = "Integer32"
_JnxVirtualChassisMemberRole_Object = MibTableColumn
jnxVirtualChassisMemberRole = _JnxVirtualChassisMemberRole_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 1, 1, 3),
    _JnxVirtualChassisMemberRole_Type()
)
jnxVirtualChassisMemberRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisMemberRole.setStatus("current")
_JnxVirtualChassisMemberMacAddBase_Type = MacAddress
_JnxVirtualChassisMemberMacAddBase_Object = MibTableColumn
jnxVirtualChassisMemberMacAddBase = _JnxVirtualChassisMemberMacAddBase_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 1, 1, 4),
    _JnxVirtualChassisMemberMacAddBase_Type()
)
jnxVirtualChassisMemberMacAddBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisMemberMacAddBase.setStatus("current")
_JnxVirtualChassisMemberSWVersion_Type = DisplayString
_JnxVirtualChassisMemberSWVersion_Object = MibTableColumn
jnxVirtualChassisMemberSWVersion = _JnxVirtualChassisMemberSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 1, 1, 5),
    _JnxVirtualChassisMemberSWVersion_Type()
)
jnxVirtualChassisMemberSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisMemberSWVersion.setStatus("current")


class _JnxVirtualChassisMemberPriority_Type(Integer32):
    """Custom type jnxVirtualChassisMemberPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxVirtualChassisMemberPriority_Type.__name__ = "Integer32"
_JnxVirtualChassisMemberPriority_Object = MibTableColumn
jnxVirtualChassisMemberPriority = _JnxVirtualChassisMemberPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 1, 1, 6),
    _JnxVirtualChassisMemberPriority_Type()
)
jnxVirtualChassisMemberPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisMemberPriority.setStatus("current")
_JnxVirtualChassisMemberUptime_Type = Integer32
_JnxVirtualChassisMemberUptime_Object = MibTableColumn
jnxVirtualChassisMemberUptime = _JnxVirtualChassisMemberUptime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 1, 1, 7),
    _JnxVirtualChassisMemberUptime_Type()
)
jnxVirtualChassisMemberUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisMemberUptime.setStatus("current")


class _JnxVirtualChassisMemberModel_Type(DisplayString):
    """Custom type jnxVirtualChassisMemberModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxVirtualChassisMemberModel_Type.__name__ = "DisplayString"
_JnxVirtualChassisMemberModel_Object = MibTableColumn
jnxVirtualChassisMemberModel = _JnxVirtualChassisMemberModel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 1, 1, 8),
    _JnxVirtualChassisMemberModel_Type()
)
jnxVirtualChassisMemberModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisMemberModel.setStatus("current")


class _JnxVirtualChassisMemberLocation_Type(DisplayString):
    """Custom type jnxVirtualChassisMemberLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_JnxVirtualChassisMemberLocation_Type.__name__ = "DisplayString"
_JnxVirtualChassisMemberLocation_Object = MibTableColumn
jnxVirtualChassisMemberLocation = _JnxVirtualChassisMemberLocation_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 1, 1, 9),
    _JnxVirtualChassisMemberLocation_Type()
)
jnxVirtualChassisMemberLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisMemberLocation.setStatus("current")
_JnxVirtualChassisPortTable_Object = MibTable
jnxVirtualChassisPortTable = _JnxVirtualChassisPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    jnxVirtualChassisPortTable.setStatus("current")
_JnxVirtualChassisPortEntry_Object = MibTableRow
jnxVirtualChassisPortEntry = _JnxVirtualChassisPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 2, 1)
)
jnxVirtualChassisPortEntry.setIndexNames(
    (0, "JUNIPER-VIRTUALCHASSIS-MIB", "jnxVirtualChassisFpcId"),
    (0, "JUNIPER-VIRTUALCHASSIS-MIB", "jnxVirtualChassisPortName"),
)
if mibBuilder.loadTexts:
    jnxVirtualChassisPortEntry.setStatus("current")


class _JnxVirtualChassisFpcId_Type(Integer32):
    """Custom type jnxVirtualChassisFpcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_JnxVirtualChassisFpcId_Type.__name__ = "Integer32"
_JnxVirtualChassisFpcId_Object = MibTableColumn
jnxVirtualChassisFpcId = _JnxVirtualChassisFpcId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 2, 1, 1),
    _JnxVirtualChassisFpcId_Type()
)
jnxVirtualChassisFpcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxVirtualChassisFpcId.setStatus("current")


class _JnxVirtualChassisPortName_Type(DisplayString):
    """Custom type jnxVirtualChassisPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_JnxVirtualChassisPortName_Type.__name__ = "DisplayString"
_JnxVirtualChassisPortName_Object = MibTableColumn
jnxVirtualChassisPortName = _JnxVirtualChassisPortName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 2, 1, 2),
    _JnxVirtualChassisPortName_Type()
)
jnxVirtualChassisPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxVirtualChassisPortName.setStatus("current")


class _JnxVirtualChassisPortAdminStatus_Type(Integer32):
    """Custom type jnxVirtualChassisPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_JnxVirtualChassisPortAdminStatus_Type.__name__ = "Integer32"
_JnxVirtualChassisPortAdminStatus_Object = MibTableColumn
jnxVirtualChassisPortAdminStatus = _JnxVirtualChassisPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 2, 1, 3),
    _JnxVirtualChassisPortAdminStatus_Type()
)
jnxVirtualChassisPortAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisPortAdminStatus.setStatus("current")


class _JnxVirtualChassisPortOperStatus_Type(Integer32):
    """Custom type jnxVirtualChassisPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_JnxVirtualChassisPortOperStatus_Type.__name__ = "Integer32"
_JnxVirtualChassisPortOperStatus_Object = MibTableColumn
jnxVirtualChassisPortOperStatus = _JnxVirtualChassisPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 2, 1, 4),
    _JnxVirtualChassisPortOperStatus_Type()
)
jnxVirtualChassisPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisPortOperStatus.setStatus("current")
_JnxVirtualChassisPortInPkts_Type = Counter64
_JnxVirtualChassisPortInPkts_Object = MibTableColumn
jnxVirtualChassisPortInPkts = _JnxVirtualChassisPortInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 2, 1, 5),
    _JnxVirtualChassisPortInPkts_Type()
)
jnxVirtualChassisPortInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisPortInPkts.setStatus("current")
_JnxVirtualChassisPortOutPkts_Type = Counter64
_JnxVirtualChassisPortOutPkts_Object = MibTableColumn
jnxVirtualChassisPortOutPkts = _JnxVirtualChassisPortOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 2, 1, 6),
    _JnxVirtualChassisPortOutPkts_Type()
)
jnxVirtualChassisPortOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisPortOutPkts.setStatus("current")
_JnxVirtualChassisPortInOctets_Type = Counter64
_JnxVirtualChassisPortInOctets_Object = MibTableColumn
jnxVirtualChassisPortInOctets = _JnxVirtualChassisPortInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 2, 1, 7),
    _JnxVirtualChassisPortInOctets_Type()
)
jnxVirtualChassisPortInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisPortInOctets.setStatus("current")
_JnxVirtualChassisPortOutOctets_Type = Counter64
_JnxVirtualChassisPortOutOctets_Object = MibTableColumn
jnxVirtualChassisPortOutOctets = _JnxVirtualChassisPortOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 2, 1, 8),
    _JnxVirtualChassisPortOutOctets_Type()
)
jnxVirtualChassisPortOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisPortOutOctets.setStatus("current")
_JnxVirtualChassisPortInMcasts_Type = Counter64
_JnxVirtualChassisPortInMcasts_Object = MibTableColumn
jnxVirtualChassisPortInMcasts = _JnxVirtualChassisPortInMcasts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 2, 1, 9),
    _JnxVirtualChassisPortInMcasts_Type()
)
jnxVirtualChassisPortInMcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisPortInMcasts.setStatus("current")
_JnxVirtualChassisPortOutMcasts_Type = Counter64
_JnxVirtualChassisPortOutMcasts_Object = MibTableColumn
jnxVirtualChassisPortOutMcasts = _JnxVirtualChassisPortOutMcasts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 2, 1, 10),
    _JnxVirtualChassisPortOutMcasts_Type()
)
jnxVirtualChassisPortOutMcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisPortOutMcasts.setStatus("current")
_JnxVirtualChassisPortInPkts1secRate_Type = Counter64
_JnxVirtualChassisPortInPkts1secRate_Object = MibTableColumn
jnxVirtualChassisPortInPkts1secRate = _JnxVirtualChassisPortInPkts1secRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 2, 1, 11),
    _JnxVirtualChassisPortInPkts1secRate_Type()
)
jnxVirtualChassisPortInPkts1secRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisPortInPkts1secRate.setStatus("current")
_JnxVirtualChassisPortOutPkts1secRate_Type = Counter64
_JnxVirtualChassisPortOutPkts1secRate_Object = MibTableColumn
jnxVirtualChassisPortOutPkts1secRate = _JnxVirtualChassisPortOutPkts1secRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 2, 1, 12),
    _JnxVirtualChassisPortOutPkts1secRate_Type()
)
jnxVirtualChassisPortOutPkts1secRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisPortOutPkts1secRate.setStatus("current")
_JnxVirtualChassisPortInOctets1secRate_Type = Counter64
_JnxVirtualChassisPortInOctets1secRate_Object = MibTableColumn
jnxVirtualChassisPortInOctets1secRate = _JnxVirtualChassisPortInOctets1secRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 2, 1, 13),
    _JnxVirtualChassisPortInOctets1secRate_Type()
)
jnxVirtualChassisPortInOctets1secRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisPortInOctets1secRate.setStatus("current")
_JnxVirtualChassisPortOutOctets1secRate_Type = Counter64
_JnxVirtualChassisPortOutOctets1secRate_Object = MibTableColumn
jnxVirtualChassisPortOutOctets1secRate = _JnxVirtualChassisPortOutOctets1secRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 2, 1, 14),
    _JnxVirtualChassisPortOutOctets1secRate_Type()
)
jnxVirtualChassisPortOutOctets1secRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisPortOutOctets1secRate.setStatus("current")
_JnxVirtualChassisPortCarrierTrans_Type = Counter64
_JnxVirtualChassisPortCarrierTrans_Object = MibTableColumn
jnxVirtualChassisPortCarrierTrans = _JnxVirtualChassisPortCarrierTrans_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 2, 1, 15),
    _JnxVirtualChassisPortCarrierTrans_Type()
)
jnxVirtualChassisPortCarrierTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisPortCarrierTrans.setStatus("current")
_JnxVirtualChassisPortInCRCAlignErrors_Type = Counter64
_JnxVirtualChassisPortInCRCAlignErrors_Object = MibTableColumn
jnxVirtualChassisPortInCRCAlignErrors = _JnxVirtualChassisPortInCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 2, 1, 16),
    _JnxVirtualChassisPortInCRCAlignErrors_Type()
)
jnxVirtualChassisPortInCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisPortInCRCAlignErrors.setStatus("current")
_JnxVirtualChassisPortOutCRCAlignErrors_Type = Counter64
_JnxVirtualChassisPortOutCRCAlignErrors_Object = MibTableColumn
jnxVirtualChassisPortOutCRCAlignErrors = _JnxVirtualChassisPortOutCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 2, 1, 17),
    _JnxVirtualChassisPortOutCRCAlignErrors_Type()
)
jnxVirtualChassisPortOutCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisPortOutCRCAlignErrors.setStatus("current")
_JnxVirtualChassisPortUndersizePkts_Type = Counter64
_JnxVirtualChassisPortUndersizePkts_Object = MibTableColumn
jnxVirtualChassisPortUndersizePkts = _JnxVirtualChassisPortUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 2, 1, 18),
    _JnxVirtualChassisPortUndersizePkts_Type()
)
jnxVirtualChassisPortUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisPortUndersizePkts.setStatus("current")
_JnxVirtualChassisPortCollisions_Type = Counter64
_JnxVirtualChassisPortCollisions_Object = MibTableColumn
jnxVirtualChassisPortCollisions = _JnxVirtualChassisPortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4, 1, 2, 1, 19),
    _JnxVirtualChassisPortCollisions_Type()
)
jnxVirtualChassisPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVirtualChassisPortCollisions.setStatus("current")
_JnxVccpNotificationsPrefix_ObjectIdentity = ObjectIdentity
jnxVccpNotificationsPrefix = _JnxVccpNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 14, 0)
)
if mibBuilder.loadTexts:
    jnxVccpNotificationsPrefix.setStatus("current")

# Managed Objects groups


# Notification objects

jnxVccpPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 14, 0, 1)
)
jnxVccpPortUp.setObjects(
      *(("JUNIPER-VIRTUALCHASSIS-MIB", "jnxVirtualChassisPortAdminStatus"),
        ("JUNIPER-VIRTUALCHASSIS-MIB", "jnxVirtualChassisPortOperStatus"),
        ("JUNIPER-VIRTUALCHASSIS-MIB", "jnxVirtualChassisMemberModel"),
        ("JUNIPER-VIRTUALCHASSIS-MIB", "jnxVirtualChassisMemberLocation"))
)
if mibBuilder.loadTexts:
    jnxVccpPortUp.setStatus(
        "current"
    )

jnxVccpPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 14, 0, 2)
)
jnxVccpPortDown.setObjects(
      *(("JUNIPER-VIRTUALCHASSIS-MIB", "jnxVirtualChassisPortAdminStatus"),
        ("JUNIPER-VIRTUALCHASSIS-MIB", "jnxVirtualChassisPortOperStatus"),
        ("JUNIPER-VIRTUALCHASSIS-MIB", "jnxVirtualChassisMemberModel"),
        ("JUNIPER-VIRTUALCHASSIS-MIB", "jnxVirtualChassisMemberLocation"))
)
if mibBuilder.loadTexts:
    jnxVccpPortDown.setStatus(
        "current"
    )

jnxVccpMemberUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 14, 0, 3)
)
jnxVccpMemberUp.setObjects(
      *(("JUNIPER-VIRTUALCHASSIS-MIB", "jnxVirtualChassisMemberSerialnumber"),
        ("JUNIPER-VIRTUALCHASSIS-MIB", "jnxVirtualChassisMemberRole"),
        ("JUNIPER-VIRTUALCHASSIS-MIB", "jnxVirtualChassisMemberModel"),
        ("JUNIPER-VIRTUALCHASSIS-MIB", "jnxVirtualChassisMemberLocation"))
)
if mibBuilder.loadTexts:
    jnxVccpMemberUp.setStatus(
        "current"
    )

jnxVccpMemberDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 14, 0, 4)
)
jnxVccpMemberDown.setObjects(
      *(("JUNIPER-VIRTUALCHASSIS-MIB", "jnxVirtualChassisMemberSerialnumber"),
        ("JUNIPER-VIRTUALCHASSIS-MIB", "jnxVirtualChassisMemberRole"),
        ("JUNIPER-VIRTUALCHASSIS-MIB", "jnxVirtualChassisMemberModel"),
        ("JUNIPER-VIRTUALCHASSIS-MIB", "jnxVirtualChassisMemberLocation"))
)
if mibBuilder.loadTexts:
    jnxVccpMemberDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-VIRTUALCHASSIS-MIB",
    **{"jnxVirtualChassisMemberMIB": jnxVirtualChassisMemberMIB,
       "jnxVirtualChassisMemberTable": jnxVirtualChassisMemberTable,
       "jnxVirtualChassisMemberEntry": jnxVirtualChassisMemberEntry,
       "jnxVirtualChassisMemberId": jnxVirtualChassisMemberId,
       "jnxVirtualChassisMemberSerialnumber": jnxVirtualChassisMemberSerialnumber,
       "jnxVirtualChassisMemberRole": jnxVirtualChassisMemberRole,
       "jnxVirtualChassisMemberMacAddBase": jnxVirtualChassisMemberMacAddBase,
       "jnxVirtualChassisMemberSWVersion": jnxVirtualChassisMemberSWVersion,
       "jnxVirtualChassisMemberPriority": jnxVirtualChassisMemberPriority,
       "jnxVirtualChassisMemberUptime": jnxVirtualChassisMemberUptime,
       "jnxVirtualChassisMemberModel": jnxVirtualChassisMemberModel,
       "jnxVirtualChassisMemberLocation": jnxVirtualChassisMemberLocation,
       "jnxVirtualChassisPortTable": jnxVirtualChassisPortTable,
       "jnxVirtualChassisPortEntry": jnxVirtualChassisPortEntry,
       "jnxVirtualChassisFpcId": jnxVirtualChassisFpcId,
       "jnxVirtualChassisPortName": jnxVirtualChassisPortName,
       "jnxVirtualChassisPortAdminStatus": jnxVirtualChassisPortAdminStatus,
       "jnxVirtualChassisPortOperStatus": jnxVirtualChassisPortOperStatus,
       "jnxVirtualChassisPortInPkts": jnxVirtualChassisPortInPkts,
       "jnxVirtualChassisPortOutPkts": jnxVirtualChassisPortOutPkts,
       "jnxVirtualChassisPortInOctets": jnxVirtualChassisPortInOctets,
       "jnxVirtualChassisPortOutOctets": jnxVirtualChassisPortOutOctets,
       "jnxVirtualChassisPortInMcasts": jnxVirtualChassisPortInMcasts,
       "jnxVirtualChassisPortOutMcasts": jnxVirtualChassisPortOutMcasts,
       "jnxVirtualChassisPortInPkts1secRate": jnxVirtualChassisPortInPkts1secRate,
       "jnxVirtualChassisPortOutPkts1secRate": jnxVirtualChassisPortOutPkts1secRate,
       "jnxVirtualChassisPortInOctets1secRate": jnxVirtualChassisPortInOctets1secRate,
       "jnxVirtualChassisPortOutOctets1secRate": jnxVirtualChassisPortOutOctets1secRate,
       "jnxVirtualChassisPortCarrierTrans": jnxVirtualChassisPortCarrierTrans,
       "jnxVirtualChassisPortInCRCAlignErrors": jnxVirtualChassisPortInCRCAlignErrors,
       "jnxVirtualChassisPortOutCRCAlignErrors": jnxVirtualChassisPortOutCRCAlignErrors,
       "jnxVirtualChassisPortUndersizePkts": jnxVirtualChassisPortUndersizePkts,
       "jnxVirtualChassisPortCollisions": jnxVirtualChassisPortCollisions,
       "jnxVccpNotificationsPrefix": jnxVccpNotificationsPrefix,
       "jnxVccpPortUp": jnxVccpPortUp,
       "jnxVccpPortDown": jnxVccpPortDown,
       "jnxVccpMemberUp": jnxVccpMemberUp,
       "jnxVccpMemberDown": jnxVccpMemberDown}
)
