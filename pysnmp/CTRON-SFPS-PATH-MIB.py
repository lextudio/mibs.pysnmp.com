# SNMP MIB module (CTRON-SFPS-PATH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-PATH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:27 2024
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

(sfpsChassisRIPPath,
 sfpsISPSwitchPath,
 sfpsPathAPI,
 sfpsPathMaskObj,
 sfpsStaticPath,
 sfpsSwitchPath,
 sfpsSwitchPathAPI,
 sfpsSwitchPathStats) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsChassisRIPPath",
    "sfpsISPSwitchPath",
    "sfpsPathAPI",
    "sfpsPathMaskObj",
    "sfpsStaticPath",
    "sfpsSwitchPath",
    "sfpsSwitchPathAPI",
    "sfpsSwitchPathStats")

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



class SfpsAddress(OctetString):
    """Custom type SfpsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class HexInteger(Integer32):
    """Custom type HexInteger based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SfpsPathAPIVerb_Type(Integer32):
    """Custom type sfpsPathAPIVerb based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("delete", 3),
          ("diameter", 6),
          ("downlink", 5),
          ("flood-add", 7),
          ("flood-delete", 8),
          ("force-idle-traffic", 9),
          ("other", 1),
          ("remove-traffic-cnx", 10),
          ("uplink", 4))
    )


_SfpsPathAPIVerb_Type.__name__ = "Integer32"
_SfpsPathAPIVerb_Object = MibScalar
sfpsPathAPIVerb = _SfpsPathAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 3, 1),
    _SfpsPathAPIVerb_Type()
)
sfpsPathAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsPathAPIVerb.setStatus("mandatory")
_SfpsPathAPISwitchMac_Type = SfpsAddress
_SfpsPathAPISwitchMac_Object = MibScalar
sfpsPathAPISwitchMac = _SfpsPathAPISwitchMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 3, 2),
    _SfpsPathAPISwitchMac_Type()
)
sfpsPathAPISwitchMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsPathAPISwitchMac.setStatus("mandatory")
_SfpsPathAPIPortName_Type = DisplayString
_SfpsPathAPIPortName_Object = MibScalar
sfpsPathAPIPortName = _SfpsPathAPIPortName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 3, 3),
    _SfpsPathAPIPortName_Type()
)
sfpsPathAPIPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsPathAPIPortName.setStatus("mandatory")
_SfpsPathAPICost_Type = Integer32
_SfpsPathAPICost_Object = MibScalar
sfpsPathAPICost = _SfpsPathAPICost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 3, 4),
    _SfpsPathAPICost_Type()
)
sfpsPathAPICost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsPathAPICost.setStatus("mandatory")
_SfpsPathAPIHop_Type = Integer32
_SfpsPathAPIHop_Object = MibScalar
sfpsPathAPIHop = _SfpsPathAPIHop_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 3, 5),
    _SfpsPathAPIHop_Type()
)
sfpsPathAPIHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsPathAPIHop.setStatus("mandatory")
_SfpsPathAPIID_Type = Integer32
_SfpsPathAPIID_Object = MibScalar
sfpsPathAPIID = _SfpsPathAPIID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 3, 6),
    _SfpsPathAPIID_Type()
)
sfpsPathAPIID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsPathAPIID.setStatus("mandatory")
_SfpsPathAPIInPort_Type = SfpsAddress
_SfpsPathAPIInPort_Object = MibScalar
sfpsPathAPIInPort = _SfpsPathAPIInPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 3, 7),
    _SfpsPathAPIInPort_Type()
)
sfpsPathAPIInPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsPathAPIInPort.setStatus("mandatory")
_SfpsPathAPISrcMac_Type = SfpsAddress
_SfpsPathAPISrcMac_Object = MibScalar
sfpsPathAPISrcMac = _SfpsPathAPISrcMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 3, 8),
    _SfpsPathAPISrcMac_Type()
)
sfpsPathAPISrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsPathAPISrcMac.setStatus("mandatory")
_SfpsPathAPIDstMac_Type = SfpsAddress
_SfpsPathAPIDstMac_Object = MibScalar
sfpsPathAPIDstMac = _SfpsPathAPIDstMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 3, 9),
    _SfpsPathAPIDstMac_Type()
)
sfpsPathAPIDstMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsPathAPIDstMac.setStatus("mandatory")
_SfpsStaticPathTable_Object = MibTable
sfpsStaticPathTable = _SfpsStaticPathTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 4, 1)
)
if mibBuilder.loadTexts:
    sfpsStaticPathTable.setStatus("mandatory")
_SfpsStaticPathEntry_Object = MibTableRow
sfpsStaticPathEntry = _SfpsStaticPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 4, 1, 1)
)
sfpsStaticPathEntry.setIndexNames(
    (0, "CTRON-SFPS-PATH-MIB", "sfpsStaticPathPort"),
)
if mibBuilder.loadTexts:
    sfpsStaticPathEntry.setStatus("mandatory")
_SfpsStaticPathPort_Type = Integer32
_SfpsStaticPathPort_Object = MibTableColumn
sfpsStaticPathPort = _SfpsStaticPathPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 4, 1, 1, 1),
    _SfpsStaticPathPort_Type()
)
sfpsStaticPathPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsStaticPathPort.setStatus("mandatory")


class _SfpsStaticPathFloodEnabled_Type(Integer32):
    """Custom type sfpsStaticPathFloodEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_SfpsStaticPathFloodEnabled_Type.__name__ = "Integer32"
_SfpsStaticPathFloodEnabled_Object = MibTableColumn
sfpsStaticPathFloodEnabled = _SfpsStaticPathFloodEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 4, 1, 1, 2),
    _SfpsStaticPathFloodEnabled_Type()
)
sfpsStaticPathFloodEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsStaticPathFloodEnabled.setStatus("mandatory")


