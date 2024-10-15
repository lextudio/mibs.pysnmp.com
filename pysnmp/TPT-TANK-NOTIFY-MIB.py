# SNMP MIB module (TPT-TANK-NOTIFY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-TANK-NOTIFY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:12 2024
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

(tptMiscNotifyDeviceID,) = mibBuilder.importSymbols(
    "TPT-MISC-NOTIFY-MIB",
    "tptMiscNotifyDeviceID")

(tpt_tpa_eventsV2,
 tpt_tpa_objs,
 tpt_tpa_unkparams) = mibBuilder.importSymbols(
    "TPT-TPAMIBS-MIB",
    "tpt-tpa-eventsV2",
    "tpt-tpa-objs",
    "tpt-tpa-unkparams")


# MODULE-IDENTITY

tpt_tank_notify = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 11)
)
tpt_tank_notify.setRevisions(
        ("2016-05-25 18:54",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ExternalVIStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )



class WebFilterStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("failure", 4),
          ("success", 2),
          ("timeout", 3),
          ("uninitialized", 1))
    )



# MIB Managed Objects in the order of their OIDs

_TptTankNotifyExternalVIStatus_Type = ExternalVIStatus
_TptTankNotifyExternalVIStatus_Object = MibScalar
tptTankNotifyExternalVIStatus = _TptTankNotifyExternalVIStatus_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 151),
    _TptTankNotifyExternalVIStatus_Type()
)
tptTankNotifyExternalVIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptTankNotifyExternalVIStatus.setStatus("current")
_TptTankNotifyWebFilterStatus_Type = WebFilterStatus
_TptTankNotifyWebFilterStatus_Object = MibScalar
tptTankNotifyWebFilterStatus = _TptTankNotifyWebFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 152),
    _TptTankNotifyWebFilterStatus_Type()
)
tptTankNotifyWebFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptTankNotifyWebFilterStatus.setStatus("current")

# Managed Objects groups


# Notification objects

tptTankNotifyExternalVI = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 22)
)
tptTankNotifyExternalVI.setObjects(
      *(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"),
        ("TPT-TANK-NOTIFY-MIB", "tptTankNotifyExternalVIStatus"))
)
if mibBuilder.loadTexts:
    tptTankNotifyExternalVI.setStatus(
        "current"
    )

tptTankNotifyWebFilter = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 23)
)
tptTankNotifyWebFilter.setObjects(
      *(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"),
        ("TPT-TANK-NOTIFY-MIB", "tptTankNotifyWebFilterStatus"))
)
if mibBuilder.loadTexts:
    tptTankNotifyWebFilter.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-TANK-NOTIFY-MIB",
    **{"ExternalVIStatus": ExternalVIStatus,
       "WebFilterStatus": WebFilterStatus,
       "tpt-tank-notify": tpt_tank_notify,
       "tptTankNotifyExternalVI": tptTankNotifyExternalVI,
       "tptTankNotifyWebFilter": tptTankNotifyWebFilter,
       "tptTankNotifyExternalVIStatus": tptTankNotifyExternalVIStatus,
       "tptTankNotifyWebFilterStatus": tptTankNotifyWebFilterStatus}
)