class _SfpsStaticPathUplinkEnabled_Type(Integer32):
    """Custom type sfpsStaticPathUplinkEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_SfpsStaticPathUplinkEnabled_Type.__name__ = "Integer32"
_SfpsStaticPathUplinkEnabled_Object = MibTableColumn
sfpsStaticPathUplinkEnabled = _SfpsStaticPathUplinkEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 4, 1, 1, 3),
    _SfpsStaticPathUplinkEnabled_Type()
)
sfpsStaticPathUplinkEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsStaticPathUplinkEnabled.setStatus("mandatory")


class _SfpsStaticPathDownlinkEnabled_Type(Integer32):
    """Custom type sfpsStaticPathDownlinkEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_SfpsStaticPathDownlinkEnabled_Type.__name__ = "Integer32"
_SfpsStaticPathDownlinkEnabled_Object = MibTableColumn
sfpsStaticPathDownlinkEnabled = _SfpsStaticPathDownlinkEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 4, 1, 1, 4),
    _SfpsStaticPathDownlinkEnabled_Type()
)
sfpsStaticPathDownlinkEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsStaticPathDownlinkEnabled.setStatus("mandatory")
_SfpsPathMaskObjLogPortMask_Type = DisplayString
_SfpsPathMaskObjLogPortMask_Object = MibScalar
sfpsPathMaskObjLogPortMask = _SfpsPathMaskObjLogPortMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 1),
    _SfpsPathMaskObjLogPortMask_Type()
)
sfpsPathMaskObjLogPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPathMaskObjLogPortMask.setStatus("mandatory")
_SfpsPathMaskObjPhysPortMask_Type = DisplayString
_SfpsPathMaskObjPhysPortMask_Object = MibScalar
sfpsPathMaskObjPhysPortMask = _SfpsPathMaskObjPhysPortMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 2),
    _SfpsPathMaskObjPhysPortMask_Type()
)
sfpsPathMaskObjPhysPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPathMaskObjPhysPortMask.setStatus("mandatory")
_SfpsPathMaskObjLogResolveMask_Type = DisplayString
_SfpsPathMaskObjLogResolveMask_Object = MibScalar
sfpsPathMaskObjLogResolveMask = _SfpsPathMaskObjLogResolveMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 3),
    _SfpsPathMaskObjLogResolveMask_Type()
)
sfpsPathMaskObjLogResolveMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPathMaskObjLogResolveMask.setStatus("mandatory")
_SfpsPathMaskObjLogFloodNoINB_Type = DisplayString
_SfpsPathMaskObjLogFloodNoINB_Object = MibScalar
sfpsPathMaskObjLogFloodNoINB = _SfpsPathMaskObjLogFloodNoINB_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 4),
    _SfpsPathMaskObjLogFloodNoINB_Type()
)
sfpsPathMaskObjLogFloodNoINB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPathMaskObjLogFloodNoINB.setStatus("mandatory")
_SfpsPathMaskObjPhysResolveMask_Type = DisplayString
_SfpsPathMaskObjPhysResolveMask_Object = MibScalar
sfpsPathMaskObjPhysResolveMask = _SfpsPathMaskObjPhysResolveMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 5),
    _SfpsPathMaskObjPhysResolveMask_Type()
)
sfpsPathMaskObjPhysResolveMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPathMaskObjPhysResolveMask.setStatus("mandatory")
_SfpsPathMaskObjPhysFloodNoINB_Type = DisplayString
_SfpsPathMaskObjPhysFloodNoINB_Object = MibScalar
sfpsPathMaskObjPhysFloodNoINB = _SfpsPathMaskObjPhysFloodNoINB_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 6),
    _SfpsPathMaskObjPhysFloodNoINB_Type()
)
sfpsPathMaskObjPhysFloodNoINB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPathMaskObjPhysFloodNoINB.setStatus("mandatory")
_SfpsPathMaskObjOldLogPortMask_Type = DisplayString
_SfpsPathMaskObjOldLogPortMask_Object = MibScalar
sfpsPathMaskObjOldLogPortMask = _SfpsPathMaskObjOldLogPortMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 7),
    _SfpsPathMaskObjOldLogPortMask_Type()
)
sfpsPathMaskObjOldLogPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPathMaskObjOldLogPortMask.setStatus("mandatory")
_SfpsPathMaskObjPathChangeEvent_Type = Integer32
_SfpsPathMaskObjPathChangeEvent_Object = MibScalar
sfpsPathMaskObjPathChangeEvent = _SfpsPathMaskObjPathChangeEvent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 8),
    _SfpsPathMaskObjPathChangeEvent_Type()
)
sfpsPathMaskObjPathChangeEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsPathMaskObjPathChangeEvent.setStatus("mandatory")
_SfpsPathMaskObjPathChangeCounter_Type = Integer32
_SfpsPathMaskObjPathChangeCounter_Object = MibScalar
sfpsPathMaskObjPathChangeCounter = _SfpsPathMaskObjPathChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 9),
    _SfpsPathMaskObjPathChangeCounter_Type()
)
sfpsPathMaskObjPathChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPathMaskObjPathChangeCounter.setStatus("mandatory")
_SfpsPathMaskObjLastChangeTime_Type = TimeTicks
_SfpsPathMaskObjLastChangeTime_Object = MibScalar
sfpsPathMaskObjLastChangeTime = _SfpsPathMaskObjLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 10),
    _SfpsPathMaskObjLastChangeTime_Type()
)
sfpsPathMaskObjLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPathMaskObjLastChangeTime.setStatus("mandatory")
_SfpsPathMaskObjPathCounterReset_Type = Integer32
_SfpsPathMaskObjPathCounterReset_Object = MibScalar
sfpsPathMaskObjPathCounterReset = _SfpsPathMaskObjPathCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 11),
    _SfpsPathMaskObjPathCounterReset_Type()
)
sfpsPathMaskObjPathCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsPathMaskObjPathCounterReset.setStatus("mandatory")
_SfpsPathMaskObjIsolatedSwitchMask_Type = DisplayString
_SfpsPathMaskObjIsolatedSwitchMask_Object = MibScalar
sfpsPathMaskObjIsolatedSwitchMask = _SfpsPathMaskObjIsolatedSwitchMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 12),
    _SfpsPathMaskObjIsolatedSwitchMask_Type()
)
sfpsPathMaskObjIsolatedSwitchMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPathMaskObjIsolatedSwitchMask.setStatus("mandatory")
_SfpsPathMaskObjPyhsIsolatedSwitchMask_Type = DisplayString
_SfpsPathMaskObjPyhsIsolatedSwitchMask_Object = MibScalar
sfpsPathMaskObjPyhsIsolatedSwitchMask = _SfpsPathMaskObjPyhsIsolatedSwitchMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 13),
    _SfpsPathMaskObjPyhsIsolatedSwitchMask_Type()
)
sfpsPathMaskObjPyhsIsolatedSwitchMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPathMaskObjPyhsIsolatedSwitchMask.setStatus("mandatory")
_SfpsPathMaskObjLogDownlinkMask_Type = DisplayString
_SfpsPathMaskObjLogDownlinkMask_Object = MibScalar
sfpsPathMaskObjLogDownlinkMask = _SfpsPathMaskObjLogDownlinkMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 14),
    _SfpsPathMaskObjLogDownlinkMask_Type()
)
sfpsPathMaskObjLogDownlinkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPathMaskObjLogDownlinkMask.setStatus("mandatory")
_SfpsPathMaskObjCoreUplinkMask_Type = DisplayString
_SfpsPathMaskObjCoreUplinkMask_Object = MibScalar
sfpsPathMaskObjCoreUplinkMask = _SfpsPathMaskObjCoreUplinkMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 15),
    _SfpsPathMaskObjCoreUplinkMask_Type()
)
sfpsPathMaskObjCoreUplinkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPathMaskObjCoreUplinkMask.setStatus("mandatory")


class _SfpsPathMaskObjOverrideFloodMask_Type(Integer32):
    """Custom type sfpsPathMaskObjOverrideFloodMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_SfpsPathMaskObjOverrideFloodMask_Type.__name__ = "Integer32"
_SfpsPathMaskObjOverrideFloodMask_Object = MibScalar
sfpsPathMaskObjOverrideFloodMask = _SfpsPathMaskObjOverrideFloodMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5, 16),
    _SfpsPathMaskObjOverrideFloodMask_Type()
)
sfpsPathMaskObjOverrideFloodMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPathMaskObjOverrideFloodMask.setStatus("mandatory")
_SfpsChassisRIPPathNumInTable_Type = Integer32
_SfpsChassisRIPPathNumInTable_Object = MibScalar
sfpsChassisRIPPathNumInTable = _SfpsChassisRIPPathNumInTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 12, 1),
    _SfpsChassisRIPPathNumInTable_Type()
)
sfpsChassisRIPPathNumInTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsChassisRIPPathNumInTable.setStatus("mandatory")
_SfpsChassisRIPPathNumRequests_Type = Integer32
_SfpsChassisRIPPathNumRequests_Object = MibScalar
sfpsChassisRIPPathNumRequests = _SfpsChassisRIPPathNumRequests_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 12, 2),
    _SfpsChassisRIPPathNumRequests_Type()
)
sfpsChassisRIPPathNumRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsChassisRIPPathNumRequests.setStatus("mandatory")
_SfpsChassisRIPPathNumReplyAck_Type = Integer32
_SfpsChassisRIPPathNumReplyAck_Object = MibScalar
sfpsChassisRIPPathNumReplyAck = _SfpsChassisRIPPathNumReplyAck_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 12, 3),
    _SfpsChassisRIPPathNumReplyAck_Type()
)
sfpsChassisRIPPathNumReplyAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsChassisRIPPathNumReplyAck.setStatus("mandatory")
_SfpsChassisRIPPathNumReplyUnk_Type = Integer32
_SfpsChassisRIPPathNumReplyUnk_Object = MibScalar
sfpsChassisRIPPathNumReplyUnk = _SfpsChassisRIPPathNumReplyUnk_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 12, 4),
    _SfpsChassisRIPPathNumReplyUnk_Type()
)
sfpsChassisRIPPathNumReplyUnk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsChassisRIPPathNumReplyUnk.setStatus("mandatory")
_SfpsServiceCenterPathTable_Object = MibTable
sfpsServiceCenterPathTable = _SfpsServiceCenterPathTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 1)
)
if mibBuilder.loadTexts:
    sfpsServiceCenterPathTable.setStatus("mandatory")
_SfpsServiceCenterPathEntry_Object = MibTableRow
sfpsServiceCenterPathEntry = _SfpsServiceCenterPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 1, 1)
)
sfpsServiceCenterPathEntry.setIndexNames(
    (0, "CTRON-SFPS-PATH-MIB", "sfpsServiceCenterPathHashLeaf"),
)
if mibBuilder.loadTexts:
    sfpsServiceCenterPathEntry.setStatus("mandatory")
_SfpsServiceCenterPathHashLeaf_Type = HexInteger
_SfpsServiceCenterPathHashLeaf_Object = MibTableColumn
sfpsServiceCenterPathHashLeaf = _SfpsServiceCenterPathHashLeaf_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 1, 1, 1),
    _SfpsServiceCenterPathHashLeaf_Type()
)
sfpsServiceCenterPathHashLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterPathHashLeaf.setStatus("mandatory")
_SfpsServiceCenterPathMetric_Type = Integer32
_SfpsServiceCenterPathMetric_Object = MibTableColumn
sfpsServiceCenterPathMetric = _SfpsServiceCenterPathMetric_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 1, 1, 2),
    _SfpsServiceCenterPathMetric_Type()
)
sfpsServiceCenterPathMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterPathMetric.setStatus("mandatory")
_SfpsServiceCenterPathName_Type = DisplayString
_SfpsServiceCenterPathName_Object = MibTableColumn
sfpsServiceCenterPathName = _SfpsServiceCenterPathName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 1, 1, 3),
    _SfpsServiceCenterPathName_Type()
)
sfpsServiceCenterPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterPathName.setStatus("mandatory")


class _SfpsServiceCenterPathOperStatus_Type(Integer32):
    """Custom type sfpsServiceCenterPathOperStatus based on Integer32"""
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
        *(("kStatusFaulted", 4),
          ("kStatusHalted", 2),
          ("kStatusNotStarted", 5),
          ("kStatusPending", 3),
          ("kStatusRunning", 1))
    )


_SfpsServiceCenterPathOperStatus_Type.__name__ = "Integer32"
_SfpsServiceCenterPathOperStatus_Object = MibTableColumn
sfpsServiceCenterPathOperStatus = _SfpsServiceCenterPathOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 1, 1, 4),
    _SfpsServiceCenterPathOperStatus_Type()
)
sfpsServiceCenterPathOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterPathOperStatus.setStatus("mandatory")


class _SfpsServiceCenterPathAdminStatus_Type(Integer32):
    """Custom type sfpsServiceCenterPathAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsServiceCenterPathAdminStatus_Type.__name__ = "Integer32"
_SfpsServiceCenterPathAdminStatus_Object = MibTableColumn
sfpsServiceCenterPathAdminStatus = _SfpsServiceCenterPathAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 1, 1, 5),
    _SfpsServiceCenterPathAdminStatus_Type()
)
sfpsServiceCenterPathAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsServiceCenterPathAdminStatus.setStatus("mandatory")
_SfpsServiceCenterPathStatusTime_Type = TimeTicks
_SfpsServiceCenterPathStatusTime_Object = MibTableColumn
sfpsServiceCenterPathStatusTime = _SfpsServiceCenterPathStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 1, 1, 6),
    _SfpsServiceCenterPathStatusTime_Type()
)
sfpsServiceCenterPathStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterPathStatusTime.setStatus("mandatory")
_SfpsServiceCenterPathRequests_Type = Integer32
_SfpsServiceCenterPathRequests_Object = MibTableColumn
sfpsServiceCenterPathRequests = _SfpsServiceCenterPathRequests_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 1, 1, 7),
    _SfpsServiceCenterPathRequests_Type()
)
sfpsServiceCenterPathRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterPathRequests.setStatus("mandatory")
_SfpsServiceCenterPathResponses_Type = Integer32
_SfpsServiceCenterPathResponses_Object = MibTableColumn
sfpsServiceCenterPathResponses = _SfpsServiceCenterPathResponses_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 1, 1, 8),
    _SfpsServiceCenterPathResponses_Type()
)
sfpsServiceCenterPathResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterPathResponses.setStatus("mandatory")
_SfpsSwitchPathStatsNumEntries_Type = Integer32
_SfpsSwitchPathStatsNumEntries_Object = MibScalar
sfpsSwitchPathStatsNumEntries = _SfpsSwitchPathStatsNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 1),
    _SfpsSwitchPathStatsNumEntries_Type()
)
sfpsSwitchPathStatsNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathStatsNumEntries.setStatus("mandatory")
_SfpsSwitchPathStatsMaxEntries_Type = Integer32
_SfpsSwitchPathStatsMaxEntries_Object = MibScalar
sfpsSwitchPathStatsMaxEntries = _SfpsSwitchPathStatsMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 2),
    _SfpsSwitchPathStatsMaxEntries_Type()
)
sfpsSwitchPathStatsMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathStatsMaxEntries.setStatus("mandatory")
_SfpsSwitchPathStatsTableSize_Type = Integer32
_SfpsSwitchPathStatsTableSize_Object = MibScalar
sfpsSwitchPathStatsTableSize = _SfpsSwitchPathStatsTableSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 3),
    _SfpsSwitchPathStatsTableSize_Type()
)
sfpsSwitchPathStatsTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathStatsTableSize.setStatus("mandatory")
_SfpsSwitchPathStatsMemUsage_Type = Integer32
_SfpsSwitchPathStatsMemUsage_Object = MibScalar
sfpsSwitchPathStatsMemUsage = _SfpsSwitchPathStatsMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 4),
    _SfpsSwitchPathStatsMemUsage_Type()
)
sfpsSwitchPathStatsMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathStatsMemUsage.setStatus("mandatory")
_SfpsSwitchPathStatsActiveLocal_Type = Integer32
_SfpsSwitchPathStatsActiveLocal_Object = MibScalar
sfpsSwitchPathStatsActiveLocal = _SfpsSwitchPathStatsActiveLocal_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 5),
    _SfpsSwitchPathStatsActiveLocal_Type()
)
sfpsSwitchPathStatsActiveLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathStatsActiveLocal.setStatus("mandatory")
_SfpsSwitchPathStatsActiveRemote_Type = Integer32
_SfpsSwitchPathStatsActiveRemote_Object = MibScalar
sfpsSwitchPathStatsActiveRemote = _SfpsSwitchPathStatsActiveRemote_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 6),
    _SfpsSwitchPathStatsActiveRemote_Type()
)
sfpsSwitchPathStatsActiveRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathStatsActiveRemote.setStatus("mandatory")
_SfpsSwitchPathStatsStaticRemote_Type = Integer32
_SfpsSwitchPathStatsStaticRemote_Object = MibScalar
sfpsSwitchPathStatsStaticRemote = _SfpsSwitchPathStatsStaticRemote_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 7),
    _SfpsSwitchPathStatsStaticRemote_Type()
)
sfpsSwitchPathStatsStaticRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathStatsStaticRemote.setStatus("mandatory")
_SfpsSwitchPathStatsDeadLocal_Type = Integer32
_SfpsSwitchPathStatsDeadLocal_Object = MibScalar
sfpsSwitchPathStatsDeadLocal = _SfpsSwitchPathStatsDeadLocal_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 8),
    _SfpsSwitchPathStatsDeadLocal_Type()
)
sfpsSwitchPathStatsDeadLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathStatsDeadLocal.setStatus("mandatory")
_SfpsSwitchPathStatsDeadRemote_Type = Integer32
_SfpsSwitchPathStatsDeadRemote_Object = MibScalar
sfpsSwitchPathStatsDeadRemote = _SfpsSwitchPathStatsDeadRemote_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 9),
    _SfpsSwitchPathStatsDeadRemote_Type()
)
sfpsSwitchPathStatsDeadRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathStatsDeadRemote.setStatus("mandatory")
_SfpsSwitchPathStatsReapReady_Type = Integer32
_SfpsSwitchPathStatsReapReady_Object = MibScalar
sfpsSwitchPathStatsReapReady = _SfpsSwitchPathStatsReapReady_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 10),
    _SfpsSwitchPathStatsReapReady_Type()
)
sfpsSwitchPathStatsReapReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathStatsReapReady.setStatus("mandatory")
_SfpsSwitchPathStatsReapAt_Type = Integer32
_SfpsSwitchPathStatsReapAt_Object = MibScalar
sfpsSwitchPathStatsReapAt = _SfpsSwitchPathStatsReapAt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 11),
    _SfpsSwitchPathStatsReapAt_Type()
)
sfpsSwitchPathStatsReapAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathStatsReapAt.setStatus("mandatory")
_SfpsSwitchPathStatsReapCount_Type = Integer32
_SfpsSwitchPathStatsReapCount_Object = MibScalar
sfpsSwitchPathStatsReapCount = _SfpsSwitchPathStatsReapCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 12),
    _SfpsSwitchPathStatsReapCount_Type()
)
sfpsSwitchPathStatsReapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathStatsReapCount.setStatus("mandatory")
_SfpsSwitchPathStatsPathReq_Type = Integer32
_SfpsSwitchPathStatsPathReq_Object = MibScalar
sfpsSwitchPathStatsPathReq = _SfpsSwitchPathStatsPathReq_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 13),
    _SfpsSwitchPathStatsPathReq_Type()
)
sfpsSwitchPathStatsPathReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathStatsPathReq.setStatus("mandatory")
_SfpsSwitchPathStatsPathAck_Type = Integer32
_SfpsSwitchPathStatsPathAck_Object = MibScalar
sfpsSwitchPathStatsPathAck = _SfpsSwitchPathStatsPathAck_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 14),
    _SfpsSwitchPathStatsPathAck_Type()
)
sfpsSwitchPathStatsPathAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathStatsPathAck.setStatus("mandatory")
_SfpsSwitchPathStatsPathNak_Type = Integer32
_SfpsSwitchPathStatsPathNak_Object = MibScalar
sfpsSwitchPathStatsPathNak = _SfpsSwitchPathStatsPathNak_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 15),
    _SfpsSwitchPathStatsPathNak_Type()
)
sfpsSwitchPathStatsPathNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathStatsPathNak.setStatus("mandatory")
_SfpsSwitchPathStatsPathUnk_Type = Integer32
_SfpsSwitchPathStatsPathUnk_Object = MibScalar
sfpsSwitchPathStatsPathUnk = _SfpsSwitchPathStatsPathUnk_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 16),
    _SfpsSwitchPathStatsPathUnk_Type()
)
sfpsSwitchPathStatsPathUnk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathStatsPathUnk.setStatus("mandatory")
_SfpsSwitchPathStatsLocateReq_Type = Integer32
_SfpsSwitchPathStatsLocateReq_Object = MibScalar
sfpsSwitchPathStatsLocateReq = _SfpsSwitchPathStatsLocateReq_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 17),
    _SfpsSwitchPathStatsLocateReq_Type()
)
sfpsSwitchPathStatsLocateReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathStatsLocateReq.setStatus("mandatory")
_SfpsSwitchPathStatsLocateAck_Type = Integer32
_SfpsSwitchPathStatsLocateAck_Object = MibScalar
sfpsSwitchPathStatsLocateAck = _SfpsSwitchPathStatsLocateAck_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 18),
    _SfpsSwitchPathStatsLocateAck_Type()
)
sfpsSwitchPathStatsLocateAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathStatsLocateAck.setStatus("mandatory")
_SfpsSwitchPathStatsLocateNak_Type = Integer32
_SfpsSwitchPathStatsLocateNak_Object = MibScalar
sfpsSwitchPathStatsLocateNak = _SfpsSwitchPathStatsLocateNak_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 19),
    _SfpsSwitchPathStatsLocateNak_Type()
)
sfpsSwitchPathStatsLocateNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathStatsLocateNak.setStatus("mandatory")
_SfpsSwitchPathStatsLocateUnk_Type = Integer32
_SfpsSwitchPathStatsLocateUnk_Object = MibScalar
sfpsSwitchPathStatsLocateUnk = _SfpsSwitchPathStatsLocateUnk_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 20),
    _SfpsSwitchPathStatsLocateUnk_Type()
)
sfpsSwitchPathStatsLocateUnk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathStatsLocateUnk.setStatus("mandatory")
_SfpsSwitchPathStatsSndDblBack_Type = Integer32
_SfpsSwitchPathStatsSndDblBack_Object = MibScalar
sfpsSwitchPathStatsSndDblBack = _SfpsSwitchPathStatsSndDblBack_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 21),
    _SfpsSwitchPathStatsSndDblBack_Type()
)
sfpsSwitchPathStatsSndDblBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathStatsSndDblBack.setStatus("mandatory")
_SfpsSwitchPathStatsRcdDblBack_Type = Integer32
_SfpsSwitchPathStatsRcdDblBack_Object = MibScalar
sfpsSwitchPathStatsRcdDblBack = _SfpsSwitchPathStatsRcdDblBack_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1, 22),
    _SfpsSwitchPathStatsRcdDblBack_Type()
)
sfpsSwitchPathStatsRcdDblBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathStatsRcdDblBack.setStatus("mandatory")


class _SfpsSwitchPathAPIVerb_Type(Integer32):
    """Custom type sfpsSwitchPathAPIVerb based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("addFind", 2),
          ("clearTable", 5),
          ("delete", 4),
          ("lose", 3),
          ("other", 1),
          ("resetStats", 6),
          ("setMaxRcvDblBck", 8),
          ("setReapAt", 7))
    )


_SfpsSwitchPathAPIVerb_Type.__name__ = "Integer32"
_SfpsSwitchPathAPIVerb_Object = MibScalar
sfpsSwitchPathAPIVerb = _SfpsSwitchPathAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 2, 1),
    _SfpsSwitchPathAPIVerb_Type()
)
sfpsSwitchPathAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSwitchPathAPIVerb.setStatus("mandatory")
_SfpsSwitchPathAPIPort_Type = Integer32
_SfpsSwitchPathAPIPort_Object = MibScalar
sfpsSwitchPathAPIPort = _SfpsSwitchPathAPIPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 2, 2),
    _SfpsSwitchPathAPIPort_Type()
)
sfpsSwitchPathAPIPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSwitchPathAPIPort.setStatus("mandatory")
_SfpsSwitchPathAPIBaseMAC_Type = SfpsAddress
_SfpsSwitchPathAPIBaseMAC_Object = MibScalar
sfpsSwitchPathAPIBaseMAC = _SfpsSwitchPathAPIBaseMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 2, 3),
    _SfpsSwitchPathAPIBaseMAC_Type()
)
sfpsSwitchPathAPIBaseMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSwitchPathAPIBaseMAC.setStatus("mandatory")
_SfpsSwitchPathAPIReapAt_Type = Integer32
_SfpsSwitchPathAPIReapAt_Object = MibScalar
sfpsSwitchPathAPIReapAt = _SfpsSwitchPathAPIReapAt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 2, 4),
    _SfpsSwitchPathAPIReapAt_Type()
)
sfpsSwitchPathAPIReapAt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSwitchPathAPIReapAt.setStatus("mandatory")
_SfpsSwitchPathAPIMaxRcvDblBack_Type = Integer32
_SfpsSwitchPathAPIMaxRcvDblBack_Object = MibScalar
sfpsSwitchPathAPIMaxRcvDblBack = _SfpsSwitchPathAPIMaxRcvDblBack_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 2, 5),
    _SfpsSwitchPathAPIMaxRcvDblBack_Type()
)
sfpsSwitchPathAPIMaxRcvDblBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSwitchPathAPIMaxRcvDblBack.setStatus("mandatory")
_SfpsSwitchPathTable_Object = MibTable
sfpsSwitchPathTable = _SfpsSwitchPathTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3)
)
if mibBuilder.loadTexts:
    sfpsSwitchPathTable.setStatus("mandatory")
_SfpsSwitchPathTableEntry_Object = MibTableRow
sfpsSwitchPathTableEntry = _SfpsSwitchPathTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1)
)
sfpsSwitchPathTableEntry.setIndexNames(
    (0, "CTRON-SFPS-PATH-MIB", "sfpsSwitchPathTableSwitchMAC"),
    (0, "CTRON-SFPS-PATH-MIB", "sfpsSwitchPathTablePort"),
)
if mibBuilder.loadTexts:
    sfpsSwitchPathTableEntry.setStatus("mandatory")
_SfpsSwitchPathTableSwitchMAC_Type = SfpsAddress
_SfpsSwitchPathTableSwitchMAC_Object = MibTableColumn
sfpsSwitchPathTableSwitchMAC = _SfpsSwitchPathTableSwitchMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 1),
    _SfpsSwitchPathTableSwitchMAC_Type()
)
sfpsSwitchPathTableSwitchMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathTableSwitchMAC.setStatus("mandatory")
_SfpsSwitchPathTablePort_Type = Integer32
_SfpsSwitchPathTablePort_Object = MibTableColumn
sfpsSwitchPathTablePort = _SfpsSwitchPathTablePort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 2),
    _SfpsSwitchPathTablePort_Type()
)
sfpsSwitchPathTablePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathTablePort.setStatus("mandatory")
_SfpsSwitchPathTableIsActive_Type = Integer32
_SfpsSwitchPathTableIsActive_Object = MibTableColumn
sfpsSwitchPathTableIsActive = _SfpsSwitchPathTableIsActive_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 3),
    _SfpsSwitchPathTableIsActive_Type()
)
sfpsSwitchPathTableIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathTableIsActive.setStatus("mandatory")
_SfpsSwitchPathTableIsStatic_Type = Integer32
_SfpsSwitchPathTableIsStatic_Object = MibTableColumn
sfpsSwitchPathTableIsStatic = _SfpsSwitchPathTableIsStatic_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 4),
    _SfpsSwitchPathTableIsStatic_Type()
)
sfpsSwitchPathTableIsStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathTableIsStatic.setStatus("mandatory")
_SfpsSwitchPathTableIsLocal_Type = Integer32
_SfpsSwitchPathTableIsLocal_Object = MibTableColumn
sfpsSwitchPathTableIsLocal = _SfpsSwitchPathTableIsLocal_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 5),
    _SfpsSwitchPathTableIsLocal_Type()
)
sfpsSwitchPathTableIsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathTableIsLocal.setStatus("mandatory")
_SfpsSwitchPathTableRefCnt_Type = Integer32
_SfpsSwitchPathTableRefCnt_Object = MibTableColumn
sfpsSwitchPathTableRefCnt = _SfpsSwitchPathTableRefCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 6),
    _SfpsSwitchPathTableRefCnt_Type()
)
sfpsSwitchPathTableRefCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathTableRefCnt.setStatus("mandatory")
_SfpsSwitchPathTableRefTime_Type = TimeTicks
_SfpsSwitchPathTableRefTime_Object = MibTableColumn
sfpsSwitchPathTableRefTime = _SfpsSwitchPathTableRefTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 7),
    _SfpsSwitchPathTableRefTime_Type()
)
sfpsSwitchPathTableRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathTableRefTime.setStatus("mandatory")
_SfpsSwitchPathTableFoundCnt_Type = Integer32
_SfpsSwitchPathTableFoundCnt_Object = MibTableColumn
sfpsSwitchPathTableFoundCnt = _SfpsSwitchPathTableFoundCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 8),
    _SfpsSwitchPathTableFoundCnt_Type()
)
sfpsSwitchPathTableFoundCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathTableFoundCnt.setStatus("mandatory")
_SfpsSwitchPathTableFoundTime_Type = TimeTicks
_SfpsSwitchPathTableFoundTime_Object = MibTableColumn
sfpsSwitchPathTableFoundTime = _SfpsSwitchPathTableFoundTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 9),
    _SfpsSwitchPathTableFoundTime_Type()
)
sfpsSwitchPathTableFoundTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathTableFoundTime.setStatus("mandatory")
_SfpsSwitchPathTableLostCnt_Type = Integer32
_SfpsSwitchPathTableLostCnt_Object = MibTableColumn
sfpsSwitchPathTableLostCnt = _SfpsSwitchPathTableLostCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 10),
    _SfpsSwitchPathTableLostCnt_Type()
)
sfpsSwitchPathTableLostCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathTableLostCnt.setStatus("mandatory")
_SfpsSwitchPathTableLostTime_Type = TimeTicks
_SfpsSwitchPathTableLostTime_Object = MibTableColumn
sfpsSwitchPathTableLostTime = _SfpsSwitchPathTableLostTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 11),
    _SfpsSwitchPathTableLostTime_Type()
)
sfpsSwitchPathTableLostTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathTableLostTime.setStatus("mandatory")
_SfpsSwitchPathTableSrcDblBackCnt_Type = Integer32
_SfpsSwitchPathTableSrcDblBackCnt_Object = MibTableColumn
sfpsSwitchPathTableSrcDblBackCnt = _SfpsSwitchPathTableSrcDblBackCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 12),
    _SfpsSwitchPathTableSrcDblBackCnt_Type()
)
sfpsSwitchPathTableSrcDblBackCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathTableSrcDblBackCnt.setStatus("mandatory")
_SfpsSwitchPathTableSrcDblBackTime_Type = TimeTicks
_SfpsSwitchPathTableSrcDblBackTime_Object = MibTableColumn
sfpsSwitchPathTableSrcDblBackTime = _SfpsSwitchPathTableSrcDblBackTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 13),
    _SfpsSwitchPathTableSrcDblBackTime_Type()
)
sfpsSwitchPathTableSrcDblBackTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathTableSrcDblBackTime.setStatus("mandatory")
_SfpsSwitchPathTableRcvDblBackCnt_Type = Integer32
_SfpsSwitchPathTableRcvDblBackCnt_Object = MibTableColumn
sfpsSwitchPathTableRcvDblBackCnt = _SfpsSwitchPathTableRcvDblBackCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 14),
    _SfpsSwitchPathTableRcvDblBackCnt_Type()
)
sfpsSwitchPathTableRcvDblBackCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathTableRcvDblBackCnt.setStatus("mandatory")
_SfpsSwitchPathTableRcvDblBackTime_Type = TimeTicks
_SfpsSwitchPathTableRcvDblBackTime_Object = MibTableColumn
sfpsSwitchPathTableRcvDblBackTime = _SfpsSwitchPathTableRcvDblBackTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 15),
    _SfpsSwitchPathTableRcvDblBackTime_Type()
)
sfpsSwitchPathTableRcvDblBackTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathTableRcvDblBackTime.setStatus("mandatory")
_SfpsSwitchPathTableDirReapCnt_Type = Integer32
_SfpsSwitchPathTableDirReapCnt_Object = MibTableColumn
sfpsSwitchPathTableDirReapCnt = _SfpsSwitchPathTableDirReapCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 16),
    _SfpsSwitchPathTableDirReapCnt_Type()
)
sfpsSwitchPathTableDirReapCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathTableDirReapCnt.setStatus("mandatory")
_SfpsSwitchPathTableDirReapTime_Type = TimeTicks
_SfpsSwitchPathTableDirReapTime_Object = MibTableColumn
sfpsSwitchPathTableDirReapTime = _SfpsSwitchPathTableDirReapTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 3, 1, 17),
    _SfpsSwitchPathTableDirReapTime_Type()
)
sfpsSwitchPathTableDirReapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchPathTableDirReapTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-PATH-MIB",
    **{"SfpsAddress": SfpsAddress,
       "HexInteger": HexInteger,
       "sfpsPathAPIVerb": sfpsPathAPIVerb,
       "sfpsPathAPISwitchMac": sfpsPathAPISwitchMac,
       "sfpsPathAPIPortName": sfpsPathAPIPortName,
       "sfpsPathAPICost": sfpsPathAPICost,
       "sfpsPathAPIHop": sfpsPathAPIHop,
       "sfpsPathAPIID": sfpsPathAPIID,
       "sfpsPathAPIInPort": sfpsPathAPIInPort,
       "sfpsPathAPISrcMac": sfpsPathAPISrcMac,
       "sfpsPathAPIDstMac": sfpsPathAPIDstMac,
       "sfpsStaticPathTable": sfpsStaticPathTable,
       "sfpsStaticPathEntry": sfpsStaticPathEntry,
       "sfpsStaticPathPort": sfpsStaticPathPort,
       "sfpsStaticPathFloodEnabled": sfpsStaticPathFloodEnabled,
       "sfpsStaticPathUplinkEnabled": sfpsStaticPathUplinkEnabled,
       "sfpsStaticPathDownlinkEnabled": sfpsStaticPathDownlinkEnabled,
       "sfpsPathMaskObjLogPortMask": sfpsPathMaskObjLogPortMask,
       "sfpsPathMaskObjPhysPortMask": sfpsPathMaskObjPhysPortMask,
       "sfpsPathMaskObjLogResolveMask": sfpsPathMaskObjLogResolveMask,
       "sfpsPathMaskObjLogFloodNoINB": sfpsPathMaskObjLogFloodNoINB,
       "sfpsPathMaskObjPhysResolveMask": sfpsPathMaskObjPhysResolveMask,
       "sfpsPathMaskObjPhysFloodNoINB": sfpsPathMaskObjPhysFloodNoINB,
       "sfpsPathMaskObjOldLogPortMask": sfpsPathMaskObjOldLogPortMask,
       "sfpsPathMaskObjPathChangeEvent": sfpsPathMaskObjPathChangeEvent,
       "sfpsPathMaskObjPathChangeCounter": sfpsPathMaskObjPathChangeCounter,
       "sfpsPathMaskObjLastChangeTime": sfpsPathMaskObjLastChangeTime,
       "sfpsPathMaskObjPathCounterReset": sfpsPathMaskObjPathCounterReset,
       "sfpsPathMaskObjIsolatedSwitchMask": sfpsPathMaskObjIsolatedSwitchMask,
       "sfpsPathMaskObjPyhsIsolatedSwitchMask": sfpsPathMaskObjPyhsIsolatedSwitchMask,
       "sfpsPathMaskObjLogDownlinkMask": sfpsPathMaskObjLogDownlinkMask,
       "sfpsPathMaskObjCoreUplinkMask": sfpsPathMaskObjCoreUplinkMask,
       "sfpsPathMaskObjOverrideFloodMask": sfpsPathMaskObjOverrideFloodMask,
       "sfpsChassisRIPPathNumInTable": sfpsChassisRIPPathNumInTable,
       "sfpsChassisRIPPathNumRequests": sfpsChassisRIPPathNumRequests,
       "sfpsChassisRIPPathNumReplyAck": sfpsChassisRIPPathNumReplyAck,
       "sfpsChassisRIPPathNumReplyUnk": sfpsChassisRIPPathNumReplyUnk,
       "sfpsServiceCenterPathTable": sfpsServiceCenterPathTable,
       "sfpsServiceCenterPathEntry": sfpsServiceCenterPathEntry,
       "sfpsServiceCenterPathHashLeaf": sfpsServiceCenterPathHashLeaf,
       "sfpsServiceCenterPathMetric": sfpsServiceCenterPathMetric,
       "sfpsServiceCenterPathName": sfpsServiceCenterPathName,
       "sfpsServiceCenterPathOperStatus": sfpsServiceCenterPathOperStatus,
       "sfpsServiceCenterPathAdminStatus": sfpsServiceCenterPathAdminStatus,
       "sfpsServiceCenterPathStatusTime": sfpsServiceCenterPathStatusTime,
       "sfpsServiceCenterPathRequests": sfpsServiceCenterPathRequests,
       "sfpsServiceCenterPathResponses": sfpsServiceCenterPathResponses,
       "sfpsSwitchPathStatsNumEntries": sfpsSwitchPathStatsNumEntries,
       "sfpsSwitchPathStatsMaxEntries": sfpsSwitchPathStatsMaxEntries,
       "sfpsSwitchPathStatsTableSize": sfpsSwitchPathStatsTableSize,
       "sfpsSwitchPathStatsMemUsage": sfpsSwitchPathStatsMemUsage,
       "sfpsSwitchPathStatsActiveLocal": sfpsSwitchPathStatsActiveLocal,
       "sfpsSwitchPathStatsActiveRemote": sfpsSwitchPathStatsActiveRemote,
       "sfpsSwitchPathStatsStaticRemote": sfpsSwitchPathStatsStaticRemote,
       "sfpsSwitchPathStatsDeadLocal": sfpsSwitchPathStatsDeadLocal,
       "sfpsSwitchPathStatsDeadRemote": sfpsSwitchPathStatsDeadRemote,
       "sfpsSwitchPathStatsReapReady": sfpsSwitchPathStatsReapReady,
       "sfpsSwitchPathStatsReapAt": sfpsSwitchPathStatsReapAt,
       "sfpsSwitchPathStatsReapCount": sfpsSwitchPathStatsReapCount,
       "sfpsSwitchPathStatsPathReq": sfpsSwitchPathStatsPathReq,
       "sfpsSwitchPathStatsPathAck": sfpsSwitchPathStatsPathAck,
       "sfpsSwitchPathStatsPathNak": sfpsSwitchPathStatsPathNak,
       "sfpsSwitchPathStatsPathUnk": sfpsSwitchPathStatsPathUnk,
       "sfpsSwitchPathStatsLocateReq": sfpsSwitchPathStatsLocateReq,
       "sfpsSwitchPathStatsLocateAck": sfpsSwitchPathStatsLocateAck,
       "sfpsSwitchPathStatsLocateNak": sfpsSwitchPathStatsLocateNak,
       "sfpsSwitchPathStatsLocateUnk": sfpsSwitchPathStatsLocateUnk,
       "sfpsSwitchPathStatsSndDblBack": sfpsSwitchPathStatsSndDblBack,
       "sfpsSwitchPathStatsRcdDblBack": sfpsSwitchPathStatsRcdDblBack,
       "sfpsSwitchPathAPIVerb": sfpsSwitchPathAPIVerb,
       "sfpsSwitchPathAPIPort": sfpsSwitchPathAPIPort,
       "sfpsSwitchPathAPIBaseMAC": sfpsSwitchPathAPIBaseMAC,
       "sfpsSwitchPathAPIReapAt": sfpsSwitchPathAPIReapAt,
       "sfpsSwitchPathAPIMaxRcvDblBack": sfpsSwitchPathAPIMaxRcvDblBack,
       "sfpsSwitchPathTable": sfpsSwitchPathTable,
       "sfpsSwitchPathTableEntry": sfpsSwitchPathTableEntry,
       "sfpsSwitchPathTableSwitchMAC": sfpsSwitchPathTableSwitchMAC,
       "sfpsSwitchPathTablePort": sfpsSwitchPathTablePort,
       "sfpsSwitchPathTableIsActive": sfpsSwitchPathTableIsActive,
       "sfpsSwitchPathTableIsStatic": sfpsSwitchPathTableIsStatic,
       "sfpsSwitchPathTableIsLocal": sfpsSwitchPathTableIsLocal,
       "sfpsSwitchPathTableRefCnt": sfpsSwitchPathTableRefCnt,
       "sfpsSwitchPathTableRefTime": sfpsSwitchPathTableRefTime,
       "sfpsSwitchPathTableFoundCnt": sfpsSwitchPathTableFoundCnt,
       "sfpsSwitchPathTableFoundTime": sfpsSwitchPathTableFoundTime,
       "sfpsSwitchPathTableLostCnt": sfpsSwitchPathTableLostCnt,
       "sfpsSwitchPathTableLostTime": sfpsSwitchPathTableLostTime,
       "sfpsSwitchPathTableSrcDblBackCnt": sfpsSwitchPathTableSrcDblBackCnt,
       "sfpsSwitchPathTableSrcDblBackTime": sfpsSwitchPathTableSrcDblBackTime,
       "sfpsSwitchPathTableRcvDblBackCnt": sfpsSwitchPathTableRcvDblBackCnt,
       "sfpsSwitchPathTableRcvDblBackTime": sfpsSwitchPathTableRcvDblBackTime,
       "sfpsSwitchPathTableDirReapCnt": sfpsSwitchPathTableDirReapCnt,
       "sfpsSwitchPathTableDirReapTime": sfpsSwitchPathTableDirReapTime}
)
